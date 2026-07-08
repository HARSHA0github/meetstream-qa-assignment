# Root Cause Analysis

## Scenario 1: "My payment was successful, but my event registration was never created."
This is a critical severity (Sev-1) issue involving a breakdown in transactional consistency.

* **Investigation Steps:** 1. Check the Payment Gateway logs (e.g., Stripe) using the user's email to confirm the charge actually succeeded.
    2. Check backend application logs for the exact timestamp of the payment webhook/callback.
    3. Query the Database to verify if the payment record exists but the `registration` row is missing.
* **Information to Collect:** User ID, Event ID, Transaction ID, timestamp, frontend error logs (if any).
* **Possible Root Causes:**
    * **Non-Atomic Transaction:** The API charged the card successfully, but the subsequent database write to create the registration failed (e.g., DB connection timeout) and there was no rollback mechanism.
    * **Webhook Failure:** The payment gateway sent a success webhook, but our backend failed to process it (e.g., endpoint returned 500, or queue worker crashed).
* **Verification:** I would simulate a successful payment in the test environment while intentionally dropping the database connection or blocking the webhook endpoint to see if the system leaves the data in the same orphaned state.

---

## Scenario 2: Intermittent duplicate confirmation emails.
This is a lower severity issue, usually tied to idempotency or frontend safeguards.

* **Investigation Steps:** 1. Inspect the Email Provider logs (e.g., SendGrid) to see if two identical requests were sent from our backend, or if the provider duplicated them.
    2. Check API gateway logs: Did the frontend send the `/api/events/register` request twice?
* **Possible Root Causes:**
    * **Frontend Double-Submit:** The "Complete Registration" button doesn't disable immediately upon click. A user on a slow network clicks it twice, sending two API requests.
    * **Missing Idempotency in Backend:** The background worker processing the email queue retries upon a slight network delay, processing the same job twice because it lacks a unique idempotency key.
* **Verification:** I would use Chrome DevTools to throttle my network speed to "Slow 3G" and double-click the checkout button. I would also check the message queue logs to see if a single job was executed twice by competing worker nodes.

---

## Scenario 3: App slows down significantly after browsing events for several minutes.
This is a performance degradation issue that typically points to memory leaks or data bloat.

* **How to Isolate the Layer:**
    * **Browser/Frontend:** Open Chrome DevTools -> Performance tab -> Record a session while scrolling events. Check the Memory tab. If the DOM Node count or JS Heap size continuously climbs without dropping (garbage collection failing), it's a frontend memory leak.
    * **Network:** Open the DevTools Network tab. Are the image payloads massive? Is the same API being called repeatedly in a loop (e.g., a React `useEffect` bug)?
    * **Backend/Database:** Open the Network tab and monitor the *Time to First Byte (TTFB)* for the `/api/events` endpoint. If TTFB starts at 100ms and grows to 3000ms over time, the backend or DB is struggling. I would then check the slow-query logs on the DB to see if we suffer from an N+1 query problem or lack pagination.
* **Likely Root Cause:** Given it happens "after browsing for several minutes", it is highly likely a **Frontend Memory Leak** (e.g., infinite scroll appending DOM nodes without virtualizing the list, or event listeners not being cleaned up when navigating between event cards).
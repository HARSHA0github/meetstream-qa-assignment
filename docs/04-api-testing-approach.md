# API Testing Approach

APIs are the backbone of the application. If the API is brittle, the UI doesn't matter. Here is how I would approach testing the six core REST endpoints.

## Tooling Choice
I prefer a hybrid approach:
* **Postman:** For initial exploration, manual testing, and sharing API collections with the frontend team. It’s the easiest way to quickly mock scenarios and verify payloads.
* **Pytest + Python `requests` (or Playwright's API context):** For automated regression testing in CI/CD. Once an endpoint is stable, its tests belong in code, not just in a Postman GUI, so they can run on every pull request.

## API Test Scenarios & Validations

### 1. `POST /api/register`
* **Validations:** Password strength rules, email format validation, and ensuring the DB record is actually created.
* **Positive:** Valid email & valid password (Expect `201 Created`).
* **Negative:** Missing fields, invalid email format, weak password (Expect `400 Bad Request`).
* **Edge:** Email with trailing spaces (should trim and succeed), extremely long email string (Expect `400` or handle gracefully).

### 2. `POST /api/login`
* **Validations:** Payload structure matches the contract. The response must contain a valid, unexpired JWT token.
* **Positive:** Correct email and password (Expect `200 OK` + JWT token).
* **Negative:** Wrong password, non-existent user, missing body (Expect `401 Unauthorized` or `400 Bad Request`).
* **Edge:** SQL injection strings in the password field (Expect `401`, verifying backend sanitation).

### 3. `GET /api/events`
* **Validations:** Ensure the returned JSON is an array of event objects. Validate data types (e.g., `capacity` is an integer, `date` is a valid ISO string).
* **Positive:** Fetching the list as an authenticated user (Expect `200 OK`).
* **Negative:** Fetching with an expired or missing token (Expect `401 Unauthorized`).
* **Edge:** Pagination—what happens if there are 10,000 events? Does it return all at once (bad) or paginate? (Expect `200 OK` but check array length).

### 4. `POST /api/events/register`
* **Validations:** Ensure the event ID exists, capacity is checked *before* locking the spot, and user isn't already registered.
* **Positive:** Valid event ID with open capacity (Expect `200 OK` or `201 Created`).
* **Negative:** Invalid event ID, user already registered (Expect `409 Conflict` or `400`).
* **Edge:** Race condition—sending two concurrent requests for an event with exactly 1 slot left.

### 5. `POST /api/payment`
* **Validations:** Secure handling of mock card data. The response must tie the payment to the correct user and event.
* **Positive:** Valid test card details (Expect `200 OK` + success message).
* **Negative:** Expired test card, invalid CVV (Expect `402 Payment Required` or `400 Bad Request`).
* **Edge:** Network timeout simulation during payment processing. 

### 6. `GET /api/registrations`
* **Validations:** Response should only show registrations belonging to the authenticated user.
* **Positive:** User with 3 registrations requests history (Expect `200 OK` with array length 3).
* **Negative:** Requesting someone else's registration history via URL manipulation (Expect `403 Forbidden`).
* **Edge:** Newly registered user with 0 registrations (Expect `200 OK` with an empty array `[]`, not a `404` or `null`).
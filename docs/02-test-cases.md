# Test Case Design & Prioritization

## 1. Test Cases
The following 14 test cases cover the critical paths for User Registration, Login, Event Registration, Payment, and Confirmation Email. 

| Test ID | Scenario | Preconditions | Test Steps | Expected Result | Priority |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-01** | Successful user registration | User is on the Registration page. | 1. Enter valid email and strong password.<br>2. Click "Register". | Account is created. User is redirected to Login or Dashboard. | **P0** |
| **TC-02** | Registration with existing email | An account with `test@test.com` already exists. | 1. Enter `test@test.com` and a password.<br>2. Click "Register". | Registration fails. UI displays "Email already in use" error. | P1 |
| **TC-03** | Successful login | User has a registered, active account. | 1. Navigate to Login page.<br>2. Enter valid credentials.<br>3. Click "Login". | User logs in successfully and is issued a valid JWT token. | **P0** |
| **TC-04** | Login with invalid credentials | User is on the Login page. | 1. Enter valid email but wrong password.<br>2. Click "Login". | Login fails. UI displays generic "Invalid credentials" error. | P1 |
| **TC-05** | View upcoming events list | User is logged in. | 1. Navigate to "Events" dashboard. | Upcoming events are displayed with title, date, and capacity details. | P1 |
| **TC-06** | Select event for registration | User is logged in. Event has available capacity. | 1. Click "Register" on an available event. | User is navigated to the payment/checkout screen for that specific event. | **P0** |
| **TC-07** | Prevent registration for full event | Event capacity is reached (0 slots). | 1. Attempt to register for the full event. | "Register" button is disabled or UI shows "Event Full" warning. | P1 |
| **TC-08** | Successful payment simulation | User is on the checkout screen. | 1. Enter valid mock payment details.<br>2. Submit payment. | Payment succeeds. User is registered. DB reflects registration. | **P0** |
| **TC-09** | Payment failure handling | User is on the checkout screen. | 1. Enter declined mock card details.<br>2. Submit payment. | Payment fails. UI shows error. User is **not** registered for the event. | P1 |
| **TC-10** | Verify Registration History | User has successfully paid for Event A. | 1. Navigate to "Registration History". | Event A appears in the list with a "Confirmed" status. | **P0** |
| **TC-11** | Confirmation email on success | User completes a successful payment (TC-08). | 1. Check the mock email inbox/logs. | Confirmation email is received with correct event details. | P2 |
| **TC-12** | No email on payment failure | User experiences a failed payment (TC-09). | 1. Check the mock email inbox/logs. | No confirmation email is triggered or sent. | P2 |
| **TC-13** | Unauthorized checkout access | User is **not** logged in. | 1. Attempt to access `/checkout/{eventId}` directly via URL. | Access denied. User is redirected to Login page. | P1 |
| **TC-14** | Concurrent registration limit | Event has 1 slot left. | 1. User A and User B attempt to pay for the last slot simultaneously. | One user succeeds; the other receives a "Capacity reached" error. | P2 |

---

## 2. Prioritization Exercise (Top 5 Cases for Launch)
If the application goes live tomorrow and I can only execute five tests, I will focus entirely on **revenue protection, basic access, and data integrity**. 

1. **TC-01 (Successful user registration):** We cannot acquire users if they cannot create an account.
2. **TC-03 (Successful login):** Existing users must be able to access the platform.
3. **TC-06 (Select event for registration):** Validates the core product offering (finding and selecting an event).
4. **TC-08 (Successful payment simulation):** The absolute critical revenue path. If payment fails, the business fails. 
5. **TC-10 (Verify Registration History):** Validates database integrity post-payment. It ensures that when a user gives us money, our system correctly associates that value with their account.
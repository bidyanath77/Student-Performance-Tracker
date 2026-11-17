# Sprint 4 - Login and Session Security Testing

**Author:** Shreya Shah
**Project:** Student Performance Tracking System

## 1. Objective

To verify successful login, failed login, unauthorized
access, session management and logout functionality.

## 2. Testing Tools

- Python unittest
- Streamlit AppTest
- unittest.mock
- Visual Studio Code

## 3. Automated Testing

Test file: test_session_security.py

| ID | Test Scenario | Expected Result | Status |
|---|---|---|---|
| TC01 | Successful login | Dashboard displayed | Pending |
| TC02 | Failed login | Invalid credentials rejected | Pending |
| TC03 | Unauthorized access | Dashboard blocked | Pending |
| TC04 | Logout | Session authentication reset and dashboard blocked | Pending |

## 4. Security Code Review

### Session Management

Streamlit session state manages authentication
using the logged_in variable.

### Logout

Logout resets the logged_in variable to False
and redirects the user to the login page.

### Access Control

Unauthenticated users are prevented from accessing
the dashboard using an authentication check
and st.stop().

## 5. Identified Security Risks

- Missing inactivity-based session expiration.
- Incomplete session state cleanup during logout.
- HTTPS configuration requires verification.

## 6. Recommended Improvements

- Implement automatic session expiration.
- Clear sensitive session information during logout.
- Ensure secure HTTPS communication.

## 7. Testing Limitations

Automated tests use mocked authentication and
student database functions. They verify application
behavior rather than actual password validation.

## 8. Conclusion

Four automated security tests were developed to
verify successful login, failed login, unauthorized
access and logout functionality.

The security code review identified additional
improvements to strengthen session management.

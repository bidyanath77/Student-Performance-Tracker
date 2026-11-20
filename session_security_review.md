
# Sprint 4 – Session Security Review

*Name:* Shreya Shah
*Project:* Student Performance Tracking System
*Sprint:* 4 (16–20 November 2026)
*Jira Tasks:* TEAM2-62 and TEAM2-63

## 1. Purpose

The purpose of this review is to evaluate login sessions,
logout functionality, and access control in our Student
Performance Tracking System.

## 2. Session Management

The application uses Streamlit session state to track
whether a user is logged in.

When authentication succeeds, the application sets:

st.session_state["logged_in"] = True

The application checks the login status before displaying
the student dashboard.

## 3. Logout Functionality

The logout button changes the login status to False
and reruns the application.

This returns the user to the login page and prevents
normal navigation to the dashboard.

## 4. Risk: Session Hijacking

*Description:*
An unauthorized person could potentially obtain access
to another user's authenticated session.

*Likelihood:* Medium (initial estimate)

*Impact:* High

*Mitigation Measures:*
- Require authentication before displaying student data.
- Provide logout functionality.
- Use HTTPS for deployment.
- Protect session credentials.
- Review secure session management and expiration.
- Test access restrictions after logout.

## 5. Risk: Unauthorized Access

*Description:*
A user may attempt to view student information without
providing valid login credentials.

*Likelihood:* Medium (initial estimate)

*Impact:* High

*Existing Controls:*
- Authentication using the login form.
- Dashboard access checking in app.py.
- Rejection of invalid login credentials.
- Logout functionality.

## 6. Testing

Automated testing is performed in
test_session_security.py.

Test cases:

1. Dashboard access without login.
2. Login with invalid credentials.
3. Login with simulated valid authentication.
4. Dashboard access after logout.

*Test Results:*
All 4 automated tests passed successfully.

## 7. Remaining Improvements

- Review automatic session expiration.
- Verify HTTPS in a deployed environment.
- Conduct further session hijacking assessments.
- Review session management limitations.
- Complete additional security testing.

## 8. Conclusion

This review examines the application's login session
management, access controls, and logout functionality.

The automated tests provide evidence of basic
application-level login protection.

Additional testing is needed to verify broader
session security before production deployment.

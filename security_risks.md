
# Sprint 4 – Individual Security Risk Assessment

**Name:** Bidya Kumari Nath  
**Project:** Student Performance Tracking System  
**Sprint:** 4 (16–20 November 2026)  
**Component:** Login Interface and Dashboard Integration

## 1. Purpose

The purpose of this assessment is to identify security
risks related to my login interface and dashboard
component and explain how these risks can be reduced.

## 2. Risk 1: Session Hijacking

**Description:**
Session hijacking occurs when an unauthorized person
gains access to another user's active login session.

**Likelihood:** Medium (initial assessment)

**Impact:** High

**Mitigation Measures:**
- Require users to log in before accessing the dashboard.
- Provide a logout button.
- Use HTTPS when deploying the application.
- Review secure session management and session expiration.
- Avoid exposing login credentials.

**Current Implementation:**
- Implemented login interface in login.py.
- Integrated authentication into the login interface.
- Added login status checking in app.py.
- Added logout functionality.
- Manually tested successful login and logout.

**Remaining Work:**
- Review session expiration.
- Verify session security in a deployed environment.
- Test additional session access scenarios.

## 3. Risk 2: Unauthorized Dashboard Access

**Description:**
An unauthorized user may attempt to access student
records without logging in.

**Likelihood:** Medium (initial assessment)

**Impact:** High

**Mitigation Measures:**
- Require successful authentication before displaying
  student information.
- Use Streamlit session state to track login status.
- Prevent unauthenticated users from accessing the
  dashboard using st.stop().
- Clear login status when the user logs out.

**Current Implementation:**
- Added login protection in app.py.
- Integrated the authentication function from auth.py.
- Added logout functionality.
- Tested dashboard navigation protection.

**Remaining Work:**
- Conduct further access-control testing.
- Review protection of any additional application pages.

## 4. Testing Evidence

I created test_login.py to test my login interface.

The following five automated tests passed:

1. Empty username and password validation.
2. Invalid login credentials.
3. Successful login state.
4. Dashboard access restriction before login.
5. Logout functionality.

I also manually tested successful login and logout
using a registered test account.

The automated login tests use mocked authentication
responses for selected scenarios. Further integration
and session security testing may be needed.

## 5. Conclusion

During Sprint 4, I implemented and integrated the
login interface with the Student Performance Tracking
System. I also added logout functionality and tested
the login-related features.

These changes provide basic application-level
access control. Further review of session management,
session expiration and deployment security is needed
to strengthen protection of student information.


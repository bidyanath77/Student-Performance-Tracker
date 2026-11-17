
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



## 5. Risk 3: Accidental Data Loss During Deletion

**Related Jira Task:** TEAM2-64

**Description:**
Student records could be accidentally deleted, resulting
in loss of important academic information.

**Likelihood:** Medium (initial assessment)

**Impact:** High

**Mitigation Measures:**
- Require confirmation before deleting student records.
- Maintain regular SQLite database backups.
- Restrict deletion to authenticated users.
- Keep backups in a secure location.
- Test database recovery procedures.

**Review and Testing:**
- Verified that a student cannot be deleted without confirmation.
- Created a database backup named students_backup.db.
- Verified that the backup contained 4 student records.
- Tested recovery using a separate database file,
  students_recovery_test.db.
- The original students.db file was not overwritten.

**Current Status:**
Deletion confirmation, manual backup and a separate
recovery test have been completed.

**Remaining Improvements:**
- Automate regular database backups.
- Establish a backup retention policy.
- Test restoration after simulated data loss.
- Review backup access permissions and storage security.

## 6. Conclusion

During Sprint 4, I implemented and integrated the login interface into our Student Performance Tracking System. I added login protection and logout functionality and successfully completed five automated login tests.

I also reviewed security risks related to session hijacking, unauthorized dashboard access and accidental data loss during deletion.

For Jira task TEAM2-64, I tested deletion confirmation, created a SQLite database backup containing four student records and tested recovery using a separate database file without affecting the original database.

These activities helped me understand the importance of authentication, access control, database backups and recovery procedures. Further improvements include automatic backups, session expiration and additional security testing.

# Sprint 5 – Final Database and Authentication Checks

**Name:** Manisha Karki
**Project:** Student Performance Tracking System
**Sprint:** 5 (23–30 November 2026)
**Testing Date:** 24 November 2026
**Jira Task:** TEAM2-67

## 1. Purpose

The purpose of this task is to perform final database and
authentication checks to ensure that existing functionality
continues to work correctly after the implementation of
the Find Student feature.

## 2. Database Checks

I reviewed database.py and checked the existing database
operations, including:

- Creating the student table
- Adding student records
- Retrieving student records
- Updating student records
- Deleting student records
- Using parameterized SQL queries

### Automated Test Results

| Test File | Tests Passed | Status |
| --- | --- | --- |
| test_database.py | 1 | PASS |
| test_update_delete.py | 1 | PASS |

Both automated database tests passed successfully.

## 3. Find Student Functionality Checks

I manually tested the find_students() function in find.py
after merging Pull Request #19 into the main branch.

| Test Case | Expected Result | Status |
| --- | --- | --- |
| Search by student ID | Correct student returned | PASS |
| Search by full name | Matching student returned | PASS |
| Search by partial name | Matching student returned | PASS |
| Search using uppercase letters | Matching student returned | PASS |
| Search with extra spaces | Matching student returned | PASS |
| Search for unknown student | Empty list returned | PASS |
| Search with empty input | Empty list returned | PASS |
| SQL injection test input | No unintended records returned | PASS |

All eight manual Find functionality checks passed.

The Find function uses parameterized SQL queries to reduce
SQL injection risks and normalizes student names to support
case-insensitive searches and extra spaces.

## 4. Authentication Checks

I executed the existing automated authentication tests
to verify that authentication continues to work correctly.

Command:

    python -m pytest test_auth.py -v

Result: 6 tests passed.

The tests include checks for invalid credentials,
unknown users and SQL injection input.

## 5. Session Security Checks

I executed the existing session security tests to verify
basic login, logout and dashboard access control.

| Test Case | Status |
| --- | --- |
| Dashboard blocked without login | PASS |
| Failed login | PASS |
| Successful login | PASS |
| Logout blocks dashboard access | PASS |

Command:

    python -m pytest test_session_security.py -v

Result: 4 tests passed.

## 6. Final Testing Summary

| Testing Area | Passed | Failed |
| --- | --- | --- |
| Database | 1 | 0 |
| Update and Delete | 1 | 0 |
| Find functionality (manual) | 8 | 0 |
| Authentication | 6 | 0 |
| Session security | 4 | 0 |
| Total | 20 | 0 |

Total automated tests passed: 12

Total manual checks passed: 8

## 7. Remaining Limitations

- Find and Filter require final application integration.
- Student Recovery requires completion and testing.
- Regression tests should be repeated after all remaining
  Sprint 5 features are merged.
- Basic security tests do not guarantee complete protection
  against all security threats.

## 8. Conclusion

All 20 checks performed during this testing session passed
successfully. The existing database, Find functionality,
authentication and basic session access controls worked
as expected in the tested cases.

No changes to the existing implementation were required
during these checks. Final integration testing should be
performed after all remaining Sprint 5 features are merged.
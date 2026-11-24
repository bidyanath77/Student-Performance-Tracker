
# Sprint 5 – Test Results

Name: Shreya Shah
Project: Student Performance Tracking System
Sprint: 5
Week: 6

## 1. Find Testing

| Test Case | Actual Result | Status |
|---|---|---|
| Search by student ID | Correct student returned | PASSED |
| Search by full name | Matching student returned | PASSED |
| Search by partial name | Matching student returned | PASSED |
| Case-insensitive search | Matching student returned | PASSED |
| Extra spaces | Spaces handled correctly | PASSED |
| Empty search | Empty list returned | PASSED |
| Non-existent student | No matching student returned | PASSED |
| SQL injection input | No matching records returned | PASSED |

### Find Testing Summary

Total tests: 8

Passed: 8

Failed: 0

Success rate: 100%

Execution time: 0.26 seconds

Testing tool: Pytest

Testing file: test_find.py

All eight automated Find tests passed successfully
using a temporary SQLite database.

## 2. Filter Testing
Test: Filter students by marks
Expected: Only matching students are returned
Actual: Correct student returned
Status: PASSED

Test: Filter students by attendance
Expected: Only matching students are returned
Actual: Correct student returned
Status: PASSED

Test: Filter students by study hours
Expected: Students meeting the minimum study hours are returned
Actual: Two matching students returned
Status: PASSED

Test: Combined filters
Expected: Students matching all selected conditions are returned
Actual: Two matching students returned
Status: PASSED

Test: Filter with no matching records
Expected: Empty results are returned
Actual: Empty list returned
Status: PASSED

Filter Testing Summary

Total tests: 5

Passed: 5

Failed: 0

Success rate: 100%

Execution time: 1.33 seconds

Testing tool: Pytest

Test file: test_filter.py

All five automated filtering tests passed successfully using a temporary SQLite database.  



## 3. Recovery Testing

| Test Case | Status |
|---|---|
| Empty Recycle Bin | PASSED |
| Move student to Recycle Bin | PASSED |
| Remove student from active records | PASSED |
| Restore original student data | PASSED |
| Remove restored student from Recycle Bin | PASSED |
| Delete non-existent student | PASSED |
| Restore non-existent student | PASSED |
| Prevent duplicate student ID | PASSED |

### Recovery Testing Summary

Total tests: 8
Passed: 8
Failed: 0
Success rate: 100%

Testing tool: Pytest
Testing file: test_recovery.py

All eight automated Recovery tests passed
successfully using a temporary SQLite database.
## 4. Final Regression Testing

Testing date: 24 November 2026

Testing tool: Pytest

Command: python -m pytest -v

Total tests: 72
Passed: 72
Failed: 0
Success rate: 100%
Execution time: 7.54 seconds

### Conclusion

All 72 automated tests passed successfully.
The Find, Filter and Recovery functionality
passed the automated tests alongside the
existing system functionality.

No regression failures were detected in
the tested local version.

Full application integration testing
is still pending.

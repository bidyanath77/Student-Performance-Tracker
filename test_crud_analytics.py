
import pandas as pd

from analytics import (
    total_students,
    average_marks,
    average_attendance,
    average_study_hours
)

# Original student data
df = pd.DataFrame({
    "student_id": [1, 2],
    "marks": [70, 80],
    "attendance": [80, 90],
    "study_hours": [2, 4]
})

# TEST 1: Before changes
assert total_students(df) == 2
assert average_marks(df) == 75
assert average_attendance(df) == 85
assert average_study_hours(df) == 3

print("Original analytics test passed!")

# TEST 2: After updating student 1
df.loc[df["student_id"] == 1, "marks"] = 90
df.loc[df["student_id"] == 1, "attendance"] = 100
df.loc[df["student_id"] == 1, "study_hours"] = 6

assert total_students(df) == 2
assert average_marks(df) == 85
assert average_attendance(df) == 95
assert average_study_hours(df) == 5

print("Student update analytics test passed!")

# TEST 3: After deleting student 2
df = df[df["student_id"] != 2].copy()

assert total_students(df) == 1
assert average_marks(df) == 90
assert average_attendance(df) == 100
assert average_study_hours(df) == 6

print("Student deletion analytics test passed!")

# TEST 4: After deleting all students
df = df.iloc[0:0].copy()

assert total_students(df) == 0
assert average_marks(df) == 0
assert average_attendance(df) == 0
assert average_study_hours(df) == 0

print("Empty dataset test passed!")
print("All Sprint 3 analytics tests passed!")

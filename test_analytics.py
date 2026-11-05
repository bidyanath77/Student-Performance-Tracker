
import pandas as pd

from analytics import (
    total_students,
    average_marks,
    average_attendance,
    average_study_hours
)

# Sample data
df = pd.DataFrame({
    "student_id": [1, 2, 3],
    "marks": [80, 90, 70],
    "attendance": [90, 95, 85],
    "study_hours": [3, 4, 2]
})

assert total_students(df) == 3
assert average_marks(df) == 80
assert average_attendance(df) == 90
assert average_study_hours(df) == 3

print("Sample data tests passed!")

# Empty DataFrame test
empty_df = pd.DataFrame()

assert total_students(empty_df) == 0
assert average_marks(empty_df) == 0
assert average_attendance(empty_df) == 0
assert average_study_hours(empty_df) == 0

print("Empty DataFrame tests passed!")
print("All analytics tests passed!")

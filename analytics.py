
import pandas as pd


def total_students(df):
    return len(df)


def average_marks(df):
    if df.empty:
        return 0
    return round(df["marks"].mean(), 2)


def average_attendance(df):
    if df.empty:
        return 0
    return round(df["attendance"].mean(), 2)


def average_study_hours(df):
    if df.empty:
        return 0
    return round(df["study_hours"].mean(), 2)

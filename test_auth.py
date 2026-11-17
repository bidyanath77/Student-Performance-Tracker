import unittest
import tempfile
from pathlib import Path
from unittest.mock import patch

import database

from auth import register_user, authenticate_user


# ==========================================
# SPRINT 4 - AUTHENTICATION TESTS
# ==========================================

class TestAuthentication(unittest.TestCase):

    # Create temporary database for each test
    def setUp(self):

        self.temp_dir = tempfile.TemporaryDirectory()

        self.test_db = str(
            Path(self.temp_dir.name) / "test_auth.db"
        )

        # Use temporary database instead of students.db
        self.db_patch = patch.object(
            database,
            "DATABASE_NAME",
            self.test_db
        )

        self.db_patch.start()

    # Clean up after each test
    def tearDown(self):

        self.db_patch.stop()

        self.temp_dir.cleanup()

    # Test 1: Register a new user
    def test_register_user(self):

        result = register_user(
            "teacher",
            "SecurePassword123!"
        )

        self.assertTrue(result)

    # Test 2: Login with correct password
    def test_correct_password(self):

        register_user(
            "teacher",
            "SecurePassword123!"
        )

        result = authenticate_user(
            "teacher",
            "SecurePassword123!"
        )

        self.assertTrue(result)

    # Test 3: Reject incorrect password
    def test_wrong_password(self):

        register_user(
            "teacher",
            "SecurePassword123!"
        )

        result = authenticate_user(
            "teacher",
            "WrongPassword123!"
        )

        self.assertFalse(result)

    # Test 4: Reject unknown username
    def test_unknown_user(self):

        result = authenticate_user(
            "unknown",
            "SecurePassword123!"
        )

        self.assertFalse(result)

    # Test 5: Prevent duplicate usernames
    def test_duplicate_username(self):

        register_user(
            "teacher",
            "SecurePassword123!"
        )

        result = register_user(
            "teacher",
            "AnotherPassword123!"
        )

        self.assertFalse(result)

    # Test 6: Prevent SQL Injection login bypass
    def test_sql_injection(self):

        register_user(
            "teacher",
            "SecurePassword123!"
        )

        result = authenticate_user(
            "' OR '1'='1",
            "anything"
        )

        self.assertFalse(result)


# ==========================================
# RUN ALL TESTS
# ==========================================

if __name__ == "__main__":
    unittest.main()
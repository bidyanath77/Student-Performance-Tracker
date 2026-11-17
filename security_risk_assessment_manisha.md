# Sprint 4 – Individual Security Risk Assessment

**Name:** Manisha Karki  
**Project:** Student Performance Tracking System  
**Sprint:** 4 (16–20 November 2026)  
**Component:** Authentication and Database Security

## 1. Purpose

The purpose of this assessment is to identify security risks related to my authentication and database component and explain how these risks can be reduced.

## 2. Security Risk Register

| Security Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| SQL Injection | Low | High | Parameterized SQL queries implemented. |
| Password Exposure | Low | High | Salted password hashing implemented. |
| Unauthorized Login | Medium | High | Authentication checks implemented. |
| Brute-Force Attacks | Medium | High | Rate limiting recommended for future work. |

*Likelihood ratings are preliminary assessments based on the current implementation.*

## 3. Work Completed

During Sprint 4, I:

- Implemented secure user registration and authentication in `auth.py`.
- Used password hashing and randomly generated salts.
- Used parameterized SQL queries to reduce SQL injection risks.
- Created `test_auth.py` and successfully ran six authentication tests.
- Tested the authentication system with the Streamlit login interface.

## 4. Remaining Improvements

Further improvements include rate limiting, session security testing, and additional security testing before deployment.

## 5. Conclusion

During Sprint 4, I implemented secure authentication and SQL injection prevention for the Student Performance Tracking System. The authentication tests passed, and the implemented measures helped reduce security risks.
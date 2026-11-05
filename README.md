Student Performance Tracking System
Project Overview
The Student Performance Tracking System is a Python-based application developed as part of our Agile Development Team Project at Niels Brock.

The system helps manage student records and provides an overview of academic performance, attendance, and study hours through an interactive dashboard.

Main Features
- Add student information through a Streamlit form.
- Store and retrieve student records using SQLite.
- Calculate total students, average marks, attendance, and study hours.
- Display student performance through an interactive dashboard.
- View student records and compare marks using charts.
- Refresh the dashboard to display updated information.
- 
Technologies Used
- Python
- Streamlit
- SQLite
- Pandas
- Plotly
- Git and GitHub
- Jira
- Python unittest and Streamlit AppTest
- 
Team Members and Responsibilities
- Bidya Kumari Nath: Dashboard and User Interface (app.py)
- Rupa Gurung: Student Entry Form (forms.py)
- Shreya Shah: Analytics (analytics.py)
- Manisha Karki: Database (database.py)
- 
Project Structure
- app.py — Main Streamlit application and dashboard
- forms.py — Student entry form
- database.py — SQLite database operations
- analytics.py — Student performance calculations
- requirements.txt — Python dependencies
- test_dashboard.py — Dashboard automated tests
- test_forms.py — Student entry form tests
- test_database.py — Database integration test
- test_analytics.py — Analytics calculation tests
The test files are contributed through individual feature branches and become available on main after their pull requests are merged.

How to Run the Application
1. Clone the GitHub repository.
2. Open the project folder in VS Code.
3. Install the required packages:
   pip install -r requirements.txt
4. Run the Streamlit application:
   streamlit run app.py
5. Open the local address displayed in the terminal.
6. 
How to Run the Tests
Run the following commands from the project folder when the corresponding test files are available:
- Dashboard: python test_dashboard.py
- Student Form: python test_forms.py
- Database: python test_database.py
- Analytics: python test_analytics.py
- 
Agile Development
Our team follows Scrum methodology with weekly sprints.

We use Jira to manage tasks and GitHub for version control, separate development branches, pull requests, and code reviews.
Sprint 1 – Initial Development
During Sprint 1, our team developed an initial working version of the Student Performance Tracking System.

The main components included the student entry form, SQLite database, analytics functions, and Streamlit dashboard.
Sprint 2 – Integration and Testing
Sprint Dates: 2–6 November 2026
Sprint Goal
Improve GitHub collaboration, test individual components, review code, and verify that the different parts of the application work together correctly.

Individual Contributions
Bidya Kumari Nath – Dashboard
- Added a dashboard refresh button and success notification.
- Created test_dashboard.py with five automated tests.
- Tested dashboard metrics, empty database handling, refresh functionality, student count updates, and the View Students page.
- Added and updated README documentation.
- Participated in code reviews and integration testing.
- 
Rupa Gurung – Student Entry Form
- Worked on testing the student entry form.
- Created test_forms.py.
- Tested form functionality and input validation.
- Successfully ran 15 automated tests.
- 
Manisha Karki – Database
- Created test_database.py.
- Tested saving and retrieving student records.
- Used a temporary SQLite database to avoid modifying real student records.
- Confirmed that the database test passed successfully.
- 
Shreya Shah – Analytics
- Created test_analytics.py.
- Tested total student count, average marks, attendance, and study hours.
- Tested calculations using sample student data and an empty dataset.
- Confirmed that the analytics tests passed successfully.
- 
Testing Results
- Dashboard: 5 automated tests passed.
- Student Entry Form: 15 automated tests passed.
- Database: Integration test passed.
- Analytics: Sample data and empty dataset tests passed.
- Manual integration testing: Added a new student and confirmed the student count increased from 4 to 5 in View Students and the dashboard.
- 
GitHub Collaboration
During Sprint 2, team members worked using separate feature branches and pull requests.

We reviewed and tested code changes before merging them into the main branch.

## Project Status

The Student Performance Tracking System has a working version with integrated student entry, SQLite database, analytics, and dashboard components.

During Sprint 2, our team focused on GitHub collaboration, component testing, and integration.

All four components passed their reported tests:

- **Dashboard:** 5 automated tests passed.
- **Student Entry Form:** 15 automated tests passed.
- **Database:** Student saving and retrieval tests passed.
- **Analytics:** Sample data and empty dataset tests passed.

We also successfully tested the integration between the student entry form, database, and dashboard by adding a new student and confirming that the total increased from 4 to 5.

Team members used separate GitHub branches, pull requests, and code reviews to collaborate on the project.

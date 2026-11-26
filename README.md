Student Performance Tracking System
Agile Development Team Project (CTEC2713) | Niels Brock, Copenhagen

About the project
The Student Performance Tracking System is a Python application that helps users manage and review student performance information in one place. Built with Streamlit and SQLite, it supports student record management, performance analysis, search and filtering, login protection, and restoration of deleted records.
The project was developed collaboratively by a four-member Computer Science team using Agile practices, GitHub for version control, and Jira for task management.

Project objectives
- Provide a clear interface for entering and maintaining student information.
- Make marks, attendance and study hours easier to monitor and understand.
- Present performance summaries and visualizations on a dashboard.
- Help users locate and filter student records efficiently.
- Protect access to student information through authentication.
- Reduce the risk of accidental data loss through a Recycle Bin and separate manual database backups.
- 
Main features
Authentication
The application displays a login form before the main dashboard. Authentication is handled through the login.py and auth.py modules. A logout option ends access to the current application session.
Student record management
Users can:
- Add students with their names, marks, attendance and study hours.
- View students in a table of active records.
- Edit students to correct or update existing information.
- Delete students with confirmation. The database deletion workflow moves records into the Recycle Bin rather than immediately discarding them.
Form validation checks that names are present and at most 100 characters, marks and attendance are between 0 and 100, and study hours are between 0 and 24.
Performance dashboard and analytics
The dashboard displays:
- Total number of students
- Average marks
- Average attendance
- Average study hours
- Student records table
- Student marks comparison chart
- Individual student performance details
The dashboard uses Pandas for tabular data, Plotly for visualizations and analytics.py for summary calculations.
Find Student
Search for a student by student ID or by full or partial name. Name matching handles differences in capitalization and extra spaces. The search logic is implemented in find.py and made available through the main Streamlit interface.
Filter Students
Filter students by ranges of marks and attendance, and a minimum value for study hours. The filtering logic and interface are implemented in filter_students.py.
Student Recovery (Recycle Bin)
The Recovery interface shows deleted student records and allows a user to restore a selected record after confirmation. Deleted records are stored in the deleted_students table within the application's SQLite database, with a deletion timestamp.

Restoration checks whether the student ID is already used by an active record. If there is a conflict, the record is not automatically overwritten and requires manual review.
Manual database backup
A separate SQLite backup can be retained to protect against broader database loss. This is a manual backup process, not a scheduled or automated feature. It is distinct from the Recycle Bin, which restores individual deleted students within the application.

Technologies and tools
Technology / tool	Role in the project
Python	Application and business logic
Streamlit	User interface, navigation and forms
SQLite	Local student record database
Pandas	Data handling and dashboard tables
Plotly	Performance charts
Git and GitHub	Source control, branches, pull requests and collaboration
Jira	Team planning and task tracking
VS Code	Development environment


Project structure
Student-Performance-Tracker/
├── app.py                 # Main application, navigation and dashboard
├── analytics.py           # Performance summary calculations
├── auth.py                # Authentication logic
├── login.py               # Login interface
├── database.py            # Database setup and student CRUD operations
├── forms.py               # Student forms and input validation
├── find.py                # Find students by ID or name
├── filter_students.py     # Filtering logic and UI
├── recovery.py            # Recycle Bin and restore operations
├── requirements.txt       # Python dependencies
├── test_*.py              # Component and application tests
├── security_risks.md      # Security risk documentation
└── README.md              # Project documentation
students.db is the local SQLite database used by the running application. Local database files and backups should be kept out of shared Git commits, especially if they contain student information.

System architecture
The application uses a modular structure:
1. Presentation layer: app.py provides Streamlit navigation, dashboard views and access to other user interfaces. login.py, forms.py, filter_students.py and recovery.py also provide interface elements.
2. Application logic: analytics.py calculates performance metrics, find.py performs student searches, auth.py handles authentication and recovery.py implements record restoration.
3. Data layer: database.py manages the primary SQLite student records. Feature modules also use SQLite queries where appropriate.
   
The main students table contains these fields:
Field	Description
student_id	Unique identifier for a student
student_name	Name of the student
marks	Numerical mark (0–100)
attendance	Attendance percentage (0–100)
study_hours	Study hours (0–24)

The deleted_students table retains the corresponding student details and a deleted_at timestamp for records moved to the Recycle Bin.

Installation and setup
Prerequisites
- Python installed
- Git (if cloning the repository)
- Access to the team's GitHub repository
1. Clone the repository
git clone https://github.com/bidyanath77/Student-Performance-Tracker.git
cd Student-Performance-Tracker
The repository is private; access must be granted by a repository collaborator.
2. Create and activate a virtual environment
Windows (PowerShell)
py -m venv .venv
.\.venv\Scripts\Activate.ps1
macOS or Linux
python3 -m venv .venv
source .venv/bin/activate
3. Install dependencies
python -m pip install -r requirements.txt
4. Run the application
python -m streamlit run app.py
Open the local URL displayed by Streamlit, normally http://localhost:8501. Sign in with an account configured for the application. Credentials are intentionally not included in this documentation.

The application initializes the main student table when it starts. The Recycle Bin table is created when its functionality is accessed.
Using the application
1. Log in to access the system.
2. Visit Dashboard to review overall performance and charts.
3. Use Add Student to create a new record.
4. Use View Students to see active records.
5. Use Edit Student to update an existing record.
6. Use Find Student or Filter Students to locate relevant records.
7. Use Delete Student to move a record to the Recycle Bin after confirmation.
8. Open Recovery to view and restore deleted records.
9. Use Logout when finished.
Testing and quality assurance
The team developed tests and performed feature reviews during development. The project includes test modules for areas such as database operations, forms, analytics, authentication, dashboard behavior and student updates/deletion. Integration checks are particularly important because features developed in separate modules are brought together in app.py.

Where pytest is installed and configured, run tests from the project directory with:
python -m pytest
The complete merged version should be verified for login, add/view/edit, Find, Filter, deletion, restoration and dashboard updates. This document does not report an overall test pass rate, because a verified result for the final merged code has not been supplied.
Security, privacy and responsible use
The system processes student information, so data protection is an important part of the design:
- Access to the main interface is controlled by a login flow.
- Student forms validate input before database updates.
- Student search and database operations use SQL parameters where implemented, reducing SQL-injection risk.
- Deletion requires confirmation, with a Recycle Bin designed to make accidental deletion recoverable.
- Local databases, backup copies, credentials and personal student records should not be committed to the repository or shared publicly.
- Database backup remains a separate manual responsibility; the Recycle Bin is not a substitute for a complete backup.
Additional controls would be necessary before using the application with real student information in a production environment.

Team contributions
Team member	Main areas of contribution
Bidya Kumari Nath	Main Streamlit dashboard and user interface, feature integration, student recovery functionality and project documentation
Rupa Gurung	Student forms, input validation, Filter Students functionality and interface review
Manisha Karki	Database operations, authentication, Find Student functionality and backend integration review
Shreya Shah	Performance analytics, automated testing and team class diagram


The application is a shared team project. Team members also participated in planning, reviews, GitHub collaboration, issue tracking and project documentation.
Development approach
The project followed an iterative Agile approach. The team identified requirements, divided work into components, maintained tasks in Jira, developed code in GitHub branches and brought features together through integration and review. The completed system combines database and CRUD operations, analytics, dashboard interfaces, authentication, Find, Filter and student recovery in a single application.
Current limitations and possible improvements
- The application uses a local SQLite database, rather than a hosted multi-user database.
- Database backups are manual; automatic backups and full database restoration are future improvements.
- A restored student ID may conflict with an active record, requiring manual review.
- Additional end-to-end tests, account administration, access roles and audit logging would strengthen the system.
- A production deployment would require further security, privacy and operational work.
- 
Conclusion
The Student Performance Tracking System brings student record management and performance monitoring together in a simple modular application. Its dashboard, validation, authentication, search, filtering and Recycle Bin features demonstrate how Python, Streamlit and SQLite can be combined to support practical data management. The project also demonstrates collaborative software development, integration and testing using Agile teamwork.

Developed by: Bidya Kumari Nath, Rupa Gurung, Manisha Karki and Shreya Shah
Course: Agile Development Team Project (CTEC2713)
Institution: Niels Brock, Copenhagen

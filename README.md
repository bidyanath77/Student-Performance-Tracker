# Student Performance Tracking System

**Agile Development Team Project (CTEC2713)**  
**Niels Brock, Copenhagen**

## About the Project

The Student Performance Tracking System is a Python application that helps users manage and review student performance information in one place.

Built with Streamlit and SQLite, it supports student record management, performance analysis, search and filtering, login protection, and restoration of deleted records.

The project was developed collaboratively by a four-member Computer Science team using Agile practices, GitHub for version control, and Jira for task management.

## Project Objectives

- Provide a clear interface for entering and maintaining student information.
- Make marks, attendance and study hours easier to monitor and understand.
- Present performance summaries and visualisations on a dashboard.
- Help users locate and filter student records efficiently.
- Protect access to student information through authentication.
- Reduce the risk of accidental data loss through a Recycle Bin and separate manual database backups.

## Main Features

### 1. Authentication

The application displays a login form before the main dashboard. Authentication is handled through the `login.py` and `auth.py` modules.

A logout option ends access to the current application session.

### 2. Student Record Management

Users can:

- **Add students** with names, marks, attendance and study hours.
- **View students** in a table of active records.
- **Edit students** to correct or update existing information.
- **Delete students** with confirmation. The deletion workflow moves records into the Recycle Bin rather than immediately discarding them.

Form validation checks that:

- Names are present and at most 100 characters.
- Marks are between 0 and 100.
- Attendance is between 0 and 100.
- Study hours are between 0 and 24.

### 3. Performance Dashboard and Analytics

The dashboard displays:

- Total number of students
- Average marks
- Average attendance
- Average study hours
- Student records table
- Student marks comparison chart
- Individual student performance details

The dashboard uses Pandas for tabular data, Plotly for visualisations, and `analytics.py` for summary calculations.

### 4. Find Student

Users can search for students by student ID or full or partial name.

Name matching handles differences in capitalisation and extra spaces.

The search logic is implemented in `find.py` and made available through the main Streamlit interface.

### 5. Filter Students

Users can filter students by:

- Marks range
- Attendance range
- Minimum study hours

The filtering logic and interface are implemented in `filter_students.py`.

### 6. Student Recovery (Recycle Bin)

The Recovery interface shows deleted student records and allows users to restore selected records after confirmation.

Deleted records are stored in the `deleted_students` table within the application's SQLite database, with a deletion timestamp.

Restoration checks whether the student ID is already used by an active record. If there is a conflict, the existing record is not overwritten, and the issue requires manual review.

### 7. Manual Database Backup

A separate SQLite backup can be retained to protect against broader database loss.

This is a **manual backup process**, not a scheduled or automated feature.

It is distinct from the Recycle Bin, which restores individual deleted students within the application.

## Technologies and Tools

| Technology | Purpose |
|---|---|
| Python | Application and business logic |
| Streamlit | User interface and dashboard |
| SQLite | Student database |
| Pandas | Data handling |
| Plotly | Performance charts |
| Git and GitHub | Version control and collaboration |
| Jira | Sprint planning and task tracking |
| VS Code | Development environment |

## Project Structure

```text
Student-Performance-Tracker/
├── app.py
├── analytics.py
├── auth.py
├── login.py
├── database.py
├── forms.py
├── find.py
├── filter_students.py
├── recovery.py
├── requirements.txt
├── README.md
└── test_*.py
```

**Main module responsibilities:**

| File | Responsibility |
|---|---|
| `app.py` | Main application, navigation and dashboard |
| `analytics.py` | Performance summary calculations |
| `auth.py` | Authentication logic |
| `login.py` | Login interface |
| `database.py` | Database setup and student CRUD operations |
| `forms.py` | Student forms and input validation |
| `find.py` | Find students by ID or name |
| `filter_students.py` | Filtering logic and interface |
| `recovery.py` | Recycle Bin and restore operations |
| `requirements.txt` | Python dependencies |
| `test_*.py` | Component and application tests |

Local database files and backups should be kept out of shared Git commits, especially when they contain student information.

## System Architecture

The application follows a modular structure with three main layers.

**1. Presentation Layer**

`app.py` provides Streamlit navigation, dashboard views and access to other user interfaces.

The modules `login.py`, `forms.py`, `filter_students.py` and `recovery.py` also provide interface elements.

**2. Application Logic Layer**

- `analytics.py` calculates performance metrics.
- `find.py` performs student searches.
- `auth.py` handles authentication.
- `recovery.py` implements record restoration.

**3. Data Layer**

`database.py` manages the primary SQLite student records. Feature modules also use SQLite queries where appropriate.

### Database Structure

The main `students` table contains:

| Field | Description |
|---|---|
| `student_id` | Unique identifier for a student |
| `student_name` | Name of the student |
| `marks` | Numerical mark (0–100) |
| `attendance` | Attendance percentage (0–100) |
| `study_hours` | Study hours (0–24) |

The `deleted_students` table retains corresponding student details and a `deleted_at` timestamp for records moved to the Recycle Bin.


## Installation and Setup

### Prerequisites

- Python installed
- Git (if cloning the repository)
- Access to the internet to download dependencies

### Step 1: Clone the Repository

```bash
git clone https://github.com/bidyanath77/Student-Performance-Tracker.git
cd Student-Performance-Tracker
```

This repository is public and can be cloned without requesting access.

### Step 2: Create and Activate a Virtual Environment

**Windows (PowerShell)**

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS or Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 4: Create a Login Account

Before accessing the application, create your own local account:

```bash
python setup_demo_user.py
```

Enter a username and a password containing at least 12 characters.

The account will be created in your local SQLite database. Passwords are stored as salted hashes rather than plaintext.

For demonstration and assessment purposes, users can create their own local demo account to explore the Student Performance Tracking System. No login credentials are provided in the public repository.

### Step 5: Run the Application

```bash
python -m streamlit run app.py
```

Open the local URL displayed by Streamlit, normally:

`http://localhost:8501`

Log in using the username and password you created in Step 4.

The application initialises the main student table when it starts. The Recycle Bin table is created when its functionality is accessed.


## Using the Application

1. Log in to access the system.
2. Visit **Dashboard** to review overall performance and charts.
3. Use **Add Student** to create a new record.
4. Use **View Students** to see active records.
5. Use **Edit Student** to update an existing record.
6. Use **Find Student** or **Filter Students** to locate relevant records.
7. Use **Delete Student** to move a record to the Recycle Bin after confirmation.
8. Open **Recovery** to view and restore deleted records.
9. Use **Logout** when finished.

## Testing and Quality Assurance

The team developed tests and performed feature reviews during development.

The project includes tests for areas such as:

- Database operations
- Student forms and validation
- Performance analytics
- Authentication
- Dashboard behaviour
- Student updates and deletion
- Find and Filter functionality
- Student Recovery

Integration testing is particularly important because features developed in separate modules are brought together in `app.py`.

Where pytest is installed and configured, tests can be run from the project directory using:

```bash
python -m pytest
```

The complete merged version should be verified for login, adding and viewing students, editing, Find, Filter, deletion, restoration and dashboard updates.

An overall test pass rate is not reported here because a verified result for the final merged version has not been supplied.

## Security, Privacy and Responsible Use

The system processes student information, so data protection is an important part of the design.

- Access to the main interface is controlled by a login flow.
- Student forms validate input before database updates.
- Student search and database operations use SQL parameters where implemented, reducing SQL injection risk.
- Deletion requires confirmation, with a Recycle Bin designed to make accidental deletion recoverable.
- Local databases, backup copies, credentials and personal student records should not be committed to the repository or shared publicly.
- Database backup remains a separate manual responsibility.
- The Recycle Bin is not a substitute for a complete database backup.

Additional controls would be necessary before using the application with real student information in a production environment.

## Team Contributions

| Team Member | Main Areas of Contribution |
|---|---|
| **Bidya Kumari Nath** | Main Streamlit dashboard and user interface, feature integration, Student Recovery functionality and project documentation |
| **Rupa Gurung** | Student forms, input validation, Filter Students functionality and interface review |
| **Manisha Karki** | Database operations, authentication, Find Student functionality and backend integration review |
| **Shreya Shah** | Performance analytics, automated testing and team class diagram |

The application is a shared team project.

All team members participated in planning, reviews, GitHub collaboration, issue tracking and project documentation.

## Development Approach

The project followed an iterative Agile approach.

The team:

1. Identified the project requirements.
2. Divided the work into individual components.
3. Planned tasks and tracked progress in Jira.
4. Developed features using GitHub branches.
5. Integrated individual modules into the main application.
6. Conducted testing and reviewed issues.
7. Prepared final project documentation.

The completed system brings together database operations, student CRUD functionality, analytics, dashboard interfaces, authentication, Find, Filter and Student Recovery.

## Current Limitations and Possible Improvements

- The application uses a local SQLite database rather than a hosted multi-user database.
- Database backups are manual; automatic backups and full database restoration are future improvements.
- Restoring a deleted student may result in an ID conflict, requiring manual review.
- Additional end-to-end testing would strengthen the application.
- Account administration, access roles and audit logging could improve security and accountability.
- A production deployment would require further security, privacy and operational work.

## Conclusion

The Student Performance Tracking System brings student record management and performance monitoring together in a modular application.

Its dashboard, validation, authentication, search, filtering and Recycle Bin features demonstrate how Python, Streamlit and SQLite can support practical data management.

The project also demonstrates collaborative software development, integration and testing through Agile teamwork.

---

**Developed by:** Bidya Kumari Nath, Rupa Gurung, Manisha Karki and Shreya Shah  
**Course:** Agile Development Team Project (CTEC2713)  
**Institution:** Niels Brock, Copenhagen

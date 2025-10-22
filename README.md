Scube Automated Timesheet Management System
A complete web based employee timesheet and HR management platform for Scube Soft Solutions

Project Overview

The Scube Automated Timesheet Management System (ATMS) is a Django-based web application that helps employees and HR teams manage working hours, attendance, and timesheet approvals.

Employees can log their daily or weekly hours, view past submissions, and track work records.

HR users can review and approve timesheets, manage employee records, and generate reports.

The system is simple, secure, and built for scalability. It can later be expanded into a complete HR management suite.

Tech Stack
Frontend	HTML, CSS, JavaScript
Backend	Python Django
Database	SQLite (local), PostgreSQL (cloud)
Server	Gunicorn (for production)
Hosting	Render
Version Control	Git + GitHub
Editor	PyCharm

SETUP GUIDE (From Scratch)
This section explains everything a new team member needs to do — from installing Python and PyCharm, to running the project locally.

Step 1: Install Python
Go to https://www.python.org/downloads
Download the latest stable version (e.g., Python 3.11 or higher)
During installation:
  Check “Add Python to PATH”
  Then click Install Now
  To verify installation, open Command Prompt and run: python --version
  You should see something like Python 3.11.9

Step 2: Install PyCharm
Go to https://www.jetbrains.com/pycharm/download
Choose PyCharm Community Edition (Free)
Install it using the default setup wizard.
Once installed, open PyCharm.

Step 3: Install Git
Go to https://git-scm.com/downloads
Download and install Git for your OS.
Verify installation: git --version

git config --global user.name "Your Name"
git config --global user.email "you@example.com"

Step 4: Clone the Project from GitHub
Open GitHub and navigate to the repo:
https://github.com/scubesoftsolutions/Scube_Automated_Timesheets_Management_System
Copy the HTTPS clone link.

In PyCharm:
Click Get from VCS → paste the repo link → choose a folder → click Clone
OR
Run this in terminal:
git clone https://github.com/scubesoftsolutions/Scube_Automated_Timesheets_Management_System.git

Step 5: Create and Activate Virtual Environment
For Windows:
python -m venv .venv
.venv\Scripts\activate

For Mac/Linux:
python3 -m venv .venv
source .venv/bin/activate

You’ll know it’s active when you see (.venv) before your terminal prompt.

Step 6: Install Dependencies
pip install -r requirements.txt

This will install Django, Gunicorn, and all other required packages.

Step 7: Run the Project Locally
python manage.py runserver

You’ll see something like:
Starting development server at http://127.0.0.1:8000/

Now open that link in your browser to see the app running locally.

Step 8: Stopping the Server
Press CTRL + C in your terminal to stop the server.

TEAM WORKFLOW
This section explains how our GitHub branches, pull requests (PRs), and roles work.

Branch Structure
We follow a professional 5-branch flow:
feature → dev → test → cicd → pre-prod → main

Branch Roles:
Branch	Purpose
feature	Developers create new features or bug fixes here
dev	Developer testing branch – all features are merged here after PR approval
test	QA team tests the features here
cicd	Deployment test branch for CI/CD integration
pre-prod	Pre-production branch for final verification
main	Stable, production-ready branch (connected to Render live app)

How the Workflow Happens
Developers:
Pull the latest dev branch:
    git checkout dev
    git pull origin dev

Create a new feature branch:
    git checkout -b feature-new-login

Make code changes → test locally.

Add and commit your changes:
    git add .
    git commit -m "Added new login feature"

Push your branch to GitHub:
    git push -u origin feature-new-login

Create a Pull Request (PR) → target dev branch.

Once reviewed and approved → your code gets merged to dev.

Testers:
Pull the latest test branch:
    git checkout test
    git pull origin test

Verify features merged from dev.

Report bugs or confirm success.

Once testing is complete → notify the CI/CD admin.

CI/CD Team:

Pull test branch → merge into cicd for deployment testing.

If successful, merge into pre-prod.

After HR/PM final confirmation → merge into main.

Automatic Deployment

Render is connected to the main branch.

Whenever code is merged into main, Render automatically rebuilds and redeploys the live site.

All other branches are for testing and should not directly deploy.

Common Commands
Task	Command
Create virtual environment	python -m venv .venv
Activate environment	.venv\Scripts\activate
Install dependencies	pip install -r requirements.txt
Run Django app	python manage.py runserver
Create migrations	python manage.py makemigrations
Apply migrations	python manage.py migrate
Add static files	python manage.py collectstatic
Commit changes	git add . && git commit -m "message"
Push to GitHub	git push origin branch-name

Team Roles Summary
Role	Responsibilities
Developers	Build new features, fix bugs, create feature branches, raise PRs to dev
Testers	Test new features in test branch, validate bug fixes, ensure stability
CI/CD Engineer	Manage deployments between cicd → pre-prod → main
HR / PM	Approve final merges and monitor overall workflow

Live Project Link: https://scube-automated-timesheets-management-q1c3.onrender.com**

✅ In summary:
Anyone joining this project: developer, tester etc can now set up the system on their laptop, contribute safely using the branch model, and know exactly how the CI/CD flow delivers to production.

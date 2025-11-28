# OctoFit Tracker (minimal scaffold)

This directory contains a minimal scaffold for the OctoFit Tracker application used for development and testing.

Backend (Django)

- Project: `octofit-tracker/backend/octofit_tracker`
- A minimal Django app `tracker` exposes basic endpoints:
  - `GET /api/health/` — service health (JSON)
  - `GET /api/activities/` — placeholder activities list (JSON)

Quick start (from workspace root):

```bash
# create venv (if not already created)
python3 -m venv octofit-tracker/backend/venv
source octofit-tracker/backend/venv/bin/activate
pip install -r octofit-tracker/backend/requirements.txt

# run migrations
octofit-tracker/backend/venv/bin/python octofit-tracker/backend/manage.py migrate

# start dev server
octofit-tracker/backend/venv/bin/python octofit-tracker/backend/manage.py runserver 0.0.0.0:8000
```

Open http://localhost:8000/api/health/ to confirm the server is running.

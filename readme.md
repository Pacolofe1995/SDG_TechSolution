# Technical Solution

This repository contains the full implementation of the technical assessment proposed by **SDG Group** for the Backend Developer position.

## Technical Solution Overview

This project is the resolution of the technical exercise requested by SDG Group. While the initial requirement only mentions the implementation of a backend API, I have chosen to extend the solution by:

* ✅ Creating a small database (SQLite) to persist essential data such as users, topics, and subscriptions.
* ✅ Storing the SQL schema separately in a dedicated `/db` folder to clearly isolate database creation logic.
* ✅ Building a simple **Streamlit frontend** to interactively demonstrate how the API can be used in real scenarios:

  * Users can register and authenticate.
  * Authenticated users can view and manage their topic subscriptions.

This approach demonstrates best practices, such as clean separation of concerns and modular architecture, and showcases how RESTful APIs can be effectively consumed from a frontend client.

---

## Project Structure

The repository is organized in a clear, modular way. Both the **API** and **Frontend** components are self-contained with their own:

* `README.md`
* `requirements.txt`

```text
SDG/
├── API/                        # FastAPI backend
│   ├── app/
│   │   ├── api/routes/        # REST endpoints
│   │   ├── core/
│   │   │   ├── alchemy/       # DB connection + models
│   │   │   ├── classes/       # Business logic
│   │   │   ├── utils/         # Notification simulation
│   │   │   ├── config.py
│   │   │   └── security.py
│   │   ├── models.py          # Pydantic schemas
│   │   └── main.py            # API entry point
│   ├── resources/             # Sample files and videos
│   ├── database.db            # SQLite file
│   ├── requirements.txt
│   ├── Readme.md
│   └── .gitignore
│
├── FRONT/                     # Streamlit frontend
│   ├── app.py                 # Entry point
│   ├── pages/pagetopic.py     # Subscription manager
│   ├── requirements.txt
│   ├── Readme.md
│   └── .gitignore
│
├── db/                        # SQL schema scripts
│   └── create_tables.sql
│
└── README.md                  # General readme (this file)
```

---

## Objective

Build a **notification system** where:

* A **Publisher** can send notifications and retrieve subscriber data.
* A **Subscriber** can register and manage topic subscriptions to receive notifications.

> Notifications are transient and not stored.

The technologies used are modern, Python-based frameworks (FastAPI, Streamlit), as suggested in the assessment brief.

---

## ▶️ How to Run the System

To test the full application, both the backend and frontend must be running in parallel.

### 1. Backend Setup (FastAPI)

```bash
cd API
python -m venv .venv
.\.venv\Scripts\activate  # or source .venv/bin/activate on Linux
pip install -r requirements.txt
```
1. Click on "Run and Debug"
2. Click on "Create a launch.json file"
3. In the new window, select "Python Debugger"
4. Choose "FastAPI"
5. Set the path to your `main.py` file (e.g. `app/main.py`)
6. A `.vscode` folder will be created with a `launch.json` config file

<div style="background-color: #fff3cd; color: #856404; border: 1px solid #ffeeba; padding: 15px; border-radius: 8px; font-family: sans-serif; margin: 20px 0;">
  <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 10px;">
    ⚠️ <span><strong>Attention:</strong> When launching the API, press <strong>F5</strong> to refresh the page and start the service.</span>
  </div>
  <div>
    <ul style="margin: 0; padding-left: 20px;">
      <li><strong>Swagger UI:</strong> <a href="http://127.0.0.1:8000/api/v1/docs" target="_blank">http://127.0.0.1:8000/api/v1/docs</a></li>
      <li><strong>OpenAPI JSON:</strong> <a href="http://127.0.0.1:8000/api/v1/openapi.json" target="_blank">http://127.0.0.1:8000/api/v1/openapi.json</a></li>
    </ul>
  </div>
</div>

### 2. Frontend Setup (Streamlit)

In another terminal:

```bash
cd FRONT
python -m venv .venv
.\.venv\Scripts\activate  # or source .venv/bin/activate on Linux
pip install -r requirements.txt
streamlit run app.py
```

Once both services are running, you can:

* Create and log in with a user.
* Manage topic subscriptions.
* Trigger simulated notifications.

<video width="1280" height="720" controls>
  <source src="example.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>


# SDG API Project

The **SDG API** is a modern, simple, and modular interface built with **FastAPI**. It allows users to register, authenticate, and subscribe to topics of interest to receive personalized notifications. 

---

## Table of Contents

* [Project Structure](#project-structure)
* [Virtual Environment & Requirements](#virtual-environment--requirements)
* [Database Structure](#database-structure)
* [Initialization](#initialization)
* [Execution](#execution)
* [Main Endpoints](#main-endpoints)
* [Security](#security)
* [Notifications](#notifications)

---

## Project Structure

```text
app/
├── api/
│   ├── main.py                         # Main router
│   └── routes/                         # REST API routes
│       ├── home.py
│       ├── publisher.py    
│       └── subscribers.py  
├── core/   
│   ├── alchemy/                        # DB models and connection
│   │   ├── database.py
│   │   └── models.py   
│   ├── classes/                        # Business logic
│   │   ├── publisherClass.py   
│   │   └── suscriberClass.py   
│   ├── config.py                       # General settings
│   ├── security.py                     # Password hashing and validation
│   └── utils/
│       └── sendMailsNotifications.py   # Email notification simulator
├── models.py                           # Pydantic schemas
└── main.py                             # API entry point
```

---

## Virtual Environment & Requirements

Once the repository is cloned, we must create a virtual environment. Depending on the Python version, use one of the following commands:

```bash
python -m venv .venv

py -m venv .venv
```

Then, activate the virtual environment:

* On Windows:

```bash
.\.venv\Scripts\activate
```

* On Linux or macOS:

```bash
source .venv/bin/activate
```

Finally, install the dependencies listed in `requirements.txt`:

```bash
pip install -r .\requirements.txt  
```

---

## Database Structure

<div style="background-color: #fff3cd; color: #856404; border: 1px solid #ffeeba; padding: 15px; border-radius: 8px; font-family: sans-serif; margin: 20px 0;">
  <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 10px;">
    ⚠️ <span><strong>Attention:</strong> These are very basic tables where only primary keys are defined. For a robust relational structure, we should define proper foreign key constraints to relate  the tables</span>
  </div>

</div>

The SQLite database (`database.db`) contains **3 main tables**:

| Table                   | Description                                                                                                                                          |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| **suscribers**          | Stores user information: `name`, `email`, encrypted `password`, and `created_at`.                                                                    |
| **topics**              | Contains the available topics that users can subscribe to. Each row is a unique topic.                                                               |
| **subscription\_table** | A relational table linking users with their subscribed topics. Includes: `user_email`, `subscribed_topic`, `active`, `created_at`, and `updated_at`. |  



This structure enables easy management of user-topic subscriptions, and tracking their activation status.

---

## Initialization

To start the API in VSCode, follow the steps in the video below:

**Steps:**

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

<video width="1280" height="720" controls>
  <source src="resources/puestaenmarcha.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>

---

## Main Endpoints

### Users (Subscribers)

* `POST /api/v1/users` — Register a new user
* `POST /api/v1/users/login` — Log in
* `POST /api/v1/subscriptions/activate` — Activate a subscription
* `POST /api/v1/subscriptions/deactivate` — Deactivate a subscription

### Publisher

* `GET /api/v1/topics` — List all topics
* `GET /api/v1/users` — List all users
* `POST /api/v1/topics/{topic}/subscribers` — Get users by topic
* `POST /api/v1/users/{email}/subscriptions` — Get topics by user
* `POST /api/v1/notifications` — Notify all users
* `POST /api/v1/topics/{topic}/notifications` — Notify users by topic

### Home

* `GET /api/v1/` — Welcome message

---

## Security

* Passwords are encrypted using `bcrypt`
* Secure validation with `passlib`
* No plain text passwords are stored

---

## Notifications

* Simulated using `print()` and `time.sleep`


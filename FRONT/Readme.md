# SDG Topics Frontend

This is the **frontend interface** for the **SDG Topics Notification System**, built using [Streamlit](https://streamlit.io/). It interacts with a FastAPI backend to allow users to:

* 🔐 Register and authenticate
* 📬 Manage topic subscriptions
* ✅ Activate or deactivate notifications

---

## Table of Contents

* [Project Structure](#project-structure)
* [Requirements & Virtual Environment](#requirements--virtual-environment)
* [Execution](#execution)
* [Pages](#pages)
* [API Integration](#api-integration)
* [Notes](#notes)

---

## Project Structure

```text
FRONT/
├── pages/
│   └── pagetopic.py          # Subscription management page
└── app.py                    # Main app (login & register)
```

---

## Requirements & Virtual Environment

1. Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate     # Linux/macOS
.\.venv\Scripts\activate      # Windows
```

2. Install Requirements:

```bash
pip intall -r .\requirements.txt
```
---

## Execution



<div style="background-color: #fff3cd; color: #856404; border: 1px solid #ffeeba; padding: 15px; border-radius: 8px; font-family: sans-serif; margin: 20px 0;">
  <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 10px;">
    ⚠️ <span><strong>Attention:</strong> It is very important to have the .venv activated</span>
  </div>
</div>
Run the app using:

```bash
streamlit run app.py
```

Once started, it will open automatically in your browser.

---

## Pages

The Streamlit frontend includes two main screens:

### `app.py`

* 🔐 **Login/Register** tabs
* Stores user session in `st.session_state`
* Redirects authenticated users to `pagetopic.py`

### `pages/pagetopic.py`

* Displays user's current subscriptions
* Allows toggling subscription status (active/inactive)
* Fetches data from the FastAPI backend

---

## API Integration

This app expects a running backend API (FastAPI) at:

```
http://127.0.0.1:8000/api/v1
```

Make sure the backend is running **before** launching the frontend. The app interacts with endpoints like:

* `POST /users/login`
* `POST /users`
* `POST /subscriptions/activate`
* `POST /subscriptions/deactivate`
* `POST /users/{email}/subscriptions`

---

## Notes

* 🔐 All session data is stored in `st.session_state`
* ⚠️ No actual authentication tokens are used — this is for simulation purposes only



import streamlit as st
import requests
import json
import time

# ✅ This must be the first Streamlit call
st.set_page_config(page_title="SDG-Group-Topics", page_icon="🔐", layout="centered")

# 🔒 Hide sidebar after set_page_config.
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            display: none;
        }
        [data-testid="stSidebarNav"] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)

st.title("SDG Group Topics")

apiUrl = "http://127.0.0.1:8000/api/v1"

# 🔄 Auto-redirect after successful login
if "redirectToPage" in st.session_state and st.session_state.redirectToPage:
    pageToRedirect = st.session_state.redirectToPage
    st.session_state.redirectToPage = None  # Clear to prevent loop
    st.switch_page(f"pages/{pageToRedirect}.py")

if "email" not in st.session_state:
    st.session_state["email"] = None

# 🔐 Check if already authenticated
if "authenticated" in st.session_state and st.session_state.authenticated:
    st.success("✅ You are already authenticated")
    if st.button("Go to Main Page"):
        st.switch_page("pages/pagetopic.py")
    st.stop()

tabs = st.tabs(["Login", "Register"])

# TAB 1: LOGIN
with tabs[0]:
    st.subheader("Login")
    with st.form("loginForm"):
        loginEmail = st.text_input("Email")
        loginPassword = st.text_input("Password", type="password")
        loginSubmit = st.form_submit_button("Login")

    if loginSubmit:
        if not loginEmail or not loginPassword:
            st.warning("⚠️ Please fill in all fields.")
        else:
            payload = {
                "email": loginEmail,
                "password": loginPassword
            }

            st.session_state["email"] = payload["email"]

            try:
                with st.spinner("Verifying credentials..."):
                    response = requests.post(f"{apiUrl}/users/login", json=payload)
                    try:
                        data = response.json()
                    except Exception:
                        data = response.text

                if response.status_code == 200:
                    st.success("✅ Login successful. Redirecting...")

                    st.session_state["authenticated"] = True
                    st.session_state["userEmail"] = loginEmail
                    if isinstance(data, dict) and "user_data" in data:
                        st.session_state["userData"] = data["user_data"]

                    st.session_state["redirectToPage"] = "pagetopic"

                    time.sleep(1)

                    st.rerun()

                else:
                    if isinstance(data, dict):
                        detail = data.get("detail") or data.get("content") or str(data)
                    else:
                        detail = str(data)
                    st.error(f"❌ {detail}")

            except requests.exceptions.ConnectionError:
                st.error("🔌 Connection error: Cannot connect to API server")
            except requests.exceptions.Timeout:
                st.error("⏱️ Error: Request timed out")
            except Exception as e:
                st.error(f"🔌 Unexpected error: {e}")

# TAB 2: REGISTER
with tabs[1]:
    st.subheader("Create an Account")
    with st.form("registerForm"):
        registerName = st.text_input("Full Name")
        registerEmail = st.text_input("Email")
        registerPassword = st.text_input("Password", type="password")
        registerPasswordConfirm = st.text_input("Confirm Password", type="password")
        registerSubmit = st.form_submit_button("Register")

    if registerSubmit:
        if not registerName or not registerEmail or not registerPassword:
            st.warning("⚠️ Please fill in all fields.")
        elif registerPassword != registerPasswordConfirm:
            st.error("❌ Passwords do not match.")
        elif len(registerPassword) < 6:
            st.warning("⚠️ Password must be at least 6 characters long.")
        else:
            payload = {
                "name": registerName,
                "email": registerEmail,
                "password": registerPassword
            }

            try:
                with st.spinner("Creating account..."):
                    response = requests.post(f"{apiUrl}/users", json=payload)
                    try:
                        data = response.json()
                    except Exception:
                        data = response.text

                if response.status_code == 200:
                    if isinstance(data, dict):
                        msg = data.get("content", "User successfully registered.")
                    else:
                        msg = str(data)
                    st.success(f"✅ {msg}")
                    st.info("👆 You can now log in with your new account.")
                else:
                    if isinstance(data, dict):
                        detail = data.get("content") or data.get("detail") or str(data)
                    else:
                        detail = str(data)
                    st.error(f"❌ {detail}")

            except requests.exceptions.ConnectionError:
                st.error("🔌 Connection error: Cannot connect to API server")
            except requests.exceptions.Timeout:
                st.error("⏱️ Error: Request timed out")
            except Exception as e:
                st.error(f"🔌 Unexpected error: {e}")

# 📋 Footer information
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666; font-size: 0.8em;'>
        🔐 Secure Authentication System
    </div>
    """,
    unsafe_allow_html=True
)
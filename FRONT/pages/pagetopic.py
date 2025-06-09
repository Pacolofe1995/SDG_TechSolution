import streamlit as st
import requests
import json

def getUserSubscriptions(email):
    """
    Retrieves the user's subscriptions from the API.
    """
    try:
        url = f"http://127.0.0.1:8000/api/v1/users/{email}/subscriptions"
        body = {"email": email}
        response = requests.post(url, json=body)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching subscriptions: {e}")
        return []
    except json.JSONDecodeError as e:
        st.error(f"Error decoding JSON response: {e}")
        return []

def updateSubscription(subscriptionId, isActive):
    """
    Calls the endpoint to activate or deactivate the subscription based on the desired status.
    """
    if isActive:
        url = "http://127.0.0.1:8000/api/v1/subscriptions/activate"
    else:
        url = "http://127.0.0.1:8000/api/v1/subscriptions/deactivate"

    payload = {"id": subscriptionId}
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error updating subscription: {e}")
        return None

# --- PAGE START ---
st.title("🔔 My Subscriptions")
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

# Check if email exists in session_state
if "email" not in st.session_state or not st.session_state["email"]:
    st.error("User email not found. Please log in.")
    st.stop()

email = st.session_state["email"]
st.write(f"**User:** {email}")

# Get subscriptions
with st.spinner("Loading subscriptions..."):
    subscriptions = getUserSubscriptions(email)

if not subscriptions:
    st.info("You currently have no subscriptions.")
else:
    st.divider()
    st.subheader("Manage your subscriptions:")

    for subscription in subscriptions:
        col1, col2 = st.columns([3, 1])
        with col1:
            topic = subscription["subscribed_topic"]
            emojiMap = {
                "Tech": "💻",
                "Science": "🔬",
                "Environment": "🌱",
                "Health": "⚕️"
            }
            emoji = emojiMap.get(topic, "📌")
            st.write(f"{emoji} **{topic}**")
        with col2:
            currentStatus = subscription["active"]
            toggleKey = f"toggle_{subscription['id']}"
            newStatus = st.toggle(
                "Active",
                value=currentStatus,
                key=toggleKey,
                help=f"Toggle subscription to {topic}"
            )
            if newStatus != currentStatus:
                with st.spinner(f"Updating {topic}..."):
                    updateSubscription(subscription["id"], newStatus)
                    st.success(f"Subscription to {topic} {'activated' if newStatus else 'deactivated'}")
                    st.rerun()
        st.divider()

    activeCount = sum(1 for sub in subscriptions if sub["active"])
    totalCount = len(subscriptions)
    st.write(f"**Total:** {totalCount} subscriptions | **Active:** {activeCount} | **Inactive:** {totalCount - activeCount}")

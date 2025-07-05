
import streamlit as st
import pandas as pd

# Sample data
orders = pd.DataFrame({
    'Order ID': ['001', '002', '003'],
    'Customer': ['John Doe', 'Alice Smith', 'Mike Lee'],
    'Item': ['iPhone 16', 'Galaxy S22', 'MacBook Air'],
    'Status': ['Delivered', 'In Transit', 'Refunded'],
    'Refund Requested': ['Yes', 'No', 'Yes']
})

# Set page config
st.set_page_config(page_title="Omega Refund Dashboard", layout="wide")

# Inject custom space-blue theme with dark background
st.markdown("""
    <style>
    body {
        background-color: #0d1b2a;
        color: #e0e1dd;
    }
    .css-18e3th9 {
        background-color: #1b263b;
    }
    .css-1d391kg {
        background-color: #415a77 !important;
        color: #ffffff;
    }
    .stButton>button {
        background-color: #778da9;
        color: white;
        border-radius: 8px;
        height: 3em;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🚀 Omega Refund Dashboard")
st.markdown("Welcome to the live *Omega-tier* dashboard with space-blue UI and tracking intelligence.")

# Orders Table
st.subheader("📋 Orders Overview")
st.dataframe(orders)

# Manual Refund Section
st.subheader("🔧 Manual Refund Control")
selected_order = st.selectbox("Select Order ID", orders['Order ID'])
if st.button("Mark as Refunded"):
    st.success(f"Order {selected_order} has been marked as refunded.")

# Upload proof
st.subheader("🧾 Upload Proof / Receipt")
uploaded_file = st.file_uploader("Upload a file for this order:", type=['png', 'jpg', 'jpeg', 'pdf'])
if uploaded_file:
    st.success("File uploaded successfully!")

# Tracking input + simulated live lookup
st.subheader("🚚 Courier Tracker (Live Preview)")
tracking = st.text_input("Enter Tracking Number")
if tracking:
    st.info(f"Tracking {tracking}... Fetching real-time data from courier API (placeholder).")
    st.warning(f"Order {selected_order} has been flagged as LOST IN TRACKING based on tracking inactivity.")

# Analytics
st.subheader("📊 Refund Stats Summary")
refund_count = (orders['Refund Requested'] == 'Yes').sum()
st.metric(label="Total Refund Requests", value=refund_count)

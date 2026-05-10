
import streamlit as st

# Page configuration
st.set_page_config(page_title="Streamlit Reviewer Demo", icon="🚀")

st.title("📊 Data Processor Apps")
st.markdown("This app demonstrates a functional UI for the automated pipeline to review.")

# Sidebar for inputs
st.sidebar.header("Settings")
user_name = st.sidebar.text_input("Enter your name", "Developer")

# Main UI logic
if st.button("Click to Process"):
    st.balloons()
    st.success(f"Hello {user_name}! The app is running correctly.")
    
    # Simple data display
    data = {"Metric A": 10, "Metric B": 20, "Metric C": 30}
    st.write("### Current Metrics", data)
else:
    st.info("Click the button above to trigger the app logic.")

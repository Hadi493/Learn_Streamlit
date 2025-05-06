import streamlit as st  # type: ignore
import numpy as np
import pandas as pd
from datetime import datetime

# Set the page title
st.set_page_config(page_title="Learning Project", layout="wide")

# Sidebar with navigation
st.sidebar.title("Navigation")
sidebar_options = ["🏠 Home", "ℹ️ About", "📊 Dashboard", "⚙️ Settings"]
selected_page = st.sidebar.radio("Go to", sidebar_options)

# Sidebar info with expander (clean UI)
with st.sidebar.expander("About this Project"):
    st.info("This is a learning project to demonstrate Streamlit's column and sidebar features.")

# Main content title
st.title(f"{selected_page.split(' ')[1]} Page")  # Strip emoji for title

# Using columns for layout
if "Home" in selected_page:
    st.write("Welcome to our Streamlit Learning Project!")

    col1, col2 = st.columns(2)

    with col1:
        st.header("Column 1")
        st.write("This is the left column of our layout.")
        st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=200)

    with col2:
        st.header("Column 2")
        st.write("This is the right column of our layout.")
        st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

elif "About" in selected_page:
    st.write("This is a demonstration of Streamlit's layout capabilities.")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("Columns")
        st.write("Streamlit allows you to organize content in columns.")

    with col2:
        st.header("Sidebar")
        st.write("The sidebar provides navigation and controls.")

    with col3:
        st.header("Widgets")
        st.write("Interactive elements to make your app dynamic.")

elif "Dashboard" in selected_page:
    st.write("Here's a sample dashboard layout:")

    # Top metrics
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Users", "100", "+5%")
    col2.metric("Sessions", "324", "+12%")
    col3.metric("Bounce Rate", "42%", "-2%")
    col4.metric("Avg. Time", "2m 34s", "+7%")

    # Charts section
    st.subheader("Data Visualization")
    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:
        st.write("Line Chart Example")
        chart_data = pd.DataFrame(
            np.random.randn(20, 3),
            columns=pd.Index(["A", "B", "C"])
        )
        st.line_chart(chart_data)



    with chart_col2:
        st.write("Bar Chart Example")
        chart_data = pd.DataFrame(
        np.random.randn(50, 3),
        columns=["X", "Y", "Z"]  # type: ignore
    )
    st.bar_chart(chart_data)

elif "Settings" in selected_page:
    st.write("Configure your application settings:")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Display Settings")
        theme = st.selectbox("Theme", ["Light", "Dark", "System Default"])
        show_animations = st.checkbox("Enable animations", True)
        language = st.selectbox("Language", ["English", "Spanish", "French", "German"])

    with col2:
        st.subheader("User Preferences")
        notifications = st.checkbox("Enable notifications", False)
        auto_refresh = st.checkbox("Auto-refresh data", True)
        refresh_rate = st.slider("Refresh rate (seconds)", 5, 60, 30)

    st.button("Save Settings")

# Footer with columns
st.markdown("---")
footer_col1, footer_col2, footer_col3 = st.columns(3)
current_year = datetime.now().year
with footer_col1:
    st.markdown(f"© {current_year} Learning Project")
with footer_col2:
    st.markdown("Created with Streamlit")
with footer_col3:
    st.markdown("[GitHub](https://github.com) | [Documentation](https://docs.streamlit.io)")

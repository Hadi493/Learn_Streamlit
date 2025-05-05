import streamlit as st  # type: ignore

st.title("Green app maker")

if st.button("Green app maker"):
    st.success("Your app has been created")

add_feture = st.checkbox("Add a feture")

if add_feture:
    st.success("Your feture has been added")

app_type = st.radio("Pick Your app base: ", [
    "Social Media", "Personal", "Chat app", "Others"
])
st.write(f"Selected base: {app_type}")

feture = st.selectbox("Select feture: ", [
    "AI", "Chat", "Animated navbar", "3D model", "Animated logo"
])

st.write(f"Selected feture: {feture}")

app_pages = st.slider("Page count: ", 0, 10, 3)
st.write(f"Selected Page Count: {app_pages}")

app_name = st.text_input("Enter your app name")
st.write(f"Your app name is : {app_name}")

dob = st.date_input("Enter your date of birth")
st.write(f"Your date of birth is : {dob}")

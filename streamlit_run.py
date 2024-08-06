import streamlit as st

st.set_page_config(page_title="Registration Form", layout="centered")
st.title("Registration Form")

with st.form(key="registration_form"):
    name = st.text_input(label="Full Name", placeholder="Enter your full name", key="name")
    email = st.text_input(label="Email Address", placeholder="Enter your email address", key="email")

    submit_button = st.form_submit_button(label="Submit")

if submit_button:
    if name and email:
        st.success(f"Thank you for registering, {name}!")
    else:
        st.error("Please fill in all the required fields.")

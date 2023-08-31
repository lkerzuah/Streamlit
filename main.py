import streamlit as st
import pandas as pd

st.write("Welcome to my Sample Data collection  App!")

age = st.text_input("What is your age?",
            value="",
            placeholder="Please enter your age here correctly",)

## basic error handling
if age != "":
    try:
        age = float(age)
        if age > 12:
            name = st.text_input("What is your full name:",
                            value="",
                            placeholder="Enter your full name")
            sex = st.selectbox(label="Gender", options=["Male", "Female"])
            phone_number =  st.number_input("Enter your phone number:")
            father_name = st.text_input("what's your father name?",
                                        placeholder="Enter father's name")
            mother_name = st.text_input("what's your mother name?",
                                        placeholder="Enter Mother's name")
            address = st.text_input("where do you live? ",
                                    placeholder="Enter your current address")
            img_file_buffer = st.camera_input("Take a picture")

            if img_file_buffer is not None:
                # To read image file buffer as bytes:
                bytes_data = img_file_buffer.getvalue()
                # Check the type of bytes_data:
                # Should output: <class 'bytes'>
                st.write(type(bytes_data))

            if name != "":
                if st.button("submit", type="primary"):
                    st.write(f"{name}, " "Thanks for your time")
        else:
            st.write("You are not qualified for this suvrey")
    except:
        st.error("Please enter a valid age")











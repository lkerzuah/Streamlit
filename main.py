import streamlit as st
import pandas as pd

primaryColor="#F63366"
backgroundColor="#FFFFFF"

st.title("My Sample Data collection  App!")

age = st.text_input("What is your age?",
            value="",
            placeholder="Please enter your age here correctly",)

st.caption("This suvery is only for age 13 and above.")
if st.button("Next"):
    have_it = age.lower() in age
    
## basic error handling
if age != "":
    try:
        age = float(age)
        if age > 12:
            name = st.text_input("What is your full name:",
                            value="",
                            placeholder="Enter your full name")
            sex = st.selectbox(label="Gender", options=["Male", "Female"])
            phone_number =  st.text_input("Enter your phone number:",
                                          value="",
                                          placeholder="Enter your phone number")
            father_name = st.text_input("what's your father name?",
                                        placeholder="Enter father's name")
            mother_name = st.text_input("what's your mother name?",
                                        placeholder="Enter Mother's name")
            address = st.text_input("where do you live? ",
                                    placeholder="Enter your current address")
            if name != "":
                if st.button("submit", type="primary"):
                    st.success("This is a success message!", icon="✅")
                    st.write(f"{name}, " "Thanks for your time")
        else:
            st.write("You are not qualified for this suvrey")

    except:
        st.error("Please enter a valid age")










import streamlit as st
import json
import os

if st.button("Write JSON"):
    data = {"test": "data"}
    try:
        with open("https://github.com/PieRatCat/ml-streamlit/blob/383ad068b5cf9fd799e80b75e634c630415212b5/feedback.json", "w") as f:
            json.dump(data, f, indent=4)
        os.sync()
        st.success("JSON written successfully!")
    except IOError as e:
        st.error(f"Error: {e}")

st.write(f"Current working directory: {os.getcwd()}")

if os.path.exists("https://github.com/PieRatCat/ml-streamlit/blob/383ad068b5cf9fd799e80b75e634c630415212b5/feedback.json"):
    st.write("feedback.json exists")
else:
    st.write("feedback.json does not exist")
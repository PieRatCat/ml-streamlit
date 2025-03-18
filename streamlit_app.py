import streamlit as st
import os

port = int(os.environ.get("PORT", 8501))
# Define the pages
page_1 = st.Page("page_1.py", title="About project", icon=":material/home:")
page_2 = st.Page("page_2.py", title="App demo", icon=":material/draw:")
test = st.Page("test.py", title="Test", icon=":material/bug_report:")

# Set up navigation
pg = st.navigation([page_1, page_2, test])

# Run the selected page
pg.run()

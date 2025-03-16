#!/bin/bash

echo "Starting Streamlit app..."

# Log environment variables
env >> startup.log

# Run Streamlit
streamlit run test.py >> startup.log 2>&1

echo "Streamlit app started."
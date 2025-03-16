import streamlit as st
from streamlit_drawable_canvas import st_canvas
import pickle
import json
import os
from PIL import Image, ImageOps
import numpy as np

st.markdown(
    """
    <style>
    html, body {
        font-size: 18px;        
    }
    a {font-size: 20px;}
    </style>
    """,
    unsafe_allow_html=True
)
st.header('Handwritten digit recognition', divider="rainbow")

# Load the trained model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)
    
FEEDBACK_FILE = "feedback.json"

def load_feedback():
    if os.path.exists(FEEDBACK_FILE):
        with open(FEEDBACK_FILE, "r") as f:
            return json.load(f)
    else:
        return {"thumbs_up": 0, "thumbs_down": 0}

def save_feedback(feedback):
    try:
        with open(FEEDBACK_FILE, "w") as f:
            json.dump(feedback, f)
    except Exception as e:
        print(f"Error saving feedback: {e}")

st.markdown('''Draw a digit between 0 and 9. For best results, draw one digit at a time, try to use the entire canvas and center the digit. 
            Use the buttons under the canvas to erase or undo the last stroke. The accuracy of the result will vary depending on your handwriting style.''') 

canvas_result = st_canvas(
    stroke_width=20,
    stroke_color="#000000",
    background_color="#FFFFFF",
    display_toolbar=True,
    height=200,
    width=200
)

if canvas_result.image_data is not None:
    img = Image.fromarray(canvas_result.image_data.astype('uint8'), 'RGBA')
    gray_image = img.convert('L') # Convert to grayscale
    resized_image = gray_image.resize((28, 28), Image.Resampling.LANCZOS) # Resize
    inverted_image = ImageOps.invert(resized_image) # Invert
    normalized_image = np.array(inverted_image).astype('float32') / 255.0 # Normalize
    flattened_image = normalized_image.reshape(1, 784)
    
    prediction = model.predict(flattened_image)
        
    st.markdown(f"<p style='font-size: 30px;'>You wrote: {prediction[0]}</p>", unsafe_allow_html=True)

# Feedback buttons and counts

if "feedback_counts" not in st.session_state:
    st.session_state.feedback_counts = load_feedback()

if "feedback_counts" not in st.session_state:
    st.session_state.feedback_counts = {"thumbs_up": 0, "thumbs_down": 0}

left, middle, right = st.columns([1, 1, 3])

with left:
    if st.button(":material/thumb_up:"):
        st.session_state.feedback_counts["thumbs_up"] += 1
        save_feedback(st.session_state.feedback_counts) 
    st.write(f"Correct: {st.session_state.feedback_counts['thumbs_up']}")
with middle:
    if st.button(":material/thumb_down:"):
        st.session_state.feedback_counts["thumbs_down"] += 1
        save_feedback(st.session_state.feedback_counts) 
    st.write(f"Incorrect: {st.session_state.feedback_counts['thumbs_down']}")
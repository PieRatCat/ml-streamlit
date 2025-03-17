import streamlit as st
from streamlit_drawable_canvas import st_canvas
import joblib
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
model = joblib.load("model.joblib") 


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

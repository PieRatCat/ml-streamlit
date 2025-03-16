import streamlit as st

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

st.header('About this project', divider="rainbow")

st.subheader('Handwritten digit recognition') 
            
st.markdown('''This project demonstrates a machine learning model, 
            trained on <a href="https://openml.org/search?type=data&status=active&id=554" style="text-decoration: none;">mnist_784</a> dataset
            from <a href="https://openml.org/" style="text-decoration: none;">openml.org</a> to recognise handwritten digits from 0 to 9. 
            The model is trained using <a href="https://xgboost.readthedocs.io/en/stable/" style="text-decoration: none;">XGBoost</a> classifier. 
            User draws input on a canvas and the model predicts the digit. 
            The input is converted to greyscale, resized to 28x28 px, inverted, normalised and flattened before being fed to the model.''', unsafe_allow_html=True)



if st.button(":material/arrow_circle_right: Try the demo", type="secondary"):
    st.session_state.page_to_switch = "page_2.py"
    st.switch_page(st.session_state.page_to_switch)


st.subheader('The web app')

st.markdown('The python script running this web app is built using <a href="https://www.streamlit.io/" style="text-decoration: none;">Streamlit</a> library. Streamlit is an open-source app framework for Machine Learning and Data Science projects.', unsafe_allow_html=True)

st.markdown('The canvas component used in the app is <a href="https://github.com/andfanilo/streamlit-drawable-canvas" style="text-decoration: none;">Drawable Canvas</a> by <a href="https://github.com/andfanilo" style="text-decoration: none;">andfanilo</a>.', unsafe_allow_html=True)

st.subheader('About the author')

st.markdown('This project was created by Amanda Sumner for a machine learning course in March 2025.')

st.link_button("Find me here", "https://linktr.ee/PieRatCat")

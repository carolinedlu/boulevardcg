  
import streamlit as st
from PIL import Image

st.balloons()
st.markdown('**Hello Boulevard Consulting Group!**')
image = Image.open('Boulevard.png')
st.image(image)
st.markdown('We are very excited to be working with you.')

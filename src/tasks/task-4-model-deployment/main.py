import streamlit as st
from helper import *
st.title("French text classifier to detect online hate")

st.markdown(
    """
    The classifer detects whether the text falls under the following categories:
    The classifier detects which of the below classes the text belongs to:
    - bullying
    - hate-speech
    - homophobia
    - racism
    - non-toxic
    """
)
st.header("Enter a text in French")

user_input = st.text_area("Enter a french text to classify")

if st.button('Classify'):
    prediction, prob_val = classify(user_input)
    st.subheader("Classification")
    st.write("The text is classified as ",prediction)
    st.write("The probability score of each class",prob_val)
   

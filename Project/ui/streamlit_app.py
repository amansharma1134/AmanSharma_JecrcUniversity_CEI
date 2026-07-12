import streamlit as st

st.title("Memory Augmented Chatbot")

query=st.text_input("Ask Question")

if st.button("Submit"):

    st.write("Searching...")

    st.success("Answer Generated")

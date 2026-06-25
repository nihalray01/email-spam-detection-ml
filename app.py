import streamlit as st
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

st.title("📧 Email Spam Detector")

# Input box
input_msg = st.text_area("Enter your message")

if st.button("Check"):
    data = vectorizer.transform([input_msg])
    result = model.predict(data)[0]

    if result == 1:
        st.error("🚫 This is SPAM")
    else:
        st.success("✅ This is NOT SPAM")
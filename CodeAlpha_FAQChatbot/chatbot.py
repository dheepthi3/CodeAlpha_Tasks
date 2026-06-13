import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

faq = {
    "What is AI?": "AI stands for Artificial Intelligence.",
    "What is Python?": "Python is a programming language.",
    "What is Machine Learning?": "Machine Learning helps computers learn from data.",
    "What is Data Science?": "Data Science is the study of data."
}

questions = list(faq.keys())

st.title("🤖 FAQ Chatbot")

user_question = st.text_input("Ask a question:")

if user_question:
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(questions + [user_question])

    similarity = cosine_similarity(vectors[-1], vectors[:-1])
    best_match = similarity.argmax()

    st.success(faq[questions[best_match]])
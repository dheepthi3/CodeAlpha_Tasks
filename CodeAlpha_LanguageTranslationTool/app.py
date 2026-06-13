import streamlit as st
from deep_translator import GoogleTranslator

st.title("🌍 Language Translation Tool")

text = st.text_area("Enter Text")

source_lang = st.selectbox(
    "Source Language",
    ["auto", "english", "tamil", "hindi", "telugu"]
)

target_lang = st.selectbox(
    "Target Language",
    ["english", "tamil", "hindi", "telugu"]
)

if st.button("Translate"):
    translated = GoogleTranslator(
        source=source_lang,
        target=target_lang
    ).translate(text)

    st.success("Translated Text:")
    st.write(translated)
‎dictionary_cos101.py‎
Original file line number	Diff line number	Diff line change
@@ -0,0 +1,50 @@
import streamlit as st
languages = {
    "Hello": "Ndewo",
    "Thank you":"Imela",
    "Water":"Mmiri",
    "Food": "Nri",
    "Mother": "Nne",
    "Father": "Nna",
    "House": "Ulo",
    "Book": "Akwukwọ",
    "School": "Ụlọ akwụkwọ",
    "Child": "Nwa",
    "Man": "Mmadu nwoke",
    "Woman": "Mmadu nwanyi",
    "Sun": "Anwu",
    "Moon": "Onwa",
    "Star": "Kpakpando",
    "Love": "Ifunanya",
    "God": "Chukwu",
    "Friend": "Enyi",
    "Name": "Aha",
    "Market": "Ahia"
}
st.set_page_config(page_title="Local Language Translator", page_icon="🌍")
st.title(" Nigerian Language Dictionary")
st.write("Translate simple English words into local Nigerian languages.")
language_choice = st.selectbox(
    "Choose a language",
    list(languages.keys())
)
word = st.text_input("Enter a word").lower()
if st.button("Translate"):
    dictionary = languages[language_choice]
    if word in dictionary:
        st.success(f"**Translation:** {dictionary[word]}")
    else:
        st.error("Word not found in dictionary.")

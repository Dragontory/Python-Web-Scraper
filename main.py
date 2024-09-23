import streamlit as st

# Streamlit UI
st.title("AI Web Scraper")
url = st.text_input("Enter Website URL")

# Scrapes the Given Website
if st.button("Scrape Website"):
    st.write("Doing some cool stuff...")
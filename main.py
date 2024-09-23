import streamlit as st
from scrape import scrape_website

# Streamlit UI
st.title("AI Web Scraper")
url = st.text_input("Enter Website URL")

# Scrapes the Given Website
if st.button("Scrape Website"):
    st.write("Doing some cool stuff...")
    result = scrape_website(url)
    print(result)
import streamlit as st
from scrape import scrape_website, split_dom_content, clean_body_content, extract_body_content

# Streamlit UI
st.title("AI Web Scraper")
url = st.text_input("Enter Website URL")

# Scrapes the Given Website
if st.button("Scrape Website"):
    st.write("Doing some cool stuff...")

    result = scrape_website(url)
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)

    # Store the DOM content in Streamlit session state
    st.session_state.dom_content = cleaned_content

    # Display the DOM content in an expandable text box
    with st.expander("View DOM Content"):
        st.text_area("DOM Content", cleaned_content, height=300)
    
    
    
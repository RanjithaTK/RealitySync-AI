import streamlit as st

def show_response(title, content):
    st.subheader(title)
    # Support long text with markdown
    st.markdown(f"```\n{content}\n```")

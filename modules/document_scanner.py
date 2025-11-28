import streamlit as st
from core.image_processing import load_image, resize_for_model
from core.gemini_client import gemini_vision_call
from core.prompt_templates import DOCUMENT_SCAN_PROMPT
from core.utils import show_response

def scan_document():
    st.title("📄 Document Scanner")
    uploaded = st.file_uploader("Upload a document/photo of text", type=["jpg", "jpeg", "png", "pdf"])
    if uploaded:
        img = load_image(uploaded)
        st.image(img, width=600)

        if st.button("Extract & Summarize"):
            with st.spinner("Extracting text and summarizing..."):
                img_small = resize_for_model(img)
                result = gemini_vision_call(img_small, DOCUMENT_SCAN_PROMPT)
                show_response("Document Summary & Actions", result or "No result returned.")

import streamlit as st
from core.image_processing import load_image, resize_for_model
from core.gemini_client import gemini_vision_call
from core.prompt_templates import ENVIRONMENT_ANALYSIS_PROMPT
from core.utils import show_response

def analyze_environment():
    st.title("🏠 Environment Insights")
    uploaded = st.file_uploader("Upload a photo of the space / room", type=["jpg", "png", "jpeg"])
    if uploaded:
        img = load_image(uploaded)
        st.image(img, width=600)

        if st.button("Analyze Environment"):
            with st.spinner("Analyzing environment..."):
                img_small = resize_for_model(img)
                result = gemini_vision_call(img_small, ENVIRONMENT_ANALYSIS_PROMPT)
                show_response("Environment Insights", result or "No result returned.")

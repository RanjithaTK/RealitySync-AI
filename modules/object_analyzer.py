import streamlit as st
from core.image_processing import load_image, resize_for_model
from core.gemini_client import gemini_vision_call
from core.prompt_templates import OBJECT_ANALYSIS_PROMPT
from core.utils import show_response

def analyze_object():
    st.title("🔍 Object Analyzer")
    uploaded = st.file_uploader("Upload an image of an object", type=["jpg", "jpeg", "png"])
    if uploaded:
        img = load_image(uploaded)
        st.image(img, caption="Uploaded Image", use_column_width=False, width=420)

        if st.button("Analyze Object"):
            with st.spinner("Analyzing..."):
                img_small = resize_for_model(img)
                result = gemini_vision_call(img_small, OBJECT_ANALYSIS_PROMPT)
                show_response("Object Analysis", result or "No result returned.")

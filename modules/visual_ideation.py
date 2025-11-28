import streamlit as st
from core.image_processing import load_image, resize_for_model
from core.gemini_client import gemini_vision_call
from core.prompt_templates import VISUAL_IDEA_PROMPT
from core.utils import show_response

def generate_visual_concepts():
    st.title("🎨 Visual Ideation")
    uploaded = st.file_uploader("Upload an inspiration image", type=["jpg", "jpeg", "png"])
    if uploaded:
        img = load_image(uploaded)
        st.image(img, width=600)

        if st.button("Generate Visual Ideas"):
            with st.spinner("Generating concepts..."):
                img_small = resize_for_model(img)
                result = gemini_vision_call(img_small, VISUAL_IDEA_PROMPT)
                show_response("Creative Concept Output", result or "No result returned.")

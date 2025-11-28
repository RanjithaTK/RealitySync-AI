import streamlit as st
from core.image_processing import load_image, resize_for_model
from core.gemini_client import gemini_vision_call
from core.prompt_templates import SHOPPING_PROMPT
from core.utils import show_response

def shopping_compare():
    st.title("🛒 Shopping Assistant")
    uploaded = st.file_uploader("Upload product image", type=["jpg", "jpeg", "png"])
    if uploaded:
        img = load_image(uploaded)
        st.image(img, width=600)

        if st.button("Analyze & Suggest"):
            with st.spinner("Comparing and recommending..."):
                img_small = resize_for_model(img)
                result = gemini_vision_call(img_small, SHOPPING_PROMPT)
                show_response("Product Analysis", result or "No result returned.")

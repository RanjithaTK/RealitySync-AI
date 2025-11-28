import streamlit as st
from core.image_processing import load_image, resize_for_model
from core.gemini_client import gemini_vision_call
from core.prompt_templates import REPAIR_PROMPT
from core.utils import show_response

def troubleshoot_item():
    st.title("🛠 Repair Troubleshooter")
    uploaded = st.file_uploader("Upload image of damaged item", type=["jpg", "jpeg", "png"])
    if uploaded:
        img = load_image(uploaded)
        st.image(img, width=600)

        if st.button("Diagnose / Suggest Fixes"):
            with st.spinner("Diagnosing..."):
                img_small = resize_for_model(img)
                result = gemini_vision_call(img_small, REPAIR_PROMPT)
                show_response("Troubleshooting Results", result or "No result returned.")

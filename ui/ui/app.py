import streamlit as st
from ui.components import header, sidebar_menu
from modules.object_analyzer import analyze_object
from modules.environment_insights import analyze_environment
from modules.document_scanner import scan_document
from modules.repair_troubleshooter import troubleshoot_item
from modules.shopping_assistant import shopping_compare
from modules.visual_ideation import generate_visual_concepts

st.set_page_config(page_title="RealitySync AI", page_icon="🤖", layout="wide")
header()

page = sidebar_menu()

if page == "Object Analyzer":
    analyze_object()
elif page == "Environment Insights":
    analyze_environment()
elif page == "Document Scanner":
    scan_document()
elif page == "Repair Troubleshooter":
    troubleshoot_item()
elif page == "Shopping Assistant":
    shopping_compare()
elif page == "Visual Ideation":
    generate_visual_concepts()
else:
    st.write("Select a tool from the sidebar.")

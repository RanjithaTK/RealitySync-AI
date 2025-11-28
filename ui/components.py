import streamlit as st

def header():
    st.markdown("<style> .big-title { font-size:32px; font-weight:700;} </style>", unsafe_allow_html=True)
    st.markdown('<div class="big-title">🤖 RealitySync AI — Visual Intelligence Agent</div>', unsafe_allow_html=True)
    st.write("Point, snap, and get instant real-world intelligence — objects, environments, documents, and more.")

def sidebar_menu():
    return st.sidebar.radio(
        "Choose a tool",
        [
            "Object Analyzer",
            "Environment Insights",
            "Document Scanner",
            "Repair Troubleshooter",
            "Shopping Assistant",
            "Visual Ideation"
        ],
        index=0
    )

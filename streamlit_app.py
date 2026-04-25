import streamlit as st
import google.generativeai as genai
import os
from forensics import verify_standing_and_identity

st.title("Nomos True Secret: Forensic Command")

# Sidebar for the big moves
if st.sidebar.button("Execute Seizure of Truth"):
    st.header("Forensic Brief: Emergency Motion to Strike")
    
    # This runs the check from your forensics.py file
    audit_hits = verify_standing_and_identity("extracted_text", "roa_text")
    
    if audit_hits:
        st.success("Identity Glitches Detected. Generating Brief...")
        # Brief logic follows here...
    else:
        st.info("No credential glitches detected in this scan.")

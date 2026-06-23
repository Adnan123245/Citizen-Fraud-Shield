import streamlit as st
import google.genai as genai
from google.genai import types

# 1. Page Configuration & Custom Theme Integration
st.set_page_config(page_title="Citizen Fraud Shield", page_icon="🛡️", layout="centered")

# Eye-Catching Header Hero Banner using custom markdown cards
st.markdown("""
    <div style="background-color: #1F2937; padding: 25px; border-radius: 12px; border-left: 6px solid #FF4B4B; margin-bottom: 25px;">
        <h1 style="color: #FFFFFF; margin: 0; font-size: 2.2rem;">🛡️ Citizen Fraud Shield</h1>
        <p style="color: #9CA3AF; margin: 8px 0 0 0; font-size: 1.1rem;">
            Advanced AI Public Safety Interface against Organized Cyber-Scam Networks
        </p>
    </div>
""", unsafe_allow_html=True)

# 2. Sidebar Configuration Panel (API Input Removed)
st.sidebar.markdown("""
    <div style="background-color: #111827; padding: 15px; border-radius: 8px; border: 1px solid #374151;">
        <h4 style="color: #FF4B4B; margin: 0 0 10px 0;">🛡️ System Status</h4>
        <span style="color: #10B981; font-weight: bold;">● Core Defense Online</span>
    </div>
""", unsafe_allow_html=True)
st.sidebar.write("")

# Hidden API Credential Variable (Safe from the UI)
API_KEY = st.secrets["GEMINI_API_KEY"]

st.sidebar.markdown("""
---
### 📊 Live Evaluation Focus
* **Classification Target:** Organized Scam Rings
* **Target Metric:** Zero False-Negatives
* **Operational Mode:** Predictive Interception
""")

# 3. Instruction Callout Box
st.info("💡 Instructions: Copy and paste the suspicious text pattern, email body, or call log transcript below to execute an immediate safety forensic audit.")

# 4. Main User Input Layout
user_input = st.text_area(
    "📋 Input Investigation Payload:",
    placeholder="Example: Someone claiming to be a CBI officer called saying my Aadhaar card is linked to an illegal parcel...",
    height=150
)

st.markdown("")

# 5. Core System Prompt Logic Structure
SYSTEM_INSTRUCTION = """
You are an expert Cyber-Forensics Analyst and AI Investigator specialized in defeating digital fraud, 
phishing schemes, and organized 'digital arrest' scam operations. Your primary objective is to analyze 
user submissions for deceptive patterns, linguistic intimidation, fake authority cues, and illicit financial demands.

Provide a highly scannable audit using bold Markdown badges and warning layouts. Avoid standard text blocks. Include:
- **RISK VERDICT SCORE**: State the evaluation category instantly (e.g., [🚨 CRITICAL DANGER] or [🟢 SAFE]).
- **SCAM TECHNIQUE PROFILE**: Match against known structural playbooks (e.g., Digital Arrest Scam).
- **CRITICAL FORENSIC INDICATORS**: Provide a bulleted layout of exactly where they used deception or fear.
- **IMMEDIATE CITIZEN DEFENSE PLAN**: Provide 3 tactical steps. Emphasize reporting to cybercrime.gov.in.
"""

# 6. Interactive Trigger Core
if st.button(" Execute Forensic Scan", use_container_width=True):
    if user_input.strip() == "":
        st.warning(" Scanner Empty: Please provide a valid communication payload text sequence to analyze.")
    else:
        # Beautiful custom scan banner animation
        with st.spinner(" Running heuristics matching against active scam databases..."):
            try:
                # Initializing the client securely behind the scenes using our hidden variable
                client = genai.Client(api_key=API_KEY)
                
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=user_input,
                    config=types.GenerateContentConfig(
                        system_instruction=SYSTEM_INSTRUCTION,
                        temperature=0.2,
                    )
                )
                
                # Render beautifully segmented cards inside the layout
                st.markdown("""
                    <div style="background-color: #111827; padding: 15px; border-radius: 8px; border: 1px solid #10B981; margin-top: 20px; margin-bottom: 15px;">
                        <span style="color: #10B981; font-weight: bold; font-size: 1.2rem;">⚡ Scan Matrix Analysis Complete</span>
                    </div>
                """, unsafe_allow_html=True)
                
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"System core exception encountered during parsing run: {e}")
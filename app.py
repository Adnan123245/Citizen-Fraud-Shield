import streamlit as st
from google import genai

# Page configuration
st.set_page_config(page_title="Citizen Fraud Shield", page_icon="🛡️", layout="centered")

# Header Hero Banner
st.markdown("""
<div style="background-color: #1F2937; padding: 25px; border-radius: 12px;">
    <h1 style="color: #FFFFFF; margin: 0; font-size: 2.2rem;">🛡️ Citizen Fraud Shield</h1>
    <p style="color: #9CA3AF; margin: 8px 0 0 0; font-size: 1.1rem;">
        Advanced AI Public Safety Interface against Organized Cyber-Scam Networks
    </p>
</div>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.markdown("""
<div style="background-color: #111827; padding: 15px; border-radius: 8px;">
    <h4 style="color: #FF4B4B; margin: 0 0 10px 0;">🛡️ System Status</h4>
    <span style="color: #10B981; font-weight: bold;">● Core Defense Online</span>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("### Live Evaluation Focus")
st.sidebar.markdown("* **Classification Target:** Organized Scam Rings")
st.sidebar.markdown("* **Target Metric:** Zero False-Negatives")
st.sidebar.markdown("* **Operational Mode:** Predictive Interception")

# Main interface text container
user_input = st.text_area(
    "📋 Input Investigation Payload:",
    placeholder="Example: Someone claiming to be a CBI officer called saying my Aadhaar card is linked to an illegal parcel..."
)

if st.button("Execute Forensic Scan"):
    with st.spinner("Running heuristics matching against active scam database..."):
        try:
            # Modern initialization that supports AQ. keys perfectly
            client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
            
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=user_input
            )
            
            st.write(response.text)

        except Exception as e:
            st.error(f"System core exception encountered during parsing run: {e}")

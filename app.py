import streamlit as st

# Page Configuration
st.set_page_config(page_title="Piano Wave", page_icon="🎹")

# Custom CSS for a clean black background
st.markdown(
    """
    <style>
    /* Set the main background to black */
    .stApp {
        background-color: #000000;
    }
    
    /* Ensure all text is white for readability */
    h1, h2, h3, p, div {
        color: #FFFFFF !important;
    }
    
    /* Make the container centered and clean */
    .block-container {
        max-width: 700px;
        padding-top: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Content
st.title("🎹 Piano Wave")
st.markdown("### Where music meets tranquility.")

st.subheader("Latest Release")
# Replace the URL below with one of your actual video links
st.video("https://www.youtube.com/watch?v=YOUR_VIDEO_ID_HERE")

st.markdown("---")

st.write("Love the vibes? Check out the full channel:")
st.link_button("Go to Piano Wave YouTube Channel", "https://youtube.com/@pianowaveyt1")

import streamlit as st

# Page Configuration
st.set_page_config(page_title="Piano Wave YT", page_icon="🎹")

# Custom CSS for a clean black background
st.markdown(
    """
    <style>
    .stApp {
        background-color: #000000;
    }
    h1, h2, h3, p, div {
        color: #FFFFFF !important;
    }
    .block-container {
        max-width: 700px;
        padding-top: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Content
st.title("🎹 Piano Wave YT")
st.markdown("### Where music meets tranquility.")

st.subheader("Latest Release")

# Using your new video ID: nAz4uF2aVC8
video_id = "nAz4uF2aVC8"
embed_url = f"https://www.youtube.com/embed/{video_id}"

st.markdown(
    f"""
    <iframe width="100%" height="400" src="{embed_url}" 
    frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
    allowfullscreen></iframe>
    """, 
    unsafe_allow_html=True
)

st.markdown("---")

st.write("Love the vibes? Check out the full channel:")
st.link_button("Go to Piano Wave YT YouTube Channel", "https://youtube.com/@pianowaveyt1")

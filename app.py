import streamlit as st

st.set_page_config(page_title="Piano Wave YT", page_icon="🎹", layout="centered")

st.markdown(
    """
    <style>
    .stApp {
        background-color: #fcfcfc;
        color: #111111;
    }
    h1, h2, h3, p, div, span {
        color: #111111 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🎹 Piano Wave YT")
st.markdown("### Where music meets tranquility.")

st.subheader("Latest Release")
st.video("https://www.youtube.com/watch?v=YOUR_VIDEO_ID_HERE")

st.markdown("---")

st.write("Love the vibes? Check out the full channel:")
st.link_button("Go to Piano Wave YT YouTube Channel", "https://youtube.com/@pianowaveyt1")

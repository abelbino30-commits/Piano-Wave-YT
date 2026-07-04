import streamlit as st

# Page Configuration
st.set_page_config(page_title="Piano Wave YT", page_icon="🎹")

# Centering the content
st.title("🎹 Piano Wave YT")
st.markdown("### Where music meets tranquility.")

# Embed your YouTube Channel/Video
# Note: st.video works best with direct video links. 
# If you want to link your channel, we can use a button.
st.subheader("Latest Release")
st.video("https://www.youtube.com/watch?v=YOUR_VIDEO_ID_HERE")

st.markdown("---")

# Direct Call to Action
st.write("Love the vibes? Check out the full channel:")
st.link_button("Go to Piano Wave YT YouTube Channel", "https://youtube.com/@pianowaveyt1")

# Optional: Add some custom styling to make it look professional
st.markdown(
    """
    <style>
    .stApp {
        background-color: #fcfcfc;
    }
    </style>
    """,
    unsafe_allow_html=True
)

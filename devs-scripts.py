import streamlit as st
import matplotlib.font_manager as fm
import os

st.set_page_config(
    page_title="Dev's Streamlit App Hub",
    layout="centered",
    page_icon="🧰"
)

st.title("🧰 Dev's Streamlit App Hub")
st.markdown("A collection of simple, free, and open-source tools for everyday use. Code on Github and hosted on Streamlit.io cloud.")

# --- Font Registration ---
font_path = os.path.join(os.path.dirname(__file__), "PermanentMarker-Regular.ttf") # Assumes font is in the same directory
# If it's in a subfolder, e.g., "fonts", use:
# font_path = os.path.join(os.path.dirname(__file__), "fonts", "PermanentMarker-Regular.ttf")

try:
    font_manager = fm.fontManager
    font_manager.addfont(font_path)
    prop = fm.FontProperties(fname=font_path)
    font_name = prop.get_name()
except Exception as e:
    st.error(f"Error loading font: {e}. Using default font.")
    font_name = None  # Use default font

# --- App Data ---
# ... (rest of your app data and card display code remains the same)
# --- App Data ---
apps = [
    {
        "name": "Passport / Polaroid Photo Editor",
        "url": "https://passportphotoeditor.streamlit.app/",
        "desc": "Format passport photos according to country-specific rqmts. (Auto-centering and resizing ). Also creates Polaroid style images",
        "icon": "https://img.icons8.com/color/96/passport.png"
    },
    {
        "name": "PDF Editor",
        "url": "https://devs-pdfeditor.streamlit.app/",
        "desc": "Merge, split, and rearrange PDF files directly in your browser. No signup or installation required.",
        "icon": "https://img.icons8.com/color/96/pdf.png"
    },
    {
        "name": "Background Remover",
        "url": "https://devs-bgremove.streamlit.app/",
        "desc": "Easily remove image backgrounds with transparency support. Ideal for profile pics, products, and more.",
        "icon": "https://img.icons8.com/color/96/remove-image.png"
    },
    {
        "name": "Curated Top Ten",
        "url": "https://curatedtopten.streamlit.app/",
        "desc": "Browse and explore fun top-ten lists on movies, books, games, and more — all in one place.",
        "icon": "https://img.icons8.com/color/96/rating.png"
    },
    {
        "name": "Video Downloader",
        "url": "https://devsvideodownloader.streamlit.app/",
        "desc": "Download videos from supported platforms in various resolutions with just a link.",
        "icon": "https://img.icons8.com/color/96/download.png"
    },
]

# Set card height and spacing
card_height = 350
card_spacing = 25  # px

# Display cards with equal horizontal and vertical spacing
for i in range(0, len(apps), 2):
    cols = st.columns([1, 0.1, 1])  # col1 | spacer | col2

    for j, col in zip([0, 1], [cols[0], cols[2]]):
        if i + j < len(apps):
            app = apps[i + j]
            html_card = f"""
            <div style="border: 1px solid #1e3a8a; border-radius: 10px; padding: 15px; text-align: center;
                        height: {card_height}px; display: flex; flex-direction: column; justify-content: space-between;
                        background-color: #022e85; box-shadow: 2px 2px 8px rgba(0,0,0,0.4); margin-bottom: {card_spacing}px;">
                <img src="{app['icon']}" width="96" style="margin: 0 auto;" />
                <h4 style="margin: 10px 0 5px 0; color: #ffffff; font-family: '{font_name}', sans-serif;">{app['name']}</h4>
                <div style="flex-grow: 1; margin-bottom: 10px; color: #d0d8ff; font-family: '{font_name}', sans-serif;">{app['desc']}</div>
                <a href="{app['url']}" target="_blank">
                    <button style="padding:8px 20px;font-size:16px;border:none;background-color:#4CAF50;
                                    color:white;border-radius:5px;cursor:pointer; font-family: '{font_name}', sans-serif;">Open App</button>
                </a>
            </div>
            """
            col.markdown(html_card, unsafe_allow_html=True)

st.markdown("----")
st.info("Built with ❤️ using [Streamlit](https://streamlit.io/) — free and open source.")

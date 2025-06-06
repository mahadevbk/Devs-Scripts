import streamlit as st

st.set_page_config(
    page_title="Dev's Streamlit App Hub",
    layout="centered",
    page_icon="🧰"
)

st.markdown("""
<style>
@font-face {
    font-family: 'Baumans';
    src: url('https://raw.githubusercontent.com/mahadevbk/Devs-Scripts/main/static/Baumans-Regular.ttf') format('truetype');
}
h4, div, button {
    font-family: 'Baumans'  !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<h1 style="font-family: 'Baumans', font-size: 3rem; margin-bottom: 0.3em;">
    🧰 Dev's Streamlit App Hub
</h1>
""", unsafe_allow_html=True)

# --- App Data ---
apps = [
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
        "name": "Polaroid Frame Generator",
        "url": "https://devs-polaroid.streamlit.app/",
        "desc": "Create stylish Polaroid-style frames for your photos. Great for social media and printing.",
        "icon": "https://img.icons8.com/fluency/96/polaroid.png"
    },
    {
        "name": "Curated Top Ten",
        "url": "https://curatedtopten.streamlit.app/",
        "desc": "Browse and explore top-ten lists on movies and tv series from TMDB , OMDB, (IMDB & RT experimental.)",
        "icon": "https://img.icons8.com/color/96/rating.png"
    },
    {
        "name": "Video Downloader",
        "url": "https://devsvideodownloader.streamlit.app/",
        "desc": "Download videos from supported platforms in various resolutions with just a link.",
        "icon": "https://img.icons8.com/color/96/download.png"
    },
    {
        "name": "Passport Photo Editor",
        "url": "https://passportphotoeditor.streamlit.app/",
        "desc": "Format passport photos according to country-specific rqmts. (Auto-centering and resizing ). Also creates Polaroid style images",
        "icon": "https://img.icons8.com/color/96/passport.png"
    },
    {
        "name": ".srt Subtitles Downloader",
        "url": "https://subtitles-downloader.streamlit.app/",
        "desc": "Paste the Video file name (upto 5 at a time) and the app search, download and rename the .srt file.",
        "icon": "https://img.icons8.com/ios-filled/50/000000/subtitles.png"
    },
    {
        "name": "Mini Tournament Organiser",
        "url": "https://tournament-organiser.streamlit.app/",
        "desc": "One Day mini tournament organiser with PDF output.",
        "icon": "https://raw.githubusercontent.com/mahadevbk/Devs-Scripts/main/static/court.png"
    },
    {
        "name": "Photo Report PDF Generator",
        "url": "https://photoreport.streamlit.app/",
        "desc": "A simple Photo report generator with PDF output.",
        "icon": "https://raw.githubusercontent.com/mahadevbk/Devs-Scripts/main/photoreporticon.png"
    },
]

card_height = 350
card_spacing = 25  # px

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
                <h4 style="margin: 10px 0 5px 0; color: #ffffff; font-family: 'Permanent Marker', cursive;">{app['name']}</h4>
                <div style="flex-grow: 1; margin-bottom: 10px; color: #d0d8ff; font-family: 'Permanent Marker', cursive;">{app['desc']}</div>
                <a href="{app['url']}" target="_blank">
                    <button style="padding:8px 20px;font-size:16px;border:none;background-color:#4CAF50;
                                    color:white;border-radius:5px;cursor:pointer; font-family: 'Permanent Marker', cursive;">Open App</button>
                </a>
            </div>
            """
            col.markdown(html_card, unsafe_allow_html=True)

st.markdown("----")
st.info("Built with ❤️ using [Streamlit](https://streamlit.io/) — free and open source. [Other Scripts by dev](https://devs-scripts.streamlit.app/) on Streamlit.")

import streamlit as st

st.set_page_config(
    page_title="Dev's Streamlit App Hub",
    layout="centered",
    page_icon="🧰"
)

st.title("🧰 Dev's Streamlit App Hub")
st.markdown("A collection of simple, free, and open-source Streamlit tools for everyday use.")

apps = [
    {
        "name": "Passport Photo Editor",
        "url": "https://passportphotoeditor.streamlit.app/",
        "desc": "Format your passport or visa photos according to country-specific dimensions. Auto-centering and resizing included.",
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

# Create two columns
col1, col2 = st.columns(2)

# Distribute apps evenly between the two columns
for i, app in enumerate(apps):
    with col1 if i % 2 == 0 else col2:
        st.markdown("----", unsafe_allow_html=True)
        st.markdown(f"<div style='text-align: center;'><img src='{app['icon']}' width='96'></div>", unsafe_allow_html=True)
        st.markdown(f"<div style='text-align: center;'><h4>{app['name']}</h4></div>", unsafe_allow_html=True)
        st.markdown(f"<div style='text-align: center;'>{app['desc']}</div>", unsafe_allow_html=True)
        st.markdown(
            f'<div style="text-align: center;"><a href="{app["url"]}" target="_blank">'
            f'<button style="padding:8px 20px;font-size:16px;border:none;background-color:#4CAF50;color:white;border-radius:5px;cursor:pointer;">Open App</button>'
            f'</a></div>',
            unsafe_allow_html=True
        )

st.markdown("----")
st.info("Built with ❤️ using [Streamlit](https://streamlit.io/) — free and open source.")

import streamlit as st

st.set_page_config(page_title="Ucapan Ulang Tahun", page_icon="🎂", layout="centered")

# === Sidebar untuk input ===
st.sidebar.header("🎉 Pengaturan")
nama = st.sidebar.text_input("Dea Anantha Munthe", value="Bro")
ucapan = st.sidebar.text_area(
    "Ucapan spesial",
    value="Hai Deaa Lama Gak Tegur Sapa hehe.Hari ini, Aku langit kan semua doa terbaik untuk kamu. Semoga hal-hal yang membuat kamu runtuh turut menjadi alasan kamu untuk tumbuh.Semoga tuhan senantiasa menjaga kamu di manapun kamu berada. Semoga hari-hari kamu selalu diiringi cinta yang tidak pernah ada batasnya.Dan semoga, senyuman kedua orang tua kamu yang selalu kamu usahakan itu kini sudah terlaksana. 💙",
    height=120
)
foto = st.sidebar.file_uploader("Upload foto (JPG/PNG)", type=["jpg", "jpeg", "png"])
tombol = st.sidebar.button("Tampilkan 🎂")

# === Tampilan utama ===
st.markdown(
    """
    <div style="
        background: linear-gradient(135deg,#1E3C72,#2A5298);
        padding: 28px; border-radius: 20px; text-align:center;
        box-shadow: 0 12px 28px rgba(0,0,0,0.15); color: #fff;
    ">
      <h1 style="margin: 0 0 8px 0; font-size: 42px;">🎂 Selamat Ulang Tahun!</h1>
      <p style="margin:0; font-size:18px; opacity:.9;">Mari rayakan hari spesial ini 💫</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")  # spasi

if tombol:
    st.balloons()

st.markdown(
    f"""
    <div style="text-align:center; margin-top: 12px; color:#1E3C72;">
      <h2 style="font-size: 32px; margin-bottom: 4px;">{nama}</h2>
    </div>
    """,
    unsafe_allow_html=True
)

if foto is not None:
    st.image(foto, use_container_width=True, caption=f"Selamat ulang tahun, {nama}! 🎉")

st.markdown(
    f"""
    <div style="
      margin-top: 16px; padding: 20px; border-radius: 16px; 
      background:#f0f8ff; border:1px solid #cce0ff; text-align:center;
      box-shadow: 0 6px 18px rgba(0,0,0,0.08);
      font-size: 18px; line-height: 1.6; color:#1E3C72;
    ">
      {ucapan}
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")
st.caption("WKWKKW MAAP MASIH PEMULA AKU NYAA  💙")

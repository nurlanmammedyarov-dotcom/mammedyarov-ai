import streamlit as st
from google import genai
from google.genai import types

# Saytın adı və brauzer tabı
st.set_page_config(page_title="𝑀𝑎𝑚𝑚𝑒𝑑𝑦𝑎𝑟𝑜𝑣 𝐴𝐼", page_icon="😎")

# ÇAT YAZI TİPİNİ (FONT) DƏYİŞƏN CSS STİLİ
st.markdown("""
    <style>
    /* Google-dan xüsusi font gətiririk (Poppins fontu) */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,300;0,400;0,600;1,400&display=swap');

    /* Çat mesajlarının yazı tipini və stilini tənzimləyirik */
    .stChatMessage, .stChatInput textarea, div[data-testid="stMarkdownContainer"] p {
        font-family: 'Poppins', sans-serif !important;
        font-size: 16px !important;
    }
    </style>
""", unsafe_allow_html=True)

# Profil şəklinin linki
BOT_AVATAR = "https://i.ibb.co/example/photo.jpg"  # Öz şəkil linkini bura yaz

# Əsas başlıq
st.title("𝑀𝑎𝑚𝑚𝑒𝑑𝑦𝑎𝑟𝑜𝑣 𝐴𝐼")
st.caption("Məmmədyarov tərəfindən yaradılmış süni intellekt")

api_key = st.secrets.get("GEMINI_API_KEY")

if not api_key:
    st.error("API Açar təyin olunmayıb! Lütfən Streamlit Secrets hissəsinə əlavə edin.")
    st.stop()

client = genai.Client(api_key=api_key)

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    avatar = BOT_AVATAR if msg["role"] == "assistant" else None
    with st.chat_message(msg["role"], avatar=avatar):
        st.write(msg["content"])

if user_input := st.chat_input("𝑀𝑎𝑚𝑚𝑒𝑑𝑦𝑎𝑟𝑜𝑣 𝐴𝐼-ya bir şey yazın..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant", avatar=BOT_AVATAR):
        with st.spinner("𝑀𝑎𝑚𝑚𝑒𝑑𝑦𝑎𝑟𝑜𝑣 𝐴𝐼 düşünür..."):
            try:
                response = client.models.generate_content(
                    model="gemini-1.5-flash",
                    contents=user_input,
                    config=types.GenerateContentConfig(
                        system_instruction="Sənin adın 𝑀𝑎𝑚𝑚𝑒𝑑𝑦𝑎𝑟𝑜𝑣 𝐴𝐼-dır. Məmmədyarov tərəfindən yaradılmısan. Hər zaman hörmətlə, aydın və azərbaycan dilində cavab verırsən.",
                        temperature=0.7,
                    )
                )
                bot_reply = response.text
                st.write(bot_reply)
                st.session_state.messages.append({"role": "assistant", "content": bot_reply})
            except Exception as e:
                st.error(f"Xəta baş verdi: {e}")
                

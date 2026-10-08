import streamlit as st
from google import genai
from google.genai import types

# Profil və İkon üçün estetik şəkil
BOT_AVATAR = "https://i.ibb.co/64598.jpg" 

st.set_page_config(
    page_title="𝑀𝑎𝑚𝑚𝑒𝑑𝑦𝑎𝑟𝑜𝑣 𝐴𝐼", 
    page_icon=BOT_AVATAR,
    layout="centered"
)

# Instagram DM stilində xüsusi CSS qrafikası
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap');
    
    /* Ümumi fon və şrift */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        font-family: 'Poppins', sans-serif !important;
        background-color: #000000 !important;
        color: #ffffff !important;
    }

    /* Başlıq sahəsi */
    h1 {
        font-family: 'Poppins', sans-serif !important;
        font-weight: 600 !important;
        text-align: center;
        color: #ffffff !important;
        margin-bottom: 0px !important;
    }
    
    div[data-testid="stCaptionContainer"] {
        text-align: center;
        color: #a0a0a0 !important;
        margin-bottom: 25px !important;
    }

    /* Çat konteyneri */
    .stChatMessage {
        background-color: transparent !important;
        padding: 6px 0px !important;
        border: none !important;
    }

    /* İstifadəçi mesajı (Sağ tərəf - Instagram Bənövşəyi Gradient) */
    div[data-testid="stChatMessage"]:has(div[data-testid="stChatMessageAvatarUser"]) {
        flex-direction: row-reverse !important;
    }
    
    div[data-testid="stChatMessage"]:has(div[data-testid="stChatMessageAvatarUser"]) div[data-testid="stMarkdownContainer"] p {
        background: linear-gradient(135deg, #6B38FB, #802BFE) !important;
        color: #ffffff !important;
        padding: 12px 18px !important;
        border-radius: 22px 22px 4px 22px !important;
        display: inline-block;
        margin-left: auto !important;
        max-width: 82% !important;
        font-size: 15px !important;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }

    /* Bot mesajı (Sol tərəf - Instagram Tünd Boz) */
    div[data-testid="stChatMessage"]:has(div[data-testid="stChatMessageAvatarCustom"]) div[data-testid="stMarkdownContainer"] p {
        background-color: #262626 !important;
        color: #ffffff !important;
        padding: 12px 18px !important;
        border-radius: 22px 22px 22px 4px !important;
        display: inline-block;
        max-width: 82% !important;
        font-size: 15px !important;
    }

    /* Avatarların tam dəyirmi və düzgün ölçüdə görünməsi */
    [data-testid="stChatMessageAvatarCustom"] img, [data-testid="stChatMessageAvatarUser"] img {
        border-radius: 50% !important;
        object-fit: cover !important;
        width: 36px !important;
        height: 36px !important;
        min-width: 36px !important;
    }

    /* Giriş paneli (Input box) */
    .stChatInputContainer {
        border-radius: 28px !important;
        background-color: #121212 !important;
        border: 1px solid #262626 !important;
        padding: 2px !important;
    }

    .stChatInput textarea {
        color: #ffffff !important;
        font-family: 'Poppins', sans-serif !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("𝑀𝑎𝑚𝑚𝑒𝑑𝑦𝑎𝑟𝑜𝑣 𝐴𝐼")
st.caption("Məmmədyarov tərəfindən yaradılmış süni intellekt")

# API Açarı yoxlanışı
api_key = st.secrets.get("GEMINI_API_KEY")

if not api_key:
    st.error("⚠️ GEMINI_API_KEY çatışmır! Lütfən Streamlit Secrets hissəsini yoxlayın.")
    st.stop()

client = genai.Client(api_key=api_key)

if "messages" not in st.session_state:
    st.session_state.messages = []

# Keçmiş mesajlar
for msg in st.session_state.messages:
    avatar = BOT_AVATAR if msg["role"] == "assistant" else None
    with st.chat_message(msg["role"], avatar=avatar):
        st.write(msg["content"])

# Yeni mesaj daxil edildikdə
if user_input := st.chat_input("𝑀𝑎𝑚𝑚𝑒𝑑𝑦𝑎𝑟𝑜𝑣 𝐴𝐼-ya bir şey yazın..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant", avatar=BOT_AVATAR):
        with st.spinner("Məmmədyarov AI yazır..."):
            try:
                response = client.models.generate_content(
                    model="gemini-3.8-flash",
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
                

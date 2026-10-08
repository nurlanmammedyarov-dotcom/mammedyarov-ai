import streamlit as st
from google import genai
from google.genai import types

BOT_AVATAR = "https://i.ibb.co/64598/image.jpg" 

st.set_page_config(
    page_title="𝑀𝑎𝑚𝑚𝑒𝑑𝑦𝑎𝑟𝑜𝑣 𝐴𝐼", 
    page_icon=BOT_AVATAR,
    layout="centered"
)

# Tam Instagram DM stili (Profil şəkilləri tamamilə yoxdur)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap');
    
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        font-family: 'Poppins', sans-serif !important;
        background-color: #000000 !important;
        color: #ffffff !important;
    }

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

    /* Streamlit-in öz profil şəkillərini və sahələrini tam gizlət */
    [data-testid="stChatMessageAvatarCustom"], 
    [data-testid="stChatMessageAvatarUser"],
    .stChatMessage img {
        display: none !important;
    }

    .stChatMessage {
        background-color: transparent !important;
        padding: 4px 0px !important;
        border: none !important;
    }

    /* Mesaj baloncukları üçün xüsusi stillər */
    .user-bubble {
        background: linear-gradient(135deg, #6B38FB, #802BFE) !important;
        color: #ffffff !important;
        padding: 12px 18px !important;
        border-radius: 22px 22px 4px 22px !important;
        max-width: 75% !important;
        font-size: 15px !important;
        margin-left: auto !important;
        margin-right: 0px !important;
        text-align: left !important;
        word-wrap: break-word !important;
        display: block !important;
    }

    .bot-bubble {
        background-color: #262626 !important;
        color: #ffffff !important;
        padding: 12px 18px !important;
        border-radius: 22px 22px 22px 4px !important;
        max-width: 75% !important;
        font-size: 15px !important;
        margin-right: auto !important;
        margin-left: 0px !important;
        text-align: left !important;
        word-wrap: break-word !important;
        display: block !important;
    }

    /* Input Sahəsi */
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

api_key = st.secrets.get("GEMINI_API_KEY")

if not api_key:
    st.error("⚠️ GEMINI_API_KEY çatışmır! Lütfən Streamlit Secrets hissəsini yoxlayın.")
    st.stop()

client = genai.Client(api_key=api_key)

if "messages" not in st.session_state:
    st.session_state.messages = []

# Keçmiş mesajların göstərilməsi
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="user-bubble">{msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-bubble">{msg["content"]}</div>', unsafe_allow_html=True)

# Yeni mesaj göndərildikdə
if user_input := st.chat

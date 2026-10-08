import streamlit as st
import google.generativeai as genai

BOT_AVATAR = "https://i.ibb.co/64598/image.jpg" 

st.set_page_config(
    page_title="𝑀𝑎𝑚𝑚𝑒𝑑𝑦𝑎𝑟𝑜𝑣 𝐴𝐼", 
    page_icon=BOT_AVATAR,
    layout="centered"
)

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
        margin-bottom: 10px !important;
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
        margin-bottom: 10px !important;
    }

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

# GenAI konfiqurasiyası
genai.configure(api_key=api_key)

# Model təyinatı (system_instruction dəstəkləyən stabil versiya)
generation_config = {
    "temperature": 0.7,
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction="Sənin adın Məmmədyarov AI-dır, Məmmədyarov tərəfindən yaradılmısan. Hər zaman hörmətlə, aydın və azərbaycan dilində cavab ver."
)

if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="user-bubble">{msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-bubble">{msg["content"]}</div>', unsafe_allow_html=True)

user_input = st.chat_input("𝑀𝑎𝑚𝑚𝑒𝑑𝑦𝑎𝑟𝑜𝑣 𝐴𝐼-ya bir şey yazın...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.markdown(f'<div class="user-bubble">{user_input}</div>', unsafe_allow_html=True)

    with st.spinner("Məmmədyarov AI yazır..."):
        try:
            response = st.session_state.chat_session.send_message(user_input)
            bot_reply = response.text
            st.markdown(f'<div class="bot-bubble">{bot_reply}</div>', unsafe_allow_html=True)
            st.session_state.messages.append({"role": "assistant", "content": bot_reply})
        except Exception as e:
            st.markdown(f'<div class="bot-bubble">Xəta baş verdi: {e}</div>', unsafe_allow_html=True)
            

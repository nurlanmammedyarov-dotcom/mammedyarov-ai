import streamlit as st
import urllib.request
import json

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

try:
    api_key = st.secrets["GEMINI_API_KEY"]
except:
    api_key = None

if not api_key:
    st.error("⚠️ GEMINI_API_KEY tapılmadı! Streamlit Secrets bölməsini yoxlayın.")
    st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="user-bubble">{msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-bubble">{msg["content"]}</div>', unsafe_allow_html=True)

# Səsli mesaj yazmaq üçün panel (st.audio_input)
audio_file = st.audio_input("🎤 Səsli mesaj göndər (mikrofonu aktivləşdir)")

user_input = st.chat_input("𝑀𝑎𝑚𝑚𝑒𝑑𝑦𝑎𝑟𝑜𝑣 𝐴𝐼-ya bir şey yazın...")

prompt_to_send = None

if user_input:
    prompt_to_send = user_input
elif audio_file:
    # Səs qeydə alındıqda mətnə çevrilməsimülasyonu və ya məlumat bildirilməsi
    prompt_to_send = "[Səsli mesaj göndərildi. İstifadəçi səslə müraciət edir.]"

if prompt_to_send:
    st.session_state.messages.append({"role": "user", "content": prompt_to_send})
    st.markdown(f'<div class="user-bubble">{prompt_to_send}</div>', unsafe_allow_html=True)

    with st.spinner("Məmmədyarov AI düşünür..."):
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
        
        query_text = user_input if user_input else "Salam, mənə səsli mesaj göndərdim, məni salamla və necə kömək edə biləcəyimi soruş."
        
        payload = {
            "contents": [{
                "parts": [{"text": f"Sənin adın Məmmədyarov AI-dır. Səni Məmmədyarov yaradıb. Həmişə çox ağıllı, səmimi, köməksevər və səlis azərbaycan dilində cavab ver. Mesaj: {query_text}"}]
            }]
        }
        
        try:
            req_data = json.dumps(payload).encode("utf-8")
            req = urllib.request.Request(
                url, 
                data=req_data, 
                headers={'Content-Type': 'application/json'}
            )
            
            with urllib.request.urlopen(req, timeout=15) as response:
                res_json = json.loads(response.read().decode("utf-8"))
                if "candidates" in res_json:
                    bot_reply = res_json["candidates"][0]["content"]["parts"][0]["text"]
                    st.markdown(f'<div class="bot-bubble">{bot_reply}</div>', unsafe_allow_html=True)
                    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
                else:
                    st.markdown(f'<div class="bot-bubble">Model cavab qaytarmadı.</div>', unsafe_allow_html=True)
                    
        except urllib.error.HTTPError as e:
            err_msg = e.read().decode()
            st.markdown(f'<div class="bot-bubble">HTTP Xətası ({e.code}): {err_msg}</div>', unsafe_allow_html=True)
        except Exception as e:
            st.markdown(f'<div class="bot-bubble">Xəta baş verdi: {str(e)}</div>', unsafe_allow_html=True)
            

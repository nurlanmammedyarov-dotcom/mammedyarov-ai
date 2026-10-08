import streamlit as st
import urllib.request
import json

BOT_AVATAR = "https://i.ibb.co/64598/image.jpg" 

st.set_page_config(
    page_title="𝑀𝑎𝑚𝑚𝑒𝑑𝑦𝑎𝑟𝑜𝑣 𝐴𝐼", 
    page_icon=BOT_AVATAR,
    layout="centered"
)

ios_css = "<style>@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap'); html, body, [data-testid=\"stAppViewContainer\"], [data-testid=\"stHeader\"] { font-family: 'Poppins', sans-serif !important; background-color: #000000 !important; color: #ffffff !important; } h1 { font-family: 'Poppins', sans-serif !important; font-weight: 600 !important; text-align: center; color: #ffffff !important; margin-bottom: 0px !important; } div[data-testid=\"stCaptionContainer\"] { text-align: center; color: #8e8e93 !important; margin-bottom: 25px !important; } .user-bubble { background: rgba(0, 122, 255, 0.85) !important; backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); color: #ffffff !important; padding: 12px 18px !important; border-radius: 20px 20px 4px 20px !important; max-width: 75% !important; font-size: 15px !important; margin-left: auto !important; margin-right: 0px !important; text-align: left !important; word-wrap: break-word !important; display: block !important; margin-bottom: 12px !important; box-shadow: 0 4px 20px rgba(0, 122, 255, 0.3); } .bot-bubble { background: rgba(44, 44, 46, 0.75) !important; backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); color: #ffffff !important; padding: 12px 18px !important; border-radius: 20px 20px 20px 4px !important; max-width: 75% !important; font-size: 15px !important; margin-right: auto !important; margin-left: 0px !important; text-align: left !important; word-wrap: break-word !important; display: block !important; margin-bottom: 12px !important; border: 1px solid rgba(255, 255, 255, 0.1); box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4); } .stChatInputContainer { border-radius: 24px !important; background: rgba(28, 28, 30, 0.8) !important; backdrop-filter: blur(25px) !important; -webkit-backdrop-filter: blur(25px) !important; border: 1px solid rgba(255, 255, 255, 0.15) !important; padding: 4px !important; } .stChatInput textarea { color: #ffffff !important; font-family: 'Poppins', sans-serif !important; }</style>"

st.markdown(ios_css, unsafe_allow_html=True)

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

user_input = st.chat_input("𝑀𝑎𝑚𝑚𝑒𝑑𝑦𝑎𝑟𝑜𝑣 𝐴𝐼-ya bir şey yazın...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.markdown(f'<div class="user-bubble">{user_input}</div>', unsafe_allow_html=True)

    with st.spinner("Məmmədyarov AI düşünür..."):
        # Model adı tam işlək versiyaya dəyişdirildi
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}"
        
        payload = {
            "contents": [{
                "parts": [{"text": f"Sənin adın Məmmədyarov AI-dır, Məmmədyarov tərəfindən yaradılmısan. Həmişə çox ağıllı, səmimi, köməksevər və səlis azərbaycan dilində cavab ver. İstifadəçinin mesajı: {user_input}"}]
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
                    st.markdown(f'<div class="bot-bubble">Cavab alınmadı.</div>', unsafe_allow_html=True)
                    
        except urllib.error.HTTPError as e:
            err_msg = e.read().decode()
            st.markdown(f'<div class="bot-bubble">Xəta ({e.code}): {err_msg}</div>', unsafe_allow_html=True)
        except Exception as e:
            st.markdown(f'<div class="bot-bubble">Xəta baş verdi: {str(e)}</div>', unsafe_allow_html=True)
            

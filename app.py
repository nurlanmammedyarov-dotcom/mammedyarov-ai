import streamlit as st
import urllib.request
import json

BOT_AVATAR = "https://i.ibb.co/64598/image.jpg" 

st.set_page_config(
    page_title="𝑀𝑎𝑚𝑚𝑒𝑑𝑦𝑎𝑟𝑜𝑣 𝐴𝐼", 
    page_icon=BOT_AVATAR,
    layout="centered"
)

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
        st.chat_message("user").write(msg["content"])
    else:
        st.chat_message("assistant", avatar=BOT_AVATAR).write(msg["content"])

user_input = st.chat_input("𝑀𝑎𝑚𝑚𝑒𝑑𝑦𝑎𝑟𝑜𝑣 𝐴𝐼-ya bir şey yazın...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    with st.spinner("Məmmədyarov AI düşünür..."):
        # Güncellenen yeni model adresi: gemini-3.8-flash
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key={api_key}"
        
        payload = {
            "contents": [{
                "parts": [{"text": f"Sənin adın Məmmədyarov AI-dır. Səni Məmmədyarov yaradıb. Həmişə çox ağıllı, səmimi, köməksevər və səlis azərbaycan dilində cavab ver. İstifadəçinin mesajı: {user_input}"}]
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
                    st.chat_message("assistant", avatar=BOT_AVATAR).write(bot_reply)
                    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
                else:
                    st.chat_message("assistant", avatar=BOT_AVATAR).write("Model cavab qaytarmadı.")
                    
        except urllib.error.HTTPError as e:
            err_msg = e.read().decode()
            st.chat_message("assistant", avatar=BOT_AVATAR).write(f"HTTP Xətası ({e.code}): {err_msg}")
        except Exception as e:
            st.chat_message("assistant", avatar=BOT_AVATAR).write(f"Xəta baş verdi: {str(e)}")
            

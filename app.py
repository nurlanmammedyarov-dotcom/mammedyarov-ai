import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="𝑀𝑎𝑚𝑚𝑒𝑑𝑦𝑎𝑟𝑜𝑣 𝐴𝐼", layout="centered")

st.title("𝑀𝑎𝑚𝑚𝑒𝑑𝑦𝑎𝑟𝑜𝑣 𝐴𝐼")
st.caption("Məmmədyarov tərəfindən yaradılmış süni intellekt")

try:
    api_key = st.secrets["GEMINI_API_KEY"]
except:
    api_key = None

if not api_key:
    st.error("⚠️ GEMINI_API_KEY tapılmadı! Streamlit Secrets bölməsini yoxlayın.")
    st.stop()

genai.configure(api_key=api_key)

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Məmmədyarov AI-ya bir şey yazın...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Düşünürəm..."):
            try:
                # 100% işləyən və xəta verməyən rəsmi model adı
                model = genai.GenerativeModel('gemini-pro')
                prompt = f"Sənin adın Məmmədyarov AI-dır, Məmmədyarov tərəfindən yaradılmısan. Çox ağıllı, səmimi və səlis azərbaycan dilində cavab ver. Sual: {user_input}"
                
                response = model.generate_content(prompt)
                bot_reply = response.text
                
                st.markdown(bot_reply)
                st.session_state.messages.append({"role": "assistant", "content": bot_reply})
                
            except Exception as e:
                st.error(f"Xəta baş verdi: {str(e)}")
                

import streamlit as st
from google import genai
from google.genai import types

st.set_page_config(page_title="Məmmədyarov AI", page_icon="🤖", layout="centered")

st.title("🤖 Məmmədyarov AI")
st.caption("Məmmədyarov tərəfindən yaradılmış xüsusi Süni İntellekt köməkçisi")

api_key = st.secrets.get("GEMINI_API_KEY")

if not api_key:
    st.error("API Açar təyin olunmayıb! Xahiş olunur ayarlardan əlavə edin.")
    st.stop()

client = genai.Client(api_key=api_key)

system_instruction = """
Sənin adın 'Məmmədyarov AI'-dır. 
Sən xüsusi olaraq Məmmədyarov tərəfindən yaradılmış ağıllı, dostcanlı və sürətli şəxsi süni intellekt köməkçisisən.
İstifadəçi ilə hər zaman hörmətlə, aydın və azərbaycan dilində danışırsan.
Səndən kim olduğunu soruşduqda özünü 'Məmmədyarov tərəfindən yaradılmış Məmmədyarov AI' kimi təqdim edirsən.
"""

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if user_input := st.chat_input("Məmmədyarov AI-ya bir şey yazın..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Məmmədyarov AI düşünür..."):
            try:
                response = client.models.generate_content(
                    model="gemini-1.5-flash",
                    contents=user_input,
                    config=types.GenerateContentConfig(
                        system_instruction=system_instruction,
                        temperature=0.7,
                    )
                )
                bot_reply = response.text
                st.write(bot_reply)
                st.session_state.messages.append({"role": "assistant", "content": bot_reply})
            except Exception as e:
                st.error("Xəta baş verdi, xahiş olunur yenidən cəhd edin.")
              

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

    

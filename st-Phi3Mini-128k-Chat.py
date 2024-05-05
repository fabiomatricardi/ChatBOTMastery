import streamlit as st
import time
import sys
from gradio_client import Client
# Internal usage
import os
from time import sleep


if "hf_model" not in st.session_state:
    st.session_state.hf_model = "Phi-3-mini-128k-instruct"
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


@st.cache_resource
def create_client():   
    yourHFtoken = "hf_xxxxxxxxxxxxxxxxxx" #here your HF token
    print(f'loading the API gradio client for {st.session_state.hf_model}')
    client = Client("eswardivi/Phi-3-mini-128k-instruct", hf_token=yourHFtoken)
    return client

# FUNCTION TO LOG ALL CHAT MESSAGES INTO chathistory.txt
def writehistory(text):
    with open('chathistoryPhi3mini.txt', 'a', encoding='utf-8') as f:
        f.write(text)
        f.write('\n')
    f.close()

#AVATARS
av_us = '🧑‍💻'  # './man.png'  #"🦖"  #A single emoji, e.g. "🧑‍💻", "🤖", "🦖". Shortcodes are not supported.
av_ass = "🤖"   #'./robot.png'
# Set a default model


### START STREAMLIT UI
st.image('https://github.com/fabiomatricardi/ChatBOTMastery/raw/main/Phi3mini128-logo.png', )
st.markdown("### *powered by Streamlit & Gradio_client*", unsafe_allow_html=True )
#st.subheader(f"Free ChatBot using {st.session_state.hf_model}")
st.markdown('---')

client = create_client()

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    if message["role"] == "user":
        with st.chat_message(message["role"],avatar=av_us):
            st.markdown(message["content"])
    else:
        with st.chat_message(message["role"],avatar=av_ass):
            st.markdown(message["content"])
# Accept user input
if myprompt := st.chat_input("What is an AI model?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": myprompt})
    # Display user message in chat message container
    with st.chat_message("user", avatar=av_us):
        st.markdown(myprompt)
        usertext = f"user: {myprompt}"
        writehistory(usertext)
        # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        res  =  client.submit(
                myprompt,
                0,	# float (numeric value between 0 and 1) in 'Temperature' Slider component
                True,	# bool  in 'Sampling' Checkbox component
                800,	# float (numeric value between 128 and 4096) in 'Max new tokens' Slider component
                api_name="/chat"
                )
        
        for r in res:
            full_response=r
            message_placeholder.markdown(r+ "▌")
        message_placeholder.markdown(full_response)
        asstext = f"assistant: {full_response}"
        writehistory(asstext)       
        st.session_state.messages.append({"role": "assistant", "content": full_response})
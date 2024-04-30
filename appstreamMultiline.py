# libraries for AI inferences
from huggingface_hub import InferenceClient
import sys
import requests# Only for Internal usage
import streamlit as st
# Internal usage
import time
from gradio_client import Client


# Set HF API token  and HF repo
yourHFtoken = "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" #here your HF token
repo="ysharma/Chat_with_Meta_llama3_8b"
print('loading the API gradio clilent')
client = Client(repo, hf_token=yourHFtoken)


while True:
    userinput = ""
    print("\033[1;30m")  #dark grey
    print("Enter your text (end input with Ctrl+D on Unix or Ctrl+Z on Windows) - type quit! to exit the chatroom:")    
    print("\033[91;1m")  #red
    lines = sys.stdin.readlines()
    for line in lines:
        userinput += line + "\n"
    if "quit!" in lines[0].lower():
        print("\033[0mBYE BYE!")
        break    
    print("\033[1;30m")  #dark grey
    print('Calling the gradio_client predicttion...')
    result = client.submit(
            message=userinput,
            request=0.45,
            param_3=512,
            api_name="/chat"
    )
    print("\033[92;1m")
    final = ''
    for chunk in result:
        if final == '':
            final=chunk
            print(chunk, end="", flush=True)
        else:
            try:
                print(chunk.replace(final,''), end="", flush=True)
                final = chunk
            except:
                pass         



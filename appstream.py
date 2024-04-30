# libraries for AI inferences
from huggingface_hub import InferenceClient
from langchain_community.llms import  HuggingFaceHub
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
print('Calling the gradio_client predicttion...')
result = client.submit(
		message="List 3 benefits of learning languages",
		request=0.45,
		param_3=512,
		api_name="/chat"
)
print('ready to print')
print("\033[92;1m")
final = ''
for chunk in result:
    if final == '':
        final=chunk
        print(chunk, end="", flush=True)#
    else:
        try:
            print(chunk.replace(final,''), end="", flush=True)#
            final = chunk
        except:
            pass         



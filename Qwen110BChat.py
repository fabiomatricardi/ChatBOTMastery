# SPACE
# https://huggingface.co/spaces/Qwen/Qwen1.5-110B-Chat-demo
import time
import sys
from gradio_client import Client

# Set HF API token  and HF repo
yourHFtoken = "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" #here your HF token
repo = 'Qwen/Qwen1.5-110B-Chat-demo'
def ConncetLLM(reponame,hftoken):
    print('loading the API gradio client for Qwen1.5-110B-Chat-demo')
    client = Client(reponame, hf_token=hftoken)
    return client

#instantiate the Gradio_client object
client = ConncetLLM(repo,yourHFtoken)

while True:
    userinput = ""
    print("\033[1;30m")  #dark grey
    print("Enter your text (end input with Ctrl+D on Unix or Ctrl+Z on Windows) - type quit! to exit the chatroom:")    
    print("\033[38;5;48m")  #User prompt color
    lines = sys.stdin.readlines()
    for line in lines:
        userinput += line + "\n"
    if "quit!" in lines[0].lower():
        print("\033[0mBYE BYE!")
        break    
    print("\033[1;30m")  #dark grey
    print('Calling the gradio_client prediction...')
    result = client.submit(
            query=userinput,
            history=[],
            system="You are a helpful assistant.",
            api_name="/model_chat"
    )
    print("\033[38;5;99m")
    final = ''
    for chunk in result:
        if final == '':
            final=chunk[1][0][1]
            print(chunk[1][0][1], end="", flush=True)
        else:
            try:
                print(chunk[1][0][1].replace(final,''), end="", flush=True)
                final = chunk[1][0][1]
            except:
                pass         
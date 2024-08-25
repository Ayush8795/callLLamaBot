from groq import Groq
import os
from dotenv import load_dotenv
import time

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
)

def stream_chat(query,history=None):
    messages = []
    
    user_input = query
    
    if history:
        full_response = ""
        for his in history:
            full_response+=his+"\n\n"
        messages.append({"role": "assistant", "content": full_response})
    messages.append({"role": "user", "content": user_input})

    
    completion = client.chat.completions.create(
        model="llama-3.1-70b-versatile",
        messages=messages,
        temperature=1,
        max_tokens=4096,
        top_p=1,
        stream=True,
        stop=None,
    )
    
    print("AI: ", end="", flush=True)
    
    ret_content = ""
    for chunk in completion:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            # print(content, end="", flush=True)
            # yield content
            ret_content += content
    
    print()  # New line after the complete response
    
    return ret_content



# def messages():
#     query= ["what is light","who discovered it"]
#     sr=''
#     for qr in query:
#         print(stream_chat(qr))
#         time.sleep(5)


# messages()
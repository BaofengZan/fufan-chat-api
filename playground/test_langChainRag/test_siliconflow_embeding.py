import requests

url = "https://api.siliconflow.cn/v1/embeddings"

payload = {
    "model": "BAAI/bge-large-zh-v1.5",
    "input": "我爱北京天安门",
    "encoding_format": "float"
}
headers = {
    "Authorization": "Bearer sk-vditflkmaxqsdqeudrkzlpkbeqrbahretirgilfgopjtgvec",
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)


# 
from langchain_openai import ChatOpenAI
# sk-vditflkmaxqsdqeudrkzlpkbeqrbahretirgilfgopjtgvec
# https://api.siliconflow.cn/v1/

chat = ChatOpenAI(
    openai_api_base="https://api.siliconflow.cn/v1/",
    openai_api_key="sk-vditflkmaxqsdqeudrkzlpkbeqrbahretirgilfgopjtgvec",    # app_key
    model_name="Qwen/Qwen2.5-7B-Instruct",   # 模型名称
)

print(chat.invoke("我爱北京天安门"))
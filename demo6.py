from openai import OpenAI
import os
# 加载环境变量
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())  # 读取本地 .env 文件，里面定义了 OPENAI_API_KEY
from demo3 import build_prompt, get_completion, prompt_template
from demo5 import vector_instance

client = OpenAI()


class RAG_Bot:
    def __init__(self, vector_db, llm_api, n_results=2):
        self.vector_db = vector_db
        self.llm_api = llm_api
        self.n_results = n_results

    def chat(self, user_query):
        # 1. 检索
        search_results = self.vector_db.search(user_query, self.n_results)

        print('检索结果： ')
        for doc in search_results['documents'][0]:
            print(doc+"\n")

        # 2. 构建 Prompt
        prompt = build_prompt(
            prompt_template, info=search_results['documents'][0], query=user_query)

        # 3. 调用 LLM
        response = self.llm_api(prompt)
        return response


if "__main__" == __name__:
    # 创建一个RAG机器人
    bot = RAG_Bot(
        vector_instance(),
        llm_api=get_completion
    )

    # user_query = "llama 2有对话版吗？"
    # user_query = "llama 2可以商用吗？"
    user_query="llama 2 chat有多少参数"

    response = bot.chat(user_query)

    print(response)


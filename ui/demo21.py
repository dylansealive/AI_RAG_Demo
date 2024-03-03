import sys
sys.path.append('../')  # 将上层目录添加到 Python 模块搜索路径中

from open_ai_client import get_embeddings_bge, get_completion_ernie
from ui.vectordb import MyVectorDBConnector
from demo10 import text_embedding
from demo3 import get_completion
import os

from demo6 import RAG_Bot

os.environ["TOKENIZERS_PARALLELISM"] = "false"

#创建一个向量数据库对象
vector_db = MyVectorDBConnector(text_embedding)

bot = RAG_Bot(
    vector_db,
    llm_api=get_completion
)

# bot = RAG_Bot(
#     vector_db,
#     llm_api= get_embeddings_bge
# )

# user_query="ChatGPT 真正发挥作用的是什么?？"
# user_query="ChatGPT如何训练的？"
# user_query="ChatGPT如何训练的？"
# user_query="好工作是什么？"
user_query="躺平和内卷是什么？"

response = bot.chat(user_query)

#
print('response:')
print(response)
from sentence_transformers import CrossEncoder

from demo3 import get_completion
from demo5 import vector_instance_2
from demo6 import RAG_Bot

model = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2', max_length=512)

def test_serarch():
    vector_db = vector_instance_2()

    user_query = "how safe is llama 2"
    search_results = vector_db.search(user_query, 5)

    for doc in search_results['documents'][0]:
        print(doc+"\n")

    # 创建一个RAG机器人
    bot = RAG_Bot(
        vector_db,
        llm_api=get_completion
    )

    response = bot.chat(user_query)
    print("====回复====")
    print(response)


    print("--- 排序 -----")
    user_query = "how safe is llama 2"

    scores = model.predict([(user_query, doc)
                            for doc in search_results['documents'][0]])
    # 按得分排序
    sorted_list = sorted(
        zip(scores, search_results['documents'][0]), key=lambda x: x[0], reverse=True)
    for score, doc in sorted_list:
        print(f"{score}\t{doc}\n")

if "__main__" == __name__:
    test_serarch()
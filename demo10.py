from sentence_transformers import SentenceTransformer

from demo4 import cos_sim

# model_name = 'BAAI/bge-large-zh-v1.5' #中文
# model_name = 'acge-large-zh' #中文
# model_path = '/Users/sea/develop/model/acge-large-zh' #中文
model_path = '/Users/sea/develop/model/bge-large-zh-v1.5' #中文
#model_name = 'moka-ai/m3e-base' #中英双语，但效果一般

# model = SentenceTransformer('acge-large-zh')
model = SentenceTransformer(model_path)


def text_embedding(text):
    return model.encode(text)

if "__main__" == __name__:
    query = "国际争端"
    #query = "global conflicts"

    documents = [
        "联合国就苏丹达尔富尔地区大规模暴力事件发出警告",
        "土耳其、芬兰、瑞典与北约代表将继续就瑞典“入约”问题进行谈判",
        "日本岐阜市陆上自卫队射击场内发生枪击事件 3人受伤",
        "国家游泳中心（水立方）：恢复游泳、嬉水乐园等水上项目运营",
        "我国首次在空间站开展舱外辐射生物学暴露实验",
    ]

    query_vec = model.encode(query)
    print(query_vec)

    doc_vecs = [
        model.encode(doc)
        for doc in documents
    ]

    print(doc_vecs)

    print("Cosine distance:")  # 越大越相似
    #print(cos_sim(query_vec, query_vec))
    for vec in doc_vecs:
        print(cos_sim(query_vec, vec))
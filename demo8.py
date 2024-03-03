# 创建向量数据库连接器
from demo4 import get_embeddings
from demo5 import MyVectorDBConnector

vecdb_connector = MyVectorDBConnector("demo_vec_rrf", get_embeddings)

query = "非小细胞肺癌的患者"

documents = [
    "李某患有肺癌，癌细胞已转移",
    "刘某肺癌I期",
    "张某经诊断为非小细胞肺癌III期",
    "小细胞肺癌是肺癌的一种"
]

# 文档灌库
vecdb_connector.add_documents(documents)

# 向量检索
vector_search_results = {
    "doc_"+str(documents.index(doc)) : {
        "text" : doc,
        "rank" : i
    }
    for i, doc in enumerate(
        vecdb_connector.search(query, 3)["documents"][0]
    )
} # 把结果转成跟上面关键字检索结果一样的格式

print(vector_search_results)
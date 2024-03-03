import chromadb
from chromadb.config import Settings
from nltk.tokenize import sent_tokenize
import json

from demo1 import extract_text_from_pdf
from demo4 import get_embeddings


def split_text(paragraphs, chunk_size=300, overlap_size=100):
    '''按指定 chunk_size 和 overlap_size 交叠割文本'''
    sentences = [s.strip() for p in paragraphs for s in sent_tokenize(p)]
    chunks = []
    i = 0
    while i < len(sentences):
        chunk = sentences[i]
        overlap = ''
        prev_len = 0
        prev = i - 1
        # 向前计算重叠部分
        while prev >= 0 and len(sentences[prev])+len(overlap) <= overlap_size:
            overlap = sentences[prev] + ' ' + overlap
            prev -= 1
        chunk = overlap+chunk
        next = i + 1
        # 向后计算当前chunk
        while next < len(sentences) and len(sentences[next])+len(chunk) <= chunk_size:
            chunk = chunk + ' ' + sentences[next]
            next += 1
        chunks.append(chunk)
        i = next
    return chunks


class MyVectorDBConnector:
    # 数据库保存路径
    savePath = '/Users/sea/develop/AI-gpt/day5-rag/demo1/ui/db'
    collection_name = 'demo_zhao_shi_11'

    def __init__(self, embedding_fn):
        chroma_client = chromadb.PersistentClient(path=self.savePath)

        # # 为了演示，实际不需要每次 reset()
        # chroma_client.reset()

        # 创建一个 collection
        self.collection = chroma_client.get_or_create_collection(name=self.collection_name)
        self.embedding_fn = embedding_fn

    def add_documents(self, index, documents):
        '''向 collection 中添加文档与向量'''
        self.collection.add(
            embeddings=self.embedding_fn(documents),  # 每个文档的向量
            documents=documents,  # 文档的原文
            ids=[f"id{index}{i}" for i in range(len(documents))]  # 每个文档的 id
        )

    def search(self, query, top_n):
        '''检索向量数据库'''
        results = self.collection.query(
            query_embeddings=self.embedding_fn([query]),
            n_results=top_n
        )
        return results


def vector_instance():
    # 为了演示方便，我们只取两页（第一章）
    paragraphs = extract_text_from_pdf(
        "llama2.pdf",
        page_numbers=[2, 3],
        min_line_length=10
    )

    # 创建一个向量数据库对象
    vector_db = MyVectorDBConnector("demo", get_embeddings)
    # 向向量数据库中添加文档
    # 向向量数据库中添加文档
    chunks = split_text(paragraphs, 300, 100)
    vector_db.add_documents(chunks)

    return vector_db


def test_serarch():
    vector_db = vector_instance()

    user_query = "Llama 2有多少参数"
    results = vector_db.search(user_query, 2)

    for para in results['documents'][0]:
        print(para + "\n")


if "__main__" == __name__:
    test_serarch()

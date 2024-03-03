import os
import sys
sys.path.append('../')  # 将上层目录添加到 Python 模块搜索路径中
import hashlib
from demo1 import get_pdf_page_count, extract_text_from_pdf
from demo10 import text_embedding
from ui.vectordb import MyVectorDBConnector, split_text


def calculate_md5(input_string):
    # 将输入字符串编码为字节串，并计算 MD5 值
    md5_hash = hashlib.md5(input_string.encode())
    # 返回计算得到的 MD5 值的十六进制表示
    return md5_hash.hexdigest()

os.environ["TOKENIZERS_PARALLELISM"] = "false"

# 创建一个向量数据库对象
vector_db = MyVectorDBConnector(text_embedding)

# filename = 'chatgptwork.pdf'
filename = 'zhaoshi.pdf'
# page_count = get_pdf_page_count(filename)
page_count = 30

# 循环获取的页面
for i in range(page_count):
    print(f"正在处理第{i + 1}页")
    # 从pdf中提取文本
    paragraphs = extract_text_from_pdf(
        filename,
        page_numbers=[i],
        min_line_length=10
    )

    #判断内容是否为空
    if not paragraphs:
        print('empty')
        continue



    # 向向量数据库中添加文档
    chunks = split_text(paragraphs, 300, 100)
    # 向向量数据库中添加文档
    vector_db.add_documents(calculate_md5(str(i)), chunks)

print('add pdf finish')

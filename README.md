
### RAG 的流程

- 离线步骤：
    1. 文档加载
    2. 文档切分
    3. 向量化
    4. 灌入向量数据库

- 在线步骤：
    1. 获得用户问题
    2. 用户问题向量化
    3. 检索向量数据库
    4. 将检索结果和用户问题填入 Prompt 模版
    5. 用最终获得的 Prompt 调用 LLM
    6. 由 LLM 生成回复

### 我用了一个开源的 RAG，不好使怎么办？

1. 检查预处理效果：文档加载是否正确，切割的是否合理
2. 测试检索效果：问题检索回来的文本片段是否包含答案
3. 测试大模型能力：给定问题和包含答案文本片段的前提下，大模型能不能正确回答问题

## 环境部署
1. python3.8以上
2. `pip install requirements.txt`安装依赖
3. docker部署Elasticsearch
```shell
#拉取Elasticsearch镜像
docker pull elasticsearch:7.17.18
#启动Elasticsearch实例
docker run -d --name elasticsearch -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" elasticsearch:7.17.18
```
4. `.env_template` 更改为 `.env` 。替换其中的值为自己的。
```
OPENAI_API_KEY=""       #opanAI key
OPENAI_BASE_URL=""      #openAI base url
ERNIE_CLIENT_ID=""      #baidu app id
ERNIE_CLIENT_SECRET=""  #baidu app secret
```

## 关键词搜索

1. 文档加载，并按一定条件**切割**成片段
2. 将切割的文本片段灌入**检索引擎**
3. 封装**检索接口**
4. 构建**调用流程**：Query -> 检索 -> Prompt -> LLM -> 回复

### pdf文档加载数据示例
demo1.py

### elasticsearch 关键词搜索
demo2.py

### openAI 搜索结果处理
demo3.py


## 向量检索 

1. 加载数据
2. 数据使用向量模型产生向量数据
3. 保存到向量数据库
4. 向量数据库搜索结果
5. 使用通用模型生成语义化结果

### 向量检索原理
计算向量间的相似度：欧式距离（越小越相似），余弦距离（越大越相似）。
demo4.py

### 向量数据库查询结果
demo5.py

### openAI 搜索结果处理(RAG)
demo6.py

## 增强知识

### 文本分割粒度调整
demo5.py vector_instance_2()


### 检索结果排序
1. 检索时过招回一部分文本
2. 通过一个排序模型对 query 和 document 重新打分排序  
demo11.py


### 混合检索 
1. es搜索 demo7.py
2. 向量检索 demo8.py
3. RRF 的融合排序 demo9.py

## 向量模型本地部署
demo10.py


## ChatPDF

1. 将pdf加载，并保存到向量数据库
demo20.py 
2. 用户搜索结果，并生成回复
demo21.py









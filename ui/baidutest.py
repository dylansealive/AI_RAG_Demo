import requests
import json

API_KEY = "bPgIKw8rlXopq24TLEhAsgz7"
SECRET_KEY = "GECHiHzcJXJ2JRHfk9yKJ9lLUAUZrkaO"

def main():

    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/embeddings/bge_large_zh?access_token=" + get_access_token()

    payload = json.dumps({
        "input": [
            "你是一个问答机器人。 你的任务是根据下述给定的已知信息回答用户问题。 确保你的回复完全依据下述已知信息。不要编造答案。 如果下述已知信息不足以回答用户的问题，请直接回复“我无法回答您的问题”。  已知信息: "
            "长大。在这种环境下，他们的自我意识越来越强，每个人都认为自己生来就是要享受美好 生活的。社会学家简·特温格把这一代人称作“自我的%的孩子认为自 "
            "己比别人漂亮，79%的孩子认为自己比别人聪明，40%的孩子认为自己到30多岁的时候 能一年挣7.5万美元。事实上，那一年30围的社会问题，才刚刚显露出来。经济学家保拉·朱利亚娜 "
            "条道路。在这条道路上，你会遇到未知的挑战，但那些都是路上的风景和奇遇。你可能走 得快，也可能走得慢，但一定会更充实、更自信。 世面，起点比我们更高，舞台比我们 "
            "更大，但他们缺少一些机会。我们那一代其实什么都不知道，所以多知道一点儿都会欢呼 雀跃。我们那太难了。他们见过的太多， 所以很难再有惊喜。他们可选的方案太多，反而迷失了方向。他们其实生活在一个一切皆  用户问： "
            "现在的年轻人知道什么是未来吗？  请用中文回答用户问题。"
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))

if __name__ == '__main__':
    main()



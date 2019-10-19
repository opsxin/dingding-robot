"""发送 URL 请求，返回数据
"""
import requests


my_header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'Content-Type': 'application/json'
}


def request_url(URL, my_data={}, requests_type="POST"):
    """发送 URL 请求
    只支持 Get、Post 方式
    """
    if requests_type.lower() == "post":
        r = requests.post(URL, data=my_data, headers=my_header)
    else:
        r = requests.get(URL, headers=my_header)
    if r.status_code == requests.codes.ok:
        return r
    else:   
        print("发送失败，请检查")


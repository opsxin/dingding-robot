"""发送 URL 请求，返回数据
"""
import requests


my_header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'Content-Type': 'application/json'
}


def request_url(URL, my_data):
    """
    发送 URL POST 请求
    """
    r = requests.post(URL, data=my_data, headers=my_header)
    if r.status_code == requests.codes.ok:
        return r
    else:   
        print("发送失败，请检查 JSON\n", my_data)

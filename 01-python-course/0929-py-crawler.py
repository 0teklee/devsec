"""
0929 월요일 오전 파이썬 크롤러 개발 실습입니다.
"""

import re

import requests


def get_my_ip():

    url = "http://ipipip.kr"
    res = requests.get(url)

    html_code = res.text

    ip_data_index = html_code.find("""ip_data \">""")
    html_code2 = html_code[ip_data_index:]
    h1_index = html_code2.find("</h1>")
    ip_addr = html_code2[9:h1_index]
    print(f"MY IP IS {ip_addr}")
    return ip_addr


test_1 = get_my_ip()

response = requests.get("https://free-proxy-list.net/ko/")
html_code_3 = response.text


pattern = re.compile(r"(?:\d{1,3}\.){3}\d{1,3}:\d{1,5}")

matches = re.findall(
    pattern,
    html_code_3,
)

print("----target-----", matches, end="------------------")
# print("----html-----", html_code_3)
proxy_list = []
for m in matches:
    proxy_list.append(m)
# proxy_ip_port = random.choice(proxy_list)
proxies = {
    # "http": proxy_ip_port,
    # "https": proxy_ip_port,
}
r = requests.get("http://ipipip.kr", proxies=proxies, timeout=5)
html_code = r.text

print(r.text)

"--------------------------------------------------------------------"
# 강사님 예제


def get_ip_addr():
    url = "http://ipipip.kr"
    # url = "http://ip.pe.kr"

    response = requests.get(url)
    html_code = response.text

    ip_data_index = html_code.find('ip_data">')
    html_code2 = html_code[ip_data_index:]
    h1_index = html_code2.find("</h1>")
    ip_addr = html_code2[9:h1_index]
    return ip_addr


my_ip = get_ip_addr()
print("MY_IP", my_ip)


response = requests.get("https://free-proxy-list.net/ko/")
html_code = response.text
# print(html_code)


# html_code = '252.123.12.23:34444'
# pattern = re.compile(r'^(?:\d{1,3}\.){3}\d{1,3}:\d{1,5}$')
pattern = re.compile(r"(?:\d{1,3}\.){3}\d{1,3}:\d{1,5}")
# ^ > 정규식의 시작(문자열의 시작)
# $ > 정규식의 끝 (문자열의 끝)
matches = re.findall(pattern, html_code)
# print("✅ 전체 매칭 문자열:")
proxy_list = []
for m in matches:
    # print(m)
    proxy_list.append(m)


# while 반복문
while True:
    proxy_ip_port = random.choice(proxy_list)
    print(f"PROXY_IP_PORT {proxy_ip_port}")
    proxies = {
        "http": proxy_ip_port,
        "https": proxy_ip_port,
    }
    # try / except 예외처리
    try:
        r = requests.get("http://ipipip.kr", proxies=proxies, timeout=5)
        break
    except Exception as e:
        print("ERROR", str(e))
        continue


html_code = r.text
print(r.text)

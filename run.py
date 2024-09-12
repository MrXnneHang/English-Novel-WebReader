from flask import Flask, request, jsonify
from flask_cors import CORS  # 引入 CORS
from api import user_query
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webrowser_config import WebConfig

app = Flask(__name__)
CORS(app)  # 允许所有来源的跨域请求

# 初始化 WebConfig 和 WebDriver
webconfig = WebConfig()

# 持久化的 Chrome WebDriver
driver = None

def initialize_webdriver():
    global driver
    if driver is None:
        # 仅当 driver 未被初始化时创建它
        driver = webdriver.Chrome(service=webconfig.service, options=webconfig.option)

def query_api(txt):
    initialize_webdriver()  # 确保 driver 已初始化
    matched = user_query(webconfig,driver,txt)
    string = ""
    for i in matched:
        string += f"{i[0]}:{i[1]}\n"
    print(string)
    return string

@app.route('/api/selected-word', methods=['POST'])
def selected_word():
    data = request.get_json()
    selected_text = data.get('selectedText', '')

    # 调用 query_api 处理单词
    response = query_api(selected_text)

    # 在返回的响应中包含翻译结果和消息
    return jsonify({
        'message': f'单词 "{selected_text}" 已成功处理。\n {response}'
    })

if __name__ == '__main__':
    initialize_webdriver()
    app.run(port=5000)

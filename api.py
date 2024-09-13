from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webrowser_config import WebConfig
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from util import setup_directory,load_config,write_yaml
import re
import time
import yaml

import requests
import json

def sentence_translate(text):
    key = load_config("key.yml")
    api_key = key["deeplx"]
    url = f"https://api.deeplx.org/{api_key}/translate"
    headers = {
        "Content-Type": "application/json"
    }
    data = {"text":text, "source_lang":"EN","target_lang":"ZH"}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        return response.json()["data"]
    else:
        print(response)
        return text

def preprocess_selected_sentence(text):
    return text.replace("\n","")

def query(webconfig,driver,query_word="hello"):

    driver.get(webconfig.config['youdao_url'].replace("word=",f"word={query_word}"))
    content = driver.page_source
    with open("src.txt","w",encoding="utf-8") as f:
        f.write(content)
    # with open("src.txt","w",encoding="utf-8") as f:
    #     f.write(content)
    # 正则表达式，匹配 <ul class="basic"> 到 <div class="exam_type"> 之间的内容
    pattern = r'<ul class="basic".*?>(.*?)<div disable-zoom=""'

    # 提取匹配内容，使用 re.DOTALL 处理多行情况
    match = re.search(pattern, content, re.DOTALL)

    if match:
        result = match.group(1)
        # 正则表达式匹配词性和解释
        pattern_1 = r'<span class="pos"[^>]*>(.*?)<\/span><span class="trans"[^>]*>(.*?)<\/span>'
        pattern_2 = r'<span class="trans"[^>]*>(.*?)<\/span>'
        # 提取匹配内容
        matches_group1 = re.findall(pattern_1, result)
        matches_group2 = re.findall(pattern_2, result)

        # 打印结果
        if matches_group1:
            print("匹配到单词")
            for pos, trans in matches_group1:
                print(f"{pos}: {trans}")
                print(matches_group1)
            return matches_group1
        else:
            if matches_group2:
                print("匹配到短语")
                phrase_group = []
                for trans in matches_group2:
                    print(f"phrase.:{trans}")
                    for matches in matches_group2:
                        phrase_group.append(("phrase.",matches))
                    print(phrase_group)
                return phrase_group
            else:
                return matches_group2

    else:
        print("没有匹配到内容")
        return 0

def found_origin_form(webconfig,matched):
    """如果是第三人称单数，复数，过去式等,
    则返回原型,并且再次query原型,否则返回0"""
    situations = webconfig.situation
    met_situation = False
    found_origin_form = []
    for mean in matched:
        for situation in situations:
            if situation in mean[1]:
                original_form = re.search(r'（(.*?)' + situation, mean[1])
                if original_form:
                    print(f"找到类似原型，是否查询:{original_form.group(1)}")
                    met_situation = True
                    found_origin_form.append(original_form.group(1))
                else:
                    print("找到疑似指向原型的句子，但未锁定原型")
                    print(mean[1])
    if met_situation:
        return found_origin_form
    else:
        return 0

def user_query(webconfig,driver,word):
    matched = query(webconfig,driver,word)
    if matched:
        found_origin_form(webconfig,matched)
        # ask = input("是否保存单词？(y/n)")
        # if ask == "y":
        #     save_word(word,matched)
        return matched


def save_word(word, matched):
    print(matched, word)
    date = time.strftime("%Y-%m-%d", time.localtime())

    # 加载配置文件
    main = load_config("main.yml")
    pos = load_config("pos.yml")

    # 检查单词是否已经存在于 main.yml 中
    for entry in main:
        if entry["word"] == word:
            # 抛出单词已存在的异常
            print(f"Word '{word}' already exists in the dictionary.")
            return f"Word '{word}' already exists in the dictionary."

    # 生成新的 ID（假设 ID 是根据现有的长度 + 1 自动生成）
    new_id = str(len(main) + 1)

    # 将 word 和其相关信息添加到 main.yml
    new_entry = {
        "ID": new_id,
        "word": word,
        "review_count": 0,
        "last_review_date": date,
        "created_at": date,
        "create_user": "xnne"
    }
    main.append(new_entry)  # 将新词条添加到 main 列表中

    # 将词性和释义保存到 pos.yml 中
    for pos_entry in matched:
        pos_type, translation = pos_entry
        pos_entry = {
            "ID": str(len(pos) + 1),  # 每条词性和释义的唯一ID
            "word_ID": new_id,        # 对应 main.yml 中的单词ID
            "pos": pos_type,
            "translation": translation
        }
        pos.append(pos_entry)

    # 保存更新后的数据到文件
    with open("main.yml", 'w', encoding='utf-8') as main_file:
        yaml.dump(main, main_file, allow_unicode=True)

    with open("pos.yml", 'w', encoding='utf-8') as pos_file:
        yaml.dump(pos, pos_file, allow_unicode=True)


    print(f"Word '{word}' and its details have been saved successfully.")
    return f"Word '{word}' and its details have been saved successfully."



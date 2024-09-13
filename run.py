from flask import Flask, request, jsonify, g
from flask_cors import CORS
from api import user_query, save_word,sentence_translate,preprocess_selected_sentence,save_sentence,get_book_list,get_book_abs_path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webrowser_config import WebConfig
import shutil
from epub_parser import convert_to_txt

app = Flask(__name__)
CORS(app)

webconfig = WebConfig()
driver = None

# Global variables to store the last word and translation
global_word = None
global_translation = None


def initialize_webdriver():
    global driver
    if driver is None:
        driver = webdriver.Chrome(service=webconfig.service, options=webconfig.option)


def word_query_api(txt):
    initialize_webdriver()
    matched = user_query(webconfig, driver, txt)
    string = ""
    for i in matched:
        string += f"{i[0]}:{i[1]}\n"
    return string, matched

def rec_sentence(text):
    count = 0
    count_list = [" ","'",",",".","?"]
    string = text
    for i in string:
        if i in count_list:
            count += 1
    if count>2:
        print(count)
        return 1
    else:
        return 0

@app.route('/api/selected-word', methods=['POST'])
def selected_word():
    global global_word, global_translation
    data = request.get_json()
    selected_text = data.get('selectedText', '')
    is_sentence = rec_sentence(selected_text)
    if is_sentence:
        print("翻译句子")
        processed_text = preprocess_selected_sentence(selected_text)
        translation = sentence_translate(processed_text)
        global_translation = translation
        global_word = processed_text
        return jsonify({
            'message': f'{processed_text}:\n{translation}'
        })
    else:
        print("翻译单词词组")
        response, matched = word_query_api(selected_text)

        # Store word and translation in global variables
        global_word = selected_text
        global_translation = matched

        return jsonify({
            'message': f'{selected_text}:\n{response}',
            'matched': matched
        })


@app.route('/api/save_word', methods=['POST'])
def save_api():
    global global_word, global_translation

    if global_word and global_translation:
        is_sentence = rec_sentence(global_word)
        if is_sentence:
            response = save_sentence(global_word, global_translation)
            return jsonify({'message': response})
        else:
            response = save_word(global_word, global_translation)
            return jsonify({'message': response})
    else:
        return jsonify({'message': '没有可保存的数据！'}), 400

@app.route('/api/get_book_list',methods=['GET'])
def get_books():
    books = get_book_list()
    return jsonify(books)


@app.route('/api/get_book_abs_path', methods=['POST'])
def get_book_abs_api():
    data = request.get_json()  # 从请求体中获取 JSON 数据
    book_title = data.get('book_title', '')  # 从 JSON 数据中提取书籍的标题
    if not book_title:
        return jsonify({'error': 'Book title is required'}), 400  # 如果没有书名，返回错误信息

    book_abs_path = get_book_abs_path(book_title)  # 获取书籍的绝对路径
    return jsonify({'book_abs_path': book_abs_path})
import os

@app.route('/api/load_book_content', methods=['POST'])
def load_book_content():
    data = request.get_json()
    book_path = data.get('bookPath', '')

    if not book_path or not os.path.exists(book_path):
        return jsonify({'error': 'Invalid book path'}), 400

    try:
        if book_path.endswith('.txt'):
            shutil.copyfile(book_path, './book_text.txt')
        elif book_path.endswith('.epub'):
            convert_to_txt(book_path)
        else:
            return jsonify({'error': 'Unsupported file format'}), 400
        with open('./book_text.txt', 'r', encoding='utf-8') as f:
            book_content = f.read()
        return jsonify({'fileContent': book_content})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    initialize_webdriver()
    app.run(port=5000)

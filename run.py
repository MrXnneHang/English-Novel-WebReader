from flask import Flask, request, jsonify, g
from flask_cors import CORS
from api import user_query, save_word,sentence_translate,preprocess_selected_sentence
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webrowser_config import WebConfig

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
    string = "hello world,hey there"
    for i in string:
        if i in count_list:
            count += 1
    if count>2:
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
        processed_text = preprocess_selected_sentence(selected_text)
        translation = sentence_translate(processed_text)
        return jsonify({
            'message': f'{processed_text}:\n{translation}'
        })
    else:
        response, matched = word_query_api(selected_text)

        # Store word and translation in global variables
        global_word = selected_text
        global_translation = matched

        return jsonify({
            'message': f'{selected_text}:\n{response}',
            'matched': matched
        })


@app.route('/api/save_word', methods=['POST'])
def save():
    global global_word, global_translation

    if global_word and global_translation:
        response = save_word(global_word, global_translation)
        return jsonify({'message': response})
    else:
        return jsonify({'message': '没有可保存的数据！'}), 400


if __name__ == '__main__':
    initialize_webdriver()
    app.run(port=5000)

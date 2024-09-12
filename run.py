from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 允许所有来源的跨域请求

@app.route('/api/selected-word', methods=['POST'])
def selected_word():
    data = request.json
    selected_text = data.get('selectedText', '')
    if selected_text:
        print(selected_text)
        return jsonify({"message": "Word received", "selectedText": selected_text})
    else:
        return jsonify({"message": "No word selected"}), 400


if __name__ == '__main__':
    app.run(port=5000, debug=True)

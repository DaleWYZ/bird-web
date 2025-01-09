from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    try:
        with open('static/birds_data.json', 'r', encoding='utf-8') as f:
            birds_data = json.load(f)
        return render_template('index.html', birds=birds_data)
    except FileNotFoundError:
        return "请先运行爬虫脚本获取鸟类数据"

if __name__ == '__main__':
    app.run(debug=True) 
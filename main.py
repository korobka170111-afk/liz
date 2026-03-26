from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Список текстов для переключения
texts = [
    "Привет, это первый текст!",
    "А это уже второй текст.",
    "Третий текст. Нажми ещё раз!",
    "Четвёртый: почти всё...",
    "Пятый: последний! Нажми, чтобы начать заново."
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_text', methods=['GET'])
def get_text():
    index = int(request.args.get('index', 0))
    # Если дошли до конца, начинаем сначала
    if index >= len(texts):
        index = 0
    return jsonify({'text': texts[index], 'next_index': index + 1})

if __name__ == '__main__':
    app.run(debug=True)
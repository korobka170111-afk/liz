from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

# Список текстов
texts = [
    'Представь...',
    'мы одни дома)...',
    'лежим на кровати)))',
    'ты достаешь наручники и цепляешь меня к батарее',
    'и начинаешь жёстко пиздить так что у меня вылетают все зубы))))',
    'мило, правда?'
]

current_index = 0


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_text')
def get_text():
    global current_index

    # Если уже дошли до конца, возвращаем пустой ответ
    if current_index >= len(texts):
        return jsonify({'finished': True})

    # Берём текущий текст
    text = texts[current_index]

    # Увеличиваем индекс для следующего раза
    current_index += 1

    # Проверяем, закончились ли тексты
    finished = (current_index >= len(texts))

    return jsonify({'text': text, 'finished': finished})


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)
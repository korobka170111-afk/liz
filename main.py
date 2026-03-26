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

current_index = 0  # храним текущий индекс на сервере

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_text')
def get_text():
    global current_index
    # Берём текущий текст
    text = texts[current_index]
    # Увеличиваем индекс для следующего раза
    current_index += 1
    # Если дошли до конца, начинаем сначала
    if current_index >= len(texts):
        current_index = 0
    return jsonify({'text': text})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

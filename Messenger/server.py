import time
from datetime import datetime

from flask import Flask, request, abort

app = Flask(__name__)
db = [
    {
        'time': time.time(),
        'name': 'Jack',
        'text': 'Привет всем!',
    },
    {
        'time': time.time(),
        'name': 'Mary',
        'text': 'Привет, Jack!',
    },
]


@app.route("/")
def hello():
    return "Hello, World 123!"


@app.route("/status")
def status():
    dt_now = datetime.now()
    users = set()
    for message in db:
        users.add(message['name'])
    return {
        'status': True,
        'name': 'Messenger',
        'count_messages' : len(db),
        'count_users' : len(users),
        #'time1': time.asctime(),
        #'time2': time.time(),
        #'time3': dt_now,
        #'time4': str(dt_now),
        'time': dt_now.strftime('%Y/%m/%d time: %H:%M:%S'),
        #'time6': dt_now.isoformat()
    }


@app.route("/send", methods=['POST'])
def send_message():
    data = request.json

    if not isinstance(data, dict):
        return abort(400)
    # if set(data.keys()) != {'name', 'text'}:
    #     return abort(400)
    if 'name' not in data or 'text' not in data:
        return abort(400)
    if len(data) != 2:
        return abort(400)

    name = data['name']
    text = data['text']

    if not isinstance(name, str) or \
            not isinstance(text, str) or \
            name == '' or \
            text == '':
        return abort(400)

    message = {
        'time': time.time(),
        'name': name,
        'text': text,
    }
    db.append(message)

    return {'ok': True}


@app.route("/messages")
def get_messages():
    """messages from db after given timestamp"""
    try:
        after = float(request.args['after'])
    except:
        return abort(400)

    result = []
    for message in db:
        if message['time'] > after:
            result.append(message)
            if message['name'] != 'Bot':
                bot(message)
            if len(result) >= 100:
                break

    return {'messages': result}

def bot(message):
    words = []
    word = ''
    for _char in message['text']:
        if _char != ' ' and _char != '!' and _char != ',' and _char != '?' and _char != ':':
            word = word + _char
        if _char == ' ' or _char == message['text'][-1]:
            words.append(word.lower())
            word = ''

    if words.count('привет') > 0 or words.count("здравствуйте") > 0 or words.count("хай") > 0:
        _text = "Доброго времени суток, " + message['name'] + "!"
        answer = {
            'time' : time.time(),
            'name' : "Bot",
            'text' : _text,
        }
        db.append(answer)

    if words.count('где') > 0 and words.count('найти') > 0 or words.count('можно') > 0:
        _text = "Пользуйтесь на здоровье: https://www.google.com/ удачи, " + message['name'] + "!"
        answer = {
            'time' : time.time(),
            'name' : "Bot",
            'text' : _text,
        }
        db.append(answer)

    if words.count('как') > 0 or words.count("получить") > 0 and words.count("скидку") > 0:
        _text = "Все просто, нажмите на кнопку под трансляцией интенсива и оставьте заявку, удачи, " + message['name'] + "!"
        answer = {
            'time' : time.time(),
            'name' : "Bot",
            'text' : _text,
        }
        db.append(answer)
    if words.count('it') > 0 or words.count("это") > 0 or words.count("программирование") > 0 and words.count("сложно") > 0:
        _text = "Для этого и существует онлайн-университет Skillbox, вас будут обучать с самых азов, лучшие наставники, со Skillbox у вас все получится https: // skillbox.ru , удачи, " + message['name'] + "!"
        answer = {
            'time' : time.time(),
            'name' : "Bot",
            'text' : _text,
        }
        db.append(answer)


    return {'ok' : True}


app.run()

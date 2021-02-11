# https://repl.it/@Levashov/messenger

import time

print('https://repl.it/@Levashov/messenger')

# None        # NoneType
# True/False  # bool
# 1           # integer
# 1.5         # float
# 'Jack'      # str
# 'Привет всем!'

l = [1, 2, 3, 4, 5, [1, 2, 3], '123', True]
# print(l[0])
# print(l[-3][1])
l = ['12-02-2021 14:53', 'Jack', 'Привет всем!']
# print(l[0], l[1])
# print(l[2])
# print()

d = {
    'time': '12-02-2021 14:53',
    'name': 'Jack',
    'text': 'Привет всем!',
}
# print(d['time'], d['name'])
# print(d['text'])
# print()


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

# import random

# print(random.random())
# print(random.randint(1, 10))

def send_message(name, text):
    message = {
        'time': time.time(),
        'name': name,
        'text': text,
    }
    db.append(message)


# send_message('123', '123')
# send_message('123', '456')
# send_message('123', '789')

# print('-' * 50)

# for message in db:
#     print(message['time'], message['name'])
#     print(message['text'])
#     print()


def get_messages(after):
    """messages from db after given timestamp"""
    result = []
    for message in db:
        if message['time'] > after:
            result.append(message)
    return result

print(db)
t1 = db[-1]['time']
print(get_messages(t1))
print(get_messages(t1))
print(get_messages(t1))

send_message('123', '123')
send_message('123', '456')
print(get_messages(t1))

t2 = db[-1]['time']
print(get_messages(t2))

send_message('123', '789')
print(get_messages(t2))

# send message == положить message в db
# get messages == достать из db сообщения,
# которые не подгружены на клиенте

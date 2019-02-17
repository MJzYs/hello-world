import json

def get_store_username():
    filename = 'username.json'
    try:
        with open (filename) as untitled:
            username = json.load(untitled)

    except FileNotFoundError:
        return None
    else:
        return username

def get_new_name():
    username = input('what is your name bro?~')
    filename = 'username.json'
    with open(filename, 'w') as untitled:
        json.dump(username, untitled)
    return username

def greet_user():
    username = get_store_username()
    if username:
        print('welcome back, ' + username + '!~')
    else:
        username = get_new_name()
        print('i will remember you when you come back bro~')
greet_user()

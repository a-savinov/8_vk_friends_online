import sys

import vk

APP_ID = 6202412  # чтобы получить app_id, нужно зарегистрировать своё приложение на https://vk.com/dev


def get_user_login():
    vk_login = sys.argv[1]
    return vk_login


def get_user_password():
    vk_password = sys.argv[2]
    return vk_password


def get_vk_session(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
    )
    api_session = vk.API(session)
    return api_session


def get_friends_list(vk_session):
    friends_list = vk_session.friends.get(fields='online')
    return friends_list


def get_online_friends(friends_list):
    online_friends_list = [
        [friend['online'], friend['first_name'], friend['last_name']]
        for friend in friends_list if friend['online'] == 1
    ]
    return online_friends_list


def output_friends_to_console(friends_online):
    print('VK online friends list: ')
    for friend in friends_online:
        print('\t' + friend[1], friend[2])


if __name__ == '__main__':
    if len(sys.argv) == 3:
        login = get_user_login()
        password = get_user_password()
        vk_session = get_vk_session(login, password)
        friends_online = get_online_friends(get_friends_list(vk_session))
        output_friends_to_console(friends_online)
    else:
        print('Please define your VK login and password \nExample: vk_friends_online.py <login> <password>')

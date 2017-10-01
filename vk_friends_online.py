import sys
import time

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
        scope='friends',
    )
    api_session = vk.API(session)
    return api_session


def get_online_friends_id_list(vk_session):
    online_friends_id_list = vk_session.friends.getOnline()
    return online_friends_id_list


def get_friends_info(online_friends_id_list):
    online_friends_info = vk_session.users.get(user_ids=online_friends_id_list)
    return online_friends_info


def output_online_friends_to_console(online_friends_info):
    print('VK online friends list: ')
    for online_friend_info in online_friends_info:
        print('\t' + online_friend_info['first_name'],
              online_friend_info['last_name'] + ' https://vk.com/id' + str(online_friend_info['uid']))


if __name__ == '__main__':
    if len(sys.argv) == 3:
        login = get_user_login()
        password = get_user_password()
        vk_session = get_vk_session(login, password)
        friends_online = get_online_friends_id_list(vk_session)
        online_friends_info = get_friends_info(friends_online)
        output_online_friends_to_console(online_friends_info)
    else:
        print('Please define your VK login and password \nExample: vk_friends_online.py <login> <password>')

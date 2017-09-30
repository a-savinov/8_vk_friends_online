import sys
import time

import vk

APP_ID = 6202412  # чтобы получить app_id, нужно зарегистрировать своё приложение на https://vk.com/dev
API_TIMEOUT = .3

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


def get_online_friends_list(vk_session):
    friends_list = vk_session.friends.getOnline()
    return friends_list


def get_friend_info(user_id):
    friend_info = vk_session.users.get(user_id=user_id)
    return friend_info


def output_friends_to_console(online_friends_id_list):
    print('VK online friends list: ')
    for online_friend_id in online_friends_id_list:
        friend_info = get_friend_info(online_friend_id)
        print('\t' + friend_info[0]['first_name'],
              friend_info[0]['last_name'] + ' https://vk.com/id' + str(online_friend_id))
        time.sleep(API_TIMEOUT)  # Api restrictions 5 requests per second


if __name__ == '__main__':
    if len(sys.argv) == 3:
        login = get_user_login()
        password = get_user_password()
        vk_session = get_vk_session(login, password)
        friends_online = get_online_friends_list(vk_session)
        output_friends_to_console(friends_online)
    else:
        print('Please define your VK login and password \nExample: vk_friends_online.py <login> <password>')

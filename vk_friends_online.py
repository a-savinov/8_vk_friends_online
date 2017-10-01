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


def output_online_friend_to_console(online_friend_info):
        print('\t %s %s https://vk.com/id%s' % (online_friend_info['first_name'],
                                                online_friend_info['last_name'],
                                                online_friend_info['uid'])
              )


if __name__ == '__main__':
    if len(sys.argv) == 3:
        login = get_user_login()
        password = get_user_password()
        vk_session = get_vk_session(login, password)
        friends_online = get_online_friends_id_list(vk_session)
        online_friends_info = get_friends_info(friends_online)
        print('VK online friends list:')
        for online_friend_info in online_friends_info:
            output_online_friend_to_console(online_friend_info)
    else:
        print('Please define your VK login and password \nExample: vk_friends_online.py <login> <password>')

import argparse
import getpass

import vk

APP_ID = 6202412  # you can get APP_ID on https://vk.com/dev


def get_user_login(namespace):
    vk_login = namespace.login
    return vk_login


def get_user_password(namespace):
    if not namespace.password:
        vk_password = getpass.getpass(prompt='Enter your VK password: ')
    else:
        vk_password = namespace.password
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
    print('\t{} {} https://vk.com/id{}'.format(online_friend_info['first_name'],
                                             online_friend_info['last_name'],
                                             online_friend_info['uid']))


def input_argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--password', required=False,
                        help='User password for VK (optional)')
    parser.add_argument('-l', '--login', required=True,
                        help='User login for VK')
    return parser


if __name__ == '__main__':
    parser = input_argument_parser()
    namespace = parser.parse_args()
    login = get_user_login(namespace)
    password = get_user_password(namespace)
    vk_session = get_vk_session(login, password)
    friends_online = get_online_friends_id_list(vk_session)
    online_friends_info = get_friends_info(friends_online)
    print('VK online friends list:')
    for online_friend_info in online_friends_info:
        output_online_friend_to_console(online_friend_info)

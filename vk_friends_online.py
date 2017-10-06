import argparse
import getpass

import vk

APP_ID = 6202412  # you can get APP_ID on https://vk.com/dev


def get_vk_session(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends',
    )
    api_session = vk.API(session)
    return api_session


def output_online_friend_to_console(online_friend_info):
    print('\t{} {} https://vk.com/id{}'.format(
                                            online_friend_info['first_name'],
                                            online_friend_info['last_name'],
                                            online_friend_info['uid']
                                              )
          )


def get_input_argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--password', required=False,
                        help='User password for VK (optional)')
    parser.add_argument('-l', '--login', required=True,
                        help='User login for VK')
    return parser


if __name__ == '__main__':
    parser = get_input_argument_parser()
    args = parser.parse_args()
    login = args.login
    if not args.password:
        password = getpass.getpass(prompt='Enter your VK password: ')
    else:
        password = args.password
    vk_session = get_vk_session(login, password)
    online_friends_id_list = vk_session.friends.getOnline()
    online_friends_info = vk_session.users.get(user_ids=online_friends_id_list)
    print('VK online friends list:')
    for online_friend_info in online_friends_info:
        output_online_friend_to_console(online_friend_info)

import vk
import getpass


def get_user_login():
    login = input('Введие Вашe имя пользователя: ')
    return login


def get_user_password():
    password = getpass.getpass('Введите Ваш пароль: ')
    return password


def get_api(login, password, APP_ID, permission):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope=permission,
    )
    api = vk.API(session)
    return api


def get_online_friends_id(api):
    friends_online_id = api.friends.getOnline()
    return friends_online_id


def get_online_friends_info(api, friends_online_id):
    friends_online_info = api.users.get(user_ids=friends_online_id)
    return friends_online_info


def output_friends_to_console(friends_online_info):
    print ('Список друзей online: ')
    for item in friends_online_info:
        print (item['first_name'], item['last_name'])


if __name__ == '__main__':
    APP_ID = 5688584
    permission = 2
    login = get_user_login()
    password = get_user_password()
    api = get_api(login, password, APP_ID, permission)
    friends_online_id = get_online_friends_id(api)
    friends_online_info = get_online_friends_info(api, friends_online_id)
    output_friends_to_console(friends_online_info)

import sys
from users.repositories import UserRepositories
from users.services import UserServices
from users.handlers import UserHandlers

def init():
    user_repositories = UserRepositories()
    user_services = UserServices(user_repositories)
    user_handlers = UserHandlers(user_services)

    while True:
        command = input('SIGN_UP or SIGN_IN or CHANGE_PASSWORD or Q: ')

        match command:
            case 'sign_up':
                username, password = input('Input your username and password for registration: ').split()
                user_handlers.sign_up(username, password)
            
            case 'sign_in':
                username, password = input('Input your username and password for login: ').split()
                user_handlers.sign_in(username, password)

            case 'change_password':
                username, password = input('Login for change password: ').split()
                correct_user = user_handlers.sign_in(username, password)
                if correct_user:
                    new_password = input('Enter new password: ')
                    user_handlers.change_password(correct_user=correct_user, password=new_password)
                else:
                    print('Wrong account!!!')
            
            case 'q':
                sys.exit(0)
            
            case _:
                print('invalid command, try again')


if __name__ == '__main__':
    init()
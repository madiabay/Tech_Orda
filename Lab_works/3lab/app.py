from BankAccount.services import BankAccountServices
from BankAccount.repositories import BankAccountRepositories
from BankAccount.handlers import BankAccountHandlers, moneyConversion


def init():
    bank_account_repositories = BankAccountRepositories()
    bank_account_services = BankAccountServices(bank_account_repositories)
    bank_account_handlers = BankAccountHandlers(bank_account_services)

    command = ''
    while True:
        if not command:
            command = input('\033[37m' + 
            """
Выберите ваше действие:
1. Создание пользователя
2. Выбрать пользователя
0. Выйти

"""
            )
        
        match command:
            case '1':
                list_user_information = input('\033[37m' + 
"""
Введите ваше имя, фамилию и тип аккаунта (через пробел):
"""
                ).split()

                print()

                if len(list_user_information) == 3:
                    name, surname, account = list_user_information

                    if bank_account_handlers.create_user(name, surname, account):
                        command = '1'
                    else:
                        command = ''
                else:
                    print('\033[31m' + 'Данные введены неверно!!! Попробуйте еще раз')
            
            case '2':
                username = input('\033[37m' + '\nВведите ваше имя пользователя:\n')

                print()

                a = bank_account_handlers.get_user(username=username)
                
                if not a:
                    command = ''

                while a:
                    command_v2 = input('\033[37m' + 
"""                        
Выберите ваше действие:
1. Добавить деньги на счет
2. Высчитать деньги со счета
3. Конвертация денег
0. Выйти

"""
                    )

                    match command_v2:
                        case '1':
                            num = float(input('\033[37m' + 'Введите сумму, которую хотите добавить: '))
                            a.cash_amount += num
                            print(a)
                        case '2':
                            while True:
                                num = float(input('\033[37m' + 'Введите сумму, которую хотите вычесть: '))
                                if a.cash_amount >= num:
                                    a.cash_amount -= num
                                    print(a)
                                    break
                                else:
                                    print('\033[31m' + 'ОШИБКА! УКАЗАННАЯ СУММА БОЛЬШЕ СУММЫ НА СЧЕТЕ!!!')
                        case '3':
                            currency = input('\033[37m' + 'На какую валюту конвертировать: ').upper()

                            if a.account.value == currency:
                                print(a)
                                print('\033[31m' + 'Уже конвертирован на эту валюту!!!')
                            else:
                                moneyConversion(a, currency)
                                print(a)
                        case '0':
                            command = ''
                            break
            case '0':
                break

if __name__ == '__main__':
    init()
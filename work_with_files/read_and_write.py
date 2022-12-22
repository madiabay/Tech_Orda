# file = open('text.txt', mode='r')
# print(file.read())
# print()

# print(file.readline())

# print(file.readlines())

# for line in file.readlines():
#     print(line, end='')
# print()



# file = open('text.txt', mode='w')
# file.write('madiabay')
# file.close()

# file = open('text.txt', mode='a')
# file.write('some data\n')
# file.close()


# with open('text.txt', mode='r') as file:
#     print(file.read())

# # print(file.read())



# # CONTEXT MANAGER CLASS
# class ContextManager:

#     def __init__(self, filename: str, data: str) -> None:
#         self.filename = filename
#         self.data = data

#     def __enter__(self):
#         print('enter to context manager')
#         with open(self.filename, mode='w') as file:
#             file.write(self.data)

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('exit to context manager')
#         print(exc_type, exc_val, exc_tb)


# with ContextManager(filename='111.txt', data='madiabay') as our_manager:
#     print(our_manager)


# CONTEXT MANAGER FUNCTION
from contextlib import contextmanager

"""Yield — это ключевое слово в Python, которое используется для возврата из функции с сохранением состояния ее локальных переменных, и при повторном вызове такой функции выполнение продолжается с оператора yield, на котором ее работа была прервана. Любая функция, содержащая ключевое слово yield, называется генератором. Можно сказать, yield — это то, что делает ее генератором. Хотя оператор yield в Python не отличается популярностью, но он имеет множество достоинств, о которых стоит знать."""

@contextmanager
def context_manager():
    file = open('111.txt', mode='a')
    try:
        print('enter to context manager')
        yield file # yield это типа return, Но yield сохраняет состояние функций. Если мы бы использовали return то у нас finally не реализовался бы. 
    finally:
        print('exit to context manager')
        file.close()

with context_manager() as our_manager:
    our_manager.write('SUIIIII')
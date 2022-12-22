import os

# try:
#     os.mkdir('my_dir')
# except FileExistsError as e:
#     print(e)

# os.makedirs('abay/baurzhan/madi')



# from fnmatch import fnmatch
# base_path = os.path.basename('./my_dir/')
# with os.scandir('./my_dir/') as entries:
#     for entry in entries:
#         if entry.is_file():
#             if fnmatch(entry.name, '*_*.txt'):
#                 with open(os.path.join(base_path, entry), mode='r') as file:
#                     print(file.read())



# os.rename('test.ipynb', 'test_ts.ipynb') # rename
# os.replace('test_ts.ipynb', 'test.ipynb') # rename and replace

# os.remove('111.txt') # remove
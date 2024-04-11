import os

def find(path):
    file_list = os.listdir(path)
    # file_list.append(find(file_list[0]))

    if (os.path.isdir(file_list[0])):

    return file_list


print(find('.'))
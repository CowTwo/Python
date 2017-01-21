import os

def find(name, path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if (str.lower(name)==str.lower(file)):
                return os.path.join(root, file)

def find_all(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if (str.lower(name)==str.lower(file)):
                result.append(os.path.join(root, file))
    return result


print(find('Img_5160.jpg','F:/備份區/照片(20160828整理)'))

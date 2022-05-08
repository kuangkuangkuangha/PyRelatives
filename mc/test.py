import string
import glob
import os
import unicodedata
all_letters = string.ascii_letters + " .,;'-"
print(all_letters)

category_lines = {}
all_categories = []

# 返回的是所有txt文件路径
dataPath = glob.glob('/Users/zhangkuang/Documents/College/kuangkaungkaungha/py/mc/data/names/*.txt')
# print("data paths: ", dataPath)


def unicodeToAscii(s):
        return ''.join(
            c for c in unicodedata.normalize('NFD', s) # 将所有的字符标准化
            if unicodedata.category(c) != 'Mn'
            and c in all_letters
        )


def readLines(file_path):
        with open(file_path, encoding='utf-8') as some_file:
            return [unicodeToAscii(line.strip()) for line in some_file]


for filePath in dataPath:
    category = os.path.splitext(os.path.basename(filename))[0]
    # splittext 分割路径，返回路径名和文件扩展名的元组
    # print(os.path.basename(filename)) 打印的是文件文字

    all_categories.append(category)
    lines = readLines(filePath)

    category_lines[category] = lines

# print(category_lines)
print(all_categories)
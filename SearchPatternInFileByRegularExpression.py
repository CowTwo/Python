import re
filename = "D:/Python/TextFile.txt"

textfile = open(filename, 'r')
filetext = textfile.read()
textfile.close()

# 尋找 < > 內有4到5個數字 的pattern

for m in re.finditer("(<(\d{4,5})>)", filetext):
    print(m.group(0))
    print(m.group(1))
    print(m.group(2))
    print("start index:", m.start())

# 通過group我們可以選擇匹配到的字符串中「需要」的部分。
# m.group(0)即整個匹配到的字符串。
# 而 m.group(1) 則是在()中的子字符串。
# 相同的，如果有多個子字符串的匹配模式亦可用group(n)來取出。

# m.start 表示match到的字串在filetext的起始位置

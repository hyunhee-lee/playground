import sys
import re

def extract_phrase(s):
    list = []
    pattern = re.compile("(?<=')[^']+(?=')")
	# pattern = re.compile("\B'.*?'(?!\w)")
    for value in pattern.findall(s):
        list.append(value)
    return list

file = open('C:\GitHub\VNTG-N-ERP\studies\현이\변경문자열.txt', 'r', encoding='UTF-8')
fileStr = file.read()

# newfileStr = re.findall(r"'([^\s']*sample_2[^\s]*?)',", fileStr)

# (["'])(?:(?=(\\?))\2.)*?\1

# str = '''(["'])(?:(?=(\\?))\2.)*?\1'''
# print(str)

# newfileStr = re.sub('\d{4}', 'xxxx', fileStr)
# newfileStr = re.sub(r'"(["'])(?:(?=(\\?))\2.)*?\1"', 'xxxx', fileStr)
newfileStr = re.sub("([""'])(?:(?=(\\?))\2.)*?\1", 'xxxx', fileStr)
# newfileStr = re.findall("(["''])(?:(?=(\\?))\2.)*?\1", fileStr)
print(newfileStr)

# print(extract_phrase(fileStr))


# # list = [for str in file.read() if str == '(["'])(?:(?=(\\?))\2.)*?\1']

# findstr = fileStr.findall('COMMENT ON TABLE')
# print(type(findstr)



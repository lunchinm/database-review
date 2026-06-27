import re
c = open('数据库/第4节_恢复与向量数据库_知识清单.html', 'r', encoding='utf-8').read()
refs = re.findall(r'\.\.\/_images\/slide\d+[^\"\s<>]*', c)
print('Remaining:', refs)
if refs:
    idx = c.find(refs[0])
    print(c[max(0,idx-100):idx+200])

with open('数据库/第4节_恢复与向量数据库_知识清单.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re
refs = re.findall(r'\.\.\/_images\/slide\d+[^\"\s<>]*', c)
print(f'Old refs ({len(refs)}):')
for r in refs:
    print(f'  {r}')

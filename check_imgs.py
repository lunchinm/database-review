import re

files = [
    '数据库/第1节_查询为王_知识清单.html',
    '数据库/第2节_建模与范式_知识清单.html',
    '数据库/第3节_事务与并发_知识清单.html',
    '数据库/第4节_恢复与向量数据库_知识清单.html',
]

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    
    imgs = re.findall(r'<img[^>]*src="([^"]+)"[^>]*>', content)
    print(f'{f}: {len(imgs)} images')
    for img in imgs:
        print(f'  src={img}')
    print()

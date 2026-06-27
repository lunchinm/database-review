import subprocess

files = [
    '数据库/第1节_查询为王_知识清单.html',
    '数据库/第2节_建模与范式_知识清单.html',
    '数据库/第3节_事务与并发_知识清单.html',
    '数据库/第4节_恢复与向量数据库_知识清单.html',
]
for f in files:
    result = subprocess.run(['git', 'show', f'a508b03:{f}'], capture_output=True, encoding='utf-8', errors='replace')
    with open(f, 'w', encoding='utf-8') as fp:
        fp.write(result.stdout)
    has_ref = '../_images/' in result.stdout
    print(f'Restored {f}: {len(result.stdout)} chars, has _images refs: {has_ref}')

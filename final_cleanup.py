"""Final cleanup: remove any remaining ../_images/ references and their surrounding figure tags"""
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
    
    # Use a more flexible regex to remove any figure containing ../_images/
    pattern = re.compile(
        r'[ \t]*<figure[^>]*>.*?\.\.\/_images\/.*?</figure>\s*',
        re.DOTALL
    )
    
    content = pattern.sub('', content)
    
    # Verify
    remaining = re.findall(r'\.\.\/_images/', content)
    new_imgs = re.findall(r'images/s\d_[^\"\s<>]+', content)
    
    with open(f, 'w', encoding='utf-8') as fp:
        fp.write(content)
    
    print(f'{f}: {len(remaining)} remaining old refs, {len(new_imgs)} new images')

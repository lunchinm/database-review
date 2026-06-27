"""只移除src中包含../_images/的figure块"""
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
    
    # Only remove figure blocks that still have ../_images/ in src
    # Pattern: <figure ...> ... ../_images/slide... ... </figure>
    pattern = re.compile(
        r'[ \t]*<figure class="figure">\s*'
        r'<img src="\.\.\/_images\/slide\d+[^"]*"[^>]*>\s*'
        r'<figcaption>[^<]*</figcaption>\s*'
        r'</figure>\s*',
        re.DOTALL
    )
    
    before = content
    content = pattern.sub('', content)
    
    # Verify no remaining ../_images/ refs
    remaining = re.findall(r'\.\.\/_images/', content)
    
    with open(f, 'w', encoding='utf-8') as fp:
        fp.write(content)
    
    removed = before.count('<figure') - content.count('<figure')
    print(f'{f}: removed {removed} old figures, remaining _images refs: {len(remaining)}')
    
    # Count remaining new images
    new_imgs = re.findall(r'images/s\d_[^\"\s<>]+', content)
    print(f'  New image refs: {len(new_imgs)}')

"""
移除HTML中指向不存在图片的figure块
"""
import re
import os

BASE = r"c:\Users\MIC lunchinm\Desktop\学习资料\大二\大二下\数据库\学习"

files = [
    "数据库/第1节_查询为王_知识清单.html",
    "数据库/第2节_建模与范式_知识清单.html",
    "数据库/第3节_事务与并发_知识清单.html",
    "数据库/第4节_恢复与向量数据库_知识清单.html",
]

for filepath in files:
    fullpath = os.path.join(BASE, filepath)
    with open(fullpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all figure blocks that still contain ../_images/ references
    pattern = re.compile(
        r'\s*<figure[^>]*>.*?\.\.\/_images\/slide\d+.*?</figure>\s*',
        re.DOTALL
    )
    
    new_content = pattern.sub('\n', content)
    
    # Also check for any remaining ../_images/ references outside figures
    remaining = re.findall(r'\.\.\/_images\/slide\d+[^\"\']*\.jpg', new_content)
    
    with open(fullpath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"{filepath}: removed figures, {len(remaining)} remaining refs")

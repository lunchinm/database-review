"""分析当前HTML状态"""
import re

files = [
    "数据库/第1节_查询为王_知识清单.html",
    "数据库/第2节_建模与范式_知识清单.html",
    "数据库/第3节_事务与并发_知识清单.html",
    "数据库/第4节_恢复与向量数据库_知识清单.html",
]

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    
    old_refs = re.findall(r'\.\.\/_images\/[^\"\']+', content)
    new_refs = re.findall(r'images/s\d_[^\"\']+', content)
    figures = re.findall(r'<figure[^>]*>.*?</figure>', content, re.DOTALL)
    
    print(f"\n=== {f} ===")
    print(f"Old refs: {len(old_refs)}, New refs: {len(new_refs)}, Figures: {len(figures)}")
    
    for i, fig in enumerate(figures):
        # Extract img src
        src_match = re.search(r'src="([^"]+)"', fig)
        cap_match = re.search(r'<figcaption>(.*?)</figcaption>', fig)
        print(f"  Fig{i+1}: src={src_match.group(1) if src_match else 'N/A'}, caption={cap_match.group(1) if cap_match else 'N/A'}")

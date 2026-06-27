with open('数据库/第2节_建模与范式_知识清单.html', 'r', encoding='utf-8') as f:
    c = f.read()

print("Has 'images/':", 'images/' in c)
print("Has 'figure':", 'figure' in c)
print("Has '<img':", '<img' in c)
print("Has 'slide':", 'slide' in c)
print("Length:", len(c))

import re
# Find all image-like references
refs = re.findall(r'images/[^\"\s<>]+', c)
print(f"Image refs: {refs}")

# Find any src= patterns
srcs = re.findall(r'src="([^"]+)"', c)
print(f"src values: {srcs}")

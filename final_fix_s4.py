"""只处理第4节中剩余的旧图片引用"""
import re

with open('数据库/第4节_恢复与向量数据库_知识清单.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 第4节剩余的7个旧slide引用
old_slides = [
    'slide1923_p305_s2.jpg',
    'slide1924_p305_s3.jpg',
    'slide1925_p305_s4.jpg',
    'slide1966_p313_s3.jpg',
    'slide1967_p313_s4.jpg',
    'slide1970_p314_s2.jpg',
    'slide1989_p317_s5.jpg',
]

for slide in old_slides:
    # Find the figure block containing this slide
    # Pattern: any <figure ...> that contains this slide reference
    pattern = re.compile(
        r'[ \t]*<figure[^>]*>\s*'
        + r'[ \t]*<img[^>]*' + re.escape(slide) + r'[^>]*>\s*'
        + r'<figcaption>[^<]*</figcaption>\s*'
        + r'</figure>\s*',
        re.DOTALL
    )
    content = pattern.sub('', content)

# Verify
remaining = re.findall(r'\.\.\/_images/', content)
new_imgs = re.findall(r'images/s4_\d[^\"\s<>]+', content)

with open('数据库/第4节_恢复与向量数据库_知识清单.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f'Remaining old refs: {len(remaining)}')
print(f'New images: {len(new_imgs)}')
for img in new_imgs:
    print(f'  {img}')

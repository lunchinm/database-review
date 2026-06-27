"""
精确替换HTML中的图片src路径（不删除figure块）
"""
import re
import os

BASE = r"c:\Users\MIC lunchinm\Desktop\学习资料\大二\大二下\数据库\学习"

# 映射：旧slide文件名 -> 新图片文件名 (None表示不替换保留原样)
# 同一张新图可以替换多张旧图
MAPPINGS = {
    # === 第1节 ===
    "数据库/第1节_查询为王_知识清单.html": {
        "slide0002_p1_s2.jpg": "s1_01_framework.png",
        "slide0005_p2_s1.jpg": "s1_02_dbms_components.png",
        "slide0013_p4_s1.jpg": "s1_03_relational_algebra.png",
        "slide0017_p5_s1.jpg": "s1_03_relational_algebra.png",
        "slide0021_p6_s1.jpg": "s1_04_sql_join.png",
        "slide0022_p6_s2.jpg": "s1_04_sql_join.png",
        "slide0029_p8_s1.jpg": "s1_05_pitfalls.png",
        "slide0031_p8_s3.jpg": "s1_05_pitfalls.png",
        # 以下旧图没有对应新图，保留原样（不替换）
    },
    # === 第2节 ===
    "数据库/第2节_建模与范式_知识清单.html": {
        "slide0033_p9_s2.jpg": "s2_01_framework.png",
        "slide0036_p10_s1.jpg": "s2_02_er_elements.png",
        "slide0037_p10_s2.jpg": "s2_02_er_elements.png",
        "slide0038_p10_s3.jpg": "s2_02_er_elements.png",
        "slide0039_p10_s4.jpg": "s2_02_er_elements.png",
        "slide0052_p14_s1.jpg": "s2_03_nf_pyramid.png",
        "slide0053_p14_s2.jpg": "s2_03_nf_pyramid.png",
        "slide0054_p14_s3.jpg": "s2_03_nf_pyramid.png",
        "slide0055_p14_s4.jpg": "s2_04_bcnf_check.png",
        "slide0056_p15_s1.jpg": "s2_04_bcnf_check.png",
        "slide0057_p15_s2.jpg": "s2_04_bcnf_check.png",
    },
    # === 第3节 ===
    "数据库/第3节_事务与并发_知识清单.html": {
        "slide0062_p17_s2.jpg": "s3_01_framework.png",
        "slide0065_p18_s1.jpg": "s3_02_acid.png",
        "slide0066_p18_s2.jpg": "s3_02_acid.png",
        "slide0067_p18_s3.jpg": "s3_02_acid.png",
        "slide0074_p20_s2.jpg": "s3_03_2pl.png",
        "slide0075_p20_s3.jpg": "s3_03_2pl.png",
        "slide0077_p21_s1.jpg": "s3_03_2pl.png",
        "slide0081_p22_s1.jpg": "s3_04_redo_undo.png",
        "slide0082_p22_s2.jpg": "s3_04_redo_undo.png",
        "slide0083_p22_s3.jpg": "s3_04_redo_undo.png",
    },
    # === 第4节 ===
    "数据库/第4节_恢复与向量数据库_知识清单.html": {
        "slide1905_p301_s5.jpg": "s4_01_failure_types.png",
        "slide1908_p302_s2.jpg": "s4_01_failure_types.png",
        "slide1909_p302_s3.jpg": "s4_01_failure_types.png",
        "slide1913_p303_s2.jpg": "s4_02_steal_force.png",
        "slide1914_p303_s3.jpg": "s4_02_steal_force.png",
        "slide1916_p303_s5.jpg": "s4_02_steal_force.png",
        "slide1918_p304_s2.jpg": "s4_03_wal.png",
        "slide1919_p304_s3.jpg": "s4_03_wal.png",
        "slide1920_p304_s4.jpg": "s4_03_wal.png",
        "slide1921_p304_s5.jpg": "s4_03_wal.png",
        "slide1960_p312_s3.jpg": "s4_04_ann_strategies.png",
        "slide1973_p314_s5.jpg": "s4_04_ann_strategies.png",
        "slide1975_p315_s2.jpg": "s4_04_ann_strategies.png",
        "slide1976_p315_s3.jpg": "s4_04_ann_strategies.png",
        "slide1977_p315_s4.jpg": "s4_04_ann_strategies.png",
        "slide1982_p316_s3.jpg": "s4_04_ann_strategies.png",
        "slide1983_p316_s4.jpg": "s4_04_ann_strategies.png",
        "slide1985_p317_s1.jpg": "s4_04_ann_strategies.png",
        "slide1988_p317_s4.jpg": "s4_04_ann_strategies.png",
    },
}

def replace_src(filepath, mappings):
    fullpath = os.path.join(BASE, filepath)
    with open(fullpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    count = 0
    for old_name, new_name in mappings.items():
        old_src = f"../_images/{old_name}"
        new_src = f"images/{new_name}"
        if old_src in content:
            content = content.replace(old_src, new_src)
            count += 1
            print(f"  Replaced: {old_name} -> {new_name}")
    
    # Count remaining old refs
    remaining = re.findall(r'\.\.\/_images\/slide\d+[^\"\']*\.jpg', content)
    
    with open(fullpath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  File: {filepath}")
    print(f"  Replaced: {count}, Remaining old refs: {len(remaining)}")
    if remaining:
        for r in remaining:
            print(f"    UNCHANGED: {r}")
    print()
    return count, len(remaining)

def main():
    total_replaced = 0
    total_remaining = 0
    for filepath, mappings in MAPPINGS.items():
        c, r = replace_src(filepath, mappings)
        total_replaced += c
        total_remaining += r
    print(f"=== TOTAL: {total_replaced} replaced, {total_remaining} remaining ===")

if __name__ == "__main__":
    main()

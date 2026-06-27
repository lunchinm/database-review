"""
替换HTML文件中的旧图片引用为新生成的AI图片
"""
import re
import os

BASE = r"c:\Users\MIC lunchinm\Desktop\学习资料\大二\大二下\数据库\学习"

# 新图片路径前缀
IMG_PREFIX = "images/"

# 每张新图对应要替换的旧图范围
REPLACEMENTS = {
    # 第1节：查询为王 (5张新图替换14张旧图)
    "数据库/第1节_查询为王_知识清单.html": [
        # 旧图范围 -> 新图文件名
        (r"slide0002_p1_s2\.jpg", "s1_01_framework.png"),
        (r"slide0005_p2_s1\.jpg", "s1_02_dbms_components.png"),
        (r"slide0013_p4_s1\.jpg|slide0017_p5_s1\.jpg", "s1_03_relational_algebra.png"),
        (r"slide0021_p6_s1\.jpg|slide0022_p6_s2\.jpg", "s1_04_sql_join.png"),
        (r"slide0029_p8_s1\.jpg|slide0031_p8_s3\.jpg", "s1_05_pitfalls.png"),
        # 移除未匹配的旧图（保留figcaption但不显示图）
        (r"slide0006_p2_s2\.jpg", None),  # 三级模式 - 文字说明即可
        (r"slide0007_p2_s3\.jpg", None),  # 四种键 - 文字说明即可
        (r"slide0008_p2_s4\.jpg", None),  # 三类完整性
        (r"slide0009_p3_s1\.jpg", None),  # 外键NULL
        (r"slide0010_p3_s2\.jpg", None),  # 视图
        (r"slide0025_p7_s1\.jpg", None),  # 相关子查询
    ],
    # 第2节：建模与范式 (4张新图替换18张旧图)
    "数据库/第2节_建模与范式_知识清单.html": [
        (r"slide0033_p9_s2\.jpg", "s2_01_framework.png"),
        (r"slide0036_p10_s1\.jpg|slide0037_p10_s2\.jpg|slide0038_p10_s3\.jpg|slide0039_p10_s4\.jpg", "s2_02_er_elements.png"),
        (r"slide0052_p14_s1\.jpg|slide0053_p14_s2\.jpg|slide0054_p14_s3\.jpg", "s2_03_nf_pyramid.png"),
        (r"slide0055_p14_s4\.jpg|slide0056_p15_s1\.jpg|slide0057_p15_s2\.jpg", "s2_04_bcnf_check.png"),
        # 移除未匹配的旧图
        (r"slide0042_p11_s3\.jpg", None),
        (r"slide0043_p11_s4\.jpg", None),
        (r"slide0046_p12_s3\.jpg", None),
        (r"slide0047_p12_s4\.jpg", None),
        (r"slide0048_p13_s1\.jpg", None),
        (r"slide0049_p13_s2\.jpg", None),
        (r"slide0060_p16_s1\.jpg", None),
    ],
    # 第3节：事务与并发 (4张新图替换15张旧图)
    "数据库/第3节_事务与并发_知识清单.html": [
        (r"slide0062_p17_s2\.jpg", "s3_01_framework.png"),
        (r"slide0065_p18_s1\.jpg|slide0066_p18_s2\.jpg|slide0067_p18_s3\.jpg", "s3_02_acid.png"),
        (r"slide0074_p20_s2\.jpg|slide0075_p20_s3\.jpg|slide0077_p21_s1\.jpg", "s3_03_2pl.png"),
        (r"slide0081_p22_s1\.jpg|slide0082_p22_s2\.jpg|slide0083_p22_s3\.jpg", "s3_04_redo_undo.png"),
        # 移除未匹配的旧图
        (r"slide0069_p19_s1\.jpg", None),
        (r"slide0070_p19_s2\.jpg", None),
        (r"slide0071_p19_s3\.jpg", None),
        (r"slide0072_p19_s4\.jpg", None),
        (r"slide0085_p23_s1\.jpg", None),
    ],
    # 第4节：恢复与向量数据库 (4张新图替换27张旧图)
    "数据库/第4节_恢复与向量数据库_知识清单.html": [
        (r"slide1905_p301_s5\.jpg|slide1908_p302_s2\.jpg|slide1909_p302_s3\.jpg", "s4_01_failure_types.png"),
        (r"slide1913_p303_s2\.jpg|slide1914_p303_s3\.jpg|slide1916_p303_s5\.jpg", "s4_02_steal_force.png"),
        (r"slide1918_p304_s2\.jpg|slide1919_p304_s3\.jpg|slide1920_p304_s4\.jpg|slide1921_p304_s5\.jpg", "s4_03_wal.png"),
        (r"slide1960_p312_s3\.jpg|slide1973_p314_s5\.jpg|slide1975_p315_s2\.jpg|slide1976_p315_s3\.jpg|slide1977_p315_s4\.jpg|slide1982_p316_s3\.jpg|slide1983_p316_s4\.jpg|slide1985_p317_s1\.jpg|slide1988_p317_s4\.jpg", "s4_04_ann_strategies.png"),
        # 移除未匹配的旧图
        (r"slide1923_p305_s2\.jpg", None),
        (r"slide1924_p305_s3\.jpg", None),
        (r"slide1925_p305_s4\.jpg", None),
        (r"slide1966_p313_s3\.jpg", None),
        (r"slide1967_p313_s4\.jpg", None),
        (r"slate1968_p313_s5\.jpg", None),
        (r"slide1970_p314_s2\.jpg", None),
        (r"slide1989_p317_s5\.jpg", None),
    ],
}

def replace_images_in_file(filepath, replacements):
    """替换文件中的图片引用"""
    fullpath = os.path.join(BASE, filepath)
    with open(fullpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    for old_pattern, new_img in replacements:
        if new_img is None:
            # 移除整个 <figure> 块
            # 匹配包含该图片的 figure 元素
            pattern = re.compile(
                r'<figure[^>]*>.*?<img[^>]*' + old_pattern + r'[^>]*>.*?</figure>',
                re.DOTALL
            )
            content = pattern.sub('', content)
        else:
            # 替换 src 路径
            old_src_pattern = r'\.\.\/_images\/' + old_pattern
            new_src = IMG_PREFIX + new_img
            content = re.sub(old_src_pattern, new_src, content)
    
    if content != original:
        with open(fullpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {filepath}")
        return True
    else:
        print(f"No changes: {filepath}")
        return False

def main():
    for filepath, replacements in REPLACEMENTS.items():
        replace_images_in_file(filepath, replacements)

if __name__ == "__main__":
    main()

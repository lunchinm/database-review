#!/usr/bin/env python3
"""
用 matplotlib 生成数据库复习资料的全部 17 张知识图表。
图片输出到 images/ 目录。
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Arc, Circle, Rectangle, Polygon, FancyArrow
import numpy as np
import os

# 统一风格
plt.rcParams.update({
    "font.sans-serif": ["Microsoft YaHei", "SimHei", "Noto Sans SC", "PingFang SC"],
    "axes.unicode_minus": False,
    "figure.dpi": 150,
    "savefig.dpi": 150,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.1,
})

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")
os.makedirs(OUTPUT_DIR, exist_ok=True)

COLORS = {
    "blue": "#2563eb", "green": "#16a34a", "red": "#dc2626", "orange": "#ea580c",
    "purple": "#7c3aed", "cyan": "#0891b2", "yellow": "#ca8a04", "pink": "#db2777",
    "teal": "#0d9488", "bg": "#f8fafc", "dark": "#1e293b", "mid": "#475569",
    "light": "#cbd5e1", "white": "#ffffff",
}


def box_text(ax, x, y, w, h, text, color=COLORS["blue"], text_color="white", fontsize=9, bold=True):
    """绘制圆角矩形文本框"""
    rect = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.15", facecolor=color,
                          edgecolor="none", alpha=0.9, linewidth=0)
    ax.add_patch(rect)
    weight = "bold" if bold else "normal"
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fontsize,
            color=text_color, fontweight=weight)
    return rect


def arrow(ax, x1, y1, x2, y2, color=COLORS["mid"], lw=1.5):
    """绘制箭头"""
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="->", color=color, lw=lw, connectionstyle="arc3,rad=0"))


def save_fig(fig, name):
    path = os.path.join(OUTPUT_DIR, name)
    fig.savefig(path, facecolor="white", edgecolor="none")
    plt.close(fig)
    print(f"  [OK] {name}")


# ============================================================
# Section 1: 查询为王 (5 images)
# ============================================================

def s1_01_framework():
    """第1节知识框架 - 四个板块"""
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_xlim(0, 10); ax.set_ylim(0, 5); ax.axis("off")
    ax.set_facecolor(COLORS["bg"])

    title = "第1节：查询为王 — 知识框架"
    ax.text(5, 4.5, title, ha="center", va="center", fontsize=16, fontweight="bold", color=COLORS["dark"])

    boxes = [
        (1, 1.5, 3.5, 2.0, "数据库系统\n与关系模型", COLORS["blue"]),
        (5.5, 1.5, 3.5, 2.0, "关系代数", COLORS["purple"]),
        (1, 3.2, 3.5, 1.0, "SQL查询", COLORS["green"]),
        (5.5, 3.2, 3.5, 1.0, "查询优化", COLORS["orange"]),
    ]
    for x, y, w, h, txt, c in boxes:
        box_text(ax, x, y, w, h, txt, c, fontsize=11)

    # Connecting arrows
    arrow(ax, 2.75, 2.75, 3.5, 2.75, COLORS["mid"])
    arrow(ax, 5.5, 2.75, 4.25, 2.75, COLORS["mid"])
    arrow(ax, 2.75, 3.2, 2.75, 3.7, COLORS["mid"])
    arrow(ax, 7.25, 3.2, 7.25, 3.7, COLORS["mid"])

    save_fig(fig, "s1_01_framework.png")


def s1_02_dbms_components():
    """DBMS五大组件"""
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_xlim(0, 10); ax.set_ylim(0, 5); ax.axis("off")
    ax.set_facecolor(COLORS["bg"])

    ax.text(5, 4.6, "DBMS 五大组件与查询处理器", ha="center", fontsize=15, fontweight="bold", color=COLORS["dark"])

    # 5 components
    comps = [
        (0.5, 2.0, 2.5, 1.8, "查询处理器\nDML编译器·优化器·执行引擎", COLORS["blue"]),
        (3.5, 2.0, 2.5, 1.8, "存储管理器\n缓冲区·文件·授权·完整性", COLORS["green"]),
        (6.5, 2.0, 2.5, 1.8, "事务管理器\n并发控制·恢复管理(ACID)", COLORS["red"]),
    ]
    for x, y, w, h, txt, c in comps:
        box_text(ax, x, y, w, h, txt, c, fontsize=9)

    # 数据流 arrows
    arrow(ax, 3, 3.8, 1.75, 3.8, COLORS["mid"])
    arrow(ax, 6, 3.8, 4.75, 3.8, COLORS["mid"])

    ax.text(5, 1.2, "SQL → 查询处理器(解析→优化→执行) → 存储管理器(缓冲→磁盘)", ha="center", fontsize=10, color=COLORS["mid"])

    save_fig(fig, "s1_02_dbms_components.png")


def s1_03_relational_algebra():
    """关系代数运算"""
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_xlim(0, 10); ax.set_ylim(0, 5); ax.axis("off")
    ax.set_facecolor(COLORS["bg"])

    ax.text(5, 4.6, "关系代数：基本运算与扩展运算", ha="center", fontsize=15, fontweight="bold", color=COLORS["dark"])

    # 基本运算
    basic = [
        (0.5, 2.5, 1.8, 1.2, "选择 σ", COLORS["blue"]),
        (2.6, 2.5, 1.8, 1.2, "投影 π", COLORS["blue"]),
        (4.7, 2.5, 1.8, 1.2, "并 ∪", COLORS["blue"]),
        (6.8, 2.5, 1.8, 1.2, "差 −", COLORS["blue"]),
    ]
    for x, y, w, h, txt, c in basic:
        box_text(ax, x, y, w, h, txt, c, fontsize=10)

    # 扩展运算
    ext = [
        (1.5, 0.8, 2.0, 1.2, "笛卡尔积 ×", COLORS["purple"]),
        (4.0, 0.8, 2.0, 1.2, "连接 Join", COLORS["purple"]),
        (6.5, 0.8, 2.0, 1.2, "除法 ÷", COLORS["purple"]),
    ]
    for x, y, w, h, txt, c in ext:
        box_text(ax, x, y, w, h, txt, c, fontsize=10)

    # Labels
    ax.text(5, 3.9, "基本运算 (5个)", ha="center", fontsize=10, color=COLORS["mid"], style="italic")
    ax.text(5, 2.2, "扩展运算 (3个)", ha="center", fontsize=10, color=COLORS["mid"], style="italic")

    # 箭头从基本到扩展
    for i in range(5):
        arrow(ax, 1.4 + i * 2.1, 2.4, 2.5 + i * 1.0, 2.1, COLORS["light"])

    # 提示
    ax.text(5, 0.2, "口诀：σ砍行、π砍列、Join是带条件的×、÷回答\"包含全部\"", ha="center", fontsize=9, color=COLORS["orange"])

    save_fig(fig, "s1_03_relational_algebra.png")


def s1_04_sql_join():
    """SQL连接查询"""
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_xlim(0, 10); ax.set_ylim(0, 5); ax.axis("off")
    ax.set_facecolor(COLORS["bg"])

    ax.text(5, 4.6, "SQL 查询：JOIN 连接类型", ha="center", fontsize=15, fontweight="bold", color=COLORS["dark"])

    # JOIN types
    joins = [
        (0.3, 2.5, 2.8, 1.6, "INNER JOIN\n匹配行拼接", COLORS["blue"]),
        (3.5, 2.5, 2.8, 1.6, "LEFT JOIN\n左表全保留", COLORS["green"]),
        (6.7, 2.5, 2.8, 1.6, "NATURAL JOIN\n自动按同名列连接", COLORS["purple"]),
    ]
    for x, y, w, h, txt, c in joins:
        box_text(ax, x, y, w, h, txt, c, fontsize=10)

    # SQL example
    ax.text(5, 1.8, "SELECT c.name, p.name", ha="center", fontsize=9, fontfamily="monospace", color=COLORS["dark"])
    ax.text(5, 1.4, "FROM Orders NATURAL JOIN Customers NATURAL JOIN Products", ha="center", fontsize=9, fontfamily="monospace", color=COLORS["dark"])
    ax.text(5, 1.0, "WHERE city = 'Shanghai' AND price > 1000", ha="center", fontsize=9, fontfamily="monospace", color=COLORS["dark"])

    ax.text(5, 0.3, "三表连接 · 多条件过滤 · 相关子查询(IN/EXISTS)", ha="center", fontsize=9, color=COLORS["orange"])

    save_fig(fig, "s1_04_sql_join.png")


def s1_05_pitfalls():
    """查询优化易错清单"""
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_xlim(0, 10); ax.set_ylim(0, 5); ax.axis("off")
    ax.set_facecolor(COLORS["bg"])

    ax.text(5, 4.6, "查询优化 — 易错清单", ha="center", fontsize=15, fontweight="bold", color=COLORS["dark"])

    # 执行计划对比
    box_text(ax, 0.5, 2.8, 4.0, 1.4, "计划A (差)：先连接后过滤\n中间结果巨大·大量白做", COLORS["red"], fontsize=9)
    box_text(ax, 5.5, 2.8, 4.0, 1.4, "计划C (优)：先过滤后连接\n中间结果极小·显著更快", COLORS["green"], fontsize=9)

    arrow(ax, 4.6, 3.5, 5.4, 3.5, COLORS["orange"])
    ax.text(5, 3.7, "优化", ha="center", fontsize=8, color=COLORS["orange"], fontweight="bold")

    # 易错点
    pitfalls = [
        "外键NULL：全参与→NOT NULL",
        "WHERE不能写聚合函数→放HAVING",
        "GROUP BY后SELECT非聚合列须在分组键",
        "投影去重·除法用于\"具备全部\"语义",
    ]
    for i, p in enumerate(pitfalls):
        ax.text(5, 1.8 - i * 0.4, f"• {p}", ha="center", fontsize=9, color=COLORS["mid"])

    save_fig(fig, "s1_05_pitfalls.png")


# ============================================================
# Section 2: 建模与范式 (4 images)
# ============================================================

def s2_01_framework():
    """第2节知识框架"""
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_xlim(0, 10); ax.set_ylim(0, 5); ax.axis("off")
    ax.set_facecolor(COLORS["bg"])

    ax.text(5, 4.6, "第2节：建模与范式 — 知识框架", ha="center", fontsize=15, fontweight="bold", color=COLORS["dark"])

    boxes = [
        (0.3, 1.2, 2.0, 2.5, "ER建模\n实体·属性\n·联系", COLORS["teal"]),
        (2.8, 1.2, 2.0, 2.5, "ER转\n关系模式\n5条规则", COLORS["blue"]),
        (5.3, 1.2, 2.0, 2.5, "函数依赖\nArmstrong\n·候选键", COLORS["purple"]),
        (7.8, 1.2, 2.0, 2.5, "范式与分解\n1NF→BCNF\n·无损连接", COLORS["orange"]),
    ]
    for x, y, w, h, txt, c in boxes:
        box_text(ax, x, y, w, h, txt, c, fontsize=10)

    for i in range(3):
        arrow(ax, 2.4 + i * 2.5, 2.5, 2.7 + i * 2.5, 2.5, COLORS["mid"])

    save_fig(fig, "s2_01_framework.png")


def s2_02_er_elements():
    """ER模型三要素 + 属性分类"""
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_xlim(0, 10); ax.set_ylim(0, 5); ax.axis("off")
    ax.set_facecolor(COLORS["bg"])

    ax.text(5, 4.6, "ER 模型：三要素与属性分类", ha="center", fontsize=15, fontweight="bold", color=COLORS["dark"])

    # 三要素
    box_text(ax, 0.5, 3.0, 2.5, 1.2, "实体 Entity\n矩形 □", COLORS["blue"], fontsize=10)
    box_text(ax, 3.8, 3.0, 2.5, 1.2, "属性 Attribute\n椭圆 ○", COLORS["green"], fontsize=10)
    box_text(ax, 7.1, 3.0, 2.5, 1.2, "联系 Relationship\n菱形 ◇", COLORS["purple"], fontsize=10)

    # 属性分类
    attrs = [
        (0.5, 0.8, 2.0, 1.0, "简单/复合", COLORS["cyan"]),
        (2.8, 0.8, 2.0, 1.0, "单值/多值", COLORS["pink"]),
        (5.1, 0.8, 2.0, 1.0, "派生属性", COLORS["orange"]),
        (7.4, 0.8, 2.0, 1.0, "主码 Key", COLORS["red"]),
    ]
    for x, y, w, h, txt, c in attrs:
        box_text(ax, x, y, w, h, txt, c, fontsize=9)

    ax.text(5, 0.2, "联系基数：1:1 / 1:N / M:N  |  参与约束：全部参与(双线) vs 部分参与(单线)", ha="center", fontsize=8, color=COLORS["mid"])

    save_fig(fig, "s2_02_er_elements.png")


def s2_03_nf_pyramid():
    """范式金字塔"""
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_xlim(0, 8); ax.set_ylim(0, 6); ax.axis("off")
    ax.set_facecolor(COLORS["bg"])

    ax.text(4, 5.6, "范式金字塔：1NF → BCNF", ha="center", fontsize=15, fontweight="bold", color=COLORS["dark"])

    # Pyramid layers (bottom to top)
    layers = [
        (1.0, 0.5, 6.0, 0.9, "1NF: 属性原子性 (不可再分)", COLORS["blue"]),
        (1.8, 1.6, 4.4, 0.9, "2NF: + 消部分依赖", COLORS["green"]),
        (2.6, 2.7, 2.8, 0.9, "3NF: + 消传递依赖", COLORS["orange"]),
        (3.2, 3.8, 1.6, 0.9, "BCNF: 决定因素=超键", COLORS["red"]),
    ]
    for x, y, w, h, txt, c in layers:
        box_text(ax, x, y, w, h, txt, c, fontsize=9)

    # 箭头
    for i in range(3):
        arrow(ax, 4, 1.5 + i * 1.1, 4, 1.5 + i * 1.1 + 0.5, COLORS["mid"], 1.5)

    # 右侧注释
    annotations = [
        (6.2, 1.0, "属性不可再分"),
        (6.2, 2.1, "非主属性完全\n依赖于候选键"),
        (6.2, 3.2, "非主属性不传递\n依赖于候选键"),
        (6.2, 4.3, "每个FD的\n左部都是超键"),
    ]
    for x, y, txt in annotations:
        ax.text(x, y, txt, fontsize=7, color=COLORS["mid"], va="center")

    save_fig(fig, "s2_03_nf_pyramid.png")


def s2_04_bcnf_check():
    """BCNF判定与3NF分解"""
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_xlim(0, 10); ax.set_ylim(0, 5); ax.axis("off")
    ax.set_facecolor(COLORS["bg"])

    ax.text(5, 4.6, "BCNF 判定 & 3NF 分解", ha="center", fontsize=15, fontweight="bold", color=COLORS["dark"])

    # BCNF check flow
    box_text(ax, 0.3, 2.5, 4.0, 1.8, "BCNF 判定流程\n① 求出所有候选键\n② 逐条检查 FD 左部是否超键\n③ 若存在非超键左部 → 不在 BCNF\n④ 否则 → 在 BCNF", COLORS["blue"], fontsize=9)

    box_text(ax, 5.0, 2.5, 4.7, 1.8, "3NF 分解步骤\n① 求最小覆盖 (Canonical Cover)\n② 每条 FD 建一张表\n③ 补一张含候选键的表 → 保证无损连接\n④ 3NF 一定无损+保持依赖", COLORS["green"], fontsize=9)

    # 对比
    ax.text(2.3, 2.0, "更严格", ha="center", fontsize=8, color=COLORS["red"], fontweight="bold")
    ax.text(7.3, 2.0, "更实用", ha="center", fontsize=8, color=COLORS["green"], fontweight="bold")

    # 底部提示
    ax.text(5, 0.5, "3NF vs BCNF 取舍：3NF 无损+保持依赖但允许主属性传递 | BCNF 更干净但可能丢失依赖", ha="center", fontsize=8, color=COLORS["orange"])

    save_fig(fig, "s2_04_bcnf_check.png")


# ============================================================
# Section 3: 事务与并发 (4 images)
# ============================================================

def s3_01_framework():
    """第3节知识框架"""
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_xlim(0, 10); ax.set_ylim(0, 5); ax.axis("off")
    ax.set_facecolor(COLORS["bg"])

    ax.text(5, 4.6, "第3节：事务与并发 — 知识框架", ha="center", fontsize=15, fontweight="bold", color=COLORS["dark"])

    boxes = [
        (0.3, 1.0, 2.0, 2.8, "事务与ACID\n原子性·一致性\n·隔离性·持久性", COLORS["pink"]),
        (2.8, 1.0, 2.0, 2.8, "调度与\n可串行化\n冲突·先行图", COLORS["purple"]),
        (5.3, 1.0, 2.0, 2.8, "封锁协议\n2PL\nS锁·X锁·死锁", COLORS["red"]),
        (7.8, 1.0, 2.0, 2.8, "故障恢复\n日志\nUNDO/REDO\n·检查点", COLORS["orange"]),
    ]
    for x, y, w, h, txt, c in boxes:
        box_text(ax, x, y, w, h, txt, c, fontsize=10)

    for i in range(3):
        arrow(ax, 2.4 + i * 2.5, 2.5, 2.7 + i * 2.5, 2.5, COLORS["mid"])

    save_fig(fig, "s3_01_framework.png")


def s3_02_acid():
    """ACID四大特性"""
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_xlim(0, 10); ax.set_ylim(0, 5); ax.axis("off")
    ax.set_facecolor(COLORS["bg"])

    ax.text(5, 4.6, "事务的四大特性 ACID", ha="center", fontsize=15, fontweight="bold", color=COLORS["dark"])

    # ACID 四象限
    acid = [
        (0.5, 1.8, 4.0, 1.8, "A 原子性 Atomicity\n全做或全不做\n机制：UNDO 日志", COLORS["blue"]),
        (5.5, 1.8, 4.0, 1.8, "C 一致性 Consistency\n事务前后DB满足约束\n机制：约束+应用逻辑", COLORS["green"]),
        (0.5, 0.2, 4.0, 1.8, "I 隔离性 Isolation\n并发事务互不干扰\n机制：封锁 / 2PL", COLORS["purple"]),
        (5.5, 0.2, 4.0, 1.8, "D 持久性 Durability\n提交后不丢失\n机制：REDO日志 + WAL", COLORS["orange"]),
    ]
    for x, y, w, h, txt, c in acid:
        box_text(ax, x, y, w, h, txt, c, fontsize=9)

    # 状态机
    states = ["活动\nactive", "部分提交\npartially\ncommitted", "提交\ncommitted"]
    state_x = [1.0, 3.5, 6.0]
    for i, (sx, st) in enumerate(zip(state_x, states)):
        box_text(ax, sx, 3.7, 2.0, 0.8, st, COLORS["teal"] if i < 2 else COLORS["green"], fontsize=8)
    arrow(ax, 3.1, 4.1, 3.4, 4.1, COLORS["mid"])
    arrow(ax, 5.6, 4.1, 5.9, 4.1, COLORS["mid"])

    # 失败路径
    box_text(ax, 1.0, 2.9, 2.0, 0.6, "失败\nfailed", COLORS["red"], fontsize=7)
    box_text(ax, 3.5, 2.9, 2.0, 0.6, "中止\naborted", COLORS["red"], fontsize=7)
    arrow(ax, 2.0, 3.5, 2.0, 3.05, COLORS["red"])
    arrow(ax, 4.5, 3.5, 4.5, 3.05, COLORS["red"])

    save_fig(fig, "s3_02_acid.png")


def s3_03_2pl():
    """两段锁协议2PL"""
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_xlim(0, 10); ax.set_ylim(0, 5); ax.axis("off")
    ax.set_facecolor(COLORS["bg"])

    ax.text(5, 4.6, "两段锁协议 2PL & 锁相容矩阵", ha="center", fontsize=15, fontweight="bold", color=COLORS["dark"])

    # Lock compatibility matrix
    ax.text(1.5, 3.8, "锁相容矩阵", fontsize=10, fontweight="bold", color=COLORS["dark"])
    cells = [
        (0.5, 2.8, 1.5, 0.7, "S OK", COLORS["green"]), (2.2, 2.8, 1.5, 0.7, "X NO", COLORS["red"]),
        (0.5, 1.9, 1.5, 0.7, "X NO", COLORS["red"]), (2.2, 1.9, 1.5, 0.7, "X NO", COLORS["red"]),
    ]
    for x, y, w, h, txt, c in cells:
        box_text(ax, x, y, w, h, txt, c, fontsize=11)
    ax.text(0.9, 3.55, "S", fontsize=10, color=COLORS["dark"], fontweight="bold")
    ax.text(2.6, 3.55, "X", fontsize=10, color=COLORS["dark"], fontweight="bold")
    ax.text(0.1, 3.1, "S", fontsize=10, color=COLORS["dark"], fontweight="bold")
    ax.text(0.1, 2.2, "X", fontsize=10, color=COLORS["dark"], fontweight="bold")

    # 2PL phases
    box_text(ax, 4.5, 2.8, 2.3, 1.8, "增长阶段\n只能申请锁\n不能释放", COLORS["blue"], fontsize=9)
    arrow(ax, 6.9, 3.7, 7.7, 3.7, COLORS["orange"], 2)
    box_text(ax, 7.5, 2.8, 2.3, 1.8, "收缩阶段\n只能释放锁\n不能申请", COLORS["green"], fontsize=9)

    # 三种变体
    variants = [
        (4.5, 0.8, 2.3, 1.5, "基本 2PL\n可串行化\n可能级联回滚", COLORS["orange"], 8),
        (7.5, 0.8, 2.3, 1.5, "强严格 2PL\n所有锁到结束\n最安全", COLORS["red"], 8),
    ]
    for x, y, w, h, txt, c, fs in variants:
        box_text(ax, x, y, w, h, txt, c, fontsize=fs)

    ax.text(5, 0.3, "核心定理：所有事务遵守2PL => 任意调度都是冲突可串行化的", ha="center", fontsize=9, color=COLORS["orange"])

    save_fig(fig, "s3_03_2pl.png")


def s3_04_redo_undo():
    """UNDO/REDO恢复"""
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_xlim(0, 10); ax.set_ylim(0, 5); ax.axis("off")
    ax.set_facecolor(COLORS["bg"])

    ax.text(5, 4.6, "崩溃恢复：UNDO 与 REDO", ha="center", fontsize=15, fontweight="bold", color=COLORS["dark"])

    # Two paths
    box_text(ax, 0.3, 2.5, 4.5, 1.8, "UNDO 撤销 (未提交事务)\n扫描方向：从后往前\n操作：数据项 <- 旧值 V1\n服务：原子性 A", COLORS["red"], fontsize=9)
    box_text(ax, 5.2, 2.5, 4.5, 1.8, "REDO 重做 (已提交事务)\n扫描方向：从前往后\n操作：数据项 <- 新值 V2\n服务：持久性 D", COLORS["green"], fontsize=9)

    # 判断规则
    ax.text(5, 2.0, "判断规则：有 COMMIT → REDO | 无 COMMIT → UNDO", ha="center", fontsize=10, color=COLORS["dark"], fontweight="bold")

    # 口诀
    ax.text(5, 0.8, '八字口诀：已提交就REDO(写新值) · 未提交就UNDO(写旧值)', ha="center", fontsize=10, color=COLORS["orange"], fontweight="bold")

    # Checkpoint
    box_text(ax, 2.0, 0.2, 6.0, 0.5, "检查点 Checkpoint：周期刷盘 → 恢复只从最近检查点开始扫描", COLORS["purple"], fontsize=8)

    save_fig(fig, "s3_04_redo_undo.png")


# ============================================================
# Section 4: 恢复与向量数据库 (4 images)
# ============================================================

def s4_01_failure_types():
    """故障类型"""
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_xlim(0, 10); ax.set_ylim(0, 5); ax.axis("off")
    ax.set_facecolor(COLORS["bg"])

    ax.text(5, 4.6, "三类故障与恢复方式", ha="center", fontsize=15, fontweight="bold", color=COLORS["dark"])

    failures = [
        (0.3, 2.5, 2.8, 1.8, "事务故障\n逻辑错误/死锁\n仅影响单事务\n恢复：UNDO", COLORS["orange"]),
        (3.6, 2.5, 2.8, 1.8, "系统崩溃\n断电/软硬件故障\n易失存储丢失\n恢复：UNDO+REDO", COLORS["red"]),
        (6.9, 2.5, 2.8, 1.8, "介质故障\n磁盘损坏\n非易失存储损坏\n恢复：备份+REDO", COLORS["purple"]),
    ]
    for x, y, w, h, txt, c in failures:
        box_text(ax, x, y, w, h, txt, c, fontsize=9)

    # 存储三级
    stores = [
        (0.5, 0.8, 2.5, 1.0, "易失性存储\n主存·缓存\n崩溃丢失", COLORS["pink"]),
        (3.8, 0.8, 2.5, 1.0, "非易失性存储\n磁盘·闪存\n能经受崩溃", COLORS["cyan"]),
        (7.1, 0.8, 2.5, 1.0, "稳定存储\n理想化介质\n日志存放处", COLORS["green"]),
    ]
    for x, y, w, h, txt, c in stores:
        box_text(ax, x, y, w, h, txt, c, fontsize=9)

    ax.text(5, 0.2, "Fail-stop 假设：崩溃不损坏非易失性存储 | 日志是唯一的真相来源", ha="center", fontsize=8, color=COLORS["mid"])

    save_fig(fig, "s4_01_failure_types.png")


def s4_02_steal_force():
    """Steal/Force策略"""
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_xlim(0, 10); ax.set_ylim(0, 5); ax.axis("off")
    ax.set_facecolor(COLORS["bg"])

    ax.text(5, 4.6, "Steal / Force 策略矩阵", ha="center", fontsize=15, fontweight="bold", color=COLORS["dark"])

    # 2x2 Matrix
    cells = [
        (0.5, 1.8, 3.5, 1.3, "NO-STEAL + FORCE\n无需UNDO·无需REDO\n最简单但I/O差", COLORS["green"]),
        (4.5, 1.8, 3.5, 1.3, "STEAL + FORCE\n需UNDO·无需REDO", COLORS["yellow"]),
        (0.5, 0.2, 3.5, 1.3, "NO-STEAL + NO-FORCE\n无需UNDO·需REDO", COLORS["yellow"]),
        (4.5, 0.2, 3.5, 1.3, "STEAL + NO-FORCE\n需UNDO + REDO\n← 真实系统选择", COLORS["red"]),
    ]
    for x, y, w, h, txt, c in cells:
        box_text(ax, x, y, w, h, txt, c, fontsize=9)

    # 定义
    box_text(ax, 0.5, 3.5, 4.0, 0.8, "STEAL：未提交脏页可写入磁盘？\nNO-STEAL：脏页固定到事务结束", COLORS["blue"], fontsize=8)
    box_text(ax, 5.5, 3.5, 4.0, 0.8, "FORCE：提交时必须全部刷盘？\nNO-FORCE：写操作可滞后于提交", COLORS["blue"], fontsize=8)

    save_fig(fig, "s4_02_steal_force.png")


def s4_03_wal():
    """WAL协议"""
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_xlim(0, 10); ax.set_ylim(0, 5); ax.axis("off")
    ax.set_facecolor(COLORS["bg"])

    ax.text(5, 4.6, "WAL (Write-Ahead Logging) 先写日志协议", ha="center", fontsize=15, fontweight="bold", color=COLORS["dark"])

    # WAL two rules
    box_text(ax, 0.3, 2.5, 4.5, 1.8, "Undo 规则\n数据页写入磁盘前，其更新日志\n必须先写入稳定存储\n→ UNDO 总是可能的", COLORS["red"], fontsize=9)
    box_text(ax, 5.2, 2.5, 4.5, 1.8, "Redo / 提交规则\n事务报告已提交前，所有日志记录\n(直到 commit) 必须在稳定存储\n→ 持久性总是可能的", COLORS["green"], fontsize=9)

    # 核心原则
    ax.text(5, 2.0, "核心原则：日志总是先进入稳定存储", ha="center", fontsize=11, color=COLORS["dark"], fontweight="bold")

    # 日志记录类型
    types = [
        (0.5, 0.8, 2.0, 0.7, "<T start>", COLORS["blue"]),
        (2.8, 0.8, 2.0, 0.7, "<T,X,V1,V2>", COLORS["purple"]),
        (5.1, 0.8, 2.0, 0.7, "<T commit>", COLORS["green"]),
        (7.4, 0.8, 2.0, 0.7, "<T abort>", COLORS["red"]),
    ]
    for x, y, w, h, txt, c in types:
        box_text(ax, x, y, w, h, txt, c, fontsize=10)

    save_fig(fig, "s4_03_wal.png")


def s4_04_ann_strategies():
    """ANN四大策略"""
    fig, ax = plt.subplots(figsize=(10, 5.5))
    ax.set_xlim(0, 10); ax.set_ylim(0, 5.5); ax.axis("off")
    ax.set_facecolor(COLORS["bg"])

    ax.text(5, 5.2, "向量数据库 — ANN 四大索引策略", ha="center", fontsize=15, fontweight="bold", color=COLORS["dark"])

    strategies = [
        (0.3, 3.0, 2.1, 1.8, "Partition & Prune\n分区与剪枝\n只看 q 附近的区域\n代表：IVF", COLORS["blue"]),
        (2.7, 3.0, 2.1, 1.8, "Compress\n压缩\n存储廉价近似\n代表：PQ", COLORS["green"]),
        (5.1, 3.0, 2.1, 1.8, "Hash\n局部敏感哈希\n附近点→同桶\n代表：LSH", COLORS["purple"]),
        (7.5, 3.0, 2.1, 1.8, "Navigate Graph\n图导航\n贪婪跳向 q\n代表：HNSW", COLORS["red"]),
    ]
    for x, y, w, h, txt, c in strategies:
        box_text(ax, x, y, w, h, txt, c, fontsize=9)

    # 相似度
    sims = [
        (0.5, 1.5, 2.5, 1.0, "欧氏距离 L2\n直线距离", COLORS["cyan"]),
        (3.5, 1.5, 2.5, 1.0, "余弦相似度\n角度·忽略长度", COLORS["orange"]),
        (6.5, 1.5, 2.5, 1.0, "内积 IP\n幅度有意义时用", COLORS["pink"]),
    ]
    for x, y, w, h, txt, c in sims:
        box_text(ax, x, y, w, h, txt, c, fontsize=9)

    ax.text(5, 1.0, "相似度度量", ha="center", fontsize=9, color=COLORS["mid"], style="italic")

    # 底部
    ax.text(5, 0.3, "维度诅咒 → ANN 近似解 | HNSW(内存)·IVF-PQ(十亿级)·DiskANN(SSD) | 三大指标：Recall·延迟·内存", ha="center", fontsize=8, color=COLORS["orange"])

    save_fig(fig, "s4_04_ann_strategies.png")


# ============================================================
# Main
# ============================================================

if __name__ == "__main__":
    print("Generating 17 database knowledge images...\n")

    print("Section 1 (查询为王):")
    s1_01_framework()
    s1_02_dbms_components()
    s1_03_relational_algebra()
    s1_04_sql_join()
    s1_05_pitfalls()

    print("\nSection 2 (建模与范式):")
    s2_01_framework()
    s2_02_er_elements()
    s2_03_nf_pyramid()
    s2_04_bcnf_check()

    print("\nSection 3 (事务与并发):")
    s3_01_framework()
    s3_02_acid()
    s3_03_2pl()
    s3_04_redo_undo()

    print("\nSection 4 (恢复与向量数据库):")
    s4_01_failure_types()
    s4_02_steal_force()
    s4_03_wal()
    s4_04_ann_strategies()

    print(f"\nDone! All 17 images saved to {OUTPUT_DIR}/")

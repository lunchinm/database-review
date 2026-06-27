"""
批量生成数据库复习资料插图脚本
"""
import subprocess
import json
import os
import time
import sys
import requests

SKILL_DIR = r"c:\Users\MIC lunchinm\AppData\Local\Programs\CodeBuddy CN\resources\app\extensions\genie\out\extension\builtin\buddy-multimodal-generation"
SCRIPT = os.path.join(SKILL_DIR, "scripts", "buddy-cloud.py")
TOKEN = sys.argv[1]
OUTPUT_DIR = sys.argv[2]

PROMPTS = {
    # ===== 第1节：查询为王 =====
    "s1_01_framework": "A clean Chinese educational mind map diagram titled '查询为王' (Query is King), 4 branches: 数据库系统与关系模型, 关系代数, SQL查询, 查询优化. Professional style, white bg, blue accents. No watermark.",
    "s1_02_dbms": "Educational diagram showing DBMS 5 major components: 查询处理器(Query Processor), 存储管理器(Storage Manager), 事务管理器(Transaction Manager). Clean infographic style, blue theme.",
    "s1_03_schema": "Chinese educational diagram: 三级模式两级映像 (Three-level schema two-level mapping): 外模式(External Schema), 概念模式(Conceptual Schema), 内模式(Internal Schema) with arrows showing mappings. Clean professional style.",
    "s1_04_keys": "Database keys comparison diagram: 超键(Super Key), 候选键(Candidate Key), 主键(Primary Key), 外键(Foreign Key) with definitions and examples. Chinese text, clean table style.",
    "s1_05_integrity": "Three types of integrity constraints diagram: 实体完整性(Entity Integrity), 参照完整性(Referential Integrity), 用户定义完整性(User-defined Integrity). Chinese educational style.",
    "s1_06_fk_null": "Flowchart: Foreign key NULL question decision tree - 外键能否为NULL？参与约束决定一切. Shows partial vs total participation. Clean Chinese educational diagram.",
    "s1_07_view": "Concept diagram: 视图(View) as virtual table. Shows base tables vs view, with SQL CREATE VIEW example. Clean educational infographic.",
    "s1_08_relational_algebra": "Relational algebra operations overview: 选择σ, 投影π, 并∪, 差−, 笛卡尔积×, 重命名ρ, 交∩, 连接⨝, 除÷. Clean diagram with symbols and brief descriptions. Chinese labels.",
    "s1_09_ra_example": "Relational algebra problem solving example with 3 tables: Student(S#,Sname,Sage,Ssex), Course(C#,Cname,Teacher), SC(S#,C#,Grade). Shows query step by step. Chinese educational style.",
    "s1_10_sql_single": "SQL single-table query example with SELECT, FROM, WHERE, LIKE, ORDER BY clauses. Shows a sample table and query result. Clean code-style educational diagram.",
    "s1_11_sql_join": "SQL multi-table JOIN example: 3 tables with INNER JOIN, LEFT JOIN diagrams. Venn diagram style showing table relationships. Clean Chinese educational diagram.",
    "s1_12_subquery": "SQL correlated subquery example: SELECT with nested query using EXISTS. Shows outer query referencing inner query. Clean code-style Chinese educational diagram.",
    "s1_13_query_opt": "Query optimization comparison: two execution plans side by side, one optimized one not. Shows index scan vs table scan, cost comparison. Chinese educational style.",
    "s1_14_pitfalls": "Chinese educational checklist: 查询优化易错清单 (Common Mistakes in Query Optimization). Key points with checkmarks and warning icons. Clean professional style.",

    # ===== 第2节：建模与范式 =====
    "s2_01_framework": "Chinese mind map: '建模与范式' (Modeling & Normalization) 4 branches: ER建模, ER转关系模式, 函数依赖与码, 范式与分解. Professional education style, white bg, green accents.",
    "s2_02_er_elements": "ER Model 3 elements diagram: 实体(Entity) rectangle, 属性(Attribute) oval, 联系(Relationship) diamond. Chinese labels, clean educational style.",
    "s2_03_attr_types": "Attribute classification diagram: 简单/复合(Simple/Composite), 单值/多值(Single/Multi-valued), 存储/派生(Stored/Derived), NULL属性. Chinese educational table style.",
    "s2_04_cardinality": "Relationship cardinality ratios: 1:1, 1:N, M:N with ER diagram examples. Shows participation constraints (total/partial) with double lines. Chinese educational style.",
    "s2_05_library_er": "Library ER diagram example: 图书(Book), 读者(Reader), 借阅(Borrow) entities with attributes and relationships. Chinese labels, professional ER notation.",
    "s2_06_er_to_relational": "ER to Relational Schema 5 rules: strong entity, weak entity, 1:1, 1:N, M:N relationships conversion rules. Clean Chinese educational diagram.",
    "s2_07_er_to_relational_example": "Library ER to Relational Schema conversion example showing primary keys and foreign keys. Chinese educational style, clean table format.",
    "s2_08_fd_types": "Functional dependency types: 完全FD(Full FD), 部分FD(Partial FD), 传递FD(Transitive FD) with examples. Chinese educational diagram with arrow notation.",
    "s2_09_armstrong": "Armstrong's Axioms: 自反律(Reflexivity), 增广律(Augmentation), 传递律(Transitivity) with formal definitions. Chinese educational style.",
    "s2_10_candidate_key": "Candidate key finding algorithm: 闭包法求候选键 step by step. Classify attributes then test. Chinese flowchart style.",
    "s2_11_minimal_cover": "Canonical cover (最小覆盖) computation steps: 1.单属性化右部 2.去掉无关属性 3.合并. With example. Chinese educational style.",
    "s2_12_nf_pyramid": "Normal Form pyramid: 1NF → 2NF → 3NF → BCNF → 4NF. Each level with key elimination rule. Clean Chinese infographic style.",
    "s2_13_nf_1nf_2nf": "1NF (atomicity) and 2NF (eliminate partial dependency) with example tables. Shows violation and fix. Chinese educational diagram.",
    "s2_14_nf_3nf": "3NF: eliminate transitive dependency. Example showing violation of 3NF and decomposition fix. Chinese educational style.",
    "s2_15_bcnf_check": "BCNF check example: determine if relation is in BCNF. Shows functional dependencies and candidate keys. Chinese educational style.",
    "s2_16_3nf_decomp": "3NF decomposition example: determine if in 3NF then decompose. Step by step with lossless join. Chinese educational style.",
    "s2_17_3nf_vs_bcnf": "3NF vs BCNF tradeoff: lossless join and dependency preservation. Shows that BCNF may lose dependencies. Chinese comparison diagram.",
    "s2_18_pitfalls": "Chinese educational checklist: 建模与范式易错清单. Key points about ER modeling and normalization mistakes. Clean professional style.",

    # ===== 第3节：事务与并发 =====
    "s3_01_framework": "Chinese mind map: '事务与并发' (Transactions & Concurrency) 4 branches: 事务与ACID, 调度与可串行化, 封锁协议2PL, 故障恢复. Red accent theme, professional education style.",
    "s3_02_tx_definition": "Transaction definition and state machine: Active → Partially Committed → Committed / Failed → Aborted. Chinese educational flowchart style.",
    "s3_03_acid": "ACID properties diagram: Atomicity(原子性), Consistency(一致性), Isolation(隔离性), Durability(持久性) with icons and Chinese descriptions. Clean infographic style.",
    "s3_04_acid_quiz": "ACID multiple choice question examples. Shows typical exam questions about which ACID property is violated. Chinese educational style.",
    "s3_05_concurrency_anomalies": "Three concurrency anomalies: 丢失修改(Lost Update), 脏读(Dirty Read), 不可重复读(Non-repeatable Read). With schedule examples. Chinese educational diagram.",
    "s3_06_conflict_serializability": "Conflict and conflict serializability: conflict operations definition, conflict equivalence, precedence graph. Chinese educational style with examples.",
    "s3_07_precedence_graph": "Precedence graph (先行图) 3-step method to determine serializability. Shows cycle detection. Chinese educational flowchart style.",
    "s3_08_serializable_example": "Serializable schedule example with two transactions T1, T2. Shows read/write operations and precedence graph. Chinese educational style.",
    "s3_09_lock_types": "Lock types: Shared lock (S) and Exclusive lock (X) with compatibility matrix. Chinese educational diagram.",
    "s3_10_2pl": "Two-Phase Locking (2PL) protocol and 3 variants: Basic 2PL, Conservative 2PL, Strict 2PL. Timeline diagrams. Chinese educational style.",
    "s3_11_lock_example": "Lock example: add exclusive locks to two transactions following Strict 2PL. Shows lock points and growing/shrinking phases. Chinese educational style.",
    "s3_12_redo_undo": "REDO vs UNDO after crash: which transactions need REDO (committed, not written) vs UNDO (uncommitted, written). Chinese educational flowchart style.",
    "s3_13_checkpoint": "Checkpoint and recovery process diagram. Shows log before and after checkpoint, recovery steps. Chinese educational style.",
    "s3_14_recovery_example": "Crash recovery log example: shows log entries, checkpoint, crash point, and which transactions get REDO/UNDO. Chinese educational problem-solving style.",
    "s3_15_pitfalls": "Chinese educational checklist: 事务与并发易错清单. Key mistakes about ACID, serializability, 2PL, recovery. Clean professional style.",

    # ===== 第4节：恢复与向量数据库 =====
    "s4_01_recovery_goal": "Diagram: Recovery in ACID - showing how recovery guarantees Atomicity and Durability. Clean Chinese educational style.",
    "s4_02_failure_types": "Three failure types: 事务故障(Transaction Failure), 系统故障(System Crash), 介质故障(Media Failure). With causes and effects. Chinese educational diagram.",
    "s4_03_storage_trust": "Three-level storage trust model: 主存(volatile), 磁盘(non-volatile), 稳定存储(stable). Chinese educational infographic.",
    "s4_04_steal_force": "Steal and Force concepts diagram: Steal=write before commit, No-Steal=write after commit. Force=write immediately, No-Force=defer write. Clean Chinese educational style.",
    "s4_05_steal_force_matrix": "Steal/Force strategy matrix: 2x2 grid showing No-Steal+Force (easiest), Steal+No-Force (hardest). REDO/UNDO requirements. Chinese educational table style.",
    "s4_06_wal": "Write-Ahead Logging (WAL) protocol: log must be written to stable storage BEFORE data page. Sequence diagram. Chinese educational style.",
    "s4_07_log_types": "Log record types: UPDATE log (before/after images), COMMIT log, ABORT log, CHECKPOINT log. Clean Chinese educational diagram.",
    "s4_08_undo_redo": "UNDO vs REDO comparison: UNDO restores old value (before image), REDO applies new value (after image). Direction arrows. Chinese educational style.",
    "s4_09_recovery_example": "Crash recovery example: log with T1(committed), T2(uncommitted), T3(committed). Shows REDO(T1,T3), UNDO(T2). Chinese educational problem-solving style.",
    "s4_10_recovery_after": "Log state after recovery: showing Compensation Log Records (CLR). Chinese educational diagram.",
    "s4_11_recovery_practice": "Recovery practice problem: given log entries, determine REDO/UNDO set after crash. Chinese educational worksheet style.",
    "s4_12_recovery_solution": "Recovery practice solution: shows answer with reasoning. Chinese educational answer key style.",
    "s4_13_checkpoint": "Checkpoint mechanism diagram: before checkpoint, during checkpoint (write dirty pages), after checkpoint. Recovery starts from last checkpoint. Chinese educational style.",
    "s4_14_vectordb_intro": "Vector database concept: from exact match to similarity search. Shows traditional DB vs vector DB comparison. Chinese educational infographic.",
    "s4_15_traditional_index": "Why traditional indexes fail for vectors: B-tree for 1D, vector in high-dimensional space. Chinese educational comparison diagram.",
    "s4_16_similarity": "Three similarity measures: Euclidean distance (L2), Inner Product (IP), Cosine similarity. With formulas and geometric interpretation. Chinese educational diagram.",
    "s4_17_knn_cost": "K-NN query cost: O(N*d) complexity, curse of dimensionality. Shows exhaustive search. Chinese educational diagram.",
    "s4_18_curse": "Curse of dimensionality visualization: distance concentration as dimensions increase, all points become equidistant. Chinese educational chart style.",
    "s4_19_ann": "Approximate Nearest Neighbor (ANN) tradeoff: accuracy vs speed. Precision-recall concept. Chinese educational style.",
    "s4_20_four_strategies": "Four ANN index strategies overview: 分区(Partitioning), 量化(Quantization), 哈希(Hashing), 图(Graph). Icons and brief descriptions. Chinese educational infographic.",
    "s4_21_ivf": "IVF (Inverted File) index: partition space into clusters, search only nearest clusters. Diagram with clusters and query point. Chinese educational style.",
    "s4_22_pq": "Product Quantization (PQ): split vector, quantize each sub-vector, approximate distance. Step-by-step diagram. Chinese educational style.",
    "s4_23_ivf_pq": "IVF-PQ combination: IVF for partition pruning, PQ for compression. Pipeline diagram. Chinese educational style.",
    "s4_24_lsh": "Locality-Sensitive Hashing (LSH): hash similar vectors to same bucket. Diagram with hash functions and buckets. Chinese educational style.",
    "s4_25_hnsw": "HNSW (Hierarchical Navigable Small World): multi-layer graph, greedy search from top layer. Diagram with layers and search path. Chinese educational style.",
    "s4_26_algorithm_comparison": "Four ANN algorithm families comparison table: IVF, PQ, HNSW, LSH. Compare speed, accuracy, memory. Chinese educational comparison chart.",
    "s4_27_system_landscape": "Vector database system landscape: 专用向量数据库(Milvus,Pinecone), 传统数据库+向量插件(pgvector), 全文搜索引擎+向量(Elasticsearch). Chinese educational infographic.",
}

def generate_image(name, prompt):
    """调用 buddy-cloud.py 生成单张图片"""
    cmd = [
        sys.executable, SCRIPT, "image", prompt,
        "--token", TOKEN
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        # Find the last JSON line in output
        lines = result.stdout.strip().split('\n')
        for line in reversed(lines):
            line = line.strip()
            if line.startswith('{'):
                data = json.loads(line)
                if data.get("status") == "DONE" and data.get("result_url"):
                    urls = data["result_url"] if isinstance(data["result_url"], list) else [data["result_url"]]
                    return urls[0]
        print(f"[FAIL] {name}: {lines[-1] if lines else 'unknown error'}")
        return None
    except Exception as e:
        print(f"[ERROR] {name}: {e}")
        return None

def download_image(url, filepath):
    """下载图片到本地"""
    try:
        r = requests.get(url, timeout=30)
        if r.status_code == 200:
            with open(filepath, 'wb') as f:
                f.write(r.content)
            return True
    except Exception as e:
        print(f"[DOWNLOAD ERROR] {filepath}: {e}")
    return False

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    total = len(PROMPTS)
    success = 0
    failed = []
    
    for i, (name, prompt) in enumerate(PROMPTS.items(), 1):
        filepath = os.path.join(OUTPUT_DIR, f"{name}.jpg")
        if os.path.exists(filepath):
            print(f"[{i}/{total}] SKIP {name} (already exists)")
            success += 1
            continue
            
        print(f"[{i}/{total}] Generating {name}...")
        url = generate_image(name, prompt)
        
        if url:
            if download_image(url, filepath):
                print(f"[{i}/{total}] OK {name}")
                success += 1
            else:
                print(f"[{i}/{total}] DOWNLOAD FAILED {name}")
                failed.append(name)
        else:
            failed.append(name)
        
        # Small delay between requests
        if i < total:
            time.sleep(1)
    
    print(f"\n=== DONE === Success: {success}/{total}")
    if failed:
        print(f"Failed: {failed}")

if __name__ == "__main__":
    main()

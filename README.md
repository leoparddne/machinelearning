# 吴恩达机器学习课程学习笔记与作业实践

## 项目简介
本仓库为吴恩达机器学习（Andrew Ng's Machine Learning）课程的学习记录，涵盖课程笔记、数据科学核心组件（NumPy、Pandas、Matplotlib）的专项练习，以及课后作业。

作业区（`homework/`）包含两类内容：
1. **原版课程内容**：课程官方提供的文档、图片、数据文件，以及所有的 Lab 与测验。
2. **个人练习内容**：在完成原版 Lab 的基础上，根据自己的理解重新实现、补充与扩展的练习。

## 目录结构与功能说明
- **`.git`**：Git 版本控制目录，用于追踪代码与笔记的迭代历史。
- **`.ipynb_checkpoints`**：Jupyter Notebook 的自动保存检查点目录。
- **`.venv`**：Python 虚拟环境目录，隔离本项目依赖，避免与全局环境冲突。
- **`0. notebook`**：机器学习核心知识点的个人学习笔记（算法组成、训练流程、概念梳理等）。
- **`1. jupyter`**：Jupyter Notebook 相关配置及基础操作笔记。
- **`2. numpy`**：NumPy（数值计算基础库）的专项学习笔记与练习。
- **`3. matplotlib`**：Matplotlib（数据可视化库）的专项学习笔记与绘图练习。
- **`4. pandas`**：Pandas（数据处理与分析库）的专项学习笔记与练习。
- **`homework`**：课程作业区，详见下方「作业区结构说明」。

## 作业区结构说明
```
homework/
└── week1/
    ├── Optional Labs/                         # 原版课程内容
    │   ├── images/                            # 原版 Lab 使用的课程图片
    │   ├── C1_W1_Lab02_Model_Representation_Soln.ipynb   # 原版 Lab：模型表示
    │   ├── C1_W1_Lab03_Cost_function_Soln.ipynb          # 原版 Lab：代价函数
    │   ├── C1_W1_Lab04_Gradient_Descent_Soln.ipynb       # 原版 Lab：梯度下降
    │   ├── lab_utils_common.py                # 原版 Lab 依赖的工具模块
    │   ├── lab_utils_uni.py                   # 原版 Lab 依赖的工具模块
    │   ├── deeplearning.mplstyle              # 原版绘图样式文件
    │   └── data.txt                           # 原版 Lab 数据文件
    │
    ├── Practice quiz - Regression/                        # 原版测验：回归
    │   └── ss1.md
    ├── Practice quiz - Supervised vs unsupervised learning/  # 原版测验：监督学习 vs 无监督学习
    │   └── ss1.md
    ├── Practice quiz - Train the model with gradient descent/ # 原版测验：用梯度下降训练模型
    │   └── ss1.md
    │
    ├── Optional Labs/C1 W1 Lab04 Gradient Descent SoLn 手写实例.ipynb   # 个人练习：手写实现梯度下降
    └── Optional Labs/C1_W1_Lab03_Cost_function_Soln_暴力搜索.ipynb      # 个人练习：暴力搜索求最优参数
```

### 一、原版课程内容
课程官方提供的材料，未作改动：

| 类型 | 文件 | 说明 |
|------|------|------|
| Lab | `C1_W1_Lab02_Model_Representation_Soln.ipynb` | 模型表示 |
| Lab | `C1_W1_Lab03_Cost_function_Soln.ipynb` | 代价函数 |
| Lab | `C1_W1_Lab04_Gradient_Descent_Soln.ipynb` | 梯度下降 |
| 资源 | `lab_utils_common.py`、`lab_utils_uni.py` | Lab 依赖的工具模块 |
| 资源 | `deeplearning.mplstyle`、`data.txt` | 绘图样式与数据文件 |
| 资源 | `images/` | 课程图片 |
| 测验 | `Practice quiz - Regression/ss1.md` | 回归 |
| 测验 | `Practice quiz - Supervised vs unsupervised learning/ss1.md` | 监督学习 vs 无监督学习 |
| 测验 | `Practice quiz - Train the model with gradient descent/ss1.md` | 用梯度下降训练模型 |

> 注：原版 Lab 已翻译为中文版本，内容与结构保持与原课程一致。

### 二、个人练习内容
在完成原版 Lab 后，根据个人理解重新实现与扩展的练习：

| 文件 | 说明 |
|------|------|
| `C1 W1 Lab04 Gradient Descent SoLn 手写实例.ipynb` | 手写实现梯度下降算法 |
| `C1_W1_Lab03_Cost_function_Soln_暴力搜索.ipynb` | 用暴力搜索方式求代价函数最优参数 |

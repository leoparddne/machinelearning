# -*- coding: utf-8 -*-
import json, os

def to_source(text):
    if text == '':
        return []
    lines = text.split('\n')
    out = []
    for i, ln in enumerate(lines):
        if i == len(lines) - 1:
            out.append(ln)
        else:
            out.append(ln + '\n')
    if out and out[-1] == '':
        out.pop()
    return out

def apply(path, mapping):
    with open(path, encoding='utf-8') as f:
        nb = json.load(f)
    n_before = len(nb['cells'])
    for idx, text in mapping.items():
        nb['cells'][idx]['source'] = to_source(text)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)
    nb2 = json.load(open(path, encoding='utf-8'))
    assert len(nb2['cells']) == n_before, 'cell count changed!'
    print(os.path.basename(path), 'cells', n_before, 'translated', len(mapping), 'OK')

# ============ F2: Lab01 ============
f2 = r'c:\Users\ives\Desktop\temp\ml\homework\week3\Optional Labs\C1_W3_Lab01_Classification_Soln.ipynb'
m2 = {
0: "# 选修实验：分类\n\n在本实验中，你将对比回归（regression）与分类（classification）。",
2: '## 分类问题\n<img align="left" src="./images/C1_W3_Classification.png"     style=" width:380px; padding: 10px; " > 分类问题的例子包括：将邮件识别为垃圾邮件或非垃圾邮件，或者判断肿瘤是恶性还是良性。特别地，这些是*二元*（binary）分类的例子，其中只有两种可能的结果。结果可以用成对的"正"/"负"来描述，例如 "yes"/"no、"true"/"false" 或 "1"/"0"。\n\n分类数据集的图通常使用符号来表示样本的结果。在下面的图中，\'X\' 用于表示正值，而 \'O\' 表示负值。',
5: "注意上图中的几点：\n- 在单变量图中，正结果既显示为红色 \'X\'，也表示为 y=1。负结果为蓝色 \'O\'，位于 y=0 处。\n   - 回想一下，在线性回归的情形下，y 不会被限制为两个值，而可以是任意值。\n- 在双变量图中，没有 y 轴。正结果显示为红色 \'X\'，而负结果使用蓝色 \'O\' 符号。\n    - 回想一下，在多元线性回归的情形下，y 不会被限制为两个值，类似的图将会是三维的。",
6: '## 线性回归方法\n在上一周，你应用线性回归构建了一个预测模型。让我们在这里用讲座中描述的简单示例尝试这种方法。该模型将根据肿瘤大小预测肿瘤是良性还是恶性。请尝试以下操作：\n- 点击 \'Run Linear Regression\' 为给定数据找到最佳线性回归模型。\n    - 注意所得到的线性模型与数据**并不**匹配得很好。\n改进结果的一种方法是应用一个*阈值*（threshold）。\n- 勾选 \'Toggle 0.5 threshold\' 复选框，以显示应用阈值后的预测结果。\n    - 这些预测看起来不错，预测结果与数据相符\n- *重要*：现在，在最右侧、较大的肿瘤尺寸范围（接近 10）内添加更多的 \'malignant\'（恶性）数据点，然后重新运行线性回归。\n    - 现在，模型能预测更大的肿瘤，但 x=3 处的数据点被错误预测了！\n- 要清除/更新图像，请重新运行包含绘图命令的 cell。',
8: '上面的示例表明，线性模型不足以对分类数据进行建模。该模型可以按下面实验所述进行扩展。',
9: '## 恭喜！\n在本实验中，你：\n- 探索了分类数据集及其绘图\n- 确定了线性回归不足以解决分类问题。',
}

# ============ F3: Lab02 ============
f3 = r'c:\Users\ives\Desktop\temp\ml\homework\week3\Optional Labs\C1_W3_Lab02_Sigmoid_function_Soln.ipynb'
m3 = {
0: "# 选修实验：逻辑回归（Logistic Regression）\n\n在这个不计分实验中，你将\n- 探索 sigmoid 函数（也称为 logistic 函数）\n- 探索逻辑回归；它使用 sigmoid 函数",
2: "## Sigmoid 或 Logistic 函数\n<img align=\"left\" src=\"./images/C1_W3_LogisticRegression_left.png\"     style=\" width:300px; padding: 10px; \" >正如讲座视频中所讨论的，对于分类任务，我们可以先使用线性回归模型 $f_{\\mathbf{w},b}(\\mathbf{x}^{(i)}) = \\mathbf{w} \\cdot  \\mathbf{x}^{(i)} + b$ 来根据 $x$ 预测 $y$。\n- 然而，我们希望分类模型的预测值介于 0 和 1 之间，因为我们的输出变量 $y$ 要么是 0 要么是 1。\n- 这可以通过使用 \"sigmoid 函数\" 来实现，它将所有输入值映射到 0 和 1 之间的值。\n\n\n让我们实现 sigmoid 函数并亲自验证这一点。\n\n## Sigmoid 函数的公式\n\nsigmoid 函数的公式如下 -\n\n$g(z) = \\frac{1}{1+e^{-z}}\\tag{1}$\n\n在逻辑回归的情形下，z（sigmoid 函数的输入）是线性回归模型的输出。\n- 对于单个样本，$z$ 是标量。\n- 对于多个样本，$z$ 可能是一个由 $m$ 个值组成的向量，每个样本对应一个值。\n- sigmoid 函数的实现应涵盖这两种可能的输入格式。\n让我们用 Python 实现它。",
3: "NumPy 有一个名为 [`exp()`](https://numpy.org/doc/stable/reference/generated/numpy.exp.html) 的函数，它提供了一种便捷的方法来计算输入数组（`z`）中所有元素的指数（ $e^{z}$）。\n\n它也可以接受单个数字作为输入，如下所示。",
4: "# 输入是一个数组。\ninput_array = np.array([1,2,3])\nexp_array = np.exp(input_array)\n\nprint(\"Input to exp:\", input_array)\nprint(\"Output of exp:\", exp_array)\n\n# 输入是单个数字\ninput_val = 1  \nexp_val = np.exp(input_val)\n\nprint(\"Input to exp:\", input_val)\nprint(\"Output of exp:\", exp_val)",
5: "`sigmoid` 函数在 Python 中的实现如下面的 cell 所示。",
6: "def sigmoid(z):\n    \"\"\"\n    计算 z 的 sigmoid\n\n    参数:\n        z (ndarray): 一个标量，或任意大小的 numpy 数组。\n\n    返回:\n        g (ndarray): sigmoid(z)，形状与 z 相同\n\n    \"\"\"\n\n    g = 1/(1+np.exp(-z))\n\n    return g",
7: "让我们看看这个函数对于不同的 `z` 值输出是什么",
8: "# 生成一个介于 -10 和 10 之间等间距值的数组\nz_tmp = np.arange(-10,11)\n\n# 使用上面实现的函数来获取 sigmoid 值\ny = sigmoid(z_tmp)\n\n# 将两个数组并排美观打印的代码\nnp.set_printoptions(precision=3)\nprint(\"Input (z), Output (sigmoid(z))\")\nprint(np.c_[z_tmp, y])",
9: "左列的值是 `z`，右列的值是 `sigmoid(z)`。如你所见，sigmoid 的输入值范围从 -10 到 10，输出值范围从 0 到 1。\n\n现在，让我们尝试使用 `matplotlib` 库绘制这个函数。",
10: "# 绘制 z 与 sigmoid(z) 的关系\nfig,ax = plt.subplots(1,1,figsize=(5,3))\nax.plot(z_tmp, y, c=\"b\")\n\nax.set_title(\"Sigmoid function\")\nax.set_ylabel('sigmoid(z)')\nax.set_xlabel('z')\ndraw_vthresh(ax,0)",
11: "如你所见，当 `z` 趋向很大的负值时，sigmoid 函数趋近于 `0`；当 `z` 趋向很大的正值时，趋近于 `1`。",
12: "## 逻辑回归\n<img align=\"left\" src=\"./images/C1_W3_LogisticRegression_right.png\"     style=\" width:300px; padding: 10px; \" > 逻辑回归模型将 sigmoid 应用于我们熟悉的线性回归模型，如下所示：\n\n$$ f_{\\mathbf{w},b}(\\mathbf{x}^{(i)}) = g(\\mathbf{w} \\cdot \\mathbf{x}^{(i)} + b ) \\tag{2} $$\n\n  其中\n\n  $g(z) = \\frac{1}{1+e^{-z}}\\tag{3}$",
13: "  \n让我们将逻辑回归应用于肿瘤分类的分类数据示例。\n首先，加载样本以及参数的初始值。\n  ",
15: "请尝试以下步骤：\n- 点击 \'Run Logistic Regression\' 为给定的训练数据找到最佳逻辑回归模型\n    - 注意所得到的模型与数据拟合得相当好。\n    - 注意，橙色线就是上面的 \'$z$\' 或 $\\mathbf{w} \\cdot \\mathbf{x}^{(i)} + b$。它与线性回归模型中的直线并不相同。\n通过应用一个*阈值*（threshold）进一步改进这些结果。\n- 勾选 \'Toggle 0.5 threshold\' 复选框，以显示应用阈值后的预测结果。\n    - 这些预测看起来不错。预测结果与数据相符\n    - 现在，在较大的肿瘤尺寸范围（接近 10）内添加更多数据点，然后重新运行逻辑回归。\n    - 与线性回归模型不同，该模型持续给出正确的预测",
17: "## 恭喜！\n你已经探索了 sigmoid 函数在逻辑回归中的使用。",
}

# ============ F4: Lab03 ============
f4 = r'c:\Users\ives\Desktop\temp\ml\homework\week3\Optional Labs\C1_W3_Lab03_Decision_Boundary_Soln.ipynb'
m4 = {
0: "# 选修实验：逻辑回归，决策边界（Decision Boundary）\n",
1: "## 目标\n在本实验中，你将：\n- 绘制逻辑回归模型的决策边界。这将让你更好地理解模型在预测什么。\n",
3: "## 数据集\n\n假设你有以下训练数据集\n- 输入变量 `X` 是一个 numpy 数组，包含 6 个训练样本，每个样本有两个特征\n- 输出变量 `y` 也是一个包含 6 个样本的 numpy 数组，且 `y` 要么是 `0` 要么是 `1`",
5: "### 绘制数据\n\n让我们使用一个辅助函数来绘制这些数据。标签为 $y=1$ 的数据点显示为红色十字，而标签为 $y=0$ 的数据点显示为蓝色圆圈。",
7: "## 逻辑回归模型\n\n\n* 假设你想在这个数据上训练一个逻辑回归模型，其形式为\n\n  $f(x) = g(w_0x_0+w_1x_1 + b)$\n\n  其中 $g(z) = \\frac{1}{1+e^{-z}}$，即 sigmoid 函数\n\n\n* 假设你训练了模型并得到参数 $b = -3, w_0 = 1, w_1 = 1$。也就是说，\n\n  $f(x) = g(x_0+x_1-3)$\n\n  （你将在课程后续部分学习如何将这些参数拟合到数据）\n\n\n让我们通过绘制该训练模型的决策边界来理解它在预测什么",
8: "### 逻辑回归与决策边界回顾\n\n* 回想一下，对于逻辑回归，模型表示为\n\n  $$f_{\\mathbf{w},b}(\\mathbf{x}^{(i)}) = g(\\mathbf{w} \\cdot \\mathbf{x}^{(i)} + b) \\tag{1}$$\n\n  其中 $g(z)$ 称为 sigmoid 函数，它将所有输入值映射到 0 和 1 之间的值：\n\n  $g(z) = \\frac{1}{1+e^{-z}}\\tag{2}$\n  而 $\\mathbf{w} \\cdot \\mathbf{x}$ 是向量点积：\n\n  $$\\mathbf{w} \\cdot \\mathbf{x} = w_0 x_0 + w_1 x_1$$\n\n\n * 我们将模型的输出（$f_{\\mathbf{w},b}(x)$）解释为在给定 $\\mathbf{x}$ 且以 $\\mathbf{w}$ 和 $b$ 为参数的情况下 $y=1$ 的概率。\n* 因此，要从逻辑回归模型得到最终预测（$y=0$ 或 $y=1$），我们可以使用以下启发式规则 -\n\n  如果 $f_{\\mathbf{w},b}(x) >= 0.5$，预测 $y=1$\n\n  如果 $f_{\\mathbf{w},b}(x) < 0.5$，预测 $y=0$\n\n\n* 让我们绘制 sigmoid 函数，看看在哪里 $g(z) >= 0.5$",
9: "# 在从 -10 到 10 的取值范围内绘制 sigmoid(z)\nz = np.arange(-10,11)\n\nfig,ax = plt.subplots(1,1,figsize=(5,3))\n# 绘制 z 与 sigmoid(z) 的关系\nax.plot(z, sigmoid(z), c=\"b\")\n\nax.set_title(\"Sigmoid function\")\nax.set_ylabel('sigmoid(z)')\nax.set_xlabel('z')\ndraw_vthresh(ax,0)",
10: "* 如你所见，当 $z >=0$ 时，$g(z) >= 0.5$\n\n* 对于逻辑回归模型，$z = \\mathbf{w} \\cdot \\mathbf{x} + b$。因此，\n\n  如果 $\\mathbf{w} \\cdot \\mathbf{x} + b >= 0$，模型预测 $y=1$\n\n  如果 $\\mathbf{w} \\cdot \\mathbf{x} + b < 0$，模型预测 $y=0$\n\n\n\n### 绘制决策边界\n\n现在，让我们回到我们的示例，来理解逻辑回归模型是如何进行预测的。\n\n* 我们的逻辑回归模型形式为\n\n  $f(\\mathbf{x}) = g(-3 + x_0+x_1)$\n\n\n* 根据你上面所学，你可以看到该模型在 $-3 + x_0+x_1 >= 0$ 时预测 $y=1$\n\n让我们看看这在图形上是什么样子。我们先绘制 $-3 + x_0+x_1 = 0$，它等价于 $x_1 = 3 - x_0$。",
11: "# 选择 0 到 6 之间的值\nx0 = np.arange(0,6)\n\nx1 = 3 - x0\nfig,ax = plt.subplots(1,1,figsize=(5,4))\n# 绘制决策边界\nax.plot(x0,x1, c=\"b\")\nax.axis([0, 4, 0, 3.5])\n\n# 填充直线下方的区域\nax.fill_between(x0,x1, alpha=0.2)\n\n# 绘制原始数据\nplot_data(X,y,ax)\nax.set_ylabel(r'$x_1$')\nax.set_xlabel(r'$x_0$')\nplt.show()",
12: "* 在上图中，蓝线表示直线 $x_0 + x_1 - 3 = 0$，它应在 3 处与 x1 轴相交（如果我们设 $x_1$ = 3，则 $x_0$ = 0），并在 3 处与 x0 轴相交（如果我们设 $x_1$ = 0，则 $x_0$ = 3）。\n\n\n* 阴影区域表示 $-3 + x_0+x_1 < 0$。直线以上的区域是 $-3 + x_0+x_1 > 0$。\n\n\n* 阴影区域（直线下方）中的任何点都被分类为 $y=0$。直线上或上方的任何点都被分类为 $y=1$。这条线称为 \"决策边界\"。\n\n正如我们在讲座中所见，通过使用更高阶的多项式项（例如：$f(x) = g( x_0^2 + x_1 -1)$），我们可以得到更复杂的非线性边界。",
13: "## 恭喜！\n你已在逻辑回归的背景下探索了决策边界。",
}

# ============ F5: Lab04 ============
f5 = r'c:\Users\ives\Desktop\temp\ml\homework\week3\Optional Labs\C1_W3_Lab04_LogisticLoss_Soln.ipynb'
m5 = {
0: "# 选修实验：逻辑回归，逻辑损失（Logistic Loss）\n\n在这个不计分实验中，你将：\n- 探索为什么平方误差损失不适用于逻辑回归\n- 探索逻辑损失函数",
2: "## 逻辑回归的平方误差？\n<img align=\"left\" src=\"./images/C1_W3_SqErrorVsLogistic.png\"     style=\" width:400px; padding: 10px; \" > 回想一下，对于**线性**回归，我们使用了**平方误差代价函数**：\n单变量的平方误差代价方程为：\n  $$J(w,b) = \\frac{1}{2m} \\sum\\limits_{i = 0}^{m-1} (f_{w,b}(x^{(i)}) - y^{(i)})^2 \\tag{1}$$\n\n其中\n  $$f_{w,b}(x^{(i)}) = wx^{(i)} + b \\tag{2}$$",
3: "回想一下，平方误差代价有一个很好的性质：沿着代价的导数方向可以到达最小值。",
5: "这个代价函数对线性回归效果很好，因此也很自然地将它考虑用于逻辑回归。然而，如上面的幻灯片所指出的，$f_{wb}(x)$ 现在有一个非线性成分，即 sigmoid 函数：   $f_{w,b}(x^{(i)}) = sigmoid(wx^{(i)} + b )$。   让我们在之前实验的示例上尝试平方误差代价，这次包含 sigmoid。\n\n以下是我们的训练数据：",
7: "现在，让我们使用*平方误差代价*得到代价的曲面图：\n  $$J(w,b) = \\frac{1}{2m} \\sum\\limits_{i = 0}^{m-1} (f_{w,b}(x^{(i)}) - y^{(i)})^2 $$\n\n其中\n  $$f_{w,b}(x^{(i)}) = sigmoid(wx^{(i)} + b )$$",
9: "虽然这产生了一个相当有趣的图，但上面的曲面远不如线性回归的 \'汤碗\'（soup bowl）那样平滑！\n\n逻辑回归需要一个更适合其非线性特性的代价函数。这要从损失（Loss）函数开始。下面将对此进行描述。",
10: "## 逻辑损失函数\n<img align=\"left\" src=\"./images/C1_W3_LogisticLoss_a.png\"     style=\" width:250px; padding: 2px; \" >\n<img align=\"left\" src=\"./images/C1_W3_LogisticLoss_b.png\"     style=\" width:250px; padding: 2px; \" >\n<img align=\"left\" src=\"./images/C1_W3_LogisticLoss_c.png\"     style=\" width:250px; padding: 2px; \" > ",
11: "逻辑回归使用一种更适合分类任务的损失函数，其中目标值为 0 或 1，而不是任意数字。\n\n>**定义说明：**   在本课程中，使用以下定义：\n**Loss**（损失）是单个样本与其目标值之间差异的度量，而\n**Cost**（代价）是对训练集上所有损失的度量\n\n\n其定义如下：\n* $loss(f_{\\mathbf{w},b}(\\mathbf{x}^{(i)}), y^{(i)})$ 是单个数据点的代价，即：\n\n\\begin{equation}\n  loss(f_{\\mathbf{w},b}(\\mathbf{x}^{(i)}), y^{(i)}) = \\begin{cases}\n    - \\log\\left(f_{\\mathbf{w},b}\\left( \\mathbf{x}^{(i)} \\right) \\right) & \\text{if $y^{(i)}=1$}\\\\\n    - \\log \\left( 1 - f_{\\mathbf{w},b}\\left( \\mathbf{x}^{(i)} \\right) \\right) & \\text{if $y^{(i)}=0$}\n  \\end{cases}\n\\end{equation}\n\n\n*  $f_{\\mathbf{w},b}(\\mathbf{x}^{(i)})$ 是模型的预测，而 $y^{(i)}$ 是目标值。\n\n*  $f_{\\mathbf{w},b}(\\mathbf{x}^{(i)}) = g(\\mathbf{w} \\cdot\\mathbf{x}^{(i)}+b)$，其中函数 $g$ 是 sigmoid 函数。\n\n这个损失函数的定义性特征在于它使用两条独立的曲线。一条用于目标为零（$y=0$）的情形，另一条用于目标为一（$y=1$）的情形。结合来看，这些曲线提供了作为损失函数有用的行为，即当预测与目标一致时为零，并随着预测偏离目标而迅速增大。考虑下面的曲线：",
13: "结合来看，这些曲线类似于平方误差损失的二次曲线。注意，x 轴是 $f_{\\mathbf{w},b}$，即 sigmoid 的输出。sigmoid 输出严格介于 0 和 1 之间。",
14: "上面的损失函数可以重写为更易于实现的形式。\n    $$loss(f_{\\mathbf{w},b}(\\mathbf{x}^{(i)}), y^{(i)}) = (-y^{(i)} \\log\\left(f_{\\mathbf{w},b}\\left( \\mathbf{x}^{(i)} \\right) \\right) - \\left( 1 - y^{(i)}\\right) \\log \\left( 1 - f_{\\mathbf{w},b}\\left( \\mathbf{x}^{(i)} \\right) \\right)$$\n\n这是一个看起来相当吓人的方程。当你考虑到 $y^{(i)}$ 只能取两个值 0 和 1 时，它就没那么令人生畏了。于是可以将方程分成两部分来考虑：\n当 $ y^{(i)} = 0$ 时，左侧项被消去：\n$$\n\\begin{align}\nloss(f_{\\mathbf{w},b}(\\mathbf{x}^{(i)}), 0) &= (-(0) \\log\\left(f_{\\mathbf{w},b}\\left( \\mathbf{x}^{(i)} \\right) \\right) - \\left( 1 - 0\\right) \\log \\left( 1 - f_{\\mathbf{w},b}\\left( \\mathbf{x}^{(i)} \\right) \\right) \\\\\n&= -\\log \\left( 1 - f_{\\mathbf{w},b}\\left( \\mathbf{x}^{(i)} \\right) \\right)\n\\end{align}\n$$\n而当 $ y^{(i)} = 1$ 时，右侧项被消去：\n$$\n\\begin{align}\n  loss(f_{\\mathbf{w},b}(\\mathbf{x}^{(i)}), 1) &=  (-(1) \\log\\left(f_{\\mathbf{w},b}\\left( \\mathbf{x}^{(i)} \\right) \\right) - \\left( 1 - 1\\right) \\log \\left( 1 - f_{\\mathbf{w},b}\\left( \\mathbf{x}^{(i)} \\right) \\right)\\\\\n  &=  -\\log\\left(f_{\\mathbf{w},b}\\left( \\mathbf{x}^{(i)} \\right) \\right)\n\\end{align}\n$$\n\n好的，有了这个新的逻辑损失函数，就可以构造一个包含所有样本损失的代价函数。这将是下一个实验的主题。现在，让我们看看上面我们所考虑的简单示例的代价与参数的关系曲线：",
16: "这条曲线非常适合梯度下降！它没有平坦区、局部最小值或间断点。注意，它不像平方误差那样是一个碗形。代价和代价的对数都被绘制出来，以说明当代价很小时，曲线仍有斜率并继续下降。提醒：你可以用鼠标旋转上面的图。",
17: "## 恭喜！\n你已经：\n - 确定了平方误差损失函数不适用于分类任务\n - 开发并检验了逻辑损失函数，它**确实**适用于分类任务。",
}

apply(f2, m2)
apply(f3, m3)
apply(f4, m4)
apply(f5, m5)
print('DONE')

# 练习测验：用梯度下降训练模型

**总分 2 分**

## 1. （1 分）

梯度下降是一种用于寻找参数 $w$ 和 $b$、使代价函数 $J$ 最小的算法。

$$
\begin{align*}
\text{重复直到收敛 \{ } & \\
w &= w - \alpha \frac{\partial}{\partial w} J(w, b) \\
b &= b - \alpha \frac{\partial}{\partial b} J(w, b)
\end{align*}
$$

当 $\frac{\partial J(w,b)}{\partial w}$ 为负数（小于零）时，在一次更新步骤后 $w$ 会发生什么变化？

- [ ] $w$ 保持不变
- [ ] 无法判断 $w$ 会增加还是减少。
- [ ] $w$ 减小
- [x] $w$ 增加。

## 2. （1 分）

对于线性回归，参数 $b$ 的更新步骤是什么？

- [ ] $b = b - \alpha \frac{1}{m} \sum\limits_{i=1}^{m} (f_{w,b}(x^{(i)}) - y^{(i)}) x^{(i)}$
- [x] $b = b - \alpha \frac{1}{m} \sum\limits_{i=1}^{m} (f_{w,b}(x^{(i)}) - y^{(i)})$

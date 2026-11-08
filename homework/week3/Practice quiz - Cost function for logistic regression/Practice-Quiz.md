# 练习测验：逻辑回归的代价函数

最新提交成绩 100%

## 1.（1 分）

$$J(\vec{w}, b) = \frac{1}{m} \sum_{i=1}^{m} L\left(f_{\vec{w},b}\left(\vec{x}^{(i)}\right), y^{(i)}\right)$$

在本系列课程中，“cost（代价）”和“loss（损失）”有着不同的含义。哪一个适用于单个训练样本？

- [x] Loss（损失）
  - ✔ 正确：在本课程中，损失是在单个训练样本上计算的。值得注意的是，这个定义并非普遍适用。其他系列课程可能有不同的定义。
- [ ] Cost（代价）
- [ ] Loss 和 Cost 都是
- [ ] 既不是 Loss 也不是 Cost

## 2.（1 分）

**简化的损失函数**

$$L\left(f_{\vec{w},b}\left(\vec{x}^{(i)}\right), y^{(i)}\right) = \begin{cases} -\log\left(f_{\vec{w},b}\left(\vec{x}^{(i)}\right)\right) & \text{如果 } y^{(i)} = 1 \\ -\log\left(1 - f_{\vec{w},b}\left(\vec{x}^{(i)}\right)\right) & \text{如果 } y^{(i)} = 0 \end{cases}$$

$$L\left(f_{\vec{w},b}\left(\vec{x}^{(i)}\right), y^{(i)}\right) = -y^{(i)}\log\left(f_{\vec{w},b}\left(\vec{x}^{(i)}\right)\right) - \left(1 - y^{(i)}\right)\log\left(1 - f_{\vec{w},b}\left(\vec{x}^{(i)}\right)\right)$$

对于简化后的损失函数，如果标签 $y^{(i)} = 0$，那么这个表达式会简化为？

- [ ] $\log(f_{\vec{w},b}(\mathbf{x}^{(i)}))$
- [ ] $\log(1 - f_{\vec{w},b}(\mathbf{x}^{(i)})) + \log(1 - f_{\vec{w},b}(\mathbf{x}^{(i)}))$
- [ ] $-\log(1 - f_{\vec{w},b}(\mathbf{x}^{(i)})) - \log(1 - f_{\vec{w},b}(\mathbf{x}^{(i)}))$
- [x] $-\log(1 - f_{\vec{w},b}(\mathbf{x}^{(i)}))$
  - ✔ 正确：当 $y^{(i)} = 0$ 时，第一项变为零。

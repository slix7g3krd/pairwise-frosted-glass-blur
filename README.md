# pairwise-frosted-glass-blur

## 领域

游戏、图形与多媒体

## 主题

磨砂玻璃模糊

## 说明

按距离模糊、自身深度与全分辨率合成。

初始状态下 `render/frosted_glass_blur.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。

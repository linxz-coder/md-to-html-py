---
title: python虚拟环境搭建-venv方法
url: python-venv
---

# python虚拟环境venv，解决依赖冲突问题

我们一般会去调试各种路径，`which python`和`pip`，以及`python3`和`pip3`，但是这些都不是问题的根源。问题的根源是**依赖冲突**。

解决方案如下：

```python
# 创建一个虚拟环境
python3 -m venv venv

# 激活虚拟环境
source venv/bin/activate

# 在虚拟环境中安装插件，如
pip install markdown

# 运行脚本
python md-html.py

# 退出虚拟环境
deactivate
```
<br>

按照以上方法，可以解决大部分**依赖冲突**问题。
就是这么简单。
# 引入必要的库
import os
import re

# 定义源文件路径
src_file = "everyday_todo.md"

# 读取源文件内容
with open(src_file, "r", encoding="utf-8") as f:
    content = f.read()

# 使用正则表达式替换 - [x] 为 - [ ]
content = re.sub(r'- \[x\]', '- [ ]', content)

# 将替换后的内容写回文件
with open(src_file, "w", encoding="utf-8") as f:
    f.write(content)

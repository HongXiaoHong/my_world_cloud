#!/usr/bin/env python
"""
该脚本可以读取JSON文件，将其转换为Markdown序列列表，并将结果保存到名为output.md的文件中
"""
import json
import sys

# 设置递归深度限制
sys.setrecursionlimit(3000)

# P5 学习路线 data.json
# learn_router.json 高级进阶
json_file_name = 'learn_router.json'

# 读取JSON文件内容
with open(json_file_name, 'r', encoding='utf-8') as file:
    json_string = file.read()

# 将JSON文本转换为Python字典
json_data = json.loads(json_string)

# 使用递归函数将JSON数据转换为Markdown
def json_to_markdown(json_data, depth=0):
    markdown_output = ''
    if 'title' in json_data:
        markdown_output += '  ' * depth + '- ' + json_data['title'] + '\n'
    if 'children' in json_data:
        for child in json_data['children']:
            markdown_output += json_to_markdown(child, depth + 1)
    return markdown_output

# 转换并打印输出的Markdown
markdown_output = json_to_markdown(json_data)
print(markdown_output)

# mindmap.md P5路线
# learn_router_mindmap 进阶路线
output_markdown_file_name = 'learn_router_mindmap.md'
# 将Markdown输出保存到文件
with open(output_markdown_file_name, 'w', encoding='utf-8') as file:
    file.write(markdown_output)

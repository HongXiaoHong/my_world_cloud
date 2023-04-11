import os

# 指定目录路径
directory = 'E:/python/wordcloud/blackboard/background'

# 获取目录中所有文件名
files = os.listdir(directory)

# 初始化计数器
count = 1

# 遍历目录中的所有文件
for filename in files:
    # 判断文件是否为图片文件
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # 构造新的文件名
        new_filename = str(count) + ".jpg"
        # 重命名文件
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
        # 更新计数器
        count += 1

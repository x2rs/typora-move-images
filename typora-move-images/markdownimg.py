import re
import os
import shutil
import sys

try:
    mdfile = sys.argv[1]
except IndexError:
    print("缺少Markdown文件名。")
    sys.exit(1)

if not os.path.exists(mdfile):
    print(f"文件 {mdfile} 不存在。")
    sys.exit(1)

def update_image_paths(mdfile):
    # 读取Markdown文件内容
    with open(f"{mdfile}", "r", encoding="utf-8") as f:
        md_content = f.read()
    img_dir_path = os.path.join(os.path.dirname(mdfile), "images/")

    if not os.path.exists(img_dir_path):
        os.makedirs(img_dir_path)
    
    # 使用正则表达式查找图片标签
    image_pattern = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(image_pattern, md_content)

    # 遍历匹配到的图片标签，并更新路径
    for _match in matches:
        old_path = _match[1]
        file_name = os.path.basename(old_path)
        new_path = f"images/{file_name}"  # 构建新路径
        md_content = md_content.replace(old_path, new_path)  # 替换路径
        
        dest_path = os.path.join(img_dir_path, file_name)
        if not os.path.exists(dest_path):
            shutil.copy(old_path, os.path.join(img_dir_path, file_name))  # 复制文件到新路径
        
    # 将更新后的内容写回文件
    with open(mdfile, "w", encoding="utf-8") as f:
        f.write(md_content)

update_image_paths(mdfile)
print("图片路径已更新。")

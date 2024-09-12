import os
import shutil
import yaml
def setup_directory(directory_path):
    """如果存在目录，则删除并重新创建"""
    if os.path.exists(directory_path):
        shutil.rmtree(directory_path)
    os.makedirs(directory_path)

def load_config(filename='config.yml'):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = yaml.safe_load(file)
            return data if data is not None else []  # 如果文件为空或无内容，返回空列表或字典
    except FileNotFoundError:
        return []  # 文件不存在时返回空列表

def write_yaml(path,data):
    with open(path, 'w', encoding='utf-8') as file:
        yaml.dump(data, file, allow_unicode=True)
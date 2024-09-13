import ebooklib
from bs4 import BeautifulSoup
from ebooklib import epub

# 读取epub文件


def clean_html(html_content):
    """使用BeautifulSoup来提取HTML内容中的纯文本，并忽略不必要的标签"""
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 移除不必要的标签，如样式、脚本、页眉等
    for tag in soup(['style', 'script', 'aside', 'footer', 'header']):
        tag.decompose()
    
    # 初始化存储段落的列表
    paragraphs = []
    
    # 提取所有的<p>标签，作为正文段落
    for p in soup.find_all('p'):
        paragraph_text = p.get_text(strip=True)
        if paragraph_text:
            paragraphs.append(paragraph_text)
    
    # 将段落连接起来，每个段落之间以两个换行符分隔
    return "\n\n".join(paragraphs)

def convert_to_txt(book_path):
    book = epub.read_epub(book_path)
    # 创建一个列表来存储所有章节的正文
    all_text = []

    # 解析每个文档项
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            content = item.get_content()
            # 调用clean_html提取出正文内容
            clean_text = clean_html(content)
            all_text.append(clean_text)

    # 将所有章节的正文连接起来
    full_text = "\n\n".join(all_text)

    full_text = reformat_text(full_text)
    # 将输出保存为txt文件，或输出到控制台
    with open("book_text.txt", "w", encoding="utf-8") as f:
        f.write(full_text)

    print("正文提取完成并保存到 book_text.txt")


def reformat_text(text):
    lines = text.splitlines()
    new_text = []
    temp_paragraph = []

    for line in lines:
        if line.strip():  # 如果行非空白
            temp_paragraph.append(line.strip())
        else:
            # 如果当前temp_paragraph有内容，说明是一个完整的段落
            if temp_paragraph:
                new_text.append(' '.join(temp_paragraph))  # 合并段落中的行
                temp_paragraph = []  # 清空当前段落临时列表
            new_text.append('')  # 保留段落间的空白行

    # 处理文件最后可能的残留段落
    if temp_paragraph:
        new_text.append(' '.join(temp_paragraph))

    return '\n'.join(new_text)
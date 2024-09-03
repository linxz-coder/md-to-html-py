import markdown
from markdown.extensions import fenced_code, codehilite

# 读取Markdown文件内容
with open("python-venv.md", "r", encoding="utf-8") as input_file:
    text = input_file.read()

# 将Markdown内容转换为HTML，使用fenced_code和codehilite扩展
html = markdown.markdown(text, extensions=[fenced_code.FencedCodeExtension(), codehilite.CodeHiliteExtension()])

# 将HTML内容写入文件
with open("output.html", "w", encoding="utf-8") as output_file:
    output_file.write(html)

print("转换完成，HTML文件已生成。")
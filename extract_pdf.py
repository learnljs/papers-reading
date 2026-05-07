import PyPDF2

# 打开PDF文件
with open('week6.pdf', 'rb') as file:
    # 创建PDF阅读器对象
    reader = PyPDF2.PdfReader(file)
    
    # 获取PDF页数
    num_pages = len(reader.pages)
    print(f"PDF共有 {num_pages} 页")
    
    # 提取文本
    text = ""
    for page_num in range(num_pages):
        page = reader.pages[page_num]
        text += page.extract_text()
        
    # 保存提取的文本到文件
    with open('week6_text.txt', 'w', encoding='utf-8') as output_file:
        output_file.write(text)
    
    print("文本提取完成，已保存到 week6_text.txt")
    
    # 打印前1000个字符预览
    print("\n文本预览:")
    print(text[:1000])
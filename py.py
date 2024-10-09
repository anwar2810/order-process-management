import os

def merge_py_files(directory, output_file):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for filename in os.listdir(directory):
            if filename.endswith(".py") and filename != output_file:
                file_path = os.path.join(directory, filename)
                with open(file_path, 'r', encoding='utf-8') as infile:
                    outfile.write(f"# Start of {filename}\n")
                    outfile.write(infile.read())
                    outfile.write(f"\n# End of {filename}\n\n")
                # 刪除舊文件
                os.remove(file_path)
    print(f"所有 .py 文件已合併並保存到 {output_file}")

# 使用示例
directory = "D:/github/order-process-management"
output_file = "merged_script.py"
merge_py_files(directory, output_file)
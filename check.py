import os
import re
import sys

def check_note_inclusion(number, name, notes_dir=os.getcwd()):
    # 构造匹配题号和题目名称的正则表达式
    # 假设格式为： "198. 打家劫舍 [中等]"
    problem_pattern = re.compile(r"(\d+)\.\s*(.*?)\s*\[.*\]")
    
    # 遍历笔记文件夹中的所有文件
    for entry in os.listdir(notes_dir):
        dir_path = os.path.join(notes_dir, entry)
        if os.path.isfile(dir_path):
            continue
        for file in os.listdir(dir_path):
            if file.endswith(".md"):  # 只处理 markdown 文件
                file_path = os.path.join(dir_path, file)
                
                # 打开并读取文件内容
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                # 查找文件中的所有二级标题
                matches = problem_pattern.findall(content)
                for match in matches:
                    problem_number = match[0]
                    problem_name = match[1]
                    
                    # 如果题号和题目名称匹配
                    if number == problem_number or (not name == "" and name.lower() in problem_name.lower()):
                        print(f"{problem_number}.{problem_name} 已收录在文件: {os.path.relpath(file_path, notes_dir)}")
                        return  # 找到匹配题目，结束查找
                

    print(f"{number}.{name} 未在任何笔记中找到。")

def usage():
    print("usage: python check.py -d <prob_number> -n <prob_name>")
    sys.exit(1)     

if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
    
    # 解析命令行参数
    args = sys.argv[1:]
    prob_name = ""
    prob_number = ""
    if "-d" in args and args.index("-d") + 1 < len(args):
        d_index = args.index("-d")
        prob_number = args[d_index + 1]
    if "-n" in args and args.index("-n") + 1 < len(args):
        n_index = args.index("-n")
        prob_name = args[n_index + 1]

    if not prob_name and not prob_number:
        usage()
    check_note_inclusion(prob_number, prob_name)
    
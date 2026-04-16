import os
import re
import sys

def colorize_difficulty(difficulty):
    """根据难度返回带颜色的难度文本"""
    # ANSI 颜色码
    GREEN = '\033[92m'
    ORANGE = '\033[33m'
    RED = '\033[91m'
    RESET = '\033[0m'
    
    if difficulty == "简单":
        return f"{GREEN}{difficulty}{RESET}"
    elif difficulty == "中等":
        return f"{ORANGE}{difficulty}{RESET}"
    elif difficulty == "困难":
        return f"{RED}{difficulty}{RESET}"
    else:
        return difficulty

def print_problems_tree(verbose=False):
    """打印题目统计或详细信息"""
    problem_pattern = re.compile(r"## (\d+)\.\s*(.*?)\s*\[(.*?)\]")
    notes_dir = os.getcwd()
    count = 0
    
    # 用于存储按文件组织的题目
    problems_by_file = {}
    
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
                file_count = len(matches)
                count += file_count
                
                if verbose:
                    # 存储每个文件中的题目（题目ID、题目名、难度）
                    file_base = os.path.splitext(file)[0]
                    problems_by_file[file_base] = [(problem_id, problem_title, difficulty) for problem_id, problem_title, difficulty in matches]
    
    if verbose:
        # 打印详细的结构
        print("\n📚 LeetCode 题目收录详情:\n")
        for file_name in sorted(problems_by_file.keys()):
            problems = sorted(problems_by_file[file_name], key=lambda x: int(x[0]))
            print(f"📄 {file_name} ({len(problems)} 题)")
            for problem_id, problem_title, difficulty in problems:
                colored_difficulty = colorize_difficulty(difficulty)
                print(f"  ├─ [{problem_id}] {problem_title} [{colored_difficulty}]")
            print()
        print(f"总共收录了 {count} 道题目。")
    else:
        print(f"总共收录了 {count} 道题目。")

if __name__ == "__main__":
    verbose = "--verbose" in sys.argv or "-v" in sys.argv
    print_problems_tree(verbose=verbose)
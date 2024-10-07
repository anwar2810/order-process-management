import os

def git_status():
    os.system('git status')

def git_commit(message):
    os.system(f'git add .')  # 添加所有更改
    os.system(f'git commit -m "{message}"')

def git_push(branch='main'):
    os.system(f'git push origin {branch}')

if __name__ == "__main__":
    git_status()  # 查看当前状态
    commit_message = input("Enter your commit message: ")
    git_commit(commit_message)  # 提交更改
    git_push()  # 推送到远程仓库

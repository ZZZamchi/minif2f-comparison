#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess
import sys
import io

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# 获取Git跟踪的文件
result = subprocess.run(['git', 'ls-files'], capture_output=True, text=True, encoding='utf-8')
git_files = result.stdout.strip().split('\n')

# 需要删除的文件
to_remove = []
for f in git_files:
    # 检查是否包含中文关键词（使用UTF-8编码检查）
    if any(x in f for x in ['上传', '项目', '快速', 'README_上传', '\344\270\212', '\351\241\271']):
        to_remove.append(f)

if to_remove:
    print(f"Removing {len(to_remove)} files from Git:")
    for f in to_remove:
        print(f"  - {f}")
        subprocess.run(['git', 'rm', '--cached', f], capture_output=True)
    print(f"\nRemoved {len(to_remove)} files from Git")
    print("\nRun: git commit -m 'Remove Chinese filename files' && git push")
else:
    print("No files to remove from Git")

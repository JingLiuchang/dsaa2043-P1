#!/usr/bin/env python3
import sys
import numpy as np
from solution import solve

def parse_input():
    """解析输入数据"""
    # 读取第一行: M,N,K,T
    first_line = input().strip()
    M, N, K, T = map(int, first_line.split(','))
    
    # 读取矩阵 A
    A = []
    for _ in range(M):
        line = input().strip()
        # 移除开头的'[' 和结尾的 '],'
        line = line.replace('[', '').replace('],', '')
        row = list(map(int, line.split(',')))
        A.append(row)
    
    # 读取矩阵 G
    G = []
    for _ in range(M):
        line = input().strip()
        # 移除开头的'[' 和结尾的 '],'
        line = line.replace('[', '').replace('],', '')
        row = list(map(int, line.split(',')))
        G.append(row)
    
    return M, N, K, T, np.array(A), np.array(G)

def main():
    try:
        # 解析输入
        M, N, K, T, A, G = parse_input()
        
        # 调用学生的解决方案
        result = solve(M, N, K, T, A, G)
        
        # 输出结果
        print(result)
        
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())

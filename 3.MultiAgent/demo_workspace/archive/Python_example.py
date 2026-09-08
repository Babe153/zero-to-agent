#!/usr/bin/env python3
"""
一个简单的 Python 示例代码
"""

def greet(name):
    """问候函数"""
    return f"Hello, {name}!"

def add(a, b):
    """加法函数"""
    return a + b

if __name__ == "__main__":
    # 测试 greet 函数
    print(greet("World"))
    
    # 测试 add 函数
    result = add(5, 3)
    print(f"5 + 3 = {result}")
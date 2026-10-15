# 密码生成器 (password-generator)

生成高强度随机密码或易记密码短语。

## 功能

- 自定义密码长度
- 可选字符类型（大写/小写/数字/符号）
- 密码强度评估
- 易记密码短语模式
- 批量生成

## 使用方法

```bash
# 生成 16 位密码
python main.py

# 生成 32 位密码
python main.py -l 32

# 生成 5 个密码
python main.py -c 5

# 不使用特殊符号
python main.py --no-symbols

# 生成易记密码短语
python main.py --passphrase

# 密码短语 6 个单词
python main.py --passphrase --words 6
```

## 依赖

仅使用 Python 标准库，无需额外安装。

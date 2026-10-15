#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
密码生成器
生成高强度随机密码，支持自定义长度和字符类型
"""

import argparse
import random
import string
import secrets


def generate_password(length=16, use_upper=True, use_lower=True,
                      use_digits=True, use_symbols=True, exclude=""):
    """生成随机密码"""
    charset = ""
    if use_upper:
        charset += string.ascii_uppercase
    if use_lower:
        charset += string.ascii_lowercase
    if use_digits:
        charset += string.digits
    if use_symbols:
        charset += "!@#$%^&*()_+-=[]{}|;:,.<>?"

    # 排除指定字符
    if exclude:
        charset = "".join(c for c in charset if c not in exclude)

    if not charset:
        print("[错误] 字符集为空，请至少选择一种字符类型")
        return None

    # 使用 secrets 模块生成加密安全的随机密码
    password = "".join(secrets.choice(charset) for _ in range(length))
    return password


def generate_passphrase(num_words=4, separator="-"):
    """生成易记的密码短语"""
    # 常用单词列表
    words = [
        "apple", "banana", "cherry", "dragon", "eagle", "forest", "galaxy",
        "harbor", "island", "jungle", "kitten", "lemon", "mountain", "night",
        "ocean", "panda", "queen", "river", "sunset", "tiger", "umbrella",
        "violet", "whale", "xenon", "yellow", "zebra", "amber", "blue",
        "coral", "diamond", "emerald", "flame", "gold", "honey", "ivory",
        "jade", "kite", "luna", "mist", "nova", "opal", "pearl", "quartz",
        "ruby", "sapphire", "topaz", "urban", "vivid", "willow", "xray",
        "yoga", "zephyr", "atom", "blaze", "cloud", "delta", "echo", "frost",
        "glow", "horizon", "ice", "jolt", "kiwi", "lagoon", "meadow", "nebula",
    ]
    chosen = random.sample(words, min(num_words, len(words)))
    # 每个单词首字母大写
    chosen = [w.capitalize() for w in chosen]
    # 添加随机数字
    chosen.append(str(random.randint(10, 99)))
    return separator.join(chosen)


def check_strength(password):
    """评估密码强度"""
    score = 0
    tips = []

    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if len(password) >= 16:
        score += 1
    else:
        tips.append("建议长度至少 16 位")

    if any(c.isupper() for c in password):
        score += 1
    else:
        tips.append("建议包含大写字母")

    if any(c.islower() for c in password):
        score += 1
    else:
        tips.append("建议包含小写字母")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        tips.append("建议包含数字")

    if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
        score += 1
    else:
        tips.append("建议包含特殊符号")

    levels = ["极弱", "弱", "一般", "较强", "强", "很强", "极强"]
    level = levels[min(score, len(levels) - 1)]
    return score, level, tips


def main():
    parser = argparse.ArgumentParser(description="密码生成器")
    parser.add_argument("-l", "--length", type=int, default=16, help="密码长度（默认 16）")
    parser.add_argument("--no-upper", action="store_true", help="不使用大写字母")
    parser.add_argument("--no-lower", action="store_true", help="不使用小写字母")
    parser.add_argument("--no-digits", action="store_true", help="不使用数字")
    parser.add_argument("--no-symbols", action="store_true", help="不使用特殊符号")
    parser.add_argument("--exclude", default="", help="排除的字符")
    parser.add_argument("-c", "--count", type=int, default=1, help="生成数量")
    parser.add_argument("--passphrase", action="store_true", help="生成易记密码短语")
    parser.add_argument("--words", type=int, default=4, help="密码短语单词数")
    args = parser.parse_args()

    if args.passphrase:
        for _ in range(args.count):
            pwd = generate_passphrase(args.words)
            score, level, tips = check_strength(pwd)
            print(f"密码短语: {pwd}")
            print(f"强度: {level} ({score}/7)")
            print()
    else:
        for _ in range(args.count):
            pwd = generate_password(
                args.length,
                use_upper=not args.no_upper,
                use_lower=not args.no_lower,
                use_digits=not args.no_digits,
                use_symbols=not args.no_symbols,
                exclude=args.exclude,
            )
            if pwd:
                score, level, tips = check_strength(pwd)
                print(f"密码: {pwd}")
                print(f"强度: {level} ({score}/7)")
                if tips:
                    print(f"建议: {'; '.join(tips)}")
                print()


if __name__ == "__main__":
    main()

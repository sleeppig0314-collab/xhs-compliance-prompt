#!/usr/bin/env python3
"""
小红书违禁词检测工具
用法: python xhs_checker.py "你的文案"
"""

import sys
import re

BANNED_WORDS = [
    (r"最[好一二三四五六七八九十百千万]+", "很"),
    (r"第一", "名列前茅"),
    (r"国家级", "专业级"),
    (r"最佳", "很不错"),
    (r"最优", "很棒"),
    (r"顶级", "高品质"),
    (r"极致", "出色"),
    (r"100%", "高"),
    (r"保证", "，力争"),
    (r"绝不", "不会"),
    (r"绝对", "非常"),
    (r"立即", "很快"),
    (r"马上", "很快"),
    (r"稳赚", "有机会获得收益"),
    (r"根治", "改善"),
    (r"治愈", "缓解"),
]

def check_text(text):
    violations = []
    for pattern, _ in BANNED_WORDS:
        if re.search(pattern, text):
            matches = re.findall(pattern, text)
            for m in matches:
                violations.append(m)
    return violations

def rewrite_text(text):
    result = text
    for pattern, replacement in BANNED_WORDS:
        result = re.sub(pattern, replacement, result)
    return result

def main():
    if len(sys.argv) < 2:
        print("用法: python xhs_checker.py \"你的文案\"")
        sys.exit(1)
    
    text = sys.argv[1]
    violations = check_text(text)
    
    print(f"\n🔍 检测结果 (发现 {len(violations)} 个风险词)")
    print("=" * 50)
    
    if violations:
        for v in violations:
            print(f"  ⚠️  {v}")
        print(f"\n📝 改写建议：\n  {rewrite_text(text)}")
    else:
        print("✅ 未发现违禁词！")
    print()

if __name__ == "__main__":
    main()

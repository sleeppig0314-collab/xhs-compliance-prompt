#!/usr/bin/env python3
"""
小红书违禁词检测工具 v2.0
用法: python xhs_checker.py "你的文案"
"""

import sys
import re

BANNED_WORDS = [
    # 最字辈
    (r"最[好一二三四五六七八九十百千万]+", "很"),
    (r"第一", "名列前茅"),
    (r"国家级", "专业级"),
    (r"最佳", "很不错"),
    (r"最优", "很棒"),
    (r"顶级", "高品质"),
    (r"极致", "出色"),
    # 绝对化用词
    (r"100%", "高"),
    (r"保证", "，力争"),
    (r"承诺", "，努力"),
    (r"绝不", "不会"),
    (r"绝对", "非常"),
    (r"完全", "基本"),
    (r"彻底", "大幅"),
    # 虚假承诺
    (r"无需", "简单"),
    (r"零门槛", "门槛低"),
    (r"一秒学会", "快速学会"),
    (r"一天见效", "持续使用后改善"),
    (r"立即", "很快"),
    (r"马上", "很快"),
    (r"立刻", "很快"),
    # 医疗相关
    (r"根治", "改善"),
    (r"治愈", "缓解"),
    (r"治疗", "护理"),
    (r"药到病除", "有助健康"),
    (r"立刻见效", "逐渐见效"),
    # 投资相关
    (r"稳赚", "有机会获得收益"),
    (r"必涨", "有上涨空间"),
    (r"收益率", "收益情况"),
    (r"投资回报", "投资收益"),
    # 违禁词（按行业）
    (r"最好", "很不错"),
    (r"最棒", "很棒"),
    (r"最强", "很强"),
    (r"最快", "很快"),
    (r"独一无二", "独特"),
    (r"史无前例", "前所未有"),
    (r"前无古人", "罕见"),
]

def check_text(text):
    """检测文案中的违禁词"""
    violations = []
    for pattern, _ in BANNED_WORDS:
        if re.search(pattern, text):
            matches = re.findall(pattern, text)
            for m in matches:
                violations.append(m)
    return list(set(violations))  # 去重

def rewrite_text(text):
    """提供改写建议"""
    result = text
    for pattern, replacement in BANNED_WORDS:
        result = re.sub(pattern, replacement, result)
    return result

def main():
    if len(sys.argv) < 2:
        print("用法: python xhs_checker.py \"你的文案\"")
        print("示例: python xhs_checker.py \"这是最棒的产品，100%有效！\"")
        print("\n也可以运行交互模式:")
        print("python xhs_checker.py --interactive")
        sys.exit(1)
    
    if sys.argv[1] == "--interactive":
        print("\n🔍 小红书违禁词检测工具 (输入 'quit' 退出)")
        print("=" * 50)
        while True:
            text = input("\n请输入文案: ")
            if text.lower() == "quit":
                print("再见！")
                break
            violations = check_text(text)
            print(f"\n检测结果: 发现 {len(violations)} 个风险词")
            if violations:
                for v in violations:
                    print(f"  ⚠️  {v}")
                print(f"\n改写建议:\n  {rewrite_text(text)}")
            else:
                print("✅ 未发现违禁词！")
        return
    
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

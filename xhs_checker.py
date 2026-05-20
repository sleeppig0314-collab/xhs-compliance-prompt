#!/usr/bin/env python3
"""
小红书违禁词检测工具 v2.1
用法: python xhs_checker.py "你的文案"
"""

import sys
import re

BANNED_WORDS = [
    # 最字辈
    (r"最[好一二三四五六七八九十百千万]+", "很"),
    (r"第一", "名列前茅"),
    (r"国家级", "知名"),
    (r"最佳", "优选"),
    (r"最优", "出色"),
    (r"顶级", "高端"),
    (r"极致", "出色"),
    # 绝对化用词
    (r"100%纯天然", "成分温和"),
    (r"100%", "很高"),
    (r"保证", "致力"),
    (r"承诺", "目标"),
    (r"绝不", "一般不会"),
    (r"绝对", "通常"),
    (r"完全", "基本"),
    (r"彻底", "大幅"),
    # 虚假承诺
    (r"无需基础", "入门友好"),
    (r"零门槛", "门槛低"),
    (r"一秒学会", "很快上手"),
    (r"一天见效", "用几天后有感觉"),
    (r"三天美白", "用一周皮肤亮了些"),
    (r"一周祛斑", "坚持用有改善"),
    (r"永久脱毛", "毛发明显减少"),
    (r"稳赚", "收益还行"),
    (r"保本", "风险较低"),
    (r"必涨", "有上涨空间"),
    (r"暴富", "多赚些"),
    (r"翻倍", "涨了不少"),
    (r"立即见效", "即时有感觉"),
    (r"马上变好", "用后有改善"),
    (r"立刻见效", "反馈不错"),
    (r"保证你", "帮你"),
    (r"保证提分", "有助提升"),
    # 医疗相关
    (r"根治", "有效改善"),
    (r"治愈", "有效缓解"),
    (r"治疗", "改善"),
    (r"药到病除", "有帮助"),
    # 投资相关
    (r"收益率", "收益情况"),
    (r"投资回报", "投资收益"),
    # 行业极致词
    (r"最好", "很不错"),
    (r"最棒", "很棒"),
    (r"最强", "很强"),
    (r"最快", "很快"),
    (r"独一无二", "独特"),
    (r"史无前例", "前所未有"),
    (r"前无古人", "独特"),
    # 直播带货
    (r"全网最低", "限时优惠"),
    (r"亏本销售", "限时让利"),
    (r"不买亏一年", "优惠别错过"),
    (r"手慢无", "抓紧下单"),
    (r"全网最低保障", "限时优惠"),
    (r"原价现价", "活动价"),
    # 食品保健品类
    (r"食疗", "食补"),
    (r"补气血", "养气色"),
    (r"祛湿", "排湿"),
    (r"清热解毒", "降火"),
    (r"滋补", "补充营养"),
    (r"养颜", "提升气色"),
    (r"通便", "顺畅"),
    (r"排毒", "代谢"),
    (r"消炎", "舒缓"),
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

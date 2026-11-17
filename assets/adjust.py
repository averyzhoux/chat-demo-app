import re

def create_svg_with_padding(input_path, output_path, padding_ratio):
    try:
        # 1. 读取原文件
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 2. 匹配原始 viewBox
        pattern = r'viewBox=["\']0\s+0\s+24\s+24["\']'

        # 3. 计算新参数
        original_size = 24.0
        added_padding = original_size * padding_ratio
        offset = added_padding / 2

        new_start = 0 - offset
        new_size = original_size + added_padding

        # 格式化去掉多余的 0
        def fmt(num):
            return f"{num:.1f}".rstrip('0').rstrip('.')

        new_viewbox_str = f'viewBox="{fmt(new_start)} {fmt(new_start)} {fmt(new_size)} {fmt(new_size)}"'

        # 4. 替换内容
        new_content, count = re.subn(pattern, new_viewbox_str, content)

        if count > 0:
            # 5. 写入到新文件
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✅ 成功！新文件已生成: {output_path}")
            print(f"   新的参数为: {new_viewbox_str}")
        else:
            print(f"⚠️ 在 {input_path} 中没找到 viewBox=\"0 0 24 24\"，请检查原文件。")

    except FileNotFoundError:
        print(f"❌ 找不到文件: {input_path}")

if __name__ == "__main__":
    PADDING_RATIO = 0.15
    INPUT_FILE = "assets/deepseek.svg"             # 你的原始文件
    OUTPUT_FILE = "assets/icon.svg"     # 生成的新文件

    create_svg_with_padding(INPUT_FILE, OUTPUT_FILE, PADDING_RATIO)

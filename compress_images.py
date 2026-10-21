#!/usr/bin/env python3
"""
图片压缩优化脚本
使用 PIL/Pillow 压缩 JPG 图片,提升页面加载速度
"""
import os
from PIL import Image
import glob

def compress_image(input_path: str, output_path: str = None, quality: int = 85, max_width: int = 1200) -> dict:
    """
    压缩图片
    - quality: 压缩质量 (1-100, 推荐 80-85)
    - max_width: 最大宽度,超过则等比缩放
    """
    if output_path is None:
        output_path = input_path

    # 获取原始文件大小
    original_size = os.path.getsize(input_path)

    # 打开图片
    with Image.open(input_path) as img:
        # 获取原始尺寸
        original_width, original_height = img.size

        # 如果宽度超过最大值,等比缩放
        if original_width > max_width:
            ratio = max_width / original_width
            new_width = max_width
            new_height = int(original_height * ratio)
            img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

        # 转换为 RGB (如果是 RGBA)
        if img.mode in ('RGBA', 'LA', 'P'):
            background = Image.new('RGB', img.size, (255, 255, 255))
            if img.mode == 'P':
                img = img.convert('RGBA')
            background.paste(img, mask=img.split()[-1] if img.mode in ('RGBA', 'LA') else None)
            img = background

        # 保存压缩后的图片
        img.save(output_path, 'JPEG', quality=quality, optimize=True, progressive=True)

    # 获取压缩后文件大小
    compressed_size = os.path.getsize(output_path)

    return {
        'original_size': original_size,
        'compressed_size': compressed_size,
        'reduction': original_size - compressed_size,
        'reduction_percent': ((original_size - compressed_size) / original_size) * 100
    }

def main():
    print("🚀 图片压缩优化工具\n")

    # 检查是否安装了 Pillow
    try:
        from PIL import Image
    except ImportError:
        print("❌ 未安装 Pillow 库")
        print("\n📦 安装方法:")
        print("   pip3 install Pillow")
        print("\n或使用系统自带的 sips 命令 (macOS):")
        print("   for img in img_*.jpg; do")
        print("     sips -s format jpeg -s formatOptions 85 \"$img\" --out \"$img\"")
        print("   done")
        return

    # 查找所有 JPG 图片
    image_files = glob.glob('img_*.jpg')

    if not image_files:
        print("⚠️  未找到需要压缩的图片")
        return

    print(f"📊 找到 {len(image_files)} 张图片\n")

    total_original = 0
    total_compressed = 0

    for img_file in sorted(image_files):
        print(f"🔧 处理: {img_file}")

        # 创建备份
        backup_file = img_file.replace('.jpg', '.jpg.bak')
        if not os.path.exists(backup_file):
            import shutil
            shutil.copy2(img_file, backup_file)
            print(f"   📦 备份: {backup_file}")

        # 压缩图片
        result = compress_image(img_file, quality=85, max_width=1200)

        total_original += result['original_size']
        total_compressed += result['compressed_size']

        print(f"   ✅ {result['original_size']/1024:.1f}KB → {result['compressed_size']/1024:.1f}KB "
              f"(减少 {result['reduction_percent']:.1f}%)")

    print("\n" + "="*60)
    print("📊 压缩完成")
    print("="*60)
    print(f"   • 原始总大小: {total_original/1024:.1f}KB")
    print(f"   • 压缩后总大小: {total_compressed/1024:.1f}KB")
    print(f"   • 总共减少: {(total_original - total_compressed)/1024:.1f}KB "
          f"({((total_original - total_compressed) / total_original) * 100:.1f}%)")

    print("\n📈 优化效果:")
    print("   • 页面加载速度提升")
    print("   • 减少带宽消耗")
    print("   • 改善移动端体验")
    print("   • Core Web Vitals 得分提升")

    print("\n💡 提示:")
    print("   • 备份文件: img_*.jpg.bak")
    print("   • 如需恢复: mv img_xxx.jpg.bak img_xxx.jpg")

if __name__ == '__main__':
    main()

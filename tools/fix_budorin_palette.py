#!/usr/bin/env python3
from PIL import Image
import sys

PALETTE_PATH = 'graphics/pokemon/budorin/normal.pal'
FILES = ['graphics/pokemon/budorin/back.png', 'graphics/pokemon/budorin/icon.png']

def read_jasc_pal(path):
    with open(path, 'r') as f:
        lines = [l.strip() for l in f.readlines()]
    # Expect header, version, count, then RGB lines
    rgb_lines = lines[3:3+16]
    palette = []
    for l in rgb_lines:
        if not l:
            palette.append((0,0,0))
            continue
        parts = l.split()
        r,g,b = map(int, parts[:3])
        palette.append((r,g,b))
    return palette

def make_palette_image(palette):
    # Create a 16-color palette image suitable for quantize()
    pal_img = Image.new('P', (16,16))
    flat = []
    for (r,g,b) in palette:
        flat.extend([r,g,b])
    # pad to 256*3
    flat += [0]* (256*3 - len(flat))
    pal_img.putpalette(flat)
    return pal_img

def remap_image(img_path, pal_img):
    im = Image.open(img_path).convert('RGBA')
    # Separate alpha and quantize RGB to palette
    rgb = Image.new('RGB', im.size, (255,255,255))
    rgb.paste(im, mask=im.split()[3])
    pal = rgb.quantize(palette=pal_img, dither=Image.FLOYDSTEINBERG)
    # Create RGBA result by applying original alpha to quantized image
    result = pal.convert('RGBA')
    result.putalpha(im.split()[3])
    result.save(img_path)
    print('Saved', img_path)

def main():
    palette = read_jasc_pal(PALETTE_PATH)
    pal_img = make_palette_image(palette)
    for f in FILES:
        remap_image(f, pal_img)

if __name__ == '__main__':
    main()

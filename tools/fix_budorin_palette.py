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

def find_nearest_palette_index(color, palette):
    r,g,b = color
    best_index = 0
    best_dist = float('inf')
    for i,(pr,pg,pb) in enumerate(palette):
        dr = pr - r
        dg = pg - g
        db = pb - b
        dist = dr*dr + dg*dg + db*db
        if dist < best_dist:
            best_dist = dist
            best_index = i
    return best_index

def remap_image(img_path, palette):
    im = Image.open(img_path).convert('RGBA')
    pixels = list(im.getdata())
    indices = []
    for pixel in pixels:
        r,g,b,a = pixel
        if a == 0:
            indices.append(0)
        else:
            indices.append(find_nearest_palette_index((r,g,b), palette))
    out = Image.new('P', im.size)
    flat = []
    for (r,g,b) in palette:
        flat.extend([r,g,b])
    flat += [0] * (256*3 - len(flat))
    out.putpalette(flat)
    out.putdata(indices)
    out.info['transparency'] = 0
    out.save(img_path, bits=4)
    print('Saved', img_path)

def main():
    palette = read_jasc_pal(PALETTE_PATH)
    for f in FILES:
        remap_image(f, palette)

if __name__ == '__main__':
    main()

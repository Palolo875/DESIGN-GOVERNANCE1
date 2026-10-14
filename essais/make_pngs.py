"""Régénère les PNG des pages de test (dégradés simples, sans dépendance). Usage : python3 -I make_pngs.py <dossier_essais>"""
import sys, zlib, struct
D = sys.argv[1]
def png(path, w, h, c1, c2):
    raw = bytearray()
    for y in range(h):
        raw.append(0); t = y / h
        for x in range(w):
            m = (x / w) * 0.6 + t * 0.4
            raw += bytes(int(c1[i] * (1 - m) + c2[i] * m) for i in range(3))
    def chunk(tag, data):
        c = struct.pack(">I", len(data)) + tag + data
        return c + struct.pack(">I", zlib.crc32(tag + data) & 0xffffffff)
    open(path, "wb").write(b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 2, 0, 0, 0)) + chunk(b"IDAT", zlib.compress(bytes(raw), 6)) + chunk(b"IEND", b""))
pal = [((30,60,90),(200,170,120)), ((40,80,60),(220,210,170)), ((90,40,40),(230,200,180)), ((50,50,70),(170,190,210))]
for i, (a, b) in enumerate(pal, 1):
    png(f"{D}/pages/clean/photo{i}.png", 1200, 800, a, b)
png(f"{D}/pages/flawed/photo1.png", 1200, 800, *pal[0])

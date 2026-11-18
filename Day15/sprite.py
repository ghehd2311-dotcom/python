# 원본 도트 캐릭터 (직접 디자인) + 타일 바닥 SVG 생성
팔레트 = {
    'o': '#1d1a24',  # 윤곽
    'h': '#b9c3d6',  # 투구
    'H': '#e8eefc',  # 투구 하이라이트
    'r': '#d83a3a',  # 깃털
    's': '#f1c9a0',  # 피부
    'e': '#1d1a24',  # 눈
    't': '#2f8f8a',  # 갑옷
    'T': '#206560',  # 갑옷 그림자
    'g': '#e8b93c',  # 금색
    'b': '#6a4527',  # 장화/벨트
    'k': '#8a93a6',  # 방패
    'K': '#5d6577',  # 방패 그림자
    'w': '#f4f7ff',  # 칼날
    'W': '#aab6d0',  # 칼날 그림자
    'p': '#8a5a2b',  # 손잡이
}

W_ = 20

def _row(lpad, text):
    return ('.' * lpad + text).ljust(W_, '.')

def _overlay(base, over):
    return ''.join(o if o != '.' else b for b, o in zip(base, over))

# 몸 (투구, 얼굴, 갑옷, 다리)
_몸 = [
    _row(8, "rr"),
    _row(7, "rrrr"),
    _row(5, "o" * 9),
    _row(5, "o" + "hhhhhHh" + "o"),
    _row(5, "o" + "hhhhhhh" + "o"),
    _row(5, "o" + "hhhhhhh" + "o"),
    _row(5, "o" + "sssssss" + "o"),
    _row(5, "o" + "sessses" + "o"),
    _row(5, "o" + "sssssss" + "o"),
    _row(6, "o" + "sssss" + "o"),
    _row(5, "oTtttttTo"),
    _row(5, "oTtttttTo"),
    _row(5, "oTtgggtTo"),
    _row(5, "oTtttttTo"),
    _row(5, "oTtttttTo"),
    _row(5, "obbbbbbbo"),
    _row(6, "oTtttTo"),
    _row(6, "ottotto"),
    _row(6, "ob.o.bo"),
    _row(6, "obb.obb" + "o"),
    _row(6, "ooo.ooo"),
    _row(0, ""),
]
# 방패 (왼쪽, y=11부터)
_방패 = {
    11: _row(0, ".ooooo"),
    12: _row(0, "okkkkko"),
    13: _row(0, "okKkkko"),
    14: _row(0, "okKkkko"),
    15: _row(1, "okkkko"),
    16: _row(2, "okKo"),
    17: _row(3, "oo"),
}
# 칼 (오른쪽) 칼날 y=3..11, 날밑 y=12, 손 y=13, 손잡이 y=14
_칼 = {}
for y in range(3, 12):
    _칼[y] = _row(16, "owWo")
_칼[2] = _row(16, "ooo")
_칼[12] = _row(15, "oggggo")
_칼[13] = _row(14, "ossso")
_칼[14] = _row(16, "opo")
_칼[15] = _row(16, "opo")
_칼[16] = _row(16, "ooo")

_lines = list(_몸)
for y, r in _방패.items():
    _lines[y] = _overlay(_lines[y], r)
for y, r in _칼.items():
    _lines[y] = _overlay(_lines[y], r)
몸 = [l[:W_] for l in _lines]

def 스프라이트_rects(grid, 칸=8, x0=0, y0=0):
    out = []
    for y, 줄 in enumerate(grid):
        x = 0
        while x < len(줄):
            c = 줄[x]
            if c == '.':
                x += 1
                continue
            j = x
            while j < len(줄) and 줄[j] == c:
                j += 1
            out.append(f'<rect x="{x0 + x*칸}" y="{y0 + y*칸}" width="{(j-x)*칸}" height="{칸}" fill="{팔레트[c]}"/>')
            x = j
    return "".join(out)

def 장면_svg(이름="용사", 레벨=1, 후광=0):
    W, H = 300, 300
    타일 = []
    # 아이소메트릭 바닥 (3x3 마름모)
    tw, th = 70, 36
    cx, cy = W // 2, 212
    색 = ["#8c8a93", "#7d7b85"]
    for i in range(-2, 3):
        for j in range(-2, 3):
            px = cx + (i - j) * tw / 2
            py = cy + (i + j) * th / 2
            c = 색[(i + j) % 2]
            타일.append(f'<polygon points="{px},{py-th/2} {px+tw/2},{py} {px},{py+th/2} {px-tw/2},{py}" fill="{c}" stroke="#5e5c66" stroke-width="1"/>')
    칸 = 8
    스프_w = len(몸[0]) * 칸
    스프_h = len(몸) * 칸
    sx = cx - 스프_w // 2
    sy = cy - 스프_h + 12
    그림자 = f'<ellipse cx="{cx}" cy="{cy+6}" rx="34" ry="10" fill="#000" opacity="0.28"/>'
    오라 = ""
    if 후광 > 0:
        오라 = f'<ellipse cx="{cx}" cy="{cy-60}" rx="{40+후광*4}" ry="{70+후광*4}" fill="#ffd466" opacity="{min(0.10+후광*0.03,0.4)}"/>'
    태그 = (f'<rect x="{cx-60}" y="8" width="120" height="26" rx="4" fill="#241810" stroke="#b8924a" stroke-width="2"/>'
            f'<text x="{cx}" y="26" text-anchor="middle" font-family="Georgia,serif" font-size="15" fill="#f0dfb0">{이름} Lv.{레벨}</text>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="100%" shape-rendering="crispEdges" style="max-width:340px">'
            f'<rect width="{W}" height="{H}" fill="#2a2420" rx="6"/>'
            + "".join(타일) + 그림자 + 오라 + 스프라이트_rects(몸, 칸, sx, sy) + 태그 + '</svg>')

if __name__ == "__main__":
    open("scene.svg", "w").write(장면_svg("용사", 1, 0))
    print("ok", len(몸), max(len(r) for r in 몸))
    assert all(len(r) == len(몸[0]) for r in 몸), [len(r) for r in 몸]

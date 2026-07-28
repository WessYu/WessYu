from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

PROJECTS = {
    "component-vault": ("Component Vault", ["Browse components", "Favorite + save", "Edit code", "Admin workspace"], "#6366F1"),
    "Conta": ("Conta", ["Login", "Track accounts", "Add income/expense", "Monthly limits"], "#16A34A"),
    "DEVMATCH": ("DevMatch", ["Discover profiles", "Check compatibility", "Create match", "Chat"], "#7C3AED"),
    "differenza-redesign": ("Differenza", ["Explore services", "Book appointment", "Admin dashboard", "Manage status"], "#C49A6C"),
    "HELENA": ("HELENA", ["Explore practice areas", "Request analysis", "Receive protocol", "Admin follow-up"], "#8B7355"),
    "imc": ("IMC Calculator", ["Enter weight", "Enter height", "Calculate BMI", "See classification"], "#2563EB"),
    "Liquid-Glass": ("Liquid Glass", ["Move pointer", "Drag card", "Glass refraction", "Animated canvas"], "#38BDF8"),
    "Logic-quest": ("Logic Quest", ["Choose module", "Solve lesson", "Checkpoint", "Earn XP"], "#22C55E"),
    "Nocturna-Atelier": ("Nocturna Atelier", ["Browse catalog", "Add to cart", "Checkout", "Order created"], "#A855F7"),
    "Receitas": ("Receitas", ["Discover recipes", "Filter ingredients", "Favorite", "Cook mode"], "#F97316"),
    "studyflow": ("StudyFlow", ["Create task", "Set priority", "Move column", "Persist progress"], "#6366F1"),
    "ToDo": ("Ritmo Habit Planner", ["Plan day", "Track habits", "Weekly review", "Journal"], "#06B6D4"),
    "todo-app-react": ("To-Do App", ["Add task", "Edit task", "Complete", "Filter list"], "#3B82F6"),
    "Travelgram": ("Travelgram", ["Profile header", "Travel gallery", "Responsive grid", "Mobile layout"], "#0EA5E9"),
    "Turismo": ("Turismo", ["Hero destination", "Explore places", "Read highlights", "Responsive layout"], "#14B8A6"),
    "vinicola-serra-dourada-main": ("Vinicola Serra Dourada", ["Browse wines", "Filter catalog", "Add to cart", "Schedule visit"], "#B45309"),
    "WessYu": ("WessYu", ["Featured projects", "Tech stack", "Portfolio links", "Contact"], "#D8CFC0"),
    "WESSYU-ARQUIVO": ("WESSYU Arquivo", ["Project reel", "Open case study", "Read decisions", "Visit project"], "#D8CFC0"),
}

OUT = Path("readme-assets")
OUT.mkdir(exist_ok=True)
FONT = ImageFont.load_default()


def rgb(hex_color: str):
    value = hex_color.lstrip("#")
    return tuple(int(value[index:index + 2], 16) for index in (0, 2, 4))


def wrap(text: str, limit: int):
    words = text.split()
    lines, line = [], ""
    for word in words:
        candidate = f"{line} {word}".strip()
        if len(candidate) > limit and line:
            lines.append(line)
            line = word
        else:
            line = candidate
    if line:
        lines.append(line)
    return lines


def generate_cover(slug: str, title: str, steps: list[str], accent: str):
    cards = []
    for index, step in enumerate(steps):
        x = 72 + index * 270
        cards.append(
            f'<rect x="{x}" y="310" width="230" height="118" rx="18" fill="#111522" stroke="#2B3142"/>'
            f'<text x="{x + 20}" y="344" fill="#7D8498" font-size="14" font-family="Arial">0{index + 1}</text>'
            f'<text x="{x + 20}" y="384" fill="#F6F7FB" font-size="18" font-family="Arial" font-weight="700">{step}</text>'
        )
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="520" viewBox="0 0 1200 520">
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#090B12"/><stop offset="1" stop-color="#111522"/></linearGradient><radialGradient id="r"><stop stop-color="{accent}" stop-opacity=".24"/><stop offset="1" stop-color="{accent}" stop-opacity="0"/></radialGradient></defs>
<rect width="1200" height="520" rx="28" fill="url(#g)"/><circle cx="1020" cy="80" r="280" fill="url(#r)"/>
<text x="72" y="92" fill="{accent}" font-size="18" font-family="Arial" font-weight="700" letter-spacing="3">WESSYU / PROJECT</text>
<text x="72" y="185" fill="#F6F7FB" font-size="64" font-family="Arial" font-weight="800">{title}</text>
<text x="72" y="236" fill="#9AA1B5" font-size="21" font-family="Arial">Interface, produto e desenvolvimento.</text>
{''.join(cards)}
<text x="72" y="482" fill="#5E667A" font-size="14" font-family="Arial">github.com/WessYu/{slug}</text>
</svg>'''
    (OUT / f"{slug}-cover.svg").write_text(svg, encoding="utf-8")


def generate_gif(slug: str, title: str, steps: list[str], accent: str):
    color = rgb(accent)
    frames = []
    width, height = 640, 330
    for frame_index in range(12):
        image = Image.new("RGB", (width, height), (8, 10, 16))
        draw = ImageDraw.Draw(image)
        draw.rounded_rectangle((16, 16, width - 16, height - 16), 18, fill=(14, 17, 26), outline=(50, 55, 70), width=1)
        draw.text((34, 32), title, fill="white", font=FONT)
        draw.text((34, 50), "FUNCTION FLOW", fill=(130, 137, 160), font=FONT)
        phase = min(3, frame_index // 3)
        gap, x0 = 12, 34
        card_width = (width - 68 - gap * 3) // 4
        for index, step in enumerate(steps):
            x = x0 + index * (card_width + gap)
            active = index <= phase
            draw.rounded_rectangle((x, 95, x + card_width, 235), 13, fill=(43, 48, 68) if active else (24, 28, 40), outline=(62, 68, 90))
            draw.text((x + 14, 110), f"0{index + 1}", fill=(150, 157, 180), font=FONT)
            for line_index, line in enumerate(wrap(step, 15)[:3]):
                draw.text((x + 14, 148 + line_index * 15), line, fill="white" if active else (135, 140, 160), font=FONT)
            if index == phase:
                radius = 4 + (frame_index % 3) * 2
                cx, cy = x + card_width - 20, 120
                draw.ellipse((cx - radius, cy - radius, cx + radius, cy + radius), fill=color)
        draw.rounded_rectangle((34, 267, width - 34, 273), 3, fill=(28, 32, 45))
        draw.rounded_rectangle((34, 267, 34 + int((width - 68) * (frame_index + 1) / 12), 273), 3, fill=color)
        draw.text((34, 289), steps[phase], fill=(188, 193, 208), font=FONT)
        frames.append(image)
    frames[0].save(OUT / f"{slug}-demo.gif", save_all=True, append_images=frames[1:], duration=210, loop=0, optimize=True)


for slug, (title, steps, accent) in PROJECTS.items():
    generate_cover(slug, title, steps, accent)
    generate_gif(slug, title, steps, accent)

print(f"Generated {len(PROJECTS)} covers and {len(PROJECTS)} GIFs in {OUT}")

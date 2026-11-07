"""
Script: Logo Generator for DataPulse AI
Student Assessment: Problem P10
Subject: Generative AI

Generates a bespoke, enterprise-grade vector SVG and PNG logo for DataPulse AI:
Visualizes a tabular matrix with a glowing neural heartbeat pulse wave.
"""

from pathlib import Path
import base64
from PIL import Image, ImageDraw, ImageFilter


def generate_svg_logo(size: int = 120) -> str:
    """Generates an enterprise-grade vector SVG logo for DataPulse AI."""
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="{size}" height="{size}">
  <defs>
    <!-- Background Gradient -->
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1E1B4B" />
      <stop offset="100%" stop-color="#0F172A" />
    </linearGradient>
    <!-- Border Gradient -->
    <linearGradient id="borderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#6366F1" />
      <stop offset="100%" stop-color="#38BDF8" />
    </linearGradient>
    <!-- Pulse Line Gradient -->
    <linearGradient id="pulseGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38BDF8" />
      <stop offset="50%" stop-color="#818CF8" />
      <stop offset="100%" stop-color="#EC4899" />
    </linearGradient>
    <!-- Bar Gradient -->
    <linearGradient id="barGrad" x1="0%" y1="100%" x2="0%" y2="0%">
      <stop offset="0%" stop-color="#312E81" />
      <stop offset="100%" stop-color="#4F46E5" />
    </linearGradient>
    <!-- Glow Filter -->
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2.5" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <!-- Base Rounded Container Shield -->
  <rect x="5" y="5" width="90" height="90" rx="22" fill="url(#bgGrad)" stroke="url(#borderGrad)" stroke-width="2.5" />

  <!-- Tabular Grid Background Gridlines (Subtle) -->
  <line x1="20" y1="36" x2="80" y2="36" stroke="#334155" stroke-width="1" stroke-dasharray="2,2" opacity="0.6" />
  <line x1="20" y1="52" x2="80" y2="52" stroke="#334155" stroke-width="1" stroke-dasharray="2,2" opacity="0.6" />
  <line x1="20" y1="68" x2="80" y2="68" stroke="#334155" stroke-width="1" stroke-dasharray="2,2" opacity="0.6" />

  <!-- Tabular Columns (3 Data Columns) -->
  <rect x="25" y="44" width="10" height="32" rx="4" fill="url(#barGrad)" opacity="0.85" />
  <rect x="45" y="28" width="10" height="48" rx="4" fill="url(#barGrad)" opacity="0.85" />
  <rect x="65" y="38" width="10" height="38" rx="4" fill="url(#barGrad)" opacity="0.85" />

  <!-- Data Pulse Heartbeat Line (High-Tech Electrocardiogram Path) -->
  <path d="M 16 56 L 32 56 L 40 38 L 48 70 L 56 22 L 64 62 L 72 56 L 84 56"
        fill="none"
        stroke="url(#pulseGrad)"
        stroke-width="3.5"
        stroke-linecap="round"
        stroke-linejoin="round"
        filter="url(#glow)" />

  <!-- Peak Intelligence Node (Glowing Spark Dot) -->
  <circle cx="56" cy="22" r="3.5" fill="#38BDF8" filter="url(#glow)" />
  <circle cx="56" cy="22" r="1.5" fill="#FFFFFF" />
</svg>"""
    return svg


def generate_png_logo(size: int = 512, out_path: Path = None) -> Path:
    """Generates a high-resolution raster PNG logo matching the SVG."""
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    scale = size / 100.0

    def s(val):
        return int(val * scale)

    # 1. Base Rounded Tile
    bg_box = [s(5), s(5), s(95), s(95)]
    radius = s(22)
    draw.rounded_rectangle(bg_box, radius=radius, fill=(15, 23, 42, 255), outline=(99, 102, 241, 255), width=s(2.5))

    # 2. Subtle Gridlines
    for y_pos in [s(36), s(52), s(68)]:
        draw.line([(s(20), y_pos), (s(80), y_pos)], fill=(51, 65, 85, 140), width=max(1, s(0.8)))

    # 3. Tabular Columns
    draw.rounded_rectangle([s(25), s(44), s(35), s(76)], radius=s(3), fill=(49, 46, 129, 230))
    draw.rounded_rectangle([s(45), s(28), s(55), s(76)], radius=s(3), fill=(67, 56, 202, 240))
    draw.rounded_rectangle([s(65), s(38), s(75), s(76)], radius=s(3), fill=(49, 46, 129, 230))

    # 4. Pulse Line Points
    pulse_pts = [
        (s(16), s(56)),
        (s(32), s(56)),
        (s(40), s(38)),
        (s(48), s(70)),
        (s(56), s(22)),
        (s(64), s(62)),
        (s(72), s(56)),
        (s(84), s(56))
    ]

    # Draw glow behind line
    draw.line(pulse_pts, fill=(56, 189, 248, 80), width=s(6), joint="round")
    # Draw primary line
    draw.line(pulse_pts, fill=(56, 189, 248, 255), width=s(3.5), joint="round")

    # 5. Glowing Intelligence Spark Peak
    spark_cx, spark_cy = s(56), s(22)
    r_outer = s(4.5)
    draw.ellipse([spark_cx - r_outer, spark_cy - r_outer, spark_cx + r_outer, spark_cy + r_outer], fill=(56, 189, 248, 160))
    r_inner = s(2)
    draw.ellipse([spark_cx - r_inner, spark_cy - r_inner, spark_cx + r_inner, spark_cy + r_inner], fill=(255, 255, 255, 255))

    if out_path:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        img.save(out_path, format="PNG")

    return out_path


if __name__ == "__main__":
    assets_dir = Path(__file__).resolve().parent.parent / "assets"
    
    # Save SVG
    svg_content = generate_svg_logo(120)
    with open(assets_dir / "logo.svg", "w", encoding="utf-8") as f:
        f.write(svg_content)
    
    # Save PNGs (High-res and Favicon)
    generate_png_logo(512, assets_dir / "logo.png")
    generate_png_logo(64, assets_dir / "favicon.png")
    print("Generated logo.svg, logo.png, and favicon.png successfully!")

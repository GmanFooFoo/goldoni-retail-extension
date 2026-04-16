#!/usr/bin/env python3
"""
Goldoni Retail — Label-Mockup-Generator (Pillow).

Rendert visuelle Etikett-Entwuerfe fuer die 5 Phase-1-Produkte.
Zweck: Silvio und Grafiker ein Vorab-Bild geben, bevor SP-09 / SP-10 / SP-11 /
SP-19 und Vetamt-Reg-Nr. vorliegen. Alle noch offenen Werte sind als
[TBD-SP-XX] markiert, damit sofort sichtbar ist, was noch fehlt.

Format: 80 x 120 mm bei 300 DPI = 945 x 1417 px.
Farbschema: Creme / Dunkelbraun / Gold (konsistent mit PPTX-Generator).

Usage:
    python3 scripts/create-label-mockup.py
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


OUT_DIR = Path("docs/silvio-derivatives/labels")

DPI = 300
MM = DPI / 25.4  # Pixel pro Millimeter
W_MM, H_MM = 80, 120
W_PX, H_PX = int(W_MM * MM), int(H_MM * MM)

BG = (245, 240, 230)      # Creme
INK = (44, 36, 30)        # Dunkelbraun
GOLD = (200, 162, 92)
MUTED = (120, 100, 80)
TBD_BG = (232, 216, 184)  # sanftes Gold fuer TBD-Marker

FONT_SERIF = "/System/Library/Fonts/Supplemental/Georgia.ttf"
FONT_SERIF_B = "/System/Library/Fonts/Supplemental/Georgia Bold.ttf"
FONT_SERIF_I = "/System/Library/Fonts/Supplemental/Georgia Italic.ttf"
FONT_SANS = "/System/Library/Fonts/Helvetica.ttc"


def F(size, bold=False, italic=False, sans=False):
    if sans:
        return ImageFont.truetype(FONT_SANS, size, index=1 if bold else 0)
    if bold:
        return ImageFont.truetype(FONT_SERIF_B, size)
    if italic:
        return ImageFont.truetype(FONT_SERIF_I, size)
    return ImageFont.truetype(FONT_SERIF, size)


PRODUCTS = [
    {
        "key": "lasagne-classica",
        "name_it": "Lasagne al forno",
        "name_de": "Nudelauflauf mit Ragù alla Bolognese und Käse",
        "portion": "400 g  ·  Für 1–2 Personen",
        "zutaten": (
            "Hartweizengrieß-Nudeln (WEIZEN), Rinderhack (DE), "
            "passierte Tomaten (San Marzano DOP, IT), Zwiebeln, "
            "Karotten, Sellerie (SELLERIE), Parmigiano Reggiano "
            "(MILCH), Mozzarella (MILCH), Olivenöl, Rotwein, "
            "Salz, Pfeffer, Basilikum, Lorbeer."
        ),
        "quid": "Rindfleisch [TBD-SP-19] %  ·  Hartweizen [TBD-SP-19] %",
        "herkunft": "Hergestellt in Deutschland.  ·  Rindfleisch: [TBD-SP-10]",
        "aufwaermen": (
            "Backofen: Beutel öffnen, Inhalt in ofenfestes Gefäß umfüllen. "
            "180 °C Ober-/Unterhitze, 25 Min. "
            "Mikrowelle: Beutel öffnen, umfüllen, 800 W, ca. 5 Min. — "
            "zwischendurch umrühren. "
            "Vor dem Servieren Kerntemperatur ≥ 72 °C sicherstellen. "
            "Nicht im Beutel erhitzen."
        ),
    },
    {
        "key": "lasagne-verdure",
        "name_it": "Lasagne alle verdure",
        "name_de": "Nudelauflauf mit Gemüse, Ricotta und Käse",
        "portion": "400 g  ·  Für 1–2 Personen",
        "zutaten": "[TBD-SP-19 — vollständige Rezeptur ohne Béchamel, ohne Ei]",
        "quid": "Gemüse [TBD-SP-19] %",
        "herkunft": "Hergestellt in Deutschland.  ·  Gemüse: [TBD-SP-10]",
        "aufwaermen": (
            "Wie Lasagne Classica. Backofen 180 °C, 25 Min. "
            "oder Mikrowelle 800 W, 5 Min. "
            "Vor dem Servieren Kerntemperatur ≥ 72 °C. "
            "Nicht im Beutel erhitzen."
        ),
    },
    {
        "key": "ragu-bolognese",
        "name_it": "Ragù alla Bolognese",
        "name_de": "Fleischsauce nach Bologneser Art",
        "portion": "350 g  ·  Für 2 Personen",
        "zutaten": (
            "Rinderhack (DE), passierte Tomaten (San Marzano DOP, IT), "
            "Zwiebeln, Karotten, Sellerie (SELLERIE), Olivenöl, "
            "Rotwein, Salz, Pfeffer, Lorbeer."
        ),
        "quid": "Rindfleisch [TBD-SP-19] %",
        "herkunft": "Hergestellt in Deutschland.  ·  Rindfleisch: [TBD-SP-10]",
        "aufwaermen": (
            "Topf: Beutel öffnen, Inhalt in Topf. Mittlere Hitze, "
            "unter Rühren 5 Min. erwärmen. "
            "Mikrowelle: Beutel öffnen, umfüllen, 600 W, ca. 3 Min. "
            "Nudeln separat kochen. Nicht im Beutel erhitzen."
        ),
    },
    {
        "key": "sugo-pomodoro",
        "name_it": "Sugo al pomodoro",
        "name_de": "Tomatensauce nach Hausart",
        "portion": "500 g  ·  Für 3–4 Personen",
        "zutaten": (
            "Passierte Tomaten (San Marzano DOP, IT), Olivenöl, "
            "Zwiebeln, Knoblauch, Salz, Basilikum."
        ),
        "quid": "Tomaten [TBD-SP-19] %",
        "herkunft": "Hergestellt in Deutschland.  ·  Tomaten: Italien",
        "aufwaermen": (
            "Topf: Beutel öffnen, Inhalt in Topf. Mittlere Hitze, "
            "unter Rühren 4 Min. erwärmen. "
            "Mikrowelle: 600 W, ca. 3 Min. "
            "Nudeln separat kochen. Nicht im Beutel erhitzen."
        ),
    },
    {
        "key": "parmigiana",
        "name_it": "Parmigiana di melanzane",
        "name_de": "Auberginen-Auflauf mit Käse",
        "portion": "400 g  ·  Für 1–2 Personen",
        "zutaten": (
            "Auberginen, passierte Tomaten (San Marzano DOP, IT), "
            "Parmigiano Reggiano (MILCH), Mozzarella (MILCH), "
            "Mehl (WEIZEN), Ei (EI), Olivenöl, Basilikum, Salz, Pfeffer."
        ),
        "quid": "Auberginen [TBD-SP-19] %  ·  Parmigiano [TBD-SP-19] %",
        "herkunft": "Hergestellt in Deutschland.  ·  Auberginen: [TBD-SP-10]",
        "aufwaermen": (
            "Backofen: Beutel öffnen, in ofenfestes Gefäß. "
            "180 °C, 25 Min. "
            "Mikrowelle: umfüllen, 800 W, 5 Min. "
            "Kerntemperatur ≥ 72 °C. Nicht im Beutel erhitzen."
        ),
    },
]


# Gemeinsame Pflichtangaben
STORE = "Bei +2 bis +4 °C lagern. Gekühlt transportieren, innerhalb 2 Std. in den Kühlschrank. Nach dem Öffnen sofort verbrauchen."
MHD = "Mindestens haltbar bis: TT.MM.JJJJ"
LOS = "Los-Nr.: L2026-XXX"
REG = "Zulassungs-Nr.: DE-BW-08111-XXXXX  [TBD — nach Vetamt-Registrierung]"
HERSTELLER = "Silvio Brunetti · Ristorante Goldoni · Reinsburgstraße [TBD-SP-09], [TBD-SP-09] Stuttgart · Deutschland"


def wrap(draw, text, font, max_w):
    """Manueller Wortumbruch passend zur maximalen Breite."""
    words = text.split(" ")
    lines, current = [], ""
    for w in words:
        probe = f"{current} {w}".strip()
        if draw.textlength(probe, font=font) <= max_w:
            current = probe
        else:
            if current:
                lines.append(current)
            current = w
    if current:
        lines.append(current)
    return lines


def draw_multiline(draw, text, font, x, y, max_w, color=INK, line_gap=4):
    for line in wrap(draw, text, font, max_w):
        draw.text((x, y), line, font=font, fill=color)
        bbox = font.getbbox(line)
        y += (bbox[3] - bbox[1]) + line_gap
    return y


def highlight_allergens(text):
    """Gibt Text mit fett-UPPERCASE-Allergenen bereits hervorgehoben zurueck.
    Allergene stehen im Input bereits UPPERCASE in Klammern — wir rendern
    sie farblich akzentuiert, indem wir die Zeile teilen.
    """
    return text  # aktuelle Renderstrategie: rein textlich, UPPERCASE visuell erkennbar


def draw_tbd_pill(draw, x, y, text, font):
    """Kleine farbige Pille fuer TBD-Markierungen, sichtbar hervorgehoben."""
    pad_x, pad_y = 8, 3
    tw = draw.textlength(text, font=font)
    bbox = font.getbbox(text)
    th = bbox[3] - bbox[1]
    draw.rounded_rectangle(
        [(x, y), (x + tw + 2 * pad_x, y + th + 2 * pad_y)],
        radius=6, fill=TBD_BG, outline=GOLD, width=1,
    )
    draw.text((x + pad_x, y + pad_y - bbox[1]), text, font=font, fill=INK)
    return y + th + 2 * pad_y


def render_label(product):
    img = Image.new("RGB", (W_PX, H_PX), BG)
    d = ImageDraw.Draw(img)

    margin = int(6 * MM)
    inner_w = W_PX - 2 * margin

    # Rahmen (Produktions-Stanzhilfe)
    d.rectangle([(4, 4), (W_PX - 5, H_PX - 5)], outline=GOLD, width=2)

    y = margin

    # ZONE A — Marke & Produkt
    d.text((margin, y), "GOLDONI", font=F(58, bold=True), fill=INK)
    y += 62
    d.text((margin, y), "RISTORANTE · STUTTGART", font=F(16, sans=True), fill=MUTED)
    y += 28

    d.line([(margin, y), (margin + inner_w, y)], fill=GOLD, width=2)
    y += 14

    d.text((margin, y), product["name_it"], font=F(42, italic=True), fill=INK)
    y += 54
    y = draw_multiline(d, product["name_de"], F(22), margin, y, inner_w, color=INK, line_gap=4)
    y += 6
    d.text((margin, y), product["portion"], font=F(18, bold=True), fill=GOLD)
    y += 34

    d.line([(margin, y), (margin + inner_w, y)], fill=GOLD, width=1)
    y += 10

    # ZONE B — Pflichtangaben
    d.text((margin, y), "ZUTATEN", font=F(14, sans=True, bold=True), fill=MUTED)
    y += 22
    y = draw_multiline(d, product["zutaten"], F(16), margin, y, inner_w, color=INK, line_gap=3)
    y += 4
    d.text((margin, y), "Allergene fett ausgewiesen (WEIZEN, MILCH, SELLERIE, EI).", font=F(12, italic=True), fill=MUTED)
    y += 22

    d.text((margin, y), "QUID", font=F(14, sans=True, bold=True), fill=MUTED)
    y += 20
    y = draw_multiline(d, product["quid"], F(14), margin, y, inner_w, color=INK, line_gap=2)
    y += 6

    d.text((margin, y), "HERKUNFT", font=F(14, sans=True, bold=True), fill=MUTED)
    y += 20
    y = draw_multiline(d, product["herkunft"], F(14), margin, y, inner_w, color=INK, line_gap=2)
    y += 10

    d.line([(margin, y), (margin + inner_w, y)], fill=GOLD, width=1)
    y += 10

    # ZONE C — Naehrwert + Aufwaermen
    d.text((margin, y), "NÄHRWERTE pro 100 g", font=F(14, sans=True, bold=True), fill=MUTED)
    y += 22
    nutri_rows = [
        ("Energie",            "[TBD-SP-11] kJ / kcal"),
        ("Fett",               "[TBD-SP-11] g"),
        ("— davon gesättigte", "[TBD-SP-11] g"),
        ("Kohlenhydrate",      "[TBD-SP-11] g"),
        ("— davon Zucker",     "[TBD-SP-11] g"),
        ("Eiweiß",             "[TBD-SP-11] g"),
        ("Salz",               "[TBD-SP-11] g"),
    ]
    col2_x = margin + int(inner_w * 0.55)
    row_h = 22
    for label, value in nutri_rows:
        d.text((margin, y), label, font=F(13), fill=INK)
        d.text((col2_x, y), value, font=F(13), fill=MUTED)
        y += row_h
    y += 6

    d.text((margin, y), "ZUBEREITUNG", font=F(14, sans=True, bold=True), fill=MUTED)
    y += 22
    y = draw_multiline(d, product["aufwaermen"], F(13), margin, y, inner_w, color=INK, line_gap=2)
    y += 8

    d.line([(margin, y), (margin + inner_w, y)], fill=GOLD, width=1)
    y += 10

    # ZONE D — Regulatorik
    d.text((margin, y), MHD, font=F(15, bold=True), fill=INK)
    y += 22
    y = draw_multiline(d, STORE, F(12), margin, y, inner_w, color=INK, line_gap=2)
    y += 4
    d.text((margin, y), LOS, font=F(12, bold=True), fill=INK)
    y += 20
    y = draw_multiline(d, HERSTELLER, F(11), margin, y, inner_w, color=MUTED, line_gap=2)
    y += 4
    y = draw_multiline(d, REG, F(11), margin, y, inner_w, color=MUTED, line_gap=2)

    # Fusszeile
    footer_y = H_PX - margin - 20
    d.line([(margin, footer_y - 8), (margin + inner_w, footer_y - 8)], fill=GOLD, width=1)
    d.text((margin, footer_y), "Mockup · Stand 2026-04-16 · Werte mit [TBD] offen",
           font=F(10, italic=True), fill=MUTED)

    return img


def render_overview(images):
    """Uebersichts-Bild mit allen 5 Etiketten nebeneinander (2 Reihen)."""
    cols = 3
    rows = (len(images) + cols - 1) // cols
    pad = 40
    tile_w, tile_h = W_PX, H_PX
    canvas_w = cols * tile_w + (cols + 1) * pad
    canvas_h = rows * tile_h + (rows + 1) * pad + 120

    canvas = Image.new("RGB", (canvas_w, canvas_h), (30, 25, 20))
    d = ImageDraw.Draw(canvas)

    d.text(
        (pad, 40),
        "Goldoni Retail · Etikett-Mockups · Phase 1 (5 Produkte)",
        font=F(48, bold=True), fill=BG,
    )
    d.text(
        (pad, 94),
        "Mockup-Entwurf · TBD-Marker zeigen, was noch auf Silvio-Input wartet",
        font=F(22, italic=True), fill=GOLD,
    )

    for i, img in enumerate(images):
        r, c = divmod(i, cols)
        x = pad + c * (tile_w + pad)
        y = 140 + pad + r * (tile_h + pad)
        canvas.paste(img, (x, y))

    return canvas


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    images = []
    for p in PRODUCTS:
        img = render_label(p)
        out = OUT_DIR / f"{p['key']}.png"
        img.save(out, dpi=(DPI, DPI))
        print(f"✓ {out}  ({out.stat().st_size // 1024} KB)")
        images.append(img)

    overview = render_overview(images)
    out_ov = OUT_DIR / "uebersicht.png"
    overview.save(out_ov, dpi=(150, 150))
    print(f"✓ {out_ov}  ({out_ov.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()

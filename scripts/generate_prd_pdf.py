from pathlib import Path
import html
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    KeepTogether,
    ListFlowable,
    ListItem,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(r"C:\Users\Faizan J")
PROJECT = ROOT / "Desktop" / "AIvoicebuilder"
SOURCE = ROOT / "WOW-voice-agent-PRD.md"
OUTPUT = PROJECT / "docs" / "WOW-voice-agent-PRD.pdf"


def register_fonts():
    regular = Path(r"C:\Windows\Fonts\arial.ttf")
    bold = Path(r"C:\Windows\Fonts\arialbd.ttf")
    italic = Path(r"C:\Windows\Fonts\ariali.ttf")
    bold_italic = Path(r"C:\Windows\Fonts\arialbi.ttf")
    for path in (regular, bold, italic, bold_italic):
        if not path.exists():
            raise FileNotFoundError(f"Required font not found: {path}")
    pdfmetrics.registerFont(TTFont("Arial", str(regular)))
    pdfmetrics.registerFont(TTFont("Arial-Bold", str(bold)))
    pdfmetrics.registerFont(TTFont("Arial-Italic", str(italic)))
    pdfmetrics.registerFont(TTFont("Arial-BoldItalic", str(bold_italic)))


def plain_text(value: str) -> str:
    # Keep the rupee symbol but normalize typography to PDF-safe ASCII punctuation.
    replacements = {
        "\u2013": "-",
        "\u2014": "-",
        "\u2011": "-",
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\u00a0": " ",
    }
    for old, new in replacements.items():
        value = value.replace(old, new)
    return value


def inline_markup(value: str) -> str:
    value = plain_text(value)
    value = html.escape(value, quote=False)
    value = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", value)
    value = re.sub(r"`([^`]+)`", r"<font name='Courier'>\1</font>", value)
    return value


def make_styles():
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="CoverTitle",
            parent=styles["Title"],
            fontName="Arial-Bold",
            fontSize=27,
            leading=32,
            textColor=colors.HexColor("#173B45"),
            alignment=TA_CENTER,
            spaceAfter=8,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CoverSubtitle",
            parent=styles["Normal"],
            fontName="Arial",
            fontSize=13,
            leading=18,
            textColor=colors.HexColor("#47636A"),
            alignment=TA_CENTER,
            spaceAfter=16,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CoverMeta",
            parent=styles["Normal"],
            fontName="Arial",
            fontSize=10.5,
            leading=16,
            textColor=colors.HexColor("#24373C"),
            alignment=TA_CENTER,
        )
    )
    styles.add(
        ParagraphStyle(
            name="H2Custom",
            parent=styles["Heading2"],
            fontName="Arial-Bold",
            fontSize=17,
            leading=21,
            textColor=colors.HexColor("#173B45"),
            spaceBefore=14,
            spaceAfter=7,
            keepWithNext=True,
        )
    )
    styles.add(
        ParagraphStyle(
            name="H3Custom",
            parent=styles["Heading3"],
            fontName="Arial-Bold",
            fontSize=12.5,
            leading=16,
            textColor=colors.HexColor("#2A626B"),
            spaceBefore=9,
            spaceAfter=4,
            keepWithNext=True,
        )
    )
    styles.add(
        ParagraphStyle(
            name="BodyCustom",
            parent=styles["BodyText"],
            fontName="Arial",
            fontSize=9.4,
            leading=13.2,
            textColor=colors.HexColor("#24373C"),
            spaceAfter=5,
        )
    )
    styles.add(
        ParagraphStyle(
            name="BulletCustom",
            parent=styles["BodyText"],
            fontName="Arial",
            fontSize=9.2,
            leading=12.7,
            leftIndent=14,
            firstLineIndent=-7,
            bulletIndent=0,
            textColor=colors.HexColor("#24373C"),
            spaceAfter=2,
        )
    )
    styles.add(
        ParagraphStyle(
            name="QuoteCustom",
            parent=styles["BodyText"],
            fontName="Arial-Italic",
            fontSize=9.5,
            leading=13.5,
            leftIndent=13,
            rightIndent=13,
            borderColor=colors.HexColor("#B9D8D4"),
            borderWidth=1,
            borderPadding=8,
            backColor=colors.HexColor("#F2F8F7"),
            textColor=colors.HexColor("#29474B"),
            spaceBefore=4,
            spaceAfter=8,
        )
    )
    styles.add(
        ParagraphStyle(
            name="SmallCustom",
            parent=styles["BodyText"],
            fontName="Arial",
            fontSize=8,
            leading=10,
            textColor=colors.HexColor("#5D7378"),
        )
    )
    return styles


def parse_table(lines, start):
    rows = []
    index = start
    while index < len(lines) and lines[index].strip().startswith("|"):
        raw = lines[index].strip().strip("|")
        cells = [cell.strip() for cell in raw.split("|")]
        if not all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
            rows.append(cells)
        index += 1
    return rows, index


def build_story(styles):
    lines = SOURCE.read_text(encoding="utf-8").splitlines()
    story = []

    # Cover page.
    story.append(Spacer(1, 30 * mm))
    story.append(Paragraph("Whispers of the Wind", styles["CoverTitle"]))
    story.append(Paragraph("Outbound AI Voice Agent - Product Requirements Document", styles["CoverSubtitle"]))
    story.append(Spacer(1, 14 * mm))
    cover_box = [
        [Paragraph("Developer", styles["SmallCustom"]), Paragraph("Divyasree Developers", styles["BodyCustom"])],
        [Paragraph("Product", styles["SmallCustom"]), Paragraph("Premium Private Valley villa plots", styles["BodyCustom"])],
        [Paragraph("Location", styles["SmallCustom"]), Paragraph("Nandi Valley near Nandi Hills, North Bengaluru", styles["BodyCustom"])],
        [Paragraph("Agent objective", styles["SmallCustom"]), Paragraph("Qualify high-value leads in a respectful 2-3 minute call and request a Property Expert follow-up", styles["BodyCustom"])],
    ]
    box = Table(cover_box, colWidths=[38 * mm, 112 * mm], hAlign="CENTER")
    box.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F2F8F7")),
                ("BOX", (0, 0), (-1, -1), 0.8, colors.HexColor("#B9D8D4")),
                ("INNERGRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#D2E6E3")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 7),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
            ]
        )
    )
    story.append(box)
    story.append(Spacer(1, 20 * mm))
    story.append(Paragraph("Prepared for AIvoicebuilder", styles["CoverMeta"]))
    story.append(Paragraph("August 2026", styles["CoverMeta"]))
    story.append(PageBreak())

    # Markdown body.
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        stripped = line.strip()
        if not stripped or stripped == "# Product Requirements Document":
            i += 1
            continue

        if stripped.startswith("|") and i + 1 < len(lines) and lines[i + 1].strip().startswith("|"):
            table_rows, next_index = parse_table(lines, i)
            if table_rows:
                table_data = [[Paragraph(inline_markup(c), styles["BodyCustom"]) for c in row] for row in table_rows]
                col_count = max(len(row) for row in table_data)
                widths = [58 * mm, 88 * mm] if col_count == 2 else [146 * mm / col_count] * col_count
                table = Table(table_data, colWidths=widths, repeatRows=1, hAlign="LEFT")
                table.setStyle(
                    TableStyle(
                        [
                            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#173B45")),
                            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                            ("FONTNAME", (0, 0), (-1, 0), "Arial-Bold"),
                            ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#B9D8D4")),
                            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F2F8F7")]),
                            ("VALIGN", (0, 0), (-1, -1), "TOP"),
                            ("LEFTPADDING", (0, 0), (-1, -1), 6),
                            ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                            ("TOPPADDING", (0, 0), (-1, -1), 5),
                            ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                        ]
                    )
                )
                story.extend([Spacer(1, 3), table, Spacer(1, 7)])
            i = next_index
            continue

        heading = re.match(r"^(#{2,3})\s+(.*)$", stripped)
        if heading:
            style = styles["H2Custom"] if len(heading.group(1)) == 2 else styles["H3Custom"]
            story.append(Paragraph(inline_markup(heading.group(2)), style))
            i += 1
            continue

        if stripped.startswith("> "):
            story.append(Paragraph(inline_markup(stripped[2:]), styles["QuoteCustom"]))
            i += 1
            continue

        if stripped.startswith("- "):
            items = []
            while i < len(lines) and lines[i].strip().startswith("- "):
                item_text = lines[i].strip()[2:]
                items.append(ListItem(Paragraph(inline_markup(item_text), styles["BodyCustom"]), leftIndent=6))
                i += 1
            story.append(ListFlowable(items, bulletType="bullet", start="circle", leftIndent=11, bulletFontName="Arial", bulletFontSize=6, bulletColor=colors.HexColor("#2A626B")))
            story.append(Spacer(1, 2))
            continue

        # Plain paragraph; join consecutive non-structural lines.
        paragraph_lines = [stripped]
        i += 1
        while i < len(lines):
            nxt = lines[i].strip()
            if not nxt or nxt.startswith(("#", "- ", "> ", "|")):
                break
            paragraph_lines.append(nxt)
            i += 1
        story.append(Paragraph(inline_markup(" ".join(paragraph_lines)), styles["BodyCustom"]))

    return story


def draw_page(canvas, doc):
    canvas.saveState()
    width, height = A4
    if doc.page > 1:
        canvas.setStrokeColor(colors.HexColor("#D2E6E3"))
        canvas.setLineWidth(0.5)
        canvas.line(18 * mm, height - 15 * mm, width - 18 * mm, height - 15 * mm)
        canvas.setFont("Arial-Bold", 8)
        canvas.setFillColor(colors.HexColor("#2A626B"))
        canvas.drawString(18 * mm, height - 11 * mm, "WHISPERS OF THE WIND")
        canvas.setFont("Arial", 8)
        canvas.setFillColor(colors.HexColor("#5D7378"))
        canvas.drawRightString(width - 18 * mm, height - 11 * mm, "Product Requirements Document")
    canvas.setStrokeColor(colors.HexColor("#D2E6E3"))
    canvas.setLineWidth(0.5)
    canvas.line(18 * mm, 14 * mm, width - 18 * mm, 14 * mm)
    canvas.setFont("Arial", 8)
    canvas.setFillColor(colors.HexColor("#5D7378"))
    canvas.drawString(18 * mm, 9 * mm, "Divyasree Developers | AIvoicebuilder")
    canvas.drawRightString(width - 18 * mm, 9 * mm, f"Page {doc.page}")
    canvas.restoreState()


def main():
    register_fonts()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    doc = BaseDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        leftMargin=18 * mm,
        rightMargin=18 * mm,
        topMargin=23 * mm,
        bottomMargin=20 * mm,
        title="Whispers of the Wind - AI Voice Agent PRD",
        author="AIvoicebuilder",
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="normal")
    doc.addPageTemplates([PageTemplate(id="main", frames=[frame], onPage=draw_page)])
    doc.build(build_story(make_styles()))
    print(OUTPUT)


if __name__ == "__main__":
    main()


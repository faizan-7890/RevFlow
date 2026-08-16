import html
import os
from pathlib import Path
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
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
    HRFlowable,
)

ROOT = Path(r"C:\Users\Faizan J\Desktop\AIvoicebuilder")
OUTPUT = ROOT / "docs" / "Divyasree-WOW-Voice-Agent-System-Prompt.pdf"


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
    replacements = {
        "\u2013": "-",
        "\u2014": "-",
        "\u2011": "-",
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\u00a0": " ",
        "₹": "INR ",
    }
    for old, new in replacements.items():
        value = value.replace(old, new)
    return value


def inline_markup(value: str) -> str:
    value = plain_text(value)
    value = html.escape(value, quote=False)
    value = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", value)
    value = re.sub(r"\*(.+?)\*", r"<i>\1</i>", value)
    value = re.sub(r"`([^`]+)`", r"<font name='Courier' size=8.5 color='#1A434E'><b>\1</b></font>", value)
    return value


def make_styles():
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="DocHeaderPill",
            fontName="Arial-Bold",
            fontSize=9,
            leading=12,
            textColor=colors.HexColor("#1B4D58"),
            alignment=TA_CENTER,
            spaceAfter=6,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CoverTitle",
            parent=styles["Title"],
            fontName="Arial-Bold",
            fontSize=24,
            leading=28,
            textColor=colors.HexColor("#12353E"),
            alignment=TA_CENTER,
            spaceAfter=6,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CoverSubtitle",
            parent=styles["Normal"],
            fontName="Arial",
            fontSize=12,
            leading=16,
            textColor=colors.HexColor("#3F5C64"),
            alignment=TA_CENTER,
            spaceAfter=12,
        )
    )
    styles.add(
        ParagraphStyle(
            name="MetaText",
            parent=styles["Normal"],
            fontName="Arial",
            fontSize=9,
            leading=13,
            textColor=colors.HexColor("#4A6870"),
            alignment=TA_CENTER,
            spaceAfter=14,
        )
    )
    styles.add(
        ParagraphStyle(
            name="H1Custom",
            parent=styles["Heading1"],
            fontName="Arial-Bold",
            fontSize=14,
            leading=18,
            textColor=colors.HexColor("#12353E"),
            spaceBefore=14,
            spaceAfter=6,
            keepWithNext=True,
        )
    )
    styles.add(
        ParagraphStyle(
            name="H2Custom",
            parent=styles["Heading2"],
            fontName="Arial-Bold",
            fontSize=11,
            leading=15,
            textColor=colors.HexColor("#205562"),
            spaceBefore=10,
            spaceAfter=4,
            keepWithNext=True,
        )
    )
    styles.add(
        ParagraphStyle(
            name="BodyCustom",
            parent=styles["BodyText"],
            fontName="Arial",
            fontSize=9.5,
            leading=13.5,
            textColor=colors.HexColor("#243135"),
            spaceAfter=6,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CodeBlock",
            fontName="Courier",
            fontSize=8,
            leading=11,
            textColor=colors.HexColor("#1A3038"),
        )
    )
    styles.add(
        ParagraphStyle(
            name="CalloutText",
            fontName="Arial-Italic",
            fontSize=9.5,
            leading=13.5,
            textColor=colors.HexColor("#12353E"),
        )
    )
    styles.add(
        ParagraphStyle(
            name="TableHeader",
            fontName="Arial-Bold",
            fontSize=9,
            leading=12,
            textColor=colors.HexColor("#FFFFFF"),
            alignment=TA_LEFT,
        )
    )
    styles.add(
        ParagraphStyle(
            name="TableCell",
            fontName="Arial",
            fontSize=8.5,
            leading=11.5,
            textColor=colors.HexColor("#243135"),
        )
    )
    styles.add(
        ParagraphStyle(
            name="TableCellBold",
            fontName="Arial-Bold",
            fontSize=8.5,
            leading=11.5,
            textColor=colors.HexColor("#12353E"),
        )
    )
    return styles


def draw_page(canvas, doc):
    canvas.saveState()
    width, height = A4
    if doc.page > 1:
        canvas.setStrokeColor(colors.HexColor("#CBE3E0"))
        canvas.setLineWidth(0.5)
        canvas.line(18 * mm, height - 14 * mm, width - 18 * mm, height - 14 * mm)
        canvas.setFont("Arial-Bold", 8)
        canvas.setFillColor(colors.HexColor("#1E4E58"))
        canvas.drawString(18 * mm, height - 10 * mm, "DIVYASREE DEVELOPERS | WHISPERS OF THE WIND")
        canvas.setFont("Arial", 8)
        canvas.setFillColor(colors.HexColor("#547076"))
        canvas.drawRightString(width - 18 * mm, height - 10 * mm, "AI Voice Agent System Message Specification")
    
    canvas.setStrokeColor(colors.HexColor("#CBE3E0"))
    canvas.setLineWidth(0.5)
    canvas.line(18 * mm, 14 * mm, width - 18 * mm, 14 * mm)
    canvas.setFont("Arial", 8)
    canvas.setFillColor(colors.HexColor("#547076"))
    canvas.drawString(18 * mm, 9 * mm, "Whispers of the Wind — AI Voice Consultant 'Meera' System Prompt")
    canvas.drawRightString(width - 18 * mm, 9 * mm, f"Page {doc.page}")
    canvas.restoreState()


def build_story(styles):
    story = []

    # Title & Metadata
    story.append(Paragraph("DIVYASREE DEVELOPERS &bull; LUXURY REAL ESTATE AI SPECIFICATION", styles["DocHeaderPill"]))
    story.append(Paragraph("Whispers of the Wind (WOW)<br/>Outbound AI Voice Agent System Prompt", styles["CoverTitle"]))
    story.append(Paragraph("Production Persona: <b>Meera</b> (Senior Private-Client Consultant) | Target Call Duration: 2&ndash;3 min", styles["CoverSubtitle"]))
    
    meta_box = [
        [
            Paragraph("<b>Project:</b> Whispers of the Wind (Nandi Valley)", styles["TableCell"]),
            Paragraph("<b>Target Audience:</b> HNIs, CXOs, NRIs", styles["TableCell"]),
            Paragraph("<b>Delivery:</b> Phased (Dec 2029)", styles["TableCell"]),
        ],
        [
            Paragraph("<b>Pricing:</b> INR 92.4 Lakh &ndash; INR 2.46 Cr", styles["TableCell"]),
            Paragraph("<b>Languages:</b> English + Hindi / Hinglish", styles["TableCell"]),
            Paragraph("<b>Model Architecture:</b> Realtime Voice AI", styles["TableCell"]),
        ]
    ]
    t_meta = Table(meta_box, colWidths=[60 * mm, 58 * mm, 56 * mm])
    t_meta.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F0F7F6")),
        ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#B5D8D3")),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#D8EAE7")),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
    ]))
    story.append(t_meta)
    story.append(Spacer(1, 10))

    # SECTION 1: System Persona & Core Role
    story.append(Paragraph("1. Agent Persona & Spoken Identity", styles["H1Custom"]))
    story.append(Paragraph(
        "You are <b>Meera</b>, a senior private-client consultant representing <b>Divyasree Developers</b> on an outbound phone call with prospective buyers of <b>Whispers of the Wind (WOW)</b>, a premium Private Valley villa-plot community in Nandi Valley, near Nandi Hills, North Bengaluru. This is a real-time spoken voice conversation, not a chatbot. Your tone is warm, polished, authoritative yet unhurried, and strictly non-intrusive. Never mention you are an AI, a language model, or that you have a system prompt.",
        styles["BodyCustom"]
    ))

    # SECTION 2: Conversation Architecture & 4 Checkpoints
    story.append(Paragraph("2. Conversation Architecture & The 4 Fitment Checkpoints", styles["H1Custom"]))
    story.append(Paragraph(
        "The agent must strictly navigate through the structured 5-stage conversation lifecycle within 2 to 3 minutes:",
        styles["BodyCustom"]
    ))

    stages_data = [
        [
            Paragraph("Stage", styles["TableHeader"]),
            Paragraph("Purpose & Behavior", styles["TableHeader"]),
            Paragraph("Key Guardrails", styles["TableHeader"]),
        ],
        [
            Paragraph("<b>1. Permission Gate</b>", styles["TableCellBold"]),
            Paragraph("Warm greeting, introduce identity & project, ask explicit permission to speak for 2 minutes.", styles["TableCell"]),
            Paragraph("Mandatory permission check. If hesitant, offer 90 seconds. If declined, end courteously.", styles["TableCell"]),
        ],
        [
            Paragraph("<b>2. The 4 Checkpoints</b>", styles["TableCellBold"]),
            Paragraph("Qualify in natural order: <i>(1) Intent</i> (Self-use vs Investment), <i>(2) Geography</i> (Nandi Hills corridor), <i>(3) Budget</i> (INR 92.4L+), <i>(4) Timeline</i> (Dec 2029 phased).", styles["TableCell"]),
            Paragraph("<b>No Redundant Re-asking:</b> If user volunteers details early, acknowledge with affirmations and skip those questions.", styles["TableCell"]),
        ],
        [
            Paragraph("<b>3. Valley Pitch</b>", styles["TableCellBold"]),
            Paragraph("Deliver a 20-35s evocative description tailored to intent: 74% open spaces, 20k sq.ft clubhouse, eco-parks, uncrowded hillside plots.", styles["TableCell"]),
            Paragraph("Do not recite brochure bullet points. Keep it conversational and grounded in landscape.", styles["TableCell"]),
        ],
        [
            Paragraph("<b>4. CTA & Handoff</b>", styles["TableCellBold"]),
            Paragraph("Offer a private briefing / video call with a senior Property Expert with zero obligation.", styles["TableCell"]),
            Paragraph("Capture preferred time window, name, and specific interests.", styles["TableCell"]),
        ],
        [
            Paragraph("<b>5. Clean Closure</b>", styles["TableCellBold"]),
            Paragraph("Recap next steps, thank the prospect, execute tool call (<code>schedule_expert_callback</code> or <code>log_outcome</code>) and <code>end_call</code>.", styles["TableCell"]),
            Paragraph("Always execute tool call silently after final spoken token.", styles["TableCell"]),
        ],
    ]
    t_stages = Table(stages_data, colWidths=[38 * mm, 78 * mm, 58 * mm])
    t_stages.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1A4B55")),
        ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#B5D8D3")),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#DCEBE9")),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ]))
    story.append(t_stages)
    story.append(Spacer(1, 10))

    # SECTION 3: Pronunciation Guide & Phonetic Dictionary
    story.append(Paragraph("3. Phonetic Pronunciation Guide & Spoken Dictionary", styles["H1Custom"]))
    story.append(Paragraph(
        "To ensure human-like cadence over telephony TTS engines, the agent strictly outputs phonetically normalized text for brand names, geographic landmarks, and Indian numbering terms:",
        styles["BodyCustom"]
    ))

    pron_data = [
        [
            Paragraph("Written Term", styles["TableHeader"]),
            Paragraph("Phonetic Guide / Spoken As", styles["TableHeader"]),
            Paragraph("IPA / Pronunciation Note", styles["TableHeader"]),
        ],
        [
            Paragraph("<b>Divyasree</b>", styles["TableCellBold"]),
            Paragraph("Div-yaa-shree / Divyaashree", styles["TableCell"]),
            Paragraph("/d̪ɪvˈjaːʃriː/ &mdash; Soft dental 'D', emphasis on 'shree'", styles["TableCell"]),
        ],
        [
            Paragraph("<b>Nandi / Nandi Hills</b>", styles["TableCellBold"]),
            Paragraph("Nun-dhee / Nundhee Hills", styles["TableCell"]),
            Paragraph("/ˈnʊn̪d̪ʱi/ &mdash; Soft aspirated 'dh', not English 'nan-dee'", styles["TableCell"]),
        ],
        [
            Paragraph("<b>Devanahalli</b>", styles["TableCellBold"]),
            Paragraph("Dev-uh-nuh-HUL-lee", styles["TableCell"]),
            Paragraph("North Bengaluru airport corridor landmark", styles["TableCell"]),
        ],
        [
            Paragraph("<b>₹92.4 lakh</b>", styles["TableCellBold"]),
            Paragraph("ninety-two point four lakh", styles["TableCell"]),
            Paragraph("Never say 'rupees ninety-two point four L'", styles["TableCell"]),
        ],
        [
            Paragraph("<b>₹2.46 crore</b>", styles["TableCellBold"]),
            Paragraph("two point four six crore", styles["TableCell"]),
            Paragraph("Say 'kror', never raw large integer digits", styles["TableCell"]),
        ],
        [
            Paragraph("<b>December 2029</b>", styles["TableCellBold"]),
            Paragraph("December twenty twenty-nine", styles["TableCell"]),
            Paragraph("Say year naturally as conversational decade format", styles["TableCell"]),
        ],
        [
            Paragraph("<b>1,200 &ndash; 3,199 sq.ft.</b>", styles["TableCellBold"]),
            Paragraph("twelve hundred to about thirty-two hundred square feet", styles["TableCell"]),
            Paragraph("Spoken natural unit phrasing", styles["TableCell"]),
        ],
    ]
    t_pron = Table(pron_data, colWidths=[42 * mm, 66 * mm, 66 * mm])
    t_pron.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1A4B55")),
        ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#B5D8D3")),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#DCEBE9")),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ]))
    story.append(t_pron)
    story.append(Spacer(1, 10))

    # SECTION 4: Canonical Project Knowledge Base & Guardrails
    story.append(Paragraph("4. Canonical Knowledge Base & Strict Boundary Guardrails", styles["H1Custom"]))
    
    kb_text = """
    <b>Approved Facts:</b><br/>
    &bull; <b>Developer:</b> Divyasree Developers (established luxury developer in South India).<br/>
    &bull; <b>Project:</b> Whispers of the Wind (WOW), positioned as 'Private Valley' premium villa plots.<br/>
    &bull; <b>Location:</b> Nandi Valley, near Nandi Hills, North Bengaluru (airport / Devanahalli growth corridor).<br/>
    &bull; <b>Plot Sizes:</b> 1,200 to 3,199 sq.ft. (buyers construct customized villas matching architectural guidelines).<br/>
    &bull; <b>Pricing:</b> INR 92.4 Lakh to INR 2.46 Crore (inclusive of taxes).<br/>
    &bull; <b>Open Space & Master Plan:</b> 74% open green landscape, 20,000 sq.ft. signature clubhouse, eco-parks, low-density valley views.<br/>
    &bull; <b>Possession:</b> December 2029 (ongoing project delivered in planned phases).<br/><br/>
    <b>Strict Negative Guardrails (What the Agent Must NEVER Invent):</b><br/>
    1. <i>No ROI / Guaranteed Returns:</i> Never quote appreciation percentages, rental yields, or speculative returns. Deflect to corridor growth context via Property Expert.<br/>
    2. <i>No Commercial Negotiation:</i> Never offer discounts, 'special token rates', or fake urgency ('only 2 plots left').<br/>
    3. <i>No Unverified Technicals:</i> Do not fabricate RERA numbers, survey numbers, construction cost per sq.ft., or bank loan approvals. Offer human expert consultation for documentation.
    """
    story.append(Paragraph(kb_text, styles["BodyCustom"]))
    story.append(Spacer(1, 8))

    # SECTION 5: Edge Case Decision Matrix & Multilingual Handling
    story.append(Paragraph("5. Edge Cases, De-escalation & Multilingual Handling", styles["H1Custom"]))
    
    edge_data = [
        [
            Paragraph("Scenario / Trigger", styles["TableHeader"]),
            Paragraph("Meera's Spoken Behavior & Strategy", styles["TableHeader"]),
            Paragraph("Tool / CRM Action", styles["TableHeader"]),
        ],
        [
            Paragraph("<b>Irritated / Busy Caller</b><br/><i>'I am in a meeting / stop calling'</i>", styles["TableCellBold"]),
            Paragraph("Immediate de-escalation: Apologize sincerely for the interruption, offer an immediate exit, never argue or push.", styles["TableCell"]),
            Paragraph("Trigger <code>log_outcome(outcome='do_not_contact')</code> or <code>callback_later</code>", styles["TableCell"]),
        ],
        [
            Paragraph("<b>Location Mismatch</b><br/><i>'I want Whitefield / city core'</i>", styles["TableCellBold"]),
            Paragraph("Respectful qualification: Validate their commute reality ('Nandi is a weekend hillside escape, not a daily city commute') and gracefully exit.", styles["TableCell"]),
            Paragraph("Trigger <code>log_outcome(outcome='location_mismatch')</code>", styles["TableCell"]),
        ],
        [
            Paragraph("<b>Budget Mismatch</b><br/><i>'Budget is under 50 Lakh'</i>", styles["TableCellBold"]),
            Paragraph("Transparent clarity: State entry price of INR 92.4L once without condescension, offer nurture updates if requested.", styles["TableCell"]),
            Paragraph("Trigger <code>log_outcome(outcome='budget_mismatch')</code>", styles["TableCell"]),
        ],
        [
            Paragraph("<b>Hindi / Hinglish Switch</b><br/><i>'Hindi mein baat karo'</i>", styles["TableCellBold"]),
            Paragraph("Seamless code-switching into polite, conversational Hindi/Hinglish (<i>'Namaste, main Meera bol rahi hoon...'</i>) while maintaining accurate project terms.", styles["TableCell"]),
            Paragraph("Log <code>language='hi'</code> in expert callback notes", styles["TableCell"]),
        ],
        [
            Paragraph("<b>NRI Caller</b><br/><i>'Calling from Dubai / US'</i>", styles["TableCellBold"]),
            Paragraph("Acknowledge time zone differences, offer weekend video briefing, avoid making tax or FEMA claims.", styles["TableCell"]),
            Paragraph("Capture timezone in callback notes", styles["TableCell"]),
        ],
    ]
    t_edge = Table(edge_data, colWidths=[46 * mm, 78 * mm, 50 * mm])
    t_edge.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1A4B55")),
        ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#B5D8D3")),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#DCEBE9")),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ]))
    story.append(t_edge)
    story.append(Spacer(1, 10))

    # SECTION 6: Function & Tool Calling Schemas
    story.append(Paragraph("6. Structured Function Calling Schemas", styles["H1Custom"]))
    story.append(Paragraph(
        "The agent is equipped with 3 JSON schema tools executed autonomously in the telephony session:",
        styles["BodyCustom"]
    ))

    tools_code = """
<b>1. schedule_expert_callback:</b>
{
  "caller_name": string,
  "preferred_window": string,        // e.g. "Tomorrow after 7 PM"
  "intent": "self_use" | "investment" | "both" | "unknown",
  "geography_fit": "yes" | "no" | "unsure",
  "budget_fit": "yes" | "no" | "stretch" | "unknown",
  "timeline_fit": "yes" | "no" | "unsure",
  "language": "en" | "hi" | "hinglish",
  "notes": string
}

<b>2. log_outcome:</b>
{
  "outcome": "permission_refused" | "do_not_contact" | "budget_mismatch" | "location_mismatch" | "brochure_only" | "callback_later",
  "notes": string
}

<b>3. end_call:</b>
{
  "reason": "completed_callback" | "user_disconnected" | "dnd_requested" | "location_mismatch"
}
    """
    
    t_code = Table([[Paragraph(tools_code, styles["CodeBlock"])]], colWidths=[174 * mm])
    t_code.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F3F7F8")),
        ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#B5D0D6")),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
    ]))
    story.append(t_code)

    return story


def main():
    register_fonts()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    doc = BaseDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        leftMargin=18 * mm,
        rightMargin=18 * mm,
        topMargin=20 * mm,
        bottomMargin=18 * mm,
        title="Divyasree WOW Voice Agent System Prompt Specification",
        author="Divyasree Developers / AIvoicebuilder",
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="normal")
    doc.addPageTemplates([PageTemplate(id="main", frames=[frame], onPage=draw_page)])
    doc.build(build_story(make_styles()))
    print(f"Generated PDF successfully: {OUTPUT}")


if __name__ == "__main__":
    main()

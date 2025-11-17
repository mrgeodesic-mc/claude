#!/usr/bin/env python3
"""
Generate a two-page PDF document describing the Narrative Journey webapp
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib import colors

def create_pdf():
    """Create a two-page PDF document about the Narrative Journey app"""

    # Create PDF document
    pdf_file = "narrative-journey/Narrative_Journey_App_Overview.pdf"
    doc = SimpleDocTemplate(pdf_file, pagesize=letter,
                           topMargin=0.5*inch, bottomMargin=0.5*inch,
                           leftMargin=0.75*inch, rightMargin=0.75*inch)

    # Container for the 'Flowable' objects
    story = []

    # Define styles
    styles = getSampleStyleSheet()

    # Custom title style
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#2C5F7C'),
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )

    # Custom subtitle style
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontSize=11,
        textColor=colors.HexColor('#4A90A4'),
        spaceAfter=20,
        alignment=TA_CENTER,
        fontName='Helvetica-Oblique'
    )

    # Custom heading style
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.HexColor('#2C5F7C'),
        spaceAfter=8,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )

    # Custom body style
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=10,
        alignment=TA_JUSTIFY,
        spaceAfter=8,
        leading=14
    )

    # Custom bullet style
    bullet_style = ParagraphStyle(
        'CustomBullet',
        parent=styles['Normal'],
        fontSize=9.5,
        leftIndent=20,
        spaceAfter=4,
        leading=13
    )

    # ============ PAGE 1 ============

    # Title
    story.append(Paragraph("Narrative Journey", title_style))
    story.append(Paragraph("Interactive Web Application for Adaptive Leadership Workshops", subtitle_style))

    # Overview section
    story.append(Paragraph("Overview", heading_style))
    story.append(Paragraph(
        "The <b>Narrative Journey</b> is a mobile-first, self-guided reflection tool designed for "
        "Adaptive Leadership workshops. It empowers participants to explore and develop control over "
        "their professional narratives, embracing the core principle: <i>\"You can't always control your "
        "positional authority—but you can always control your narrative.\"</i>",
        body_style
    ))

    story.append(Spacer(1, 0.1*inch))

    # Purpose & Goals
    story.append(Paragraph("Purpose & Goals", heading_style))
    story.append(Paragraph("• Build awareness of how participants frame their career narratives", bullet_style))
    story.append(Paragraph("• Develop intentional communication strategies for professional growth", bullet_style))
    story.append(Paragraph("• Enable participants to take agency over their career trajectory", bullet_style))
    story.append(Paragraph("• Provide structured reflection on identity, communication, and career planning", bullet_style))

    story.append(Spacer(1, 0.1*inch))

    # Key Features
    story.append(Paragraph("Key Features", heading_style))

    features_data = [
        ["<b>Mobile-First Design</b>", "Optimized for smartphones and tablets, accessed via QR codes"],
        ["<b>Progressive Journey</b>", "Three themed exploration sections with guided reflective questions"],
        ["<b>Local Storage</b>", "Automatic browser-based data persistence (no server, complete privacy)"],
        ["<b>Export Functionality</b>", "Download complete journey as a text file for personal records"],
        ["<b>Progress Tracking</b>", "Visual progress indicators showing completion status"],
        ["<b>Offline-Capable</b>", "Works without internet once initially loaded"]
    ]

    features_table = Table(features_data, colWidths=[1.5*inch, 4.5*inch])
    features_table.setStyle(TableStyle([
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('TEXTCOLOR', (0, 0), (0, -1), colors.HexColor('#2C5F7C')),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]))

    story.append(features_table)
    story.append(Spacer(1, 0.15*inch))

    # The Three Themes
    story.append(Paragraph("The Three-Theme Journey", heading_style))

    story.append(Paragraph(
        "<b>Theme 1: Owning Your Narrative</b>",
        ParagraphStyle('ThemeTitle', parent=body_style, fontSize=10.5, textColor=colors.HexColor('#E8A87C'),
                      spaceAfter=4, fontName='Helvetica-Bold')
    ))
    story.append(Paragraph(
        "Moving from passive observation to active storytelling. Participants reflect on how "
        "Adaptive Leadership has helped them reframe their role, what story they're telling about "
        "their leadership identity, and what experiments have shifted their sense of direction.",
        bullet_style
    ))

    story.append(Spacer(1, 0.05*inch))

    story.append(Paragraph(
        "<b>Theme 2: Sharing Your Story with Colleagues</b>",
        ParagraphStyle('ThemeTitle', parent=body_style, fontSize=10.5, textColor=colors.HexColor('#E8A87C'),
                      spaceAfter=4, fontName='Helvetica-Bold')
    ))
    story.append(Paragraph(
        "Treating storytelling as a learnable communication skill. Participants explore how they've "
        "shared insights with teammates, where they want deeper understanding, and how to stay grounded "
        "when facing pushback. <i>\"Repetition is a tool—it helps you teach others who you're becoming.\"</i>",
        bullet_style
    ))

    story.append(Spacer(1, 0.05*inch))

    story.append(Paragraph(
        "<b>Theme 3: Narrative as Career Pathway</b>",
        ParagraphStyle('ThemeTitle', parent=body_style, fontSize=10.5, textColor=colors.HexColor('#E8A87C'),
                      spaceAfter=4, fontName='Helvetica-Bold')
    ))
    story.append(Paragraph(
        "Understanding storytelling as career strategy, not self-promotion. Participants identify which "
        "parts of their story open doors, what they've learned about themselves through challenges, and "
        "how articulating growth builds ownership over career direction.",
        bullet_style
    ))

    # Page break
    story.append(PageBreak())

    # ============ PAGE 2 ============

    # Technical Highlights
    story.append(Paragraph("Technical Highlights", heading_style))

    tech_data = [
        ["<b>Architecture</b>", "Single-page application (SPA), client-side only, no backend required"],
        ["<b>Technology Stack</b>", "Pure HTML/CSS/JavaScript with zero external dependencies"],
        ["<b>File Size</b>", "29KB single-file application—lightweight and fast-loading"],
        ["<b>Data Storage</b>", "Browser localStorage for complete privacy (no server uploads)"],
        ["<b>Deployment</b>", "Static hosting on any platform (GitHub Pages, Netlify, Vercel, etc.)"],
        ["<b>Compatibility</b>", "Modern browsers (Chrome 90+, Safari 14+, Firefox 88+)"],
        ["<b>Accessibility</b>", "Responsive design, semantic HTML, sufficient color contrast"]
    ]

    tech_table = Table(tech_data, colWidths=[1.4*inch, 4.6*inch])
    tech_table.setStyle(TableStyle([
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('TEXTCOLOR', (0, 0), (0, -1), colors.HexColor('#2C5F7C')),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]))

    story.append(tech_table)
    story.append(Spacer(1, 0.15*inch))

    # User Experience Flow
    story.append(Paragraph("User Experience Flow", heading_style))
    story.append(Paragraph("1. <b>Welcome Screen</b> — Introduction to Adaptive Leadership and narrative control", bullet_style))
    story.append(Paragraph("2. <b>Theme Selection</b> — Choose from three themes with progress tracking", bullet_style))
    story.append(Paragraph("3. <b>Guided Reflection</b> — Answer prompting questions with personal insights", bullet_style))
    story.append(Paragraph("4. <b>Auto-Save</b> — Reflections automatically persist in browser storage", bullet_style))
    story.append(Paragraph("5. <b>Journey Summary</b> — Review all reflections and export as text file", bullet_style))
    story.append(Paragraph("6. <b>Closing Commitment</b> — Identify one actionable step for the next two weeks", bullet_style))

    story.append(Spacer(1, 0.1*inch))

    # Use Cases & Benefits
    story.append(Paragraph("Use Cases & Benefits", heading_style))

    story.append(Paragraph(
        "<b>For Workshop Facilitators:</b> A structured tool to guide participants through narrative "
        "development without requiring technical setup. Participants can access via QR code and work "
        "at their own pace during or between sessions.",
        body_style
    ))

    story.append(Paragraph(
        "<b>For Participants:</b> A private, judgment-free space to explore professional identity, "
        "practice articulating growth, and develop concrete communication strategies. The export feature "
        "allows them to retain their reflections for future reference.",
        body_style
    ))

    story.append(Paragraph(
        "<b>For Organizations:</b> A zero-cost, privacy-first solution that requires no user accounts, "
        "data collection, or ongoing maintenance. Can be deployed once and used indefinitely.",
        body_style
    ))

    story.append(Spacer(1, 0.15*inch))

    # Privacy & Data Security
    story.append(Paragraph("Privacy & Data Security", heading_style))
    story.append(Paragraph(
        "All participant reflections are stored <b>exclusively in their browser's local storage</b>. "
        "No data is transmitted to servers, no analytics are collected, and no accounts are required. "
        "Participants maintain complete control over their data and can export or delete it at any time. "
        "This design ensures psychological safety for honest, vulnerable reflection.",
        body_style
    ))

    story.append(Spacer(1, 0.15*inch))

    # Getting Started
    story.append(Paragraph("Getting Started", heading_style))
    story.append(Paragraph(
        "The application includes comprehensive documentation (README.md and QUICKSTART.md) plus QR code "
        "generation tools (qr-display.html and generate-qr.py) for easy mobile access. Deploy to any "
        "static hosting service, generate a QR code, and you're ready for your first workshop.",
        body_style
    ))

    story.append(Spacer(1, 0.2*inch))

    # Footer
    footer_style = ParagraphStyle(
        'Footer',
        parent=styles['Normal'],
        fontSize=8,
        textColor=colors.grey,
        alignment=TA_CENTER,
        spaceAfter=0
    )

    story.append(Paragraph(
        "<i>Narrative Journey — Empowering professionals to control their career narratives through intentional storytelling</i>",
        footer_style
    ))

    # Build PDF
    doc.build(story)
    print(f"PDF created successfully: {pdf_file}")
    return pdf_file

if __name__ == "__main__":
    create_pdf()

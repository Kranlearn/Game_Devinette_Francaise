#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Build a clean, exam-ready PowerPoint for the BBC 6 Minute English oral."""
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

# ---------- palette ----------
NAVY   = RGBColor(0x1F, 0x38, 0x64)   # titles
BLUE   = RGBColor(0x2E, 0x74, 0xB5)   # accents
TEAL   = RGBColor(0x0F, 0x6F, 0x6F)   # secondary
DARK   = RGBColor(0x26, 0x26, 0x26)   # body
GREY   = RGBColor(0x59, 0x59, 0x59)   # muted
LIGHT  = RGBColor(0xEE, 0xF2, 0xF7)   # background strip
WHITE  = RGBColor(0xFF, 0xFF, 0xFF)

FONT = "Calibri"
FONT_LG = 28
FONT_MD = 20
FONT_SM = 16

prs = Presentation()
prs.slide_width = Inches(13.33)
prs.slide_height = Inches(7.5)
SW, SH = prs.slide_width, prs.slide_height
BLANK = prs.slide_layouts[6]

def add_slide():
    return prs.slides.add_slide(BLANK)

def rect(slide, x, y, w, h, color, line=None):
    from pptx.enum.shapes import MSO_SHAPE
    shp = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, w, h)
    shp.fill.solid(); shp.fill.fore_color.rgb = color
    if line is None:
        shp.line.fill.background()
    else:
        shp.line.color.rgb = line; shp.line.width = Pt(1)
    shp.shadow.inherit = False
    return shp

def txt(slide, x, y, w, h, runs, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP,
        space_after=6, line_spacing=1.0, wrap=True):
    """runs = list of paragraphs; each paragraph = list of (text, size, bold, color, italic)"""
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = wrap
    tf.vertical_anchor = anchor
    tf.margin_left = 0; tf.margin_right = 0
    tf.margin_top = 0; tf.margin_bottom = 0
    for i, para in enumerate(runs):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.space_after = Pt(space_after)
        p.space_before = Pt(0)
        p.line_spacing = line_spacing
        for (t, size, bold, color, *rest) in para:
            italic = rest[0] if rest else False
            r = p.add_run()
            r.text = t
            r.font.name = FONT
            r.font.size = Pt(size)
            r.font.bold = bold
            r.font.italic = italic
            r.font.color.rgb = color
    return tb

def bullets(slide, x, y, w, h, items, size=FONT_MD, gap=10, color=DARK,
            bullet_color=BLUE, lead_bold=True, line_spacing=1.05):
    """items: list of (bold_lead, rest) or plain strings."""
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = 0; tf.margin_right = 0; tf.margin_top = 0; tf.margin_bottom = 0
    for i, item in enumerate(items):
        if isinstance(item, tuple):
            lead, rest = item
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            p.space_after = Pt(gap); p.space_before = Pt(0)
            p.line_spacing = line_spacing
            r1 = p.add_run(); r1.text = "▪  "; r1.font.name = FONT
            r1.font.size = Pt(size); r1.font.bold = True
            r1.font.color.rgb = bullet_color
            r2 = p.add_run(); r2.text = lead; r2.font.name = FONT
            r2.font.size = Pt(size); r2.font.bold = True; r2.font.color.rgb = NAVY
            r3 = p.add_run(); r3.text = rest; r3.font.name = FONT
            r3.font.size = Pt(size); r3.font.color.rgb = color
        else:
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            p.space_after = Pt(gap); p.space_before = Pt(0)
            p.line_spacing = line_spacing
            r1 = p.add_run(); r1.text = "▪  "; r1.font.name = FONT
            r1.font.size = Pt(size); r1.font.bold = True
            r1.font.color.rgb = bullet_color
            r2 = p.add_run(); r2.text = item; r2.font.name = FONT
            r2.font.size = Pt(size); r2.font.color.rgb = color
    return tb

def header(slide, title, subtitle=None):
    rect(slide, 0, 0, SW, Inches(1.15), NAVY)
    rect(slide, 0, Inches(1.15), SW, Inches(0.06), BLUE)
    txt(slide, Inches(0.55), Inches(0.12), SW - Inches(1.1), Inches(0.9),
        [[(title, FONT_LG, True, WHITE)]], anchor=MSO_ANCHOR.MIDDLE)
    if subtitle:
        txt(slide, Inches(0.57), Inches(0.72), SW - Inches(1.1), Inches(0.4),
            [[(subtitle, 13, False, RGBColor(0xCF,0xDA,0xEA))]])

def footer(slide, num, note):
    rect(slide, 0, SH - Inches(0.34), SW, Inches(0.34), LIGHT)
    txt(slide, Inches(0.4), SH - Inches(0.33), Inches(9), Inches(0.32),
        [[(note, 9, False, GREY)]], anchor=MSO_ANCHOR.MIDDLE)
    txt(slide, SW - Inches(1.3), SH - Inches(0.33), Inches(0.9), Inches(0.32),
        [[("BBC 6 Min. English · Oral", 9, False, GREY)]], align=PP_ALIGN.RIGHT,
        anchor=MSO_ANCHOR.MIDDLE)

OUT = r"C:/Users/HP OMEN/Documents/Can_apps_teach_you_a_language.pptx"

# =========================================================================
# SLIDE 1 — Title
# =========================================================================
s = add_slide()
rect(s, 0, 0, SW, SH, NAVY)
rect(s, 0, Inches(2.6), SW, Inches(0.08), BLUE)
txt(s, Inches(0.9), Inches(1.15), SW - Inches(1.8), Inches(1.4),
    [[("Can Apps Teach You a Language?", FONT_LG, True, WHITE)]],
    align=PP_ALIGN.CENTER)
txt(s, Inches(0.9), Inches(2.85), SW - Inches(1.8), Inches(1.0),
    [[("An oral presentation · ~2 minutes", FONT_MD, False, RGBColor(0xCF,0xDA,0xEA))]],
    align=PP_ALIGN.CENTER)
txt(s, Inches(0.9), Inches(4.4), SW - Inches(1.8), Inches(1.6),
    [[("BBC Learning English  —  6 Minute English  ·  10 September 2026", FONT_SM, False, WHITE)],
     [("Presenters: Neil & Pippa", FONT_SM, False, RGBColor(0xCF,0xDA,0xEA))]],
    align=PP_ALIGN.CENTER, space_after=6)
txt(s, Inches(0.9), SH - Inches(1.25), SW - Inches(1.8), Inches(0.6),
    [[("Student: __________________        Date: ______________", FONT_SM, False, WHITE)]],
    align=PP_ALIGN.CENTER)

# =========================================================================
# SLIDE 2 — The question
# =========================================================================
s = add_slide()
header(s, "The Question", "Hook + topic + main question")
bullets(s, Inches(0.7), Inches(1.6), Inches(7.6), Inches(4.8), [
    ("Have you ever used ", "a language app while travelling on the bus?"),
    ("It is convenient, ", "but is it enough to learn a language?"),
    ("Today I'm talking about ", "\"Can apps teach you a language?\""),
    ("The episode: ", "BBC 6 Minute English, 10 September 2026"),
    ("Presenters: ", "Neil & Pippa"),
], size=FONT_MD, gap=14)
rect(s, Inches(8.6), Inches(1.7), Inches(4.0), Inches(4.4), LIGHT)
txt(s, Inches(8.8), Inches(1.95), Inches(3.6), Inches(4.0), [
    [("Key idea", FONT_MD, True, BLUE)],
    [("Convenience", FONT_SM, True, NAVY)],
    [("vs.", FONT_SM, False, DARK)],
    [("Effectiveness", FONT_SM, True, NAVY)],
    [("", FONT_SM, False, DARK)],
    [("Short lessons,", FONT_SM, False, DARK)],
    [("repetition,", FONT_SM, False, DARK)],
    [("flexibility", FONT_SM, False, DARK)],
    [("", FONT_SM, False, DARK)],
    [("But can it replace", FONT_SM, True, NAVY)],
    [("real exposure?", FONT_SM, True, NAVY)],
], space_after=8, line_spacing=1.1)
footer(s, 2, "Oral preparation · BBC 6 Minute English · 10 Sep 2026")

# =========================================================================
# SLIDE 3 — The source
# =========================================================================
s = add_slide()
header(s, "The Source", "Where the ideas come from")
bullets(s, Inches(0.7), Inches(1.7), Inches(7.4), Inches(4.5), [
    ("Source: ", "BBC Learning English, \"Can apps teach you a language?\""),
    ("Episode: ", "6 Minute English — published 10 September 2026"),
    ("Presenters: ", "Neil & Pippa"),
    ("Aim of the programme: ", "to discuss whether apps really help"),
    ("Experts: ", "references a study on language learning"),
], size=FONT_MD, gap=14)
rect(s, Inches(8.5), Inches(1.7), Inches(4.1), Inches(4.4), LIGHT)
txt(s, Inches(8.7), Inches(2.0), Inches(3.7), Inches(4.0), [
    [("Why it matters", FONT_MD, True, BLUE)],
    [("Trusted English-learning", FONT_SM, True, NAVY)],
    [("content", FONT_SM, False, DARK)],
    [("", FONT_SM, False, DARK)],
    [("10 / Sept / 2026", FONT_SM, True, NAVY)],
    [("", FONT_SM, False, DARK)],
    [("News + language", FONT_SM, False, DARK)],
    [("in 6 minutes", FONT_SM, False, DARK)],
], space_after=8, line_spacing=1.1)
footer(s, 3, "Oral preparation · BBC 6 Minute English · 10 Sep 2026")

# =========================================================================
# SLIDE 4 — Key findings
# =========================================================================
s = add_slide()
header(s, "What the Episode Says", "Key findings")
bullets(s, Inches(0.7), Inches(1.6), Inches(7.7), Inches(5.0), [
    ("Apps ", "— Duolingo, Babbel, Busuu — use short lessons and repetition."),
    ("They help learners ", "practise regularly, which builds habit."),
    ("Children: ", "learn by constant exposure."),
    ("Adults: ", "usually study only a few hours a week."),
    ("Explicit teaching: ", "clear explanations of grammar and vocabulary."),
    ("For adults, ", "this direct guidance is especially valuable."),
], size=FONT_MD, gap=10)
rect(s, Inches(8.7), Inches(1.7), Inches(3.9), Inches(4.6), LIGHT)
txt(s, Inches(8.9), Inches(2.0), Inches(3.5), Inches(4.1), [
    [("Takeaway", FONT_MD, True, BLUE)],
    [("Apps are useful", FONT_SM, True, NAVY)],
    [("for regular practice", FONT_SM, False, DARK)],
    [("", FONT_SM, False, DARK)],
    [("But they are not", FONT_SM, True, NAVY)],
    [("a complete method", FONT_SM, True, NAVY)],
    [("", FONT_SM, False, DARK)],
    [("Exposure matters", FONT_SM, True, NAVY)],
], space_after=8, line_spacing=1.1)
footer(s, 4, "Oral preparation · BBC 6 Minute English · 10 Sep 2026")

# =========================================================================
# SLIDE 5 — The study
# =========================================================================
s = add_slide()
header(s, "A Study Compared Two Ways", "Evidence")
bullets(s, Inches(0.7), Inches(1.65), Inches(7.6), Inches(4.4), [
    ("App learners ", "improved more in written grammar tests."),
    ("Classroom learners ", "improved more in listening."),
    ("Why the difference? ", "each method suits a different skill."),
    ("Reality check: ", "the study used one app, one language, one school."),
    ("So results ", "are promising, but limited."),
], size=FONT_MD, gap=11)
# two-column result boxes
def col_box(x, title, lines, color):
    rect(s, x, Inches(1.95), Inches(4.0), Inches(0.5), color)
    txt(s, x+Inches(0.2), Inches(1.95), Inches(3.6), Inches(0.5),
        [[(title, FONT_MD, True, WHITE)]], anchor=MSO_ANCHOR.MIDDLE)
    rect(s, x, Inches(2.45), Inches(4.0), Inches(3.2), LIGHT)
    bullets(s, x+Inches(0.2), Inches(2.6), Inches(3.6), Inches(2.9), lines, size=FONT_MD, gap=10, bullet_color=color)
col_box(Inches(0.7), "With the App", [
    "better written grammar",
    "short, repeatable lessons",
    "easy to use on the bus",
], BLUE)
col_box(Inches(6.65), "In Class", [
    "better listening",
    "real conversation",
    "interaction with peers",
], TEAL)
footer(s, 5, "Oral preparation · BBC 6 Minute English · 10 Sep 2026")

# =========================================================================
# SLIDE 6 — My favourite word
# =========================================================================
s = add_slide()
header(s, "My Favourite Word", "Vocabulary you can reuse")
txt(s, Inches(0.7), Inches(1.6), Inches(5), Inches(1.0),
    [[("\u201CImmersion\u201D", FONT_LG, True, TEAL)]])
rect(s, Inches(0.7), Inches(2.9), Inches(7.4), Inches(3.6), LIGHT)
bullets(s, Inches(0.95), Inches(3.1), Inches(6.9), Inches(3.3), [
    ("Meaning: ", "being completely surrounded by a language."),
    ("Example: ", "living abroad, watching films without subtitles."),
    ("Why I like it: ", "it captures real, natural learning."),
    ("Contract: ", "immerse = to surround someone with a language."),
], size=FONT_MD, gap=10)
rect(s, Inches(8.4), Inches(1.7), Inches(4.2), Inches(4.6), NAVY)
txt(s, Inches(8.6), Inches(2.0), Inches(3.8), Inches(4.1), [
    [("Pronunciation", FONT_MD, True, WHITE)],
    [("im-MER-sion", FONT_LG, True, RGBColor(0xCF,0xDA,0xEA))],
    [("", FONT_SM, False, WHITE)],
    [("/ɪmˈɜːʒ.ən/", FONT_SM, False, RGBColor(0xCF,0xDA,0xEA))],
    [("", FONT_SM, False, WHITE)],
    [("Stress: ", FONT_SM, False, WHITE), ("on the second syllable", FONT_SM, True, RGBColor(0xCF,0xDA,0xEA))],
], space_after=8, line_spacing=1.1)
footer(s, 6, "Oral preparation · BBC 6 Minute English · 10 Sep 2026")

# =========================================================================
# SLIDE 7 — Conclusion
# =========================================================================
s = add_slide()
header(s, "My Conclusion", "Opinion + balance")
bullets(s, Inches(0.7), Inches(1.65), Inches(7.8), Inches(4.6), [
    ("In my opinion, ", "apps are useful, but not the only way to learn."),
    ("They offer ", "repetition and flexibility — ideal for quick practice."),
    ("However, ", "real conversations build listening and speaking skills."),
    ("Classes ", "also give feedback and structure."),
    ("Best way: ", "combine both methods for steady progress."),
], size=FONT_MD, gap=12)
rect(s, Inches(8.8), Inches(1.7), Inches(3.8), Inches(4.4), NAVY)
txt(s, Inches(9.0), Inches(2.0), Inches(3.4), Inches(4.0), [
    [("My view", FONT_MD, True, WHITE)],
    [("Apps + real", FONT_LG, True, WHITE)],
    [("use = best result", FONT_LG, True, WHITE)],
    [("", FONT_SM, False, RGBColor(0xCF,0xDA,0xEA))],
    [("", FONT_SM, False, WHITE)],
    [("I'm convinced", FONT_SM, True, WHITE)],
    [("that a mix of", FONT_SM, False, WHITE)],
    [("app + speaking", FONT_SM, False, WHITE)],
    [("is the key.", FONT_SM, False, WHITE)],
], space_after=8, line_spacing=1.1)
footer(s, 7, "Oral preparation · BBC 6 Minute English · 10 Sep 2026")

# =========================================================================
# SLIDE 8 — Language for 18/20
# =========================================================================
s = add_slide()
header(s, "Language to Reach 18/20", "Connectors · vocabulary · grammar")
txt(s, Inches(0.55), Inches(1.4), Inches(3.6), Inches(0.4),
    [[("Connectors", FONT_LG, True, BLUE)]])
bullets(s, Inches(0.6), Inches(1.9), Inches(3.7), Inches(3.4), [
    ("However, ", "but"),
    ("Moreover, ", "in addition"),
    ("Nevertheless, ", "nevertheless"),
    ("On the other hand, ", "contrast"),
    ("As a result, ", "effect"),
], size=FONT_MD, gap=9)
txt(s, Inches(4.55), Inches(1.4), Inches(3.6), Inches(0.4),
    [[("Vocabulary", FONT_LG, True, BLUE)]])
bullets(s, Inches(4.6), Inches(1.9), Inches(3.7), Inches(3.4), [
    ("Exposure ", "— contact with a language"),
    ("Repetition ", "— practising again and again"),
    ("Explicit teaching ", "— clear, direct explanations"),
    ("Immersion ", "— being surrounded by a language"),
    ("Flexibility ", "— ability to change"),
], size=FONT_MD, gap=8)
txt(s, Inches(8.65), Inches(1.4), Inches(4.1), Inches(0.4),
    [[("Grammar to reuse", FONT_LG, True, BLUE)]])
bullets(s, Inches(8.7), Inches(1.9), Inches(4.1), Inches(3.4), [
    ("Passive voice: ", "is improved by..."),
    ("Relative clauses: ", "apps that teach..."),
    ("Linkers of contrast: ", "although, despite, whereas"),
    ("Conditionals: ", "If you practise..."),
], size=FONT_MD, gap=8)
footer(s, 8, "Oral preparation · BBC 6 Minute English · 10 Sep 2026")

# =========================================================================
# SLIDE 9 — Full script (2 min) — on-slide + notes
# =========================================================================
s = add_slide()
header(s, "Full Script — About 2 Minutes", "Read, then speak from memory")
script = [
    "Good morning. Today I'd like to answer a question we all face when learning English: can apps really teach you a language?",
    "Have you ever used a language app while travelling on the bus? It is convenient, but is it enough? Today I'm discussing \"Can apps teach you a language?\" — an episode of BBC 6 Minute English, published on 10 September 2026.",
    "Neil and Pippa explore how effective language apps really are. The answer is mixed. Apps such as Duolingo, Babbel and Busuu use short lessons and repetition, so they help learners practise regularly. However, children learn through constant exposure, while adults usually study for only a few hours a week. For this reason, adults also benefit from explicit teaching — clear explanations of grammar and vocabulary.",
    "The programme cites a study comparing people learning English with an app and people learning in class. The results are interesting: app learners improved more in written grammar tests, while classroom learners improved more in listening. Nevertheless, the study looked at only one app, one language and one school, so its results are promising but limited.",
    "One expression I admire is \"immersion\". It means being completely surrounded by a language, and it reminds me that real learning goes far beyond an app.",
    "In my opinion, apps are useful, but they should not be the only way to learn. They offer repetition and flexibility, but classes and real conversations help us practise listening and speaking. So I'm convinced that combining both methods is the best way to improve.",
    "Thank you for listening. Are there any questions?",
]
tb = s.shapes.add_textbox(Inches(0.7), Inches(1.5), Inches(11.9), Inches(5.0))
tf = tb.text_frame
tf.word_wrap = True
tf.margin_left=0;tf.margin_right=0;tf.margin_top=0;tf.margin_bottom=0
for i, line in enumerate(script):
    p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
    p.space_after = Pt(11); p.line_spacing = 1.12
    r = p.add_run(); r.text = f"{i+1}.  "; r.font.name=FONT; r.font.size=Pt(17); r.font.bold=True; r.font.color.rgb=BLUE
    r2 = p.add_run(); r2.text = line; r2.font.name=FONT; r2.font.size=Pt(17); r2.font.color.rgb=DARK
footer(s, 9, "Oral preparation · BBC 6 Minute English · 10 Sep 2026")

# =========================================================================
# SLIDE 10 — Thank you
# =========================================================================
s = add_slide()
rect(s, 0, 0, SW, SH, NAVY)
rect(s, 0, Inches(3.4), SW, Inches(0.08), BLUE)
txt(s, Inches(0.9), Inches(2.0), SW - Inches(1.8), Inches(1.2),
    [[("Thank you for listening", FONT_LG, True, WHITE)]], align=PP_ALIGN.CENTER)
txt(s, Inches(0.9), Inches(3.7), SW - Inches(1.8), Inches(1.0),
    [[("Are there any questions?", FONT_MD, False, RGBColor(0xCF,0xDA,0xEA))]],
    align=PP_ALIGN.CENTER)
txt(s, Inches(0.9), SH - Inches(1.3), SW - Inches(1.8), Inches(0.6),
    [[("Can apps teach you a language?  ·  BBC 6 Minute English · 10 September 2026", FONT_SM, False, WHITE)]],
    align=PP_ALIGN.CENTER)

# =========================================================================
# Speaker notes (added after the deck)
# =========================================================================
NOTES = {
    1: "Hook: smile and make eye contact. This is a question the student has actually asked themselves.",
    2: "Say the first bullet naturally, with a slight pause after the question. The 'Key idea' box is there to help the student structure the answer.",
    3: "Mention the source clearly — examiners like the candidate to say where the ideas come from.",
    4: "Read each bullet. The student should not read the slide word-for-word; only use it as a memory aid.",
    5: "Tell the student to compare the two columns. Stress: 'one app, one language, one school' → limited / promising.",
    6: "Pick 1-2 phonemes to work on (the /ɪmˈɜːʒ.ən/ stress). Recommends pronouncing 'immersion' naturally.",
    7: "The student's personal opinion is the most important part. Encourage them to say it in their own words.",
    8: "This is a revision slide, not something to read aloud. It should be studied before the exam.",
    9: "Full script for the 2-minute oral. About 240 words at a natural pace. Practice 3 times aloud.",
    10: "End on a smile. Wait for questions. It is better to be honest than to guess.",
}
for idx, slide in enumerate(prs.slides):
    notes = NOTES.get(idx + 1, "")
    slide.notes_slide.notes_text_frame.text = notes

prs.save(OUT)
print("SAVED:", OUT)
print("slides:", len(prs.slides._sldIdLst))

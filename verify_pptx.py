from pptx import Presentation
p = Presentation(r'C:/Users/HP OMEN/Documents/Can_apps_teach_you_a_language.pptx')
for i, s in enumerate(p.slides, 1):
    print("=" * 70)
    print("SLIDE", i)
    print("=" * 70)
    for sh in s.shapes:
        if sh.has_text_frame and sh.text_frame.text.strip():
            line = sh.text_frame.text.strip().replace("\n", " | ")
            print("  -", line[:160])
    if s.has_notes_slide and s.notes_slide.notes_text_frame.text.strip():
        nt = s.notes_slide.notes_text_frame.text.strip()
        print("  [NOTES]", nt[:100])
print()
print("FILE OK - slides:", len(p.slides._sldIdLst))

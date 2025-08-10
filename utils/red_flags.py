
import re

def detect_red_flags_from_text(text: str):
    issues = []
    ltext = text.lower()
    # Jurisdiction check: flag if ADGM not mentioned or UAE Federal Courts explicitly referenced
    if "adgm" not in ltext and ("federal court" in ltext or "u.a.e" in ltext or "uae federal" in ltext or "federal court of the uae" in ltext):
        issues.append({
            "section": "Jurisdiction",
            "issue": "Jurisdiction clause may not reference ADGM",
            "severity": "High",
            "suggestion": "Update jurisdiction to explicitly reference ADGM Courts."
        })
    # Signature check
    if not re.search(r"(signature|signed by|date:|signatory)", ltext):
        issues.append({
            "section": "Signatory",
            "issue": "Missing signatory block or signature lines",
            "severity": "Medium",
            "suggestion": "Add signature block with name, title, and date."
        })
    # Placeholder / TODO check
    if any(k in ltext for k in ['tbd', 'to be decided', '[insert', '<<insert', 'insert here']):
        issues.append({
            "section": "Placeholder Text",
            "issue": "Contains placeholder text (TBD/Insert)",
            "severity": "Low",
            "suggestion": "Replace placeholders with final content."
        })
    return issues

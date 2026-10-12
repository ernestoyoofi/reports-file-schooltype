"""
Automated DOCX Structure and Formatting Validation Engine
Validates generated report files against strict font and layout requirements.
STRICT RULE: ONLY Times New Roman font allowed. Base font size is 12 pt.
"""

import sys
import os
import json
import re
from docx import Document
from docx.shared import Cm, Pt

class ReportValidator:
    def __init__(self, docx_path):
        self.docx_path = docx_path
        self.doc = Document(docx_path)
        self.results = {
            "file": os.path.basename(docx_path),
            "passed": True,
            "checks": [],
            "errors": [],
            "warnings": [],
            "unfilled_placeholders": []
        }

    def validate_all(self):
        self.check_paper_size_and_margins()
        self.check_sections_and_headers()
        self.check_strict_typography()
        self.check_placeholders()
        return self.results

    def check_paper_size_and_margins(self):
        """Validates A4 size (21.0 x 29.7 cm) and 4-4-3-3 cm margins."""
        for idx, section in enumerate(self.doc.sections):
            width_cm = round(section.page_width.cm, 1)
            height_cm = round(section.page_height.cm, 1)
            top_cm = round(section.top_margin.cm, 1)
            left_cm = round(section.left_margin.cm, 1)
            bottom_cm = round(section.bottom_margin.cm, 1)
            right_cm = round(section.right_margin.cm, 1)

            is_a4 = (width_cm == 21.0 and height_cm == 29.7)
            is_valid_margin = (top_cm == 4.0 and left_cm == 4.0 and bottom_cm == 3.0 and right_cm == 3.0)

            if is_a4 and is_valid_margin:
                self.results["checks"].append(f"Section {idx+1}: A4 Paper (21x29.7 cm) with 4-4-3-3 cm margins PASS")
            else:
                self.results["passed"] = False
                err_msg = f"Section {idx+1}: Invalid layout! Size={width_cm}x{height_cm}cm, Margins=Top:{top_cm}, Left:{left_cm}, Bottom:{bottom_cm}, Right:{right_cm}"
                self.results["errors"].append(err_msg)

    def check_sections_and_headers(self):
        """Validates that document contains at least 2 sections (Cover + Prelim / Main)."""
        section_count = len(self.doc.sections)
        if section_count >= 2:
            self.results["checks"].append(f"Section separation PASS: {section_count} sections present")
        else:
            self.results["warnings"].append(f"Document has only {section_count} section. Recommended >= 2 for pagination rules.")

    def check_strict_typography(self):
        """Strictly validates that ONLY Times New Roman font is used throughout the document."""
        non_standard_fonts = set()
        for p in self.doc.paragraphs:
            for run in p.runs:
                if run.font.name and run.font.name != "Times New Roman":
                    non_standard_fonts.add(run.font.name)

        for tbl in self.doc.tables:
            for row in tbl.rows:
                for cell in row.cells:
                    for p in cell.paragraphs:
                        for run in p.runs:
                            if run.font.name and run.font.name != "Times New Roman":
                                non_standard_fonts.add(run.font.name)

        if not non_standard_fonts:
            self.results["checks"].append("Strict Typography PASS: ONLY Times New Roman font detected throughout document")
        else:
            self.results["passed"] = False
            self.results["errors"].append(f"STRICT TYPOGRAPHY VIOLATION! Unapproved fonts detected: {list(non_standard_fonts)}. ONLY Times New Roman is permitted.")

    def check_placeholders(self):
        """Scans text for unpopulated bracketed placeholders like [NAMA_PENULIS]."""
        placeholder_pattern = re.compile(r'\[[A-Z0-9_]{3,}\]')
        found = set()
        for p in self.doc.paragraphs:
            matches = placeholder_pattern.findall(p.text)
            for m in matches:
                found.add(m)
        
        for table in self.doc.tables:
            for row in table.rows:
                for cell in row.cells:
                    matches = placeholder_pattern.findall(cell.text)
                    for m in matches:
                        found.add(m)

        if found:
            self.results["unfilled_placeholders"] = list(found)
            self.results["warnings"].append(f"Unfilled placeholders detected ({len(found)}): {list(found)[:5]}")
        else:
            self.results["checks"].append("Placeholder Audit PASS: No unfilled bracket placeholders")

def main():
    if len(sys.argv) < 2:
        print("Usage: python validate_report.py <path_to_docx>")
        sys.exit(1)
    
    target_docx = sys.argv[1]
    validator = ReportValidator(target_docx)
    results = validator.validate_all()
    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()

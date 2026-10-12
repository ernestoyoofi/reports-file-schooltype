import os
import pytest
from scripts.docx_builder import ReportDocxBuilder
from scripts.validate_report import ReportValidator

def test_report_validator(tmp_path):
    output_docx = os.path.join(tmp_path, "valid_report.docx")
    builder = ReportDocxBuilder()
    builder.add_cover_page(title="LAPORAN UJI COBA VALIDASI")
    builder.start_preliminary_section()
    builder.add_foreword_page(["Paragraf pembuka..."])
    builder.start_main_chapters_section()
    builder.add_chapter_title("BAB I", "PENDAHULUAN")
    builder.add_body_paragraph("Teks isi pendahuluan...")
    builder.save(output_docx)

    validator = ReportValidator(output_docx)
    res = validator.validate_all()
    assert res["passed"] is True
    assert len(res["errors"]) == 0

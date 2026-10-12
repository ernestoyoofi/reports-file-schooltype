import os
import pytest
from docx import Document
from docx.shared import Cm
from scripts.docx_builder import ReportDocxBuilder

def test_docx_builder_creation(tmp_path):
    output_docx = os.path.join(tmp_path, "test_pkl_report.docx")
    
    config = {
        "title": "LAPORAN PRAKTIK KERJA LAPANGAN DI PT TELEKOMUNIKASI INDONESIA",
        "report_type": "pkl",
        "author_name": "Ahmad Rizky",
        "author_id": "20261001",
        "institution_name": "SMK Negeri 1 Jakarta",
        "department_name": "Teknik Komputer dan Jaringan",
        "company_name": "PT Telekomunikasi Indonesia",
        "city": "Jakarta",
        "year": "2026",
        "font_family": "Times New Roman",
        "margins_cm": {"top": 4.0, "left": 4.0, "bottom": 3.0, "right": 3.0}
    }

    builder = ReportDocxBuilder(config=config)
    builder.add_cover_page(title=config["title"], subtitle="Disusun Guna Memenuhi Syarat Kelulusan PKL")
    builder.start_preliminary_section()
    builder.add_approval_page(school_supervisor="Drs. Budi Santoso", field_supervisor="Eko Prasetyo, S.T.", headmaster="Dr. Ir. H. Mulyono, M.Pd.")
    builder.add_foreword_page([
        "Puji dan syukur penulis panjatkan kehadirat Allah SWT...",
        "Laporan ini disusun guna memenuhi syarat kelulusan..."
    ])
    builder.add_table_of_contents_placeholder()

    builder.start_main_chapters_section()
    builder.add_chapter_title("BAB I", "PENDAHULUAN")
    builder.add_section_heading(level=2, number_str="1.1", title_str="Latar Belakang PKL")
    builder.add_body_paragraph("Praktik Kerja Lapangan (PKL) merupakan kegiatan wajib bagi siswa vocational...")
    
    builder.add_table_with_caption(
        caption_text="Tabel 1.1 Jadwal Pelaksanaan Kegiatan PKL",
        headers=["No", "Hari / Tanggal", "Jenis Kegiatan", "Keterangan"],
        rows_data=[
            ["1", "Senin, 10 Feb 2026", "Orientasi Lapangan", "Selesai"],
            ["2", "Selasa, 11 Feb 2026", "Konfigurasi Router Mikrotik", "Selesai"]
        ]
    )

    saved_path = builder.save(output_docx)
    assert os.path.exists(saved_path)

    # Verify created document geometry
    doc = Document(saved_path)
    assert len(doc.sections) == 3
    sec1 = doc.sections[0]
    assert round(sec1.top_margin.cm, 1) == 4.0
    assert round(sec1.left_margin.cm, 1) == 4.0
    assert round(sec1.bottom_margin.cm, 1) == 3.0
    assert round(sec1.right_margin.cm, 1) == 3.0

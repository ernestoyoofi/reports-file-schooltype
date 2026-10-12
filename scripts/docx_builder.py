"""
DOCX Document Generation Engine for Indonesian School & University Reports
STRICT RULE: ONLY Times New Roman font allowed across all elements. Base font size is 12 pt.
"""

import os
import json
from docx import Document
from docx.shared import Inches, Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

class ReportDocxBuilder:
    def __init__(self, config=None):
        self.doc = Document()
        self.config = config or self._default_config()
        # Force strict font family
        self.config["font_family"] = "Times New Roman"
        self._setup_document_geometry_and_styles()

    def _default_config(self):
        return {
            "title": "LAPORAN PRAKTIK KERJA LAPANGAN",
            "report_type": "pkl",
            "author_name": "[NAMA_PENULIS]",
            "author_id": "[NISN_NIM]",
            "institution_name": "[NAMA_SEKOLAH_UNIVERSITAS]",
            "department_name": "[JURUSAN_PROGRAM_KEAHLIAN]",
            "company_name": "[NAMA_PERUSAHAAN_DUDI]",
            "city": "[KOTA_KABUPATEN]",
            "year": "2026",
            "font_family": "Times New Roman",
            "margins_cm": {"top": 4.0, "left": 4.0, "bottom": 3.0, "right": 3.0}
        }

    def _apply_strict_run_font(self, run, size_pt=12, bold=False, italic=False):
        """Forces Times New Roman font on any text run."""
        run.font.name = "Times New Roman"
        run.font.size = Pt(size_pt)
        run.font.color.rgb = RGBColor(0, 0, 0)
        run.bold = bold
        run.italic = italic

    def _setup_document_geometry_and_styles(self):
        # Configure initial section geometry (Cover page section)
        section = self.doc.sections[0]
        section.page_width = Cm(21.0)
        section.page_height = Cm(29.7)
        section.top_margin = Cm(self.config["margins_cm"]["top"])
        section.left_margin = Cm(self.config["margins_cm"]["left"])
        section.bottom_margin = Cm(self.config["margins_cm"]["bottom"])
        section.right_margin = Cm(self.config["margins_cm"]["right"])
        
        # Cover page has different first page (no header/footer)
        section.different_first_page_header_footer = True

        # Configure Base Styles
        styles = self.doc.styles
        normal_style = styles['Normal']
        normal_font = normal_style.font
        normal_font.name = "Times New Roman"
        normal_font.size = Pt(12)
        normal_font.color.rgb = RGBColor(0, 0, 0)

        # Configure Heading 1
        h1_style = styles['Heading 1']
        h1_font = h1_style.font
        h1_font.name = "Times New Roman"
        h1_font.size = Pt(14)
        h1_font.bold = True
        h1_font.color.rgb = RGBColor(0, 0, 0)
        h1_style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        h1_style.paragraph_format.space_before = Pt(12)
        h1_style.paragraph_format.space_after = Pt(12)
        h1_style.paragraph_format.keep_with_next = True

        # Configure Heading 2
        h2_style = styles['Heading 2']
        h2_font = h2_style.font
        h2_font.name = "Times New Roman"
        h2_font.size = Pt(12)
        h2_font.bold = True
        h2_font.color.rgb = RGBColor(0, 0, 0)
        h2_style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
        h2_style.paragraph_format.space_before = Pt(6)
        h2_style.paragraph_format.space_after = Pt(6)
        h2_style.paragraph_format.keep_with_next = True

        # Configure Heading 3
        h3_style = styles['Heading 3']
        h3_font = h3_style.font
        h3_font.name = "Times New Roman"
        h3_font.size = Pt(12)
        h3_font.bold = True
        h3_font.color.rgb = RGBColor(0, 0, 0)
        h3_style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
        h3_style.paragraph_format.space_before = Pt(6)
        h3_style.paragraph_format.space_after = Pt(6)
        h3_style.paragraph_format.keep_with_next = True

    def _add_page_number_field(self, paragraph, num_format="arabic"):
        """Inserts dynamic Word page number XML field into footer in Times New Roman 12pt."""
        paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = paragraph.add_run()
        fldChar1 = parse_xml(r'<w:fldChar %s w:fldCharType="begin"/>' % nsdecls('w'))
        instrText = parse_xml(r'<w:instrText %s xml:space="preserve"> PAGE </w:instrText>' % nsdecls('w'))
        fldChar2 = parse_xml(r'<w:fldChar %s w:fldCharType="separate"/>' % nsdecls('w'))
        fldChar3 = parse_xml(r'<w:fldChar %s w:fldCharType="end"/>' % nsdecls('w'))
        run._r.append(fldChar1)
        run._r.append(instrText)
        run._r.append(fldChar2)
        run._r.append(fldChar3)
        self._apply_strict_run_font(run, size_pt=12)

    def add_cover_page(self, title, subtitle=None, logo_path=None):
        """Builds standardized cover page in Times New Roman."""
        p_title = self.doc.add_paragraph()
        p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_title.paragraph_format.space_before = Pt(24)
        p_title.paragraph_format.space_after = Pt(12)
        r = p_title.add_run(f"LAPORAN PRAKTIK KERJA LAPANGAN\n{title.upper()}")
        self._apply_strict_run_font(r, size_pt=14, bold=True)

        if subtitle:
            p_sub = self.doc.add_paragraph()
            p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_sub.paragraph_format.space_after = Pt(24)
            r_sub = p_sub.add_run(subtitle)
            self._apply_strict_run_font(r_sub, size_pt=11)

        # Logo placeholder or image
        p_logo = self.doc.add_paragraph()
        p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_logo.paragraph_format.space_before = Pt(36)
        p_logo.paragraph_format.space_after = Pt(36)
        if logo_path and os.path.exists(logo_path):
            p_logo.add_run().add_picture(logo_path, width=Cm(4.5))
        else:
            r_logo = p_logo.add_run("[ LOGO INSTANSI / SEKOLAH ]")
            self._apply_strict_run_font(r_logo, size_pt=11, bold=True)

        # Author section
        p_author = self.doc.add_paragraph()
        p_author.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_author.paragraph_format.space_after = Pt(36)
        r_auth_lbl = p_author.add_run("Disusun Oleh:\n")
        self._apply_strict_run_font(r_auth_lbl, size_pt=12, bold=True)
        r_auth_val = p_author.add_run(f"Nama : {self.config['author_name']}\nNISN/NIM : {self.config['author_id']}")
        self._apply_strict_run_font(r_auth_val, size_pt=12)

        # Institutional Identity
        p_inst = self.doc.add_paragraph()
        p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_inst.paragraph_format.space_before = Pt(36)
        r_inst = p_inst.add_run(
            f"{self.config['department_name'].upper()}\n"
            f"{self.config['institution_name'].upper()}\n"
            f"{self.config['city'].upper()}\n"
            f"{self.config['year']}"
        )
        self._apply_strict_run_font(r_inst, size_pt=12, bold=True)

    def start_preliminary_section(self):
        """Creates Section 2 for preliminary pages (Roman lower footer: i, ii, iii...)."""
        sec2 = self.doc.add_section()
        sec2.page_width = Cm(21.0)
        sec2.page_height = Cm(29.7)
        sec2.top_margin = Cm(self.config["margins_cm"]["top"])
        sec2.left_margin = Cm(self.config["margins_cm"]["left"])
        sec2.bottom_margin = Cm(self.config["margins_cm"]["bottom"])
        sec2.right_margin = Cm(self.config["margins_cm"]["right"])
        sec2.header.is_linked_to_previous = False
        sec2.footer.is_linked_to_previous = False
        
        p_footer = sec2.footer.paragraphs[0]
        self._add_page_number_field(p_footer, num_format="roman")

    def start_main_chapters_section(self):
        """Creates Section 3 for Main Chapters (Arabic footer starting at 1)."""
        sec3 = self.doc.add_section()
        sec3.page_width = Cm(21.0)
        sec3.page_height = Cm(29.7)
        sec3.top_margin = Cm(self.config["margins_cm"]["top"])
        sec3.left_margin = Cm(self.config["margins_cm"]["left"])
        sec3.bottom_margin = Cm(self.config["margins_cm"]["bottom"])
        sec3.right_margin = Cm(self.config["margins_cm"]["right"])
        sec3.header.is_linked_to_previous = False
        sec3.footer.is_linked_to_previous = False

        p_footer = sec3.footer.paragraphs[0]
        self._add_page_number_field(p_footer, num_format="arabic")

    def add_approval_page(self, school_supervisor, field_supervisor, headmaster):
        """Adds Lembar Pengesahan page in Times New Roman."""
        self.add_chapter_title("", "LEMBAR PENGESAHAN")
        
        p_info = self.doc.add_paragraph()
        p_info.paragraph_format.line_spacing = 1.5
        p_info.paragraph_format.space_after = Pt(18)
        r_info = p_info.add_run(
            f"Judul Laporan\t: {self.config['title']}\n"
            f"Nama Siswa/i\t: {self.config['author_name']}\n"
            f"NISN / NIM\t: {self.config['author_id']}\n"
            f"Sekolah/Univ\t: {self.config['institution_name']}\n"
            f"Perusahaan/DUDI\t: {self.config['company_name']}"
        )
        self._apply_strict_run_font(r_info, size_pt=12)

        p_agree = self.doc.add_paragraph()
        p_agree.paragraph_format.space_after = Pt(12)
        r_agree = p_agree.add_run("Menyetujui,")
        self._apply_strict_run_font(r_agree, size_pt=12, bold=True)

        # 2-column signature table
        tbl = self.doc.add_table(rows=2, cols=2)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER

        r_l1 = tbl.cell(0, 0).paragraphs[0].add_run("Pembimbing Sekolah,\n\n\n\n( " + school_supervisor + " )\nNIP. [NIP_GURU]")
        self._apply_strict_run_font(r_l1, size_pt=12)
        r_r1 = tbl.cell(0, 1).paragraphs[0].add_run("Pembimbing Lapangan,\n\n\n\n( " + field_supervisor + " )\nNIK/NIP. [NIK_PEMBIMBING]")
        self._apply_strict_run_font(r_r1, size_pt=12)

        p_know = self.doc.add_paragraph()
        p_know.paragraph_format.space_before = Pt(18)
        p_know.paragraph_format.space_after = Pt(36)
        r_know = p_know.add_run("Mengetahui,\nKepala Sekolah / Ketua Program Keahlian,")
        self._apply_strict_run_font(r_know, size_pt=12, bold=True)
        
        p_head = self.doc.add_paragraph()
        p_head.paragraph_format.keep_with_next = True
        r_head = p_head.add_run(f"( {headmaster} )\nNIP. [NIP_KEPALA_SEKOLAH]")
        self._apply_strict_run_font(r_head, size_pt=12)

        self.doc.add_page_break()

    def add_foreword_page(self, content_paragraphs):
        """Adds Kata Pengantar page in Times New Roman."""
        self.add_chapter_title("", "KATA PENGANTAR")
        
        for para_text in content_paragraphs:
            p = self.doc.add_paragraph()
            p.paragraph_format.line_spacing = 1.5
            p.paragraph_format.space_after = Pt(6)
            p.paragraph_format.first_line_indent = Cm(1.27)
            p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            r = p.add_run(para_text)
            self._apply_strict_run_font(r, size_pt=12)

        p_sig = self.doc.add_paragraph()
        p_sig.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        p_sig.paragraph_format.space_before = Pt(24)
        r_sig = p_sig.add_run(f"{self.config['city']}, {self.config['year']}\nPenulis,\n\n\n\n{self.config['author_name']}")
        self._apply_strict_run_font(r_sig, size_pt=12)

        self.doc.add_page_break()

    def add_table_of_contents_placeholder(self):
        """Adds Table of Contents preliminary page."""
        self.add_chapter_title("", "DAFTAR ISI")
        p = self.doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(24)
        p.paragraph_format.space_after = Pt(24)
        r = p.add_run("[DAFTAR ISI OTOMATIS MICROSOFT WORD]")
        self._apply_strict_run_font(r, size_pt=12, bold=True)
        self.doc.add_page_break()

    def add_chapter_title(self, chapter_number_str, title_str):
        """Adds Chapter Heading in Times New Roman 14 pt Bold Centered."""
        p = self.doc.add_paragraph(style='Heading 1')
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        full_title = f"{chapter_number_str.upper()}\n{title_str.upper()}" if chapter_number_str else title_str.upper()
        r = p.add_run(full_title)
        self._apply_strict_run_font(r, size_pt=14, bold=True)

    def add_section_heading(self, level, number_str, title_str):
        """Adds Sub-heading in Times New Roman 12 pt Bold Left."""
        style_name = 'Heading 2' if level == 2 else 'Heading 3'
        p = self.doc.add_paragraph(style=style_name)
        r = p.add_run(f"{number_str} {title_str}")
        self._apply_strict_run_font(r, size_pt=12, bold=True)

    def add_body_paragraph(self, text):
        """Adds regular body paragraph complying with 12 pt Times New Roman, 1.5 line spacing, justified, 1.27cm indent."""
        p = self.doc.add_paragraph()
        p.paragraph_format.line_spacing = 1.5
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.first_line_indent = Cm(1.27)
        p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        r = p.add_run(text)
        self._apply_strict_run_font(r, size_pt=12)

    def add_table_with_caption(self, caption_text, headers, rows_data):
        """Adds table with Times New Roman font, cell padding, and caption above table."""
        p_cap = self.doc.add_paragraph()
        p_cap.paragraph_format.space_before = Pt(6)
        p_cap.paragraph_format.space_after = Pt(4)
        p_cap.paragraph_format.keep_with_next = True
        r_cap = p_cap.add_run(caption_text)
        self._apply_strict_run_font(r_cap, size_pt=11, bold=True)

        tbl = self.doc.add_table(rows=len(rows_data) + 1, cols=len(headers))
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER

        hdr_cells = tbl.rows[0].cells
        for i, header_text in enumerate(headers):
            hdr_cells[i].text = header_text
            p = hdr_cells[i].paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            if p.runs:
                self._apply_strict_run_font(p.runs[0], size_pt=11, bold=True)

        for r_idx, row in enumerate(rows_data):
            row_cells = tbl.rows[r_idx + 1].cells
            for c_idx, val in enumerate(row):
                row_cells[c_idx].text = str(val)
                p = row_cells[c_idx].paragraphs[0]
                if p.runs:
                    self._apply_strict_run_font(p.runs[0], size_pt=11)

    def save(self, filepath):
        """Saves document to designated absolute output path."""
        os.makedirs(os.path.dirname(os.path.abspath(filepath)), exist_ok=True)
        self.doc.save(filepath)
        return filepath

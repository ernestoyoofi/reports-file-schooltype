# reports-file-schooltype: Indonesian School & University Report Generator

`reports-file-schooltype` is a production-grade AI Agent skill designed to automate the creation, structuring, drafting, formatting, validation, and export of Indonesian school and university reports in editable Microsoft Word (`.docx`) format.

---

## 1. Features & Capabilities

- **8 Supported Report Types**:
  1. `pkl`: Laporan Praktik Kerja Lapangan / Magang / Prakerin (SMK, D3, S1).
  2. `skripsi`: Skripsi / Tugas Akhir / Thesis (D4, S1, S2).
  3. `makalah`: Makalah Akademik / Class Paper.
  4. `proposal`: Proposal Penelitian / Proposal Kegiatan.
  5. `proyek`: Laporan Proyek / Project Report.
  6. `laporan_kegiatan`: Laporan Kegiatan Sekolah / Instansi (RKAS, activity report).
  7. `research`: Laporan Penelitian / Research Report.
  8. `paper`: Scientific Paper / Jurnal.

- **Strict Compliance with Layout & Academic Standards**:
  - **Font Family**: **Times New Roman ONLY** (Strictly enforced; no other font family permitted).
  - **Base Font Size**: **12 pt** for all body paragraphs, sub-headings, and signature lines.
  - Paper: A4 (21.0 x 29.7 cm).
  - Binding Margins (4-4-3-3 Rule): Top: 4.0 cm, Left: 4.0 cm, Bottom: 3.0 cm, Right: 3.0 cm.
  - Line Spacing: 1.5 lines, 6 pt space after, justified alignment.
  - Section Breaks & Dual Pagination:
    - Preliminary Pages (Pengesahan, Kata Pengantar, Daftar Isi): Lowercase Roman numerals (`i, ii, iii...`), bottom center in Times New Roman 12 pt.
    - Main Chapters (BAB I to End, Daftar Pustaka, Lampiran): Arabic numerals (`1, 2, 3...`), bottom center starting at 1 in Times New Roman 12 pt.

---

## 2. Directory Structure

```text
reports-file-schooltype/
├── SKILL.md                          # Primary AI Agent skill activation definition
├── README.md                         # Installation & usage documentation
├── assets/                           # Reusable report templates & JSON configs
│   ├── REPORTS_TEMPLATE_PKL.md
│   └── default_institutional_profile.json
├── references/                       # Research guides & playbooks
│   ├── sample-analysis.md            # Empirical sample inspection analysis
│   ├── report-type-registry.md       # Master registry of 8 report types
│   ├── indonesian-academic-writing-guide.md
│   ├── foreword-writing-playbook.md
│   ├── institutional-formatting-guidelines.md
│   └── citations-and-bibliography-guide.md
├── scripts/                          # DOCX generation & validation utilities
│   ├── docx_builder.py
│   └── validate_report.py
└── tests/                            # Automated pytest test suite
    ├── test_docx_builder.py
    ├── test_validate_report.py
    └── test_report_types.py
```

---

## 3. Usage Instructions

### Primary Invocation
```text
/reports-file-schooltype <report-type>
```

### Examples
- `/reports-file-schooltype pkl`
- `/reports-file-schooltype skripsi`
- `/reports-file-schooltype makalah`
- `/reports-file-schooltype proposal`
- `/reports-file-schooltype proyek`

---

## 4. Testing & Validation

Run the automated pytest test suite:
```bash
PYTHONPATH=reports-file-schooltype pytest reports-file-schooltype/tests
```

Validate a generated `.docx` file:
```bash
python3 reports-file-schooltype/scripts/validate_report.py path/to/generated_report.docx
```

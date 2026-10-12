# Empirical Sample Analysis & Evidence Report

## 1. Overview & Inspection Methodology

This document presents the detailed empirical analysis of seven sample PDF reports from `file-laporan/` and three sample foreword images from `kata-pengantar/`. The analysis forms the foundational evidence base for the `reports-file-schooltype` AI Agent skill.

### Files Inspected
1. **PDF Reports (`file-laporan/`)**:
   - `example-report-file-completed-1.pdf` (37 pages): Comprehensive PKL Report (SMK N 1 Kedungwuni - TKJ at PT Telekomunikasi Indonesia Tbk).
   - `example-report-file-completed-2.pdf` (19 pages): Technical PKL Report (Perakitan & Maintenance PC).
   - `example-report-file-completed-3.pdf` (10 pages): Short Internship Report (PT Boc Indonesia).
   - `example-report-file-completed-4.pdf` (41 pages): School Educational Unit Report (Laporan Satuan Pendidikan / RKAS SMP Bhakti).
   - `example-report-file-completed-5.pdf` (15 pages): Activity Report (Laporan Kegiatan UPT SD Negeri 060946 Medan).
   - `example-report-file-completed-6.pdf` (33 pages): Academic & Institutional Activity Report (SD Negeri 1 Bandengan Jepara).
   - `example-report-file-completed-7.pdf` (13 pages): Administrative PKL Report (Kelurahan Awipari).

2. **Foreword Images (`kata-pengantar/`)**:
   - `example-kata-pengantar-1.jpg`: Formal University Industrial Internship Foreword (ITS Surabaya - D3 Teknik Mesin at PT Alim Ampuhjaya Steel).
   - `example-kata-pengantar-2.png`: Vocational/University PKL Foreword (Lippo Malls Indonesia - Blu Plaza).
   - `example-kata-pengantar-3.jpg`: Non-Profit/Community Internship Foreword (PKPU Balikpapan).

---

## 2. Structural Patterns Across Report Types

### A. PKL / Industrial Internship Reports (Samples 1, 2, 3, 7)
- **Preliminary Pages**: Cover Page, Lembar Pengesahan (Approval Page by School & Industry Supervisors), Kata Pengantar (Foreword), Daftar Isi (Table of Contents), Daftar Gambar/Tabel (List of Figures/Tables).
- **Core Chapter Structure**:
  - **BAB I: PENDAHULUAN** (Latar Belakang PKL, Maksud dan Tujuan, Manfaat, Waktu dan Tempat Pelaksanaan).
  - **BAB II: PROFIL PERUSAHAAN / GAMBARAN UMUM** (Sejarah Perusahaan, Visi & Misi, Struktur Organisasi, Bidang Usaha).
  - **BAB III: PELAKSANAAN PRAKTIK KERJA LAPANGAN** (Dasar Teori, Pembahasan Kegiatan / Jurnal Kegiatan, Workflows, Troubleshooting, Tanggung Jawab Jobdesk).
  - **BAB IV: PENUTUP** (Kesimpulan, Saran untuk Sekolah & Perusahaan).
- **Ending Pages**: Daftar Pustaka (References), Lampiran (Appendices: Portofolio Foto, Jurnal Harian, Surat Keterangan).

### B. School & Institutional Reports (Samples 4, 5, 6)
- **Structure**: Cover, Kata Pengantar, Pendahuluan (Latar Belakang & Tujuan), Program Kegiatan / Pelaksanaan, Capaian / Evaluasi & Anggaran (RKAS), Penutup, Lampiran Dokumentasi.
- **Focus**: Operational metrics, activity logs, budget breakdown, photo documentation of events.

---

## 3. Foreword (Kata Pengantar) Structural Breakdown

Analysis of `kata-pengantar/` images reveals a standard 5-part structure:
1. **Opening Religious & Praise Expression**: "Puji dan syukur kami panjatkan kehadirat Allah SWT..."
2. **Context & Purpose Statement**: Stating the internship/report title, institution, department, and company.
3. **Hierarchical Acknowledgments (Ucapan Terima Kasih)**:
   - God / Divine blessings.
   - Parents / Family for moral & financial support.
   - Headmaster / Dean / University Principal.
   - Head of Department / Academic Advisor.
   - Industry Supervisor & Company Management.
   - Colleagues, teachers, and peers.
4. **Humble Disclaimer & Openness to Criticism**: "Penulis menyadari bahwa laporan ini masih jauh dari sempurna..."
5. **Closing Statement, Date, & Signature Block**: Location (e.g. "Medan, 12 Oktober 2026") and Author Name ("Penulis").

---

## 4. Typography, Layout, and Pagination Evidence

1. **Paper & Margins**:
   - Standard size: A4 (21.0 x 29.7 cm).
   - Margins: Top: 4 cm, Left: 4 cm, Bottom: 3 cm, Right: 3 cm (standard 4-4-3-3 rule for binding).
2. **Typography**:
   - Font Family: Times New Roman (or Arial for specific school guidelines).
   - Document Title: 14-16 pt BOLD UPPERCASE.
   - Chapter Headings: 12-14 pt BOLD UPPERCASE (e.g. `BAB I PENDAHULUAN`).
   - Section Headings: 12 pt BOLD Title Case / Uppercase (e.g. `1.1 Latar Belakang`).
   - Body Text: 12 pt Regular, 1.5 line spacing, Justified alignment.
   - First line paragraph indent: 1.0 - 1.27 cm (0.5 inch).
3. **Pagination System**:
   - **Cover Page**: Unnumbered (no visible header/footer).
   - **Preliminary Pages** (Pengesahan, Kata Pengantar, Daftar Isi, Daftar Gambar): Lowercase Roman numerals (`i, ii, iii, iv...`), centered at bottom footer.
   - **Main Content Chapters** (Bab I through Bab IV/V, Daftar Pustaka, Lampiran): Arabic numerals (`1, 2, 3...`), bottom center footer (or top right for non-chapter-start pages if required by institution).

---

## 5. Synthesis into Skill Rules

1. Never generate arbitrary styles; enforce strict semantic Word styles (`Heading 1`, `Heading 2`, `Normal`, `Table Header`).
2. Include placeholder tags `[NAME]`, `[NISN/NIM]`, `[COMPANY_NAME]`, `[DATE]` when exact user input is missing.
3. Enforce valid section breaks (`next_page`) between preliminary pages and Chapter 1 to restart page numbering from Roman to Arabic.

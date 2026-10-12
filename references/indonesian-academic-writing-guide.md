# Indonesian Academic Writing Guide (PUEBI / EYD Standards)

## 1. Overview & Objective

This document outlines the standard Indonesian formal academic writing rules (Pedoman Umum Ejaan Bahasa Indonesia / EYD V) required for generating reports in `reports-file-schooltype`.

---

## 2. Formal Indonesian Language Rules

### 2.1 Passive Voice vs. Active First Person
- **Prohibited**: Do NOT use personal pronouns like `saya`, `aku`, `kami`, `kita` in body text paragraphs (except in Kata Pengantar acknowledgments).
- **Required**: Use passive or objective formal phrasing:
  - *Incorrect*: "Saya melakukan instalasi sistem operasi Windows 11."
  - *Correct*: "Instalasi sistem operasi Windows 11 dilakukan pada laboratorium komputer."
  - *Incorrect*: "Kami mengumpulkan data melalui wawancara."
  - *Correct*: "Pengumpulan data dilakukan melalui wawancara terstruktur."

### 2.2 Standard Academic Connectives and Sentence Structure
- Use standard academic conjunctions at paragraph transitions:
  - *Penambahan*: `Selain itu,`, `Di samping itu,`, `Selanjutnya,`
  - *Sebab-Akibat*: `Oleh karena itu,`, `Hal ini mengakibatkan,`, `Sejalan dengan hal tersebut,`
  - *Pertentangan*: `Namun demikian,`, `Meskipun demikian,`, `Di sisi lain,`
  - *Kesimpulan*: `Berdasarkan uraian tersebut, dapat disimpulkan bahwa...`

### 2.3 Foreign Terms and Italicization
- All foreign terms (English, technical jargon, Latin terms) must be formatted in *Italics*.
  - Examples: *troubleshooting*, *hardware*, *software*, *database*, *setup*, *user interface*, *et al.*
- Indonesian loanwords that have been standardized in KBBI must be written in normal upright font:
  - Examples: *kamera*, *sistem*, *objek*, *analisis*, *kualitas*, *efektivitas*.

---

## 3. Paragraph Formatting and Spacing

1. **Paragraph Alignment**: Fully Justified (`justify`).
2. **First Line Indentation**: 1.0 cm to 1.27 cm (0.5 in).
3. **Line Spacing**: 1.5 lines.
4. **Paragraph Spacing**: 0 pt before, 6 pt after (or 0 pt before/after if blank line is used).
5. **No Orphan/Widow Lines**: Heading lines must stay with the next paragraph (`keep_with_next = True`).

---

## 4. Section & Table/Figure Caption Naming Rules

1. **Chapter Titles**: Bold Uppercase, centered (e.g. `BAB I\nPENDAHULUAN`).
2. **Level 1 Subsections**: Bold Titlecase, numbered with chapter prefix (e.g. `1.1 Latar Belakang`).
3. **Level 2 Subsections**: Bold Titlecase, numbered with level 1 prefix (e.g. `1.1.1 Latar Belakang Masalah`).
4. **Table Captions**: Placed ABOVE the table, aligned left or center, numbered per chapter (e.g. `Tabel 3.1 Spesifikasi Perangkat Harddisk`).
5. **Figure Captions**: Placed BELOW the figure, centered, numbered per chapter (e.g. `Gambar 2.1 Topologi Jaringan Local Area Network`).
6. **Sources**: Placed directly below the table/figure in 10 pt italics (e.g. *Sumber: Dokumentasi Penulis, 2026*).

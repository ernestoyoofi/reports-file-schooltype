# Indonesian School & University Report Type Registry

## 1. Overview

This registry defines the mandatory structural configurations, chapter schemas, required preliminary pages, and validation metadata for all supported Indonesian report types in `reports-file-schooltype`.

---

## 2. Report Types Master Table

| Report Type Code | Formal Name | Target Institution Level | Standard Chapter Count | Core Focus |
| :--- | :--- | :--- | :--- | :--- |
| `pkl` | Laporan Praktik Kerja Lapangan (PKL) / Magang | SMK / D3 / S1 | 4 - 5 Chapters | Practical experience, company profile, daily jobdesk, troubleshooting, logs. |
| `skripsi` | Laporan Skripsi / Tugas Akhir | D4 / S1 / S2 | 5 Chapters | Scientific research, methodology, empirical data analysis, thesis defense. |
| `makalah` | Makalah Akademik / Paper Class | SMP / SMA / SMK / S1 | 3 Chapters | Literature review, topic analysis, discussion, conclusion. |
| `proposal` | Proposal Penelitian / Proposal Kegiatan | SMK / S1 / Organization | 3 - 4 Chapters | Plan, research background, proposed methodology, timeline, budget. |
| `proyek` | Laporan Proyek / Project Report | SMK / D3 / S1 | 4 Chapters | Product/system development, engineering design, implementation, testing. |
| `laporan_kegiatan` | Laporan Kegiatan Sekolah / Instansi | Sekolah / Instansi | 4 Chapters | Activity implementation, committee rundown, financial report (RKAS), photos. |
| `research` | Laporan Penelitian / Research Report | High School / Univ | 5 Chapters | Independent research, experimental findings, statistical analysis. |
| `paper` | Scientific Paper / Jurnal | S1 / S2 | IMRaD format | Introduction, Methods, Results, and Discussion. |

---

## 3. Detailed Structural Schemas

### 3.1 PKL / Internship (`pkl`)
- **Preliminary Pages**: Cover, Halaman Pengesahan Sekolah, Halaman Pengesahan Industri, Kata Pengantar, Daftar Isi, Daftar Gambar, Daftar Tabel, Daftar Lampiran.
- **Chapter Outline**:
  - `BAB I PENDAHULUAN`: Latar Belakang, Maksud & Tujuan, Manfaat, Waktu & Tempat Pelaksanaan.
  - `BAB II GAMBARAN UMUM PERUSAHAAN`: Sejarah Instansi, Visi & Misi, Struktur Organisasi, Tata Tertib & Bidang Usaha.
  - `BAB III PELAKSANAAN PRAKTIK KERJA LAPANGAN`: Dasar Teori, Uraian Kegiatan / Pembahasan Pekerjaan, Kendala & Pemecahan Masalah (Troubleshooting).
  - `BAB IV PENUTUP`: Kesimpulan, Saran (Untuk Sekolah & Untuk Instansi/DUDI).
- **Required Appendices**: Jurnal Harian PKL, Fotokopi Surat Keterangan / Sertifikat, Foto Dokumentasi Kegiatan.

### 3.2 Skripsi / Thesis (`skripsi`)
- **Preliminary Pages**: Cover, Halaman Judul, Halaman Pernyataan Keaslian, Halaman Pengesahan Penguji & Pembimbing, Abstrak (Indonesian & English), Kata Pengantar, Daftar Isi, Daftar Gambar, Daftar Tabel, Daftar Singkatan.
- **Chapter Outline**:
  - `BAB I PENDAHULUAN`: Latar Belakang Masalah, Identifikasi Masalah, Rumusan Masalah, Batasan Masalah, Tujuan Penelitian, Manfaat Penelitian.
  - `BAB II TINJAUAN PUSTAKA`: Landasan Teori, Penelitian Relevan, Kerangka Pemikiran, Hipotesis (jika kuantitatif).
  - `BAB III METODE PENELITIAN`: Jenis Penelitian, Populas & Sampel / Subjek, Teknik Pengumpulan Data, Instrumen Penelitian, Teknik Analisis Data.
  - `BAB IV HASIL DAN PEMBAHASAN`: Deskripsi Data, Analisis Data / Pengujian Hipotesis, Pembahasan Hasil Penelitian.
  - `BAB V PENUTUP`: Kesimpulan, Implikasi, Saran.
- **Required Backmatter**: Daftar Pustaka (APA/IEEE style), Lampiran Instrumen, Data Mentah, Surat Izin Penelitian.

### 3.3 Makalah (`makalah`)
- **Preliminary Pages**: Cover, Kata Pengantar, Daftar Isi.
- **Chapter Outline**:
  - `BAB I PENDAHULUAN`: Latar Belakang, Rumusan Masalah, Tujuan Penulisan, Manfaat Penulisan.
  - `BAB II PEMBAHASAN`: Kaji Literatur, Analisis Topik Utama, Sub-pembahasan Topik A, Sub-pembahasan Topik B.
  - `BAB III PENUTUP`: Kesimpulan, Saran.
- **Backmatter**: Daftar Pustaka.

### 3.4 Proposal (`proposal`)
- **Preliminary Pages**: Cover, Halaman Pengesahan Proposal, Kata Pengantar, Daftar Isi.
- **Chapter Outline**:
  - `BAB I PENDAHULUAN`: Latar Belakang, Maksud & Tujuan Kegiatan/Penelitian, Ruang Lingkup.
  - `BAB II RENCANA KEGIATAN / METODOLOGI`: Rencana Pelaksanaan, Metode Work Plan, Susunan Panitia / Peneliti.
  - `BAB III JADWAL DAN ANGGARAN BIAYA`: Timeline Kegiatan (Gantt Chart), Rincian Anggaran Biaya (RAB).
  - `BAB IV PENUTUP`: Harapan & Permohonan Persetujuan.

### 3.5 Project Report (`proyek`)
- **Preliminary Pages**: Cover, Lembar Pengesahan Project Lead & Advisor, Kata Pengantar, Daftar Isi, Abstrak Ringkas.
- **Chapter Outline**:
  - `BAB I PENDAHULUAN`: Latar Belakang Proyek, Tujuan & Spesifikasi Proyek, Batasan Sistem.
  - `BAB II PERANCANGAN SISTEM / PRODUCT DESIGN`: Arsitektur Sistem, Perancangan Hardware/Software/UI, Diagram Workflow/ERD/UML.
  - `BAB III IMPLEMENTASI DAN PENGUJIAN`: Tahap Pembentukan / Coding / Assembly, Hasil Testing (Unit/Integration Test, Acceptance Criteria).
  - `BAB IV PENUTUP`: Kesimpulan Kinerja Proyek, Rencana Pengembangan Selanjutnya.

### 3.6 School Activity Report (`laporan_kegiatan`)
- **Preliminary Pages**: Cover, Lembar Pengesahan Kepala Sekolah & Ketua Panitia, Kata Pengantar, Daftar Isi.
- **Chapter Outline**:
  - `BAB I PENDAHULUAN`: Latar Belakang Kegiatan, Nama & Tema Kegiatan, Tujuan Kegiatan.
  - `BAB II PELAKSANAAN KEGIATAN`: Waktu & Tempat, Rundown Acara, Susunan Panitia, Peserta Kegiatan.
  - `BAB III CAPAIAN DAN LAPORAN KEUANGAN`: Evaluasi Pelaksanaan, Laporan Realisasi Anggaran.
  - `BAB IV PENUTUP`: Kesimpulan & Rekomendasi Kegiatan Mendatang.
- **Appendices**: Foto Kegiatan, Bukti Nota & Kwitansi, Daftar Hadir.

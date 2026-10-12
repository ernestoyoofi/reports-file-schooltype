import pytest

SUPPORTED_TYPES = ["pkl", "skripsi", "makalah", "proposal", "proyek", "laporan_kegiatan", "research", "paper"]

def test_supported_report_types():
    assert len(SUPPORTED_TYPES) == 8
    for rtype in ["pkl", "skripsi", "makalah", "proposal", "proyek"]:
        assert rtype in SUPPORTED_TYPES

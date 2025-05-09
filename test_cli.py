import pytest
from cli import get_file_size_in_mb
import os

def test_2mb_file(tmp_path):
    """Test correct size calculation for a 2MB file."""
    test_file = tmp_path / "test.txt"
    test_file.write_text("a" * (1024 * 1024 * 2))  # 2MB
    assert get_file_size_in_mb(str(test_file)) == 2

def test_empty_file(tmp_path):
    """Test 0-byte file."""
    test_file = tmp_path / "empty.txt"
    test_file.write_text("")
    assert get_file_size_in_mb(str(test_file)) == 0

def test_nonexistent_file():
    """Test FileNotFoundError."""
    with pytest.raises(FileNotFoundError):
        get_file_size_in_mb("nonexistent.txt")

def test_directory_path(tmp_path):
    """Test ValueError for directory inputs."""
    with pytest.raises(ValueError):
        get_file_size_in_mb(str(tmp_path))

def test_verbose_output(capsys, tmp_path):
    """Test verbose mode prints progress."""
    test_file = tmp_path / "verbose.txt"
    test_file.write_text("test")
    get_file_size_in_mb(str(test_file), verbose=True)
    captured = capsys.readouterr()
    assert "Calculating size" in captured.out
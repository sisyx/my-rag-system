import pytest
from chunker import chunk_text

def test_normal_input():
    assert chunk_text("111122223333444455556666", 4, 1) == ["11112", "122223", "233334", "344445", "455556", "56666"], "Normal input produces the expected number of chunks"

def test_empty_string():
    assert chunk_text("", 4, 1) == [], "Empty string input"

def test_string_shorter_than_chunk_size():
    assert chunk_text("111", 4, 1) == ["111"], "A text shorter than chunk_size still produces at least one chunk"

def test_overlap_boundaries():
    chunks = chunk_text("111122223333", 4, 1)
    assert chunks[0][-2:] == chunks[1][:2]
    assert chunks[1][-2:] == chunks[2][:2]

def test_overlap_bt_chunk_size():
    with pytest.raises(ValueError): 
        chunk_text("111", 4, 5)
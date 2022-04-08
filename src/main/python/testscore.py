import pytest
import core
import pathlib
import logging

logging.basicConfig(filename='test.log', encoding='utf-8', level=logging.DEBUG, filemode='w')

def test_can_make_folders(tmp_path,caplog):
    caplog.set_level(logging.DEBUG)
    # tmp_path should be clean, between tests.
    test1 = tmp_path / "music"
    assert not test1.exists()
        
    # create directories
    core.mkdirs(tmp_path)

    test2 = tmp_path / "music"
    assert test2.exists()
    
    

def test_can_move_files(tmp_path,caplog):
    caplog.set_level(logging.DEBUG)

    (tmp_path / "test.pdf").touch()
    assert (tmp_path / "test.pdf").exists()
    core.mkdirs(tmp_path)
    core.move_files(tmp_path)
    assert (tmp_path / "documents" / "test.pdf").exists()
    assert not (tmp_path / "test.pdf").exists()


def test_doesnt_touch_unknown_files(tmp_path,caplog):
    caplog.set_level(logging.DEBUG)

    (tmp_path / "test.nyxie").touch()
    assert (tmp_path / "test.nyxie").exists()
    core.mkdirs(tmp_path)
    core.move_files(tmp_path)
    assert (tmp_path / "test.nyxie").exists()

def test_skips_recurisive_by_default(tmp_path, caplog):
    caplog.set_level(logging.DEBUG)
    (tmp_path / "donttouch").mkdir()
    t = (tmp_path / "donttouch" / "secret.pdf")
    t.touch()
    assert t.exists()
    core.mkdirs(tmp_path)
    core.move_files(tmp_path)
    assert t.exists()
    assert not (tmp_path / "documents" / "secret.pdf").exists()

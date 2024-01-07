"""Tests for the outpy/file_base.py file."""

import os

import pytest

from outpy.file import File


class TestFile:
    @pytest.fixture()
    def file(self, temporary_file):
        return File(temporary_file)

    def test_file_is_initialised(self, file):
        assert os.path.isfile(file.path)

    def test_write_to_file(self, file):
        file.write("this is a test function")
        assert file.read() == "this is a test function"

    def test_append_to_file(self, file):
        file.append("line 1")
        file.append("line 2")
        assert file.read() == "line 1line 2"

    def test_clear_file(self, file):
        file.write("this is a test")
        file.clear()
        assert file.read() == ""

    def test_write_to_file_overwrites_content(self, file):
        file.write("this is a test")
        file.write("this should overwrite the contents")
        assert file.read() == "this should overwrite the contents"

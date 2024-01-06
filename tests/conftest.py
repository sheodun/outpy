"""The pytest fixtures used in the unit tests."""

import pytest


@pytest.fixture(scope="function")
def temporary_file(tmp_path):
    """Return the file path for `test_file.txt`.

    Returns:
        The temporary_path/to_file/test_file.txt.
    """
    temp_dir = tmp_path / "temp"
    temp_dir.mkdir()

    temp_file = temp_dir / "test_file.txt"
    return str(temp_file)

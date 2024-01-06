"""The file_base module.

File - the base file class
"""

from typing import Generator

from outpy.decorators import open_file


class File:
    """Base file class for handling file opening/closing roles.

    Attributes:
        path: a string with the file path and file name.
    """

    def __init__(self, path: str):
        """Initialise the File class with the file path and name."""
        self._path = path

    @property
    def path(self) -> str:
        """Return the file path with the file name."""
        return self._path

    @open_file("w")
    def clear(file) -> None:
        """Write an empty file."""
        file.write("")

    @open_file("w")
    def write(file, text: str) -> None:
        """Write a string to the file.

        This method will overwrite the contents of the file.

        Args:
            text: the string to write to the file.
        """
        file.write(text)

    @open_file("a")
    def append(file, text: str) -> None:
        """Append a string to the file.

        Args:
            text: the string to append to the file.
        """
        file.write(text)

    @open_file("r")
    def read(file) -> str:
        """Return the text in the file.

        Returns:
            The file contents as a string.
        """
        return file.read()

    @open_file("r")
    def readlines(file) -> Generator[str, None, None]:
        """Return each line of the file.

        Returns:
            Each line of the file as a generator. Can handle
            large files.
        """
        return file.readlines()

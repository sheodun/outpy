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
        self.write("")  # Initialise an empty file.

    @property
    def path(self) -> str:
        """Return the file path with the file name."""
        return self._path

    @open_file("w")
    def clear(self, file: str) -> None:
        """Write an empty file.

        Args:
            file: path to the file.
        """
        file.write("")

    @open_file("w")
    def write(self, file: str, text: str) -> None:
        """Write a string to the file.

        This method will overwrite the contents of the file.

        Args:
            file: path to the file.
            text: the string to write to the file.
        """
        file.write(text)

    @open_file("a")
    def append(self, file: str, text: str) -> None:
        """Append a string to the file.

        Args:
            file: path to the file.
            text: the string to append to the file.
        """
        file.write(text)

    @open_file("r")
    def read(self, file: str) -> str:
        """Return the text in the file.

        Args:
            file: path to the file.

        Returns:
            The file contents as a string.
        """
        return file.read()

    @open_file("r")
    def readlines(self, file: str) -> Generator[str, None, None]:
        """Return each line of the file.

        Args:
            file: path to the file.

        Returns:
            Each line of the file as a generator. Can handle
            large files.
        """
        return file.readlines()

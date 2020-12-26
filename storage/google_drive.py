from pathlib import Path

from config import BlackBox
from storage._base import BlackBoxStorageProvider


class GoogleDrive(BlackBoxStorageProvider):
    enabled = BlackBox.gdrive_enabled

    def sync(self, file_path: Path) -> None:
        """Sync a file to Google Drive."""
        raise NotImplementedError

    def rotate(self) -> None:
        """
        Rotate the files in the storage provider.

        This deletes all files older than `rotation_days` days old, as long as
        those files fit certain regular expressions. We don't want to delete
        files that are not related to backup or logging.
        """
        raise NotImplementedError


if __name__ == "__main__":
    gdrive = GoogleDrive()

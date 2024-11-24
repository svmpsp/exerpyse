import shutil
from pathlib import Path

from .utils import get_datadir_path


class FileManager:
    def __init__(self, output_path: str = "./exerpyses"):
        self._exercise_folder = Path(output_path)
        self._source_folder = get_datadir_path() / "exercises"

    def _check_setup(self):
        folder_exists = self._exercise_folder.exists()
        return folder_exists and all(
            filepath.exists()
            for filepath in [
                self._exercise_folder / ex_path.name
                for ex_path in self._source_folder.glob("./*.py")
            ]
        )

    def clear_exercises(self):
        shutil.rmtree(self._exercise_folder)

    def setup_exercises(self):
        if self._check_setup():
            return

        self._exercise_folder.mkdir(parents=True, exist_ok=True)

        for filepath in self._source_folder.glob("./*.py"):
            dest = self._exercise_folder / filepath.name
            if not dest.exists():
                shutil.copy2(filepath, dest)

from pathlib import Path

from .console import ConsolePrinter

class FileManager:

    def __init__(self, console: ConsolePrinter):
        self._exercise_folder = Path("./exerpyses")
        self._console = console

    def _check_setup(self):
        return self._exercise_folder.exists()
    
    def setup_exercises(self):
        if self._check_setup():
            return
        self._console.print_setup()
        self._exercise_folder.mkdir(parents=True, exist_ok=False)

def create_folder_if_not_exists(path: Path):
    pass

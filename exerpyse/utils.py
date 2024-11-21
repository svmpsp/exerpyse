from pathlib import Path


def get_datadir_path() -> Path:
    return Path(__file__).parent / "include"

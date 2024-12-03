from pathlib import Path


def get_datadir_path() -> Path:
    return Path(__file__).parent / "include"


def get_exerpyse_paths() -> list[Path]:
    return sorted(
        [
            path
            for path in Path("./exerpyses").glob("./*.py")
            if not "__init__.py" in str(path)
        ]
    )

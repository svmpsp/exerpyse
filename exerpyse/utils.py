from pathlib import Path


def get_datadir_path() -> Path:
    return Path(__file__).parent / "include"


def get_exerpyse_path_from_id(exerpyse_id: int) -> Path:
    return Path(f"./exerpyses/ex{exerpyse_id:02d}.py")


def get_exerpyse_paths() -> list[Path]:
    return sorted(
        [
            path
            for path in Path("./exerpyses").glob("./*.py")
            if "__init__.py" not in str(path)
        ]
    )

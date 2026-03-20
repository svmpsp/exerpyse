from pathlib import Path


def get_datadir_path() -> Path:
    return Path(__file__).parent / "include"


def get_exerpyse_paths() -> list[Path]:
    return sorted(
        [
            path
            for path in Path("./exerpyses").glob("./*.py")
            if "__init__.py" not in str(path)
        ]
    )


def get_exerpyse_path_from_id(exercise_id: int) -> Path:
    return Path(f"./exerpyses/ex{exercise_id:02d}.py")

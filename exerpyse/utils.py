from pathlib import Path


def get_datadir_path() -> Path:
    return Path(__file__).parent / "include"


def get_exerpyse_path_from_id(exerpyse_id: int) -> Path:
    return Path(f"./exerpyses/ex{exerpyse_id:02}.py")

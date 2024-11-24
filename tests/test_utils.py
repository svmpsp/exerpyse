from pathlib import Path

from exerpyse.utils import get_exerpyse_path_from_id


def test_get_exerpyse_path_from_id():
    expected_path = Path("./exerpyses/ex09.py")
    assert get_exerpyse_path_from_id(9) == expected_path

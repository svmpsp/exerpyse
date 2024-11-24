"""Runs exercises and check whether the results are correct.

Stops at the first failing test.
"""
import sys

from .utils import get_exerpyse_path_from_id


class ExerpyseRunner:
    def load_exercise(self, exerpyse_id: int = 1):
        sys.path.append(str(get_exerpyse_path_from_id(exerpyse_id)))

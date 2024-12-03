"""Runs exercises and check whether the results are correct.

Stops at the first failing test.
"""
import importlib
import sys
from pathlib import Path

from .console import ConsolePrinter
from .tests import TEST_SUITE
from .utils import get_exerpyse_paths


class ExerpyseRunner:
    def __init__(self, console: ConsolePrinter) -> None:
        self._console = console

    def _test_exercise(self, impl, tests):
        for test in tests:
            test(impl)

    def _run_exercise(self, ex_path: Path):
        sys.path.append(str(ex_path))

        mod_name = ex_path.stem
        ex_mod = importlib.import_module(f"exerpyses.{mod_name}")
        self._test_exercise(ex_mod.do_things, tests=TEST_SUITE[ex_path.name])
        sys.path.remove(str(ex_path))

    def run(self) -> bool:
        for path in get_exerpyse_paths():
            try:
                self._console.start_exercise(path)
                self._run_exercise(path)
                self._console.end_exercise(path)
            except ValueError:
                self._console.abort_exercise(path)
                return False
        return True

"""Compatibility entry point: the actor check verifies exact copy and invariant text/background pixels."""
from pathlib import Path
import runpy
runpy.run_path(str(Path(__file__).resolve().with_name('check-actors.py')),run_name='__main__')

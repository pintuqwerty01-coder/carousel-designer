"""Render selected slides with lossless H.264 to preserve static text pixels."""
import importlib.util, pathlib, sys

project=pathlib.Path(__file__).resolve().parent
renderer=project.parents[1]/'art-carousel-kit'/'scripts'/'render.py'
spec=importlib.util.spec_from_file_location('kit_renderer',renderer)
module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
original=module.sh
def sh(cmd,cwd):
    if ' render --quality delivery ' in cmd:
        cmd+=' --crf 0'
    return original(cmd,cwd)
module.sh=sh
raise SystemExit(module.main(project,sys.argv[1].split(',') if len(sys.argv)>1 else None))

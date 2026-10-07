"""Use the kit's unchanged renderer with supported lossless encoding for static-copy validation."""
import importlib.util,pathlib,sys
spec=importlib.util.spec_from_file_location('renderkit','/workspace/art-carousel-kit/scripts/render.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
original=m.sh
def sh(cmd,cwd):
 if ' render --quality delivery ' in cmd:cmd+=' --crf 0'
 return original(cmd,cwd)
m.sh=sh
raise SystemExit(m.main(pathlib.Path(__file__).resolve().parent,sys.argv[1].split(',') if len(sys.argv)>1 else None))

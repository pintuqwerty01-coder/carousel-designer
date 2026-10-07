"""Copy approved text/photo layouts with their articulated 2D actor scenes to the video workspace."""
from pathlib import Path
import shutil
p=Path(__file__).resolve().parent;m=p/'motion'
shutil.copytree(p/'slides/assets',m/'slides/assets',dirs_exist_ok=True)
for n in range(1,7):shutil.copy2(p/f'slides/slide-{n:02d}.html',m/f'slides/slide-{n:02d}.html')
print('Six real 2D character animation sources copied; photographic backgrounds are stationary')

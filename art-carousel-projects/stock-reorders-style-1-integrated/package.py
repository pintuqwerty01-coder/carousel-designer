"""Package the eight native-size slide masters, stills and review copies."""
import io, json, pathlib, subprocess, zipfile
from PIL import Image, ImageChops, ImageStat

P=pathlib.Path(__file__).resolve().parent
proof=P/'proof'
delivery=P/'delivery'
delivery.mkdir(exist_ok=True)
videos=[P/'render'/'out'/f'slide-{n:02}.mp4' for n in range(1,9)]
export_frames=[]
export_checks=[]
for video in videos:
    info=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(video)]))
    stream=info['streams'][0]
    assert (stream['width'],stream['height'],int(stream['nb_frames']))==(1080,1350,120)
    assert float(info['format']['duration'])==4
    data=subprocess.check_output(['ffmpeg','-v','error','-ss','3.7','-i',str(video),'-frames:v','1','-f','image2pipe','-vcodec','png','-'])
    actual=Image.open(io.BytesIO(data)).convert('RGB')
    expected=Image.open(P/'stills'/f'{video.stem}.png').convert('RGB')
    error=sum(ImageStat.Stat(ImageChops.difference(actual,expected)).mean)/3
    assert error<6,(video.name,error)
    export_frames.append(actual)
    export_checks.append({'slide':video.stem,'actual_export_background_and_design':'matches approved-layout still','mean_rgb_pixel_error':round(error,3)})
(proof/'export-validation.json').write_text(json.dumps(export_checks,indent=2)+'\n')
cmd=['ffmpeg','-v','error','-y']
for video in videos:cmd+=['-i',str(video)]
cmd+=['-filter_complex',''.join(f'[{i}:v]' for i in range(8))+'concat=n=8:v=1:a=0[v]','-map','[v]','-c:v','libx264','-crf','16','-preset','medium','-pix_fmt','yuv420p','-movflags','+faststart','-threads','2',str(proof/'ART-stock-reorders-v5-preview.mp4')]
subprocess.run(cmd,check=True)
subprocess.run(['ffmpeg','-v','error','-y','-i',str(videos[4]),'-filter_complex','fps=12,scale=540:675:flags=lanczos,split[a][b];[a]palettegen=stats_mode=diff[p];[b][p]paletteuse=dither=sierra2_4a','-loop','0',str(proof/'slide-05-threshold-v5.gif')],check=True)
images=[]
storyboard=Image.new('RGB',(1440,900),'#DDE8EC')
for n in range(1,9):
    im=Image.open(P/'stills'/f'slide-{n:02}.png').convert('RGB')
    assert im.size==(1080,1350)
    im.save(delivery/f'slide-{n:02}.jpg',quality=98,subsampling=0,dpi=(300,300))
    images.append(im)
    storyboard.paste(export_frames[n-1].resize((352,440),Image.Resampling.LANCZOS),(((n-1)%4)*360+4,((n-1)//4)*450+5))
images[0].save(delivery/'ART-stock-reorders-v5.pdf',save_all=True,append_images=images[1:],resolution=72,quality=100,subsampling=0,title='ART stock reorders — Style 1 revision 5')
storyboard.save(proof/'ART-stock-reorders-v5-storyboard.jpg',quality=95)
for n,name in [(1,'cover-video-frame.png'),(5,'threshold-video-frame.png')]:
    subprocess.run(['ffmpeg','-v','error','-y','-ss','3.4','-i',str(videos[n-1]),'-frames:v','1',str(proof/name)],check=True)
with zipfile.ZipFile(delivery/'ART-stock-reorders-v5-all-slides.zip','w',zipfile.ZIP_DEFLATED) as z:
    for n,video in enumerate(videos,1):
        z.write(video,f'videos/slide-{n:02}.mp4')
        z.write(delivery/f'slide-{n:02}.jpg',f'JPEGs/slide-{n:02}.jpg')
    for f in ['README.md','content.json']:z.write(P/f,f)
    z.write(delivery/'ART-stock-reorders-v5.pdf','ART-stock-reorders-v5.pdf')
    z.write(proof/'validation.json','validation.json')
    z.write(proof/'export-validation.json','export-validation.json')
    z.write(proof/'ART-stock-reorders-v5-storyboard.jpg','storyboard.jpg')
print('Packaged 8 MP4s, 8 JPEGs, PDF, storyboard and validation report.')

import bpy, math, os
from mathutils import Vector
bpy.ops.object.select_all(action='SELECT');bpy.ops.object.delete(use_global=False)
s=bpy.context.scene;s.render.engine='BLENDER_EEVEE_NEXT';s.render.resolution_x=680;s.render.resolution_y=1020;s.render.resolution_percentage=100;s.render.fps=30;s.frame_start=1;s.frame_end=120;s.eevee.taa_render_samples=8;s.render.film_transparent=True;s.render.image_settings.file_format='PNG';s.render.image_settings.color_mode='RGBA';s.render.filepath='/workspace/container-3d-frames/'
s.world.color=(.1,.15,.18);s.view_settings.view_transform='AgX'
def mat(name,c,metal=0,rough=.45):
 m=bpy.data.materials.new(name);m.diffuse_color=(*c,1);m.use_nodes=True;bs=m.node_tree.nodes.get('Principled BSDF');bs.inputs['Base Color'].default_value=(*c,1);bs.inputs['Metallic'].default_value=metal;bs.inputs['Roughness'].default_value=rough
 no=m.node_tree.nodes.new('ShaderNodeTexNoise');no.inputs['Scale'].default_value=65;bu=m.node_tree.nodes.new('ShaderNodeBump');bu.inputs['Strength'].default_value=.12;bu.inputs['Distance'].default_value=.035;m.node_tree.links.new(no.outputs['Fac'],bu.inputs['Height']);m.node_tree.links.new(bu.outputs['Normal'],bs.inputs['Normal']);return m
teal=mat('Painted turquoise steel',(.018,.36,.41),.68);navy=mat('Deep blue steel',(.012,.055,.12),.65);cream=mat('Warm white steel',(.57,.55,.47),.55);silver=mat('Brushed locking steel',(.48,.52,.53),.87,.27);gold=mat('Weathered corner castings',(.35,.24,.065),.75);black=mat('Rubber seals',(.015,.021,.022),0,.7);card=mat('Kraft cardboard',(.42,.23,.10),0,.75);tape=mat('Turquoise parcel tape',(.02,.37,.42),.05);wood=mat('Pallet wood',(.27,.17,.095),0,.75)
def cube(name,loc,scale,ma,parent=None):
 bpy.ops.mesh.primitive_cube_add(size=1,location=loc);o=bpy.context.object;o.name=name;o.dimensions=scale;bpy.ops.object.transform_apply(location=False,rotation=False,scale=True);o.data.materials.append(ma);be=o.modifiers.new('Soft manufactured edges','BEVEL');be.width=.012;be.segments=2;o.modifiers.new('Weighted normals','WEIGHTED_NORMAL');
 if parent:o.parent=parent;o.matrix_parent_inverse=parent.matrix_world.inverted()
 return o
moving=None
for level,ma in enumerate([cream,navy,teal]):
 z=1.15+2.3*level;cube('Back wall',(0,1.97,z),(2.4,.06,2.27),ma);cube('Roof',(0,0,z+1.105),(2.4,4,.06),ma);cube('Base',(0,0,z-1.105),(2.4,4,.06),ma)
 for xx in [-1.18,1.18]:cube('Side wall',(xx,0,z),(.06,4,2.27),ma)
 cube('Dark interior',(0,1.91,z),(2.30,.035,2.15),black)
 for k in range(27):
  y=-1.9+k*.146
  for x in [-1.21,1.21]:cube('Steel side corrugation',(x,y,z),(.055,.048,2.07),ma)
 for x in [-1.13,1.13]:
  for y in [-1.95,1.95]:
   for zz in [z-1.04,z+1.04]:
    cube('Corner casting',(x,y,zz),(.22,.18,.22),gold);cube('Corner casting aperture',(x,y-.095,zz),(.095,.008,.07),black)
 for side in [-1,1]:
  pivot=bpy.data.objects.new('Door hinge',None);bpy.context.collection.objects.link(pivot);pivot.location=(side*1.18,-2.045,z)
  center=side*.59
  door=cube('Steel door',(center,-2.06,z),(1.16,.07,2.05),ma,pivot)
  for j in range(5):cube('Door corrugation',(side*(.12+j*.22),-2.109,z),(.047,.05,1.98),ma,pivot)
  for x in [side*.3,side*.89]:
   cube('Locking rod',(x,-2.17,z),(.032,.04,1.95),silver,pivot)
   for zz in [z-.85,z-.3,z+.3,z+.85]:cube('Rod bracket',(x,-2.18,zz),(.10,.05,.08),silver,pivot)
   cube('Lock handle',(x+side*.10,-2.23,z-.26),(.23,.04,.045),silver,pivot)
  for zz in [z-.78,z,z+.78]:cube('Hinge',(side*1.16,-2.14,zz),(.10,.10,.17),silver,pivot)
  if level==1 and side==1:moving=pivot
# grounded parcels and pallet
for y in [-3.05,-3.52,-3.99]:cube('Pallet plank',(.35,y,.10),(2.35,.30,.14),wood)
for x in [-.52,.35,1.22]:cube('Pallet block',(x,-3.5,.23),(.22,1.18,.22),wood)
for x,y,z,w,d,h in [(-.3,-3.3,.68,.78,.75,.78),(.58,-3.3,.75,.9,.78,.92),(.4,-3.3,1.58,.7,.70,.70),(-1.1,-3.3,.42,.62,.65,.75)]:
 cube('Parcel',(x,y,z),(w,d,h),card);cube('Parcel tape front',(x,y-d/2-.006,z),(.11,.012,h),tape);cube('Parcel tape top',(x,y,z+h/2+.006),(.11,d,.012),tape)
for f,ang in [(1,0),(16,0),(46,24),(66,24),(100,0),(120,0)]:moving.rotation_euler.z=math.radians(ang);moving.keyframe_insert(data_path='rotation_euler',frame=f)
def light(name,loc,power,color,size):
 bpy.ops.object.light_add(type='AREA',location=loc);o=bpy.context.object;o.name=name;o.data.energy=power;o.data.color=color;o.data.shape='DISK';o.data.size=size;o.rotation_euler=(Vector((0,0,3.2))-o.location).to_track_quat('-Z','Y').to_euler()
light('Cyan rim',(3,2,10),2300,(.43,.87,1),5);light('Soft key',(-4,-7,9),2000,(.78,.94,1),6);light('Warm cardboard fill',(2,-7,3),500,(1,.78,.52),4)
bpy.ops.object.camera_add(location=(8,-16,7));cam=bpy.context.object;cam.rotation_euler=(Vector((0,-.4,3.3))-cam.location).to_track_quat('-Z','Y').to_euler();cam.data.type='ORTHO';cam.data.ortho_scale=9.1;s.camera=cam
os.makedirs('/workspace/container-3d-frames',exist_ok=True);bpy.ops.wm.save_as_mainfile(filepath='/workspace/container-depth-motion.blend');s.frame_set(46);s.render.filepath='/workspace/container-depth-test.png';bpy.ops.render.render(write_still=True)
import shutil
cache={}
for i,f in enumerate(range(1,121,2)):
 s.frame_set(f);dest=f'/workspace/container-3d-frames/{i:04}.png';key=round(moving.rotation_euler.z,7)
 if key in cache:shutil.copyfile(cache[key],dest)
 else:
  s.render.filepath=dest;bpy.ops.render.render(write_still=True);cache[key]=dest

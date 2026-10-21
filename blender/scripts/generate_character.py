"""Francisco: static low-poly study. Run in Blender's Text Editor.
Creates its own collection; preserves other scene objects. +Y is forward.
No rig or animation. Head is one separate mesh with pivot at the neck.
"""
from pathlib import Path
import math
import random
import bpy
from mathutils import Vector

# Text Editor execution does not always provide __file__.
PROJECT_ROOT = Path('/Users/fespinozag/Documents/portafolios')
OUTPUT = PROJECT_ROOT / 'public/models/francisco.glb'
COLLECTION = 'Francisco_Generated'


def material(name, color):
    mat = bpy.data.materials.get(name) or bpy.data.materials.new(name)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get('Principled BSDF')
    bsdf.inputs['Base Color'].default_value = (*color, 1)
    bsdf.inputs['Roughness'].default_value = 0.88
    mat.diffuse_color = (*color, 1)
    return mat


def register(obj, name, mat):
    obj.name = name
    for col in list(obj.users_collection):
        col.objects.unlink(obj)
    collection.objects.link(obj)
    obj.data.materials.append(mat)
    for face in obj.data.polygons:
        face.use_smooth = False
    return obj


def ellipsoid(name, location, scale, mat, segments=10, rings=6):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=segments, ring_count=rings, location=location)
    obj = register(bpy.context.object, name, mat)
    obj.scale = scale
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    return obj


def box(name, location, scale, mat, bevel=0.0):
    bpy.ops.mesh.primitive_cube_add(size=1, location=location)
    obj = register(bpy.context.object, name, mat)
    obj.scale = scale
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    if bevel:
        modifier = obj.modifiers.new('Angular edges', 'BEVEL')
        modifier.width = bevel
        modifier.segments = 1
        bpy.ops.object.modifier_apply(modifier=modifier.name)
    return obj


def limb(name, start, end, radius1, radius2, mat, vertices=8):
    midpoint = (Vector(start) + Vector(end)) / 2
    bpy.ops.mesh.primitive_cone_add(vertices=vertices, radius1=radius2,
        radius2=radius1, depth=(Vector(end)-Vector(start)).length, location=midpoint)
    obj = register(bpy.context.object, name, mat)
    obj.rotation_euler = (Vector(end)-Vector(start)).to_track_quat('Z', 'Y').to_euler()
    return obj


def join(objects, name, pivot):
    bpy.ops.object.select_all(action='DESELECT')
    for obj in objects:
        obj.select_set(True)
    bpy.context.view_layer.objects.active = objects[0]
    bpy.ops.object.join()
    obj = bpy.context.object
    obj.name = name
    cursor = bpy.context.scene.cursor.location.copy()
    bpy.context.scene.cursor.location = pivot
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
    bpy.context.scene.cursor.location = cursor
    return obj


# Replace only this script's previous generated collection.
if bpy.context.object and bpy.context.object.mode != 'OBJECT':
    bpy.ops.object.mode_set(mode='OBJECT')
old = bpy.data.collections.get(COLLECTION)
if old:
    for obj in list(old.objects):
        bpy.data.objects.remove(obj, do_unlink=True)
    bpy.data.collections.remove(old)
collection = bpy.data.collections.new(COLLECTION)
bpy.context.scene.collection.children.link(collection)
skin = material('Francisco_Skin', (.40, .18, .095))
hair = material('Francisco_Hair', (0.028, 0.022, 0.020))
beard = material('Francisco_Beard', (0.065, 0.043, 0.033))
shirt = material('Francisco_Petrol', (0.025, 0.20, 0.23))
denim = material('Francisco_Denim', (0.035, 0.065, 0.13))
shoe = material('Francisco_Sneakers', (0.78, 0.79, 0.73))
sole = material('Francisco_Soles', (0.94, 0.93, 0.86))
white = material('Francisco_EyeWhite', (0.84, 0.80, 0.71))
eye = material('Francisco_Eyes', (0.025, 0.018, 0.014))

# v2: anatomical proportions, sculpted face planes, surface stubble.
random.seed(23)
def mesh_object(name, verts, faces, mat):
    mesh=bpy.data.meshes.new(name+'Mesh')
    mesh.from_pydata(verts,[],[tuple(reversed(f)) for f in faces])
    mesh.update()
    obj=bpy.data.objects.new(name,mesh)
    collection.objects.link(obj)
    obj.data.materials.append(mat)
    mat.use_backface_culling = False
    return obj


def rings(name, levels, mat, count=24):
    verts=[]
    for z,w,d,cy in levels:
        for i in range(count):
            a=2*math.pi*i/count
            verts.append((w*math.sin(a),cy+d*math.cos(a),z))
    faces=[tuple(reversed(range(count))),tuple(range((len(levels)-1)*count,len(levels)*count))]
    for r in range(len(levels)-1):
        for i in range(count):
            a=r*count+i;b=r*count+(i+1)%count;c=b+count;d=a+count
            faces.extend([(a,b,c),(a,c,d)])
    return mesh_object(name,verts,faces,mat)


def mottled(obj, base, name, amount=.07):
    # Small deterministic flat-color facets export as portable glTF materials.
    palette=[]
    for i in range(7):
        f=1+amount*(i-3)/3
        palette.append(material(name+str(i),tuple(min(1,c*f) for c in base)))
    for m in palette: obj.data.materials.append(m)
    for poly in obj.data.polygons: poly.material_index=1+random.randrange(7)

for side,x in [('L',-.105),('R',.105)]:
    box('Sole_'+side,(x,.045,.023),(.125,.265,.046),sole,.012)
    box('Sneaker_'+side,(x,.045,.082),(.123,.245,.095),shoe,.026)
    rings('Jeans_'+side,[(.12,.062,.066,0),(.33,.068,.07,0),(.52,.073,.076,.008),(.72,.084,.083,0),(.94,.091,.09,0)],denim,12)
    obj=bpy.context.object
    # Offset leg mesh without changing its anatomical cross sections.
    leg=collection.objects.get('Jeans_'+side)
    leg.location.x=x
box('Hips',(0,0,.94),(.36,.205,.15),denim,.05)
torso=rings('TShirt',[(.98,.179,.109,0),(1.07,.182,.113,0),(1.17,.192,.119,0),(1.29,.216,.125,0),(1.39,.231,.115,0),(1.45,.205,.097,0),(1.485,.086,.075,0)],shirt,32)
mottled(torso,(.009,.038,.047),'PetrolFacet',.16)
for sign,side in [(-1,'L'),(1,'R')]:
    limb('Sleeve_'+side,(sign*.18,0,1.398),(sign*.27,0,1.245),.087,.104,shirt,12)
    limb('UpperArm_'+side,(sign*.27,0,1.255),(sign*.303,.008,1.075),.059,.073,skin,12)
    limb('Forearm_'+side,(sign*.303,.008,1.075),(sign*.325,.025,.878),.039,.059,skin,12)
    palm=ellipsoid('Palm_'+side,(sign*.326,.027,.841),(.041,.027,.064),skin,12,8)
    for j in range(4):
        x=sign*(.299+j*.016)
        limb('Finger_'+side+str(j),(x,.035,.824),(x,.04,.783+abs(j-1.5)*.007),.008,.010,skin,8)
    limb('Thumb_'+side,(sign*.296,.031,.858),(sign*.282,.061,.813),.012,.017,skin,8)
rings('Neck',[(1.43,.071,.066,0),(1.51,.069,.066,-.005),(1.57,.071,.073,-.007)],skin,16)

head=[]
def h(*args,**kwargs):
    obj=ellipsoid(*args,**kwargs);head.append(obj);return obj
# Front surface follows forehead, brow ridge, recessed orbits, cheekbones,
# projecting nose/muzzle, jaw and chin. The rear remains a rounded cranium.
levels=[(1.515,.045,.057,.041),(1.535,.071,.077,.057),
 (1.56,.087,.088,.073),(1.585,.097,.086,.083),
 (1.61,.102,.086,.087),(1.635,.106,.090,.086),
 (1.66,.110,.094,.081),(1.68,.112,.091,.077),
 (1.697,.109,.086,.079),(1.714,.107,.096,.082),
 (1.735,.105,.094,.080),(1.76,.105,.088,.076),
 (1.79,.099,.077,.069),(1.815,.078,.059,.052),
 (1.83,.045,.035,.030)]
verts=[];N=48
for z,w,front,back in levels:
    for i in range(N):
        a=2*math.pi*i/N;x=w*math.sin(a);c=math.cos(a)
        y=(front if c>=0 else back)*c
        if c>0:
            # Broad planar face with a smooth transition to the temples.
            y=front*(1-.27*(abs(x)/w)**2)*min(1,c*2.8)
            orbit=math.exp(-((abs(x)-.044)/.025)**2-((z-1.693)/.016)**2)
            y-=.013*orbit
            y+=.009*math.exp(-((abs(x)-.067)/.027)**2-((z-1.655)/.023)**2)
        verts.append((x,y,z))
faces=[]
for r in range(len(levels)-1):
    for i in range(N):
        a=r*N+i;b=r*N+(i+1)%N;c=b+N;d=a+N
        faces.extend([(a,b,c),(a,c,d)])
faces.extend([tuple(reversed(range(N))),tuple(range((len(levels)-1)*N,len(levels)*N))])
face=mesh_object('SculptedFace',verts,faces,skin);head.append(face)
# Stubble is coloration on the skin surface, never a separate bulky beard.
for i in range(8):
    shade=1+(i-3.5)*.023
    face.data.materials.append(material('Complexion'+str(i),(.40*shade,.18*shade,.095*shade)))
for i in range(8):
    shade=.32+i*.025
    face.data.materials.append(material('Stubble'+str(i),(.40*shade,.18*shade,.095*shade)))
for poly in face.data.polygons:
    center=sum((face.data.vertices[v].co for v in poly.vertices),Vector())/len(poly.vertices)
    x,y,z=center
    stubble=(y>.025 and z<1.595 and (z<1.566 or abs(x)>.040)) or (abs(x)>.087 and 1.59<z<1.66 and y>0)
    poly.material_index=(9 if stubble else 1)+random.randrange(8)
for sign in [-1,1]:
    ear=h('Ear',(sign*.111,-.004,1.667),(.019,.025,.038),skin,10,7)
    h('EarInner',(sign*.118,.014,1.667),(.009,.006,.024),material('EarShade',(.36,.16,.105)),8,5)
# Nose bridge and tip, using a continuous small wedge.
nose=mesh_object('Nose',[
 (-.011,.090,1.718),(.011,.090,1.718),(-.013,.115,1.662),(.013,.115,1.662),
 (-.020,.104,1.644),(.020,.104,1.644),(0,.134,1.652),(0,.109,1.638)],
 [(0,1,3,2),(2,3,6),(2,6,4),(3,5,6),(4,6,7),(6,5,7),(4,7,5)],skin)
head.append(nose)
nostril=material('Nostrils',(.12,.054,.033))
for sign in [-1,1]: h('Nostril',(sign*.012,.112,1.644),(.006,.003,.0035),nostril,8,4)
# Narrow almond shaped eyes; iris is partly covered by lids.
lidmat=material('Lid',(.38,.19,.12))
iris=material('Iris',(.075,.048,.027))
for sign in [-1,1]:
    cx=sign*.044;z=1.695;y=.0785
    outline=[(-.022,0),(-.011,.005),(0,.006),(.012,.004),(.023,-.001),(.011,-.005),(0,-.006),(-.012,-.004)]
    ev=[(cx+dx,y,z+dz) for dx,dz in outline]+[(cx,y+.002,z)]
    ob=mesh_object('Eye',ev,[(i,(i+1)%8,8) for i in range(8)],white);head.append(ob)
    h('Iris',(cx,y+.003,z),(.0065,.002,.006),iris,12,6)
    h('Pupil',(cx,y+.005,z),(.0034,.001,.0045),eye,10,6)
    h('Catchlight',(cx-.002,y+.006,z+.002),(.0012,.0008,.0012),white,6,4)
    for j in range(4):
        dx,dz=outline[j];ex,ez=outline[j+1]
        ob=limb('UpperLid',(cx+dx,y+.001,z+dz),(cx+ex,y+.001,z+ez),.0018,.0018,lidmat,6);head.append(ob)
    browverts=[(cx-.026,.091,1.718),(cx-.013,.097,1.726),(cx+.008,.097,1.726),(cx+.025,.089,1.718),(cx+.024,.091,1.711),(cx+.006,.099,1.718),(cx-.012,.099,1.718),(cx-.025,.093,1.712)]
    head.append(mesh_object('Eyebrow',browverts,[(0,1,6,7),(1,2,5,6),(2,3,4,5)],beard))
lips=material('Lips',(.23,.075,.042))
head.append(mesh_object('Lips',[(-.031,.086,1.615),(-.013,.094,1.620),(0,.096,1.617),(.013,.094,1.620),(.031,.086,1.615),(0,.097,1.608)],[(0,1,2,5),(2,3,4,5)],lips))
for sign in [-1,1]:
    # Thin moustache follows upper lip.
    head.append(mesh_object('Moustache',[(sign*.003,.098,1.627),(sign*.016,.096,1.630),(sign*.031,.088,1.622),(sign*.031,.089,1.616),(sign*.014,.098,1.622),(sign*.003,.099,1.621)],[(0,1,4,5),(1,2,3,4)],beard))
# Short sides and irregular swept waves on top.
h('HairBack',(0,-.047,1.763),(.111,.063,.078),hair,16,9)
for sign in [-1,1]:
    h('HairSide',(sign*.098,-.010,1.745),(.017,.065,.065),hair,10,7)
    h('Sideburn',(sign*.105,.014,1.698),(.009,.018,.026),hair,8,5)
for row in range(4):
    for col in range(6):
        x=(col-2.5)*.036+random.uniform(-.008,.008)
        y=(row-1.5)*.042
        z=1.799+.020*(1-(x/.12)**2)+random.uniform(-.008,.009)
        ob=h('Wave',(x,y,z),(.032+random.random()*.009,.038,.024+random.random()*.012),hair,7,5)
        ob.rotation_euler=(random.uniform(-.3,.3),-.38,random.uniform(-.5,.5))
        mottled(ob,(.009,.005,.003),'HairFacet',.35)
head_obj=join(head,'Head',(0,0,1.50))
head_obj['description']='v2 anatomical study from supplied reference; surface stubble; neck pivot.'
root=bpy.data.objects.new('Francisco',None)
collection.objects.link(root)
for obj in list(collection.objects):
    if obj.type=='MESH': obj.parent=root
bpy.ops.object.select_all(action='DESELECT')
for obj in collection.objects: obj.select_set(True)
bpy.context.view_layer.objects.active=head_obj
OUTPUT.parent.mkdir(parents=True,exist_ok=True)
bpy.ops.export_scene.gltf(filepath=str(OUTPUT),export_format='GLB',use_selection=True,
 export_yup=True,export_animations=False,export_cameras=False,export_lights=False)
print('Francisco v2 exported:',OUTPUT)

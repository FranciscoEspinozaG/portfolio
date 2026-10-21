"""Francisco: static low-poly study. Run in Blender's Text Editor.
Creates its own collection; preserves other scene objects. +Y is forward.
No rig or animation. Head is one separate mesh with pivot at the neck.
"""
from pathlib import Path
import math
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
    bpy.ops.mesh.primitive_cone_add(vertices=vertices, radius1=radius1,
        radius2=radius2, depth=(Vector(end)-Vector(start)).length, location=midpoint)
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
skin = material('Francisco_Skin', (0.57, 0.34, 0.23))
hair = material('Francisco_Hair', (0.028, 0.022, 0.020))
beard = material('Francisco_Beard', (0.065, 0.043, 0.033))
shirt = material('Francisco_Petrol', (0.025, 0.20, 0.23))
denim = material('Francisco_Denim', (0.035, 0.065, 0.13))
shoe = material('Francisco_Sneakers', (0.78, 0.79, 0.73))
sole = material('Francisco_Soles', (0.94, 0.93, 0.86))
white = material('Francisco_EyeWhite', (0.84, 0.80, 0.71))
eye = material('Francisco_Eyes', (0.025, 0.018, 0.014))

# Feet touch z=0. Human-scale body, relaxed arms.
for side, x in [('L', -0.115), ('R', 0.115)]:
    box('Sole_'+side, (x, 0.058, 0.025), (0.16, 0.29, 0.05), sole, 0.012)
    box('Sneaker_'+side, (x, 0.055, 0.095), (0.15, 0.27, 0.11), shoe, 0.025)
    limb('Shin_'+side, (x, 0, 0.15), (x, -0.012, 0.54), 0.077, 0.09, denim)
    limb('Thigh_'+side, (x, -0.012, 0.54), (x, 0, 0.94), 0.09, 0.105, denim)
box('Hips', (0, 0, 0.94), (0.38, 0.22, 0.18), denim, 0.04)
# Tapered torso with elliptical cross-sections.
verts=[]
for z, width, depth in [(0.99, .18, .115), (1.32, .225, .13), (1.43, .19, .11)]:
    for i in range(8):
        a=2*math.pi*i/8
        verts.append((math.cos(a)*width, math.sin(a)*depth, z))
faces=[tuple(reversed(range(8))), tuple(range(16,24))]
for row in range(2):
    for i in range(8):
        j=(i+1)%8
        faces.append((row*8+i,row*8+j,(row+1)*8+j,(row+1)*8+i))
mesh=bpy.data.meshes.new('TorsoMesh')
mesh.from_pydata(verts, [], faces)
mesh.update()
torso=bpy.data.objects.new('TShirt', mesh)
collection.objects.link(torso)
torso.data.materials.append(shirt)
for sign, side in [(-1,'L'),(1,'R')]:
    limb('Sleeve_'+side, (sign*.19,0,1.36), (sign*.285,0,1.19), .11,.105,shirt)
    limb('Arm_'+side, (sign*.28,0,1.20), (sign*.33,.025,.99), .071,.08,skin)
    limb('Forearm_'+side, (sign*.33,.025,.99), (sign*.35,.045,.83), .055,.068,skin)
    ellipsoid('Hand_'+side, (sign*.35,.045,.79), (.059,.046,.085),skin)
limb('Neck', (0,0,1.40),(0,0,1.55), .075,.075,skin)

# All facial features and hair join into an independent Head mesh.
head=[]
def h(*args, **kwargs):
    obj=ellipsoid(*args, **kwargs)
    head.append(obj)
    return obj
h('Face',(0,0,1.665),(.133,.113,.18),skin,12,8)
h('Jaw',(0,.018,1.565),(.105,.096,.075),skin)
for sign in [-1,1]:
    h('Ear',(sign*.13,0,1.66),(.027,.023,.045),skin,8,4)
# Low-profile dark lower-face volumes make short beard and moustache readable.
h('ChinBeard',(0,.077,1.548),(.086,.046,.045),beard)
for sign in [-1,1]:
    h('BeardSide',(sign*.083,.068,1.585),(.032,.042,.061),beard)
    h('Moustache',(sign*.031,.112,1.607),(.042,.014,.015),beard,8,4)
    h('EyeWhite',(sign*.052,.103,1.698),(.025,.012,.014),white,8,4)
    h('Pupil',(sign*.052,.114,1.698),(.009,.005,.010),eye,8,4)
    brow=box('Brow',(sign*.052,.108,1.726),(.059,.018,.013),hair)
    brow.rotation_euler.y=sign*.10
    head.append(brow)
h('Nose',(0,.119,1.652),(.024,.034,.040),skin,8,4)
h('HairCap',(0,-.018,1.797),(.139,.113,.083),hair,12,6)
h('HairBack',(0,-.080,1.72),(.123,.047,.108),hair)
for x,z in [(-.10,1.815),(-.055,1.851),(0,1.866),(.052,1.847),(.103,1.811)]:
    tuft=h('HairTuft',(x,.026,z),(.045,.080,.033),hair,7,4)
    tuft.rotation_euler.y=-.25
head_obj=join(head,'Head',(0,0,1.49))
head_obj['description']='Independent head mesh; neck pivot; stylized interpretation.'

root=bpy.data.objects.new('Francisco',None)
collection.objects.link(root)
for obj in list(collection.objects):
    if obj.type=='MESH':
        obj.parent=root
bpy.ops.object.select_all(action='DESELECT')
for obj in collection.objects:
    obj.select_set(True)
bpy.context.view_layer.objects.active=head_obj
OUTPUT.parent.mkdir(parents=True,exist_ok=True)
bpy.ops.export_scene.gltf(filepath=str(OUTPUT),export_format='GLB',
    use_selection=True,export_yup=True,export_animations=False,export_cameras=False,
    export_lights=False)
assert OUTPUT.is_file() and OUTPUT.stat().st_size > 1000
print('Francisco exported:', OUTPUT)
print('Static avatar; independent Head; +Y forward in Blender, meters; no rig.')

"""Neutral human photo-texturing base for Blender 4.x / 5.x.
Run from Text Editor > Run Script. No downloads or add-ons required.
Creates a dedicated scene. Body is one connected mesh; Head is separate.
White image textures and UVs are ready for texture painting.
This is a generic mannequin, not a reconstruction of a particular person.
Hands have joined fingers and separate thumb volumes; no skeleton, clothing folds or hair are generated.
"""
import math
import bpy
import bmesh
from mathutils import Vector

HEIGHT = 1.88                 # meters; change before running
SUBDIVISIONS = 1              # 0 for coarse geometry, 1 for the working base
BODY_TEXTURE_SIZE = 2048
HEAD_TEXTURE_SIZE = 1024
KEEP_PAINTED_IMAGES = True    # rerunning preserves images with these names
SCENE_NAME = 'PhotoBody_Workspace'
COLLECTION_NAME = 'PhotoBody_Generated'
GENERATOR_ID = 'photo_body_base_v1'


class Surface:
    def __init__(self):
        self.verts = []
        self.faces = []
        self.seams = set()

    def vert(self, value):
        self.verts.append(tuple(value))
        return len(self.verts)-1

    def seam(self, a, b):
        self.seams.add(tuple(sorted((a,b))))

    def bridge(self, a, b):
        assert len(a) == len(b)
        for i in range(len(a)):
            j = (i+1) % len(a)
            self.faces.append((a[i],a[j],b[j],b[i]))

    def ring(self, z, width, depth, cy=0, count=16):
        return [self.vert((width*math.sin(2*math.pi*i/count),
                           cy+depth*math.cos(2*math.pi*i/count),z))
                for i in range(count)]

    def mark_ring(self, ring):
        for i,a in enumerate(ring):
            self.seam(a,ring[(i+1)%len(ring)])

    def tube(self, boundary, direction, sections):
        # Sort the attachment boundary in the limb's local plane.
        axis = Vector(direction).normalized()
        u = Vector((0,1,0))
        u = (u-axis*u.dot(axis)).normalized()
        v = axis.cross(u).normalized()
        center = sum((Vector(self.verts[i]) for i in boundary),Vector())/len(boundary)
        ordered = sorted(boundary, key=lambda i: math.atan2(
            (Vector(self.verts[i])-center).dot(v),
            (Vector(self.verts[i])-center).dot(u)))
        count=len(ordered)
        angles=[math.atan2((Vector(self.verts[i])-center).dot(v),
                          (Vector(self.verts[i])-center).dot(u)) for i in ordered]
        previous=ordered
        chains=[ordered]
        self.mark_ring(previous)
        back=min(range(count),key=lambda i:Vector(self.verts[ordered[i]]).y)
        for location, depth, width in sections:
            location=Vector(location)
            current=[self.vert(location+u*(depth*math.cos(a))+v*(width*math.sin(a)))
                     for a in angles]
            self.bridge(previous,current)
            self.seam(previous[back],current[back])
            previous=current
            chains.append(current)
        self.faces.append(tuple(previous))
        self.mark_ring(previous)
        return chains

    def object(self, name, collection):
        mesh=bpy.data.meshes.new(name+'_Mesh')
        mesh.from_pydata(self.verts,[],self.faces)
        mesh.update()
        for edge in mesh.edges:
            edge.use_seam=tuple(sorted(edge.vertices)) in self.seams
        # Recalculate normals and discard vertices unused by shoulder openings.
        bm=bmesh.new()
        bm.from_mesh(mesh)
        unused=[v for v in bm.verts if not v.link_edges]
        if unused:
            bmesh.ops.delete(bm,geom=unused,context='VERTS')
        bmesh.ops.recalc_face_normals(bm,faces=list(bm.faces))
        nonmanifold=sum(not e.is_manifold for e in bm.edges)
        bm.to_mesh(mesh)
        bm.free()
        if nonmanifold:
            raise RuntimeError(f'{name}: {nonmanifold} non-manifold edges')
        obj=bpy.data.objects.new(name,mesh)
        collection.objects.link(obj)
        for poly in mesh.polygons:
            poly.use_smooth=True
        return obj


def activate(obj):
    bpy.ops.object.select_all(action='DESELECT')
    obj.select_set(True)
    bpy.context.view_layer.objects.active=obj


def white_material(name, image_name, size):
    image=bpy.data.images.get(image_name) if KEEP_PAINTED_IMAGES else None
    if image is None:
        image=bpy.data.images.new(image_name,width=size,height=size,alpha=False)
        image.generated_color=(1,1,1,1)
        image.generated_type='BLANK'
    mat=bpy.data.materials.get(name) or bpy.data.materials.new(name)
    mat.use_nodes=True
    nodes=mat.node_tree.nodes
    nodes.clear()
    tex=nodes.new('ShaderNodeTexImage')
    tex.name='PaintCanvas'
    tex.label='White canvas: paint photos here'
    tex.image=image
    tex.location=(-320,80)
    tex.select=True
    nodes.active=tex
    bsdf=nodes.new('ShaderNodeBsdfPrincipled')
    bsdf.inputs['Roughness'].default_value=.78
    bsdf.inputs['Metallic'].default_value=0
    bsdf.location=(0,80)
    out=nodes.new('ShaderNodeOutputMaterial')
    out.location=(320,80)
    mat.node_tree.links.new(tex.outputs['Color'],bsdf.inputs['Base Color'])
    mat.node_tree.links.new(bsdf.outputs['BSDF'],out.inputs['Surface'])
    mat.diffuse_color=(1,1,1,1)
    return mat


def unwrap(obj):
    activate(obj)
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.uv.unwrap(method='ANGLE_BASED',margin=.02)
    bpy.ops.uv.average_islands_scale()
    bpy.ops.uv.pack_islands(rotate=True,margin=.025)
    bpy.ops.object.mode_set(mode='OBJECT')
    obj.data.uv_layers.active.name='PhotoUV'


def subdivide(obj):
    if SUBDIVISIONS:
        activate(obj)
        modifier=obj.modifiers.new('Base surface refinement','SUBSURF')
        modifier.subdivision_type='CATMULL_CLARK'
        modifier.levels=SUBDIVISIONS
        bpy.ops.object.modifier_apply(modifier=modifier.name)


if bpy.context.object and bpy.context.object.mode!='OBJECT':
    bpy.ops.object.mode_set(mode='OBJECT')
scene=bpy.data.scenes.get(SCENE_NAME)
if scene is None or scene.get('generator')!=GENERATOR_ID:
    scene=bpy.data.scenes.new(SCENE_NAME)
    scene['generator']=GENERATOR_ID
bpy.context.window.scene=scene
for col in list(scene.collection.children):
    if col.get('generator')==GENERATOR_ID:
        for obj in list(col.objects):
            bpy.data.objects.remove(obj,do_unlink=True)
        bpy.data.collections.remove(col)
collection=bpy.data.collections.new(COLLECTION_NAME)
collection['generator']=GENERATOR_ID
scene.collection.children.link(collection)
scene.unit_settings.system='METRIC'
scene.unit_settings.scale_length=1

# Continuous torso with open shoulder patches for branching arms.
s=Surface()
levels=[(.91,.176,.099,0),(.98,.185,.112,0),(1.09,.173,.105,0),
        (1.22,.197,.117,0),(1.34,.222,.126,0),(1.43,.222,.112,-.006),
        (1.48,.128,.078,-.009),(1.515,.067,.061,-.009),(1.56,.066,.063,-.008),(1.59,.064,.062,-.008)]
tr=[s.ring(*level) for level in levels]
for row in range(len(tr)-1):
    for i in range(16):
        # Four quads per shoulder opening, eight boundary vertices.
        if row in (3,4) and i in (3,4,11,12):
            continue
        j=(i+1)%16
        s.faces.append((tr[row][i],tr[row][j],tr[row+1][j],tr[row+1][i]))
    s.seam(tr[row][8],tr[row+1][8])
s.faces.append(tuple(tr[-1]))
s.mark_ring(tr[-1])

for sign,sideidx in [(1,4),(-1,12)]:
    a=sideidx-1;b=sideidx;c=sideidx+1
    boundary=[tr[3][a],tr[3][b],tr[3][c],tr[4][c],tr[5][c],tr[5][b],tr[5][a],tr[4][a]]
    # Upper arm, elbow, forearm, wrist, palm and joined fingers.
    sections=[((sign*.255,0,1.31),.076,.079),
              ((sign*.300,-.006,1.21),.064,.066),
              ((sign*.345,-.008,1.105),.051,.052),
              ((sign*.368,0,1.045),.051,.056),
              ((sign*.397,.007,.973),.040,.043),
              ((sign*.416,.013,.917),.026,.032),
              ((sign*.430,.015,.879),.024,.041),
              ((sign*.450,.019,.831),.023,.042),
              ((sign*.463,.022,.792),.017,.032),
              ((sign*.468,.023,.776),.010,.020)]
    chains=s.tube(boundary,(sign*.25,0,-.55),sections)
    # Branch a small thumb from the inside of the palm, keeping a single mesh.
    a,b=chains[6],chains[7]
    thumb_index=min(range(len(a)),key=lambda i:abs(sum(s.verts[j][0] for j in (a[i],a[(i+1)%len(a)],b[i],b[(i+1)%len(a)]))/4))
    j=(thumb_index+1)%len(a)
    patch=(a[thumb_index],a[j],b[j],b[thumb_index])
    s.faces.remove(patch)
    center=sum((Vector(s.verts[i]) for i in patch),Vector())/4
    delta=Vector((-sign*.045,.025,-.050))
    s.tube(list(patch),delta,[
        (center+delta*.30,.015,.017),
        (center+delta*.75,.012,.013),
        (center+delta,.006,.008)])

# Shared central bridge forms a continuous crotch between the two leg openings.
mid=[s.vert((0,y,.913)) for y in (-.048,0,.048)]
right=[tr[0][i] for i in range(9)]+mid
left=[tr[0][i%16] for i in range(8,17)]+list(reversed(mid))
for sign,boundary in [(1,right),(-1,left)]:
    # z-directed elliptical sections; distal sections expand into feet.
    sections=[((sign*.103,0,.846),.100,.094),
              ((sign*.108,.002,.745),.095,.088),
              ((sign*.110,.008,.625),.078,.074),
              ((sign*.111,.012,.535),.064,.064),
              ((sign*.112,0,.469),.064,.062),
              ((sign*.113,-.009,.364),.069,.060),
              ((sign*.114,-.012,.252),.055,.047),
              ((sign*.114,-.010,.147),.040,.039),
              ((sign*.114,.023,.088),.085,.052),
              ((sign*.114,.066,.045),.138,.057),
              ((sign*.114,.066,.012),.136,.056)]
    s.tube(boundary,(0,0,-1),sections)
body=s.object('Body',collection)
subdivide(body)
unwrap(body)
body.data.materials.append(white_material('PhotoBody_White','Body_Paint_2048',BODY_TEXTURE_SIZE))
body['notes']='Connected generic mannequin. Joined fingers. No rig. PhotoUV for painting.'

# Separate head. Its back seam creates one large face island for projection.
h=Surface()
profile=[(1.565,.028,.043,.035),(1.58,.046,.061,.047),
         (1.60,.069,.077,.061),(1.62,.087,.084,.077),
         (1.65,.100,.088,.090),(1.68,.107,.091,.098),
         (1.72,.111,.095,.104),(1.75,.109,.096,.106),
         (1.78,.108,.098,.105),(1.81,.107,.096,.101),
         (1.84,.096,.086,.089),(1.863,.074,.065,.070),
         (1.88,.039,.036,.037)]

def interp(z,index):
    for lo,hi in zip(profile,profile[1:]):
        if lo[0]<=z<=hi[0]:
            f=(z-lo[0])/(hi[0]-lo[0])
            return lo[index]*(1-f)+hi[index]*f
    return profile[0 if z<profile[0][0] else -1][index]

def bump(x,z,cx,cz,sx,sz):
    return math.exp(-((x-cx)/sx)**2-((z-cz)/sz)**2)

headrings=[]
count=48
zs=sorted(set([p[0] for p in profile]+[1.58+i*.0075 for i in range(40)]))
for z in zs:
    w=interp(z,1);front=interp(z,2);back=interp(z,3)
    ring=[]
    for i in range(count):
        angle=2*math.pi*i/count
        x=w*math.sin(angle);c=math.cos(angle)
        y=(front if c>=0 else back)*c-.009
        if c>0:
            y=front*(1-.36*(abs(x)/w)**2)*min(1,c*2.9)-.009
            feature=(.020*bump(x,z,0,1.738,.014,.037)
                     +.034*bump(x,z,0,1.700,.017,.013)
                     +.010*bump(abs(x),z,.019,1.696,.010,.010)
                     -.012*bump(abs(x),z,.045,1.746,.024,.013)
                     +.006*bump(abs(x),z,.045,1.766,.030,.008)
                     +.007*bump(abs(x),z,.067,1.714,.026,.020)
                     +.004*bump(x,z,0,1.667,.035,.006)
                     -.004*bump(x,z,0,1.659,.033,.003)
                     +.007*bump(x,z,0,1.625,.041,.018))
            y+=feature*min(1,c*3)
        ring.append(h.vert((x,y,z)))
    if headrings:
        h.bridge(headrings[-1],ring)
        h.seam(headrings[-1][count//2],ring[count//2])
    headrings.append(ring)
h.faces.append(tuple(headrings[0]))
h.faces.append(tuple(headrings[-1]))
h.mark_ring(headrings[0]);h.mark_ring(headrings[-1])
head=h.object('Head',collection)
subdivide(head)
# Low-profile ears, joined into Head, then independently packed UV islands.
activate(head)
for sign in (-1,1):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=12,ring_count=8,location=(sign*.112,-.007,1.723))
    ear=bpy.context.object
    for col in list(ear.users_collection): col.objects.unlink(ear)
    collection.objects.link(ear)
    ear.scale=(.014,.023,.034)
    bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
    for edge in ear.data.edges:
        a,b=(ear.data.vertices[i].co for i in edge.vertices)
        # Pole-to-pole cut on the back side of each ear.
        if abs(a.x)<.00001 and abs(b.x)<.00001 and a.y<.00001 and b.y<.00001:
            edge.use_seam=True
    activate(head)
    ear.select_set(True)
    bpy.ops.object.join()
unwrap(head)
head.data.materials.clear()
head.data.materials.append(white_material('PhotoHead_White','Head_Paint_1024',HEAD_TEXTURE_SIZE))
for poly in head.data.polygons:
    poly.material_index=0
    poly.use_smooth=True
cursor=scene.cursor.location.copy()
scene.cursor.location=(0,0,1.565)
activate(head)
bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
scene.cursor.location=cursor
head['notes']='Generic facial volume. Fit proportions to photos before painting. Back UV seam.'

root=bpy.data.objects.new('PhotoBody',None)
collection.objects.link(root)
root.empty_display_type='PLAIN_AXES'
root.empty_display_size=.10
for obj in (body,head):
    obj.parent=root
root.scale=(HEIGHT/1.88,)*3
root['front']='Blender +Y; up +Z; units meters'
# Smooth studio display; the paint canvases stay pure white.
activate(body)
head.select_set(True)
for screen in bpy.data.screens:
    for area in screen.areas:
        if area.type=='VIEW_3D':
            space=area.spaces.active
            space.shading.type='SOLID'
            space.shading.color_type='MATERIAL'
            space.shading.light='STUDIO'
            space.shading.show_cavity=True
            space.region_3d.view_location=(0,0,.98)
            space.region_3d.view_distance=3.2
            # Front view: looking from +Y, Z up.
            space.region_3d.view_rotation=Vector((0,-1,0)).to_track_quat('-Z','Y')
print('White base created in scene:',scene.name)
print('Objects: Body, Head; textures: Body_Paint_2048, Head_Paint_1024')
print('Keep this scene as .blend. Save painted images or pack them before closing.')

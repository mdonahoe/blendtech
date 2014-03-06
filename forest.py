import bpy
import random

numTrees = 200

trunkRadius = .01
trunkDepth = .25
treeTopRadius = .05
treeTopDepth = .25

landscapeScale = 3
bpy.ops.mesh.primitive_plane_add(location=(0,0,0))
bpy.context.active_object.scale = (landscapeScale,) * 3
landscapeMaterial = bpy.data.materials.new('Landscape Material')
landscapeMaterial.diffuse_color = (.375, .75, 0.0)
obj = bpy.context.active_object
mesh = obj.data
mesh.materials.append(landscapeMaterial)

r = lambda s: random.random() * s - s / 2.0

for i in range(numTrees):
    x = r(landscapeScale)
    y = r(landscapeScale)

    # trunk
    bpy.ops.mesh.primitive_cylinder_add(
            #radius=trunkRadius,  # weirdly this isn't supported
            depth=trunkDepth,
            location=(x,y,0.1))
    trunkMaterial = bpy.data.materials.new('Trunk Material')
    trunkMaterial.diffuse_color = (0.8, 0.4, 0.25)
    obj = bpy.context.active_object
    obj.scale = (trunkRadius, trunkRadius, 1)
    obj.data.materials.append(trunkMaterial)

    # top
    bpy.ops.mesh.primitive_cone_add(
            #radius=treeTopRadius,  # weirdly this isn't supported
            depth=treeTopDepth,
            location=(x,y,0.2))
    topMaterial = bpy.data.materials.new('Top Material')
    topMaterial.diffuse_color = (0.25, 0.8, 0.0)
    obj = bpy.context.active_object
    obj.scale = (treeTopRadius, treeTopRadius, 1)
    obj.data.materials.append(topMaterial)
bpy.ops.object.camera_add()
cam = bpy.context.selected_objects[0]
cam.name = 'the best camera'
cam.game.physics_type = 'NO_COLLISION'
bpy.data.scenes['Scene'].render.filepath = 'test.png'
bpy.ops.render.render(write_still=True)

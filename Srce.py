import bpy
context = bpy.context

#kordinate za srce
x = 0
y = 2
z = 2

#ustvarimo 2d krog z izbranimi podatki
bpy.ops.mesh.primitive_circle_add(fill_type='TRIFAN', vertices=16, enter_editmode=False, align='WORLD', location=(x, y, z), scale=(1, 1, 1))


ob = context.object
me = ob.data

#rotiramo 2d krog po x osi v pokončno stanje
bpy.ops.transform.rotate(value=1.5708, orient_axis='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

#po defaltu imamo v object modu izbrano vse, zato odizberemo vse
for g in me.vertices[:] + me.edges[:] + me.polygons[:]:
    g.select = False

#izberemo prvo vozlišče    
me.vertices[1].select = True

#premaknemo se v edit mode
bpy.ops.object.mode_set(mode='EDIT')

#izbrišemo izbrano vozlišče
bpy.ops.mesh.delete(type='VERT')

#premaknemo se v object mode
bpy.ops.object.editmode_toggle()

#izberemo podana vozlišča
me.vertices[5].select = True
me.vertices[6].select = True
me.vertices[7].select = True
me.vertices[8].select = True
me.vertices[9].select = True
me.vertices[10].select = True
me.vertices[11].select = True

#premaknemo se v edit mode
bpy.ops.object.mode_set(mode='EDIT')

#naredimo translacijo nad podanimi vozlišči
bpy.ops.transform.translate(value=(-0, -0, -0.142955), orient_axis_ortho='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

#premaknemo se v object mode
bpy.ops.object.editmode_toggle()

#odizberemo vse
for g in me.vertices[:] + me.edges[:] + me.polygons[:]:
    g.select = False
    
#izberemo podana vozlišča
me.vertices[6].select = True
me.vertices[7].select = True
me.vertices[8].select = True
me.vertices[9].select = True
me.vertices[10].select = True
#premaknemo se v edit mode
bpy.ops.object.mode_set(mode='EDIT')
#naredimo translacijo nad podanimi vozlišči
bpy.ops.transform.translate(value=(-0, -0, -0.127633), orient_axis_ortho='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
#premaknemo se v object mode
bpy.ops.object.editmode_toggle()
#odizberemo vse
for g in me.vertices[:] + me.edges[:] + me.polygons[:]:
    g.select = False 
#izberemo podana vozlišča   
me.vertices[7].select = True
me.vertices[8].select = True
me.vertices[9].select = True
#premaknemo se v edit mode    
bpy.ops.object.mode_set(mode='EDIT')
#naredimo translacijo nad podanimi vozlišči
bpy.ops.transform.translate(value=(-0, -0, -0.159289), orient_axis_ortho='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
#premaknemo se v object mode
bpy.ops.object.editmode_toggle()
#odizberemo vse
for g in me.vertices[:] + me.edges[:] + me.polygons[:]:
    g.select = False
#izberemo podano vozlišče    
me.vertices[8].select = True
#premaknemo se v edit mode 
bpy.ops.object.mode_set(mode='EDIT')
#naredimo translacijo nad podanim vozliščem
bpy.ops.transform.translate(value=(-0, -0, -0.268162), orient_axis_ortho='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
#izberemo vsa vozlišča  
bpy.ops.mesh.select_all(action='SELECT')
#Premaknemo regijo in naredimo iz 2D v 3D
bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, "use_dissolve_ortho_edges":False, "mirror":False}, TRANSFORM_OT_translate={"value":(0, 0, 0.229283), "orient_axis_ortho":'X', "orient_type":'NORMAL', "orient_matrix":((1.58214e-07, 3.26625e-06, -1), (1, -4.76416e-13, 1.58214e-07), (4.03487e-14, -1, -3.26625e-06)), "orient_matrix_type":'NORMAL', "constraint_axis":(False, False, True), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "view2d_edge_pan":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
#premaknemo se v object mode
bpy.ops.object.editmode_toggle()

#dodamo modifikator glajenja in naštimamo lastnosti
bpy.ops.object.modifier_add(type='SUBSURF')
bpy.context.object.modifiers["Subdivision"].levels = 6
bpy.context.object.modifiers["Subdivision"].render_levels = 6
#dodamo modifikator zrcaljenja in naštimamo lastnosti
bpy.ops.object.modifier_add(type='MIRROR')
bpy.context.object.modifiers["Mirror"].use_axis[0] = False

#odizberemo vse
for g in me.vertices[:] + me.edges[:] + me.polygons[:]:
    g.select = False
#izberemo 2 vozlišči
me.vertices[0].select = True
me.vertices[16].select = True
#gremo v edit mode
bpy.ops.object.mode_set(mode='EDIT')
#naredimo translacijo po x osi
bpy.ops.transform.translate(value=(-0, -0.16705, -0), orient_axis_ortho='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
#premaknemo se v object mode
bpy.ops.object.editmode_toggle()
#odizberemo vse
for g in me.vertices[:] + me.edges[:] + me.polygons[:]:
    g.select = False
#izberemo vozlišče    
me.vertices[0].select = True
#gremo v edit mode
bpy.ops.object.mode_set(mode='EDIT')
#naredimo translacijo po x osi
bpy.ops.transform.translate(value=(-0, -0.142823, -0), orient_axis_ortho='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
#premaknemo se v object mode
bpy.ops.object.editmode_toggle()
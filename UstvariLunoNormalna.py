import bpy

context = bpy.context

#kordinate zvezde
x = 0
y = 2
z = 2

#ustvarimo 2d krog z izbranimi podatki
bpy.ops.mesh.primitive_circle_add(fill_type='TRIFAN', vertices=24, enter_editmode=False, align='WORLD', location=(x, y, z), scale=(1, 1, 1))

ob = context.object
me = ob.data

#rotiramo 2d krog po x osi v pokončno stanje
bpy.ops.transform.rotate(value=1.5708, orient_axis='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

#po defaltu imamo v object modu izbrano vse, zato odizberemo vse
for g in me.vertices[:] + me.edges[:] + me.polygons[:]:
    g.select = False

#izberemo podana vozlišča
me.vertices[15].select = True
me.vertices[16].select = True
me.vertices[17].select = True
me.vertices[18].select = True
me.vertices[19].select = True
me.vertices[20].select = True
me.vertices[21].select = True
me.vertices[22].select = True
me.vertices[23].select = True


#prestavimo se v edit mode kjer vidimo nasa izbrana vozlišča
bpy.ops.object.mode_set(mode='EDIT')

#izbrišemo podana vozlišča
bpy.ops.mesh.delete(type='VERT')

#gremo nazaj v object mode
bpy.ops.object.editmode_toggle()

#izberemo sredinsko vozlišče
me.vertices[0].select = True

#prestavimo se v edit mode kjer vidimo naše podano vozlišče
bpy.ops.object.mode_set(mode='EDIT')

#premaknemo naše podano vozlišče po x osi
bpy.ops.transform.translate(value=(-0.424556, -0, -0), orient_axis_ortho='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

#izberemo vsa vozlišča
bpy.ops.mesh.select_all(action='SELECT')

#celotno označeno regijo razširimo iz 2d v 3d
#bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, "use_dissolve_ortho_edges":False, "mirror":False}, TRANSFORM_OT_translate={"value":(0, 0, 0.072929), "orient_axis_ortho":'X', "orient_type":'NORMAL', "orient_matrix":((-1, -1.45785e-13, 4.02721e-08), (-4.02721e-08, 3.61999e-06, -1), (0, -1, -3.61999e-06)), "orient_matrix_type":'NORMAL', "constraint_axis":(False, False, True), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "view2d_edge_pan":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, "use_dissolve_ortho_edges":False, "mirror":False}, TRANSFORM_OT_translate={"value":(0, 0, 0.447995), "orient_axis_ortho":'X', "orient_type":'NORMAL', "orient_matrix":((-1, -1.45785e-13, 4.02721e-08), (-4.02721e-08, 3.61999e-06, -1), (0, -1, -3.61999e-06)), "orient_matrix_type":'NORMAL', "constraint_axis":(False, False, True), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "view2d_edge_pan":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})


#izberemo vsa vozlišča, nova smo dobili z razširitvijo v 3d
bpy.ops.mesh.select_all(action='SELECT')

#dodamo modifikator subdivisionsurface 
bpy.ops.object.modifier_add(type='SUBSURF')

#dodamo mirror modifikator
bpy.ops.object.modifier_add(type='MIRROR')

#odaktiviramo po x osi preslikavo
bpy.context.object.modifiers["Mirror"].use_axis[0] = False

#naštimamo stopnjo subdivision modifikatorja
bpy.context.object.modifiers["Subdivision"].levels = 5

#naštimamo renderdiranje subdivision modifikatorja
bpy.context.object.modifiers["Subdivision"].render_levels = 5

#gremo nazaj v object mode
bpy.ops.object.editmode_toggle()

#rotiramo luno po y osi
bpy.ops.transform.rotate(value=-0.849088, orient_axis='Y', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=0.263331, use_proportional_connected=False, use_proportional_projected=False)
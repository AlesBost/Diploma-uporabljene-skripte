import bpy

context = bpy.context

#kordinate zvezde
x = 0
y = 2
z = 2

#ustvarimo 2d krog z izbranimi podatki
bpy.ops.mesh.primitive_circle_add(fill_type='TRIFAN', vertices=10, enter_editmode=False, align='WORLD', location=(x, y, z), scale=(1, 1, 1))

ob = context.object
me = ob.data

#rotiramo 2d krog po x osi v pokončno stanje
bpy.ops.transform.rotate(value=1.5708, orient_axis='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

#po defaltu imamo v object modu izbrano vse, zato odizberemo vse
for g in me.vertices[:] + me.edges[:] + me.polygons[:]:
    g.select = False

#izberemo vsako drugo vozlisce
me.vertices[2].select = True
me.vertices[4].select = True
me.vertices[6].select = True
me.vertices[8].select = True
me.vertices[10].select = True

#prestavimo se v edit mode kjer vidimo nasa izbrana vozlišča
bpy.ops.object.mode_set(mode='EDIT')

#oznacena vozlišča premaknemo v notranjost da dobimo iz 2d kroga 2d zvezdo
bpy.ops.transform.resize(value=(0.413366, 0.413366, 0.413366), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
#označimo vsa vozlišča
bpy.ops.mesh.select_all(action='SELECT')
#celotno označeno regijo razširimo iz 2d v 3d
bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, "use_dissolve_ortho_edges":False, "mirror":False}, TRANSFORM_OT_translate={"value":(0, 0, 0.271342), "orient_axis_ortho":'X', "orient_type":'NORMAL', "orient_matrix":((-1, 2.03288e-21, 0), (7.359e-27, 3.61999e-06, -1), (-2.03288e-21, -1, -3.61999e-06)), "orient_matrix_type":'NORMAL', "constraint_axis":(False, False, True), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "view2d_edge_pan":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
#vse izbrane točke odizberemo
bpy.ops.mesh.select_all(action='DESELECT')
#postavimo se iz edit moda v object mode
bpy.ops.object.editmode_toggle()

#izberemo sredinjsko sprednjo in zadnjo točko
me.vertices[0].select = True
me.vertices[11].select = True

#gremo nazaj v edit mode iz object moda
bpy.ops.object.mode_set(mode='EDIT')
#naredimo transformacijo iz izbranih dveh točk kjer je napihnemo na izven za lepši izgled zvezde
bpy.ops.transform.shrink_fatten(value=0.182248, use_even_offset=False, mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
#gremo nazaj v object mode
bpy.ops.object.editmode_toggle()
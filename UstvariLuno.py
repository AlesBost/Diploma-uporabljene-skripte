import bpy
from random import randint

#kordinate za črto
x = randint(0,2)
y = randint(2,5)
z = randint(2,5)

#ustvarimo črto
bpy.ops.curve.primitive_nurbs_path_add(radius=1, enter_editmode=False, align='WORLD', location=(x, y, z), scale=(1, 1, 1))
# rotiramo za 90 stopinj po y osi
bpy.ops.transform.rotate(value=1.5708, orient_axis='Y', orient_type='VIEW', orient_matrix=((1, -0, 0), (-0, -1.34359e-07, 1), (0, -1, -1.34359e-07)), orient_matrix_type='VIEW', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
#gremo v edit mode
bpy.ops.object.editmode_toggle()
#odizberemo prvo točko
bpy.ops.curve.de_select_first()
#odizberemo zadnjo točko
bpy.ops.curve.de_select_last()
#naredimo translacijo z našimi 3 od 5 izbranimi točkami
bpy.ops.transform.translate(value=(-1.98354, -5.02841e-09, 0.0374252), orient_axis_ortho='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
#imamo izbrano samo sredinsko točko
bpy.ops.curve.select_less()
#naredimo translacijo z podano točko
bpy.ops.transform.translate(value=(-1.1, 0, 0), orient_axis_ortho='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
#izberemo tri notranje točke
bpy.ops.curve.select_more()
#skaliramo izbrane 3 točke
bpy.ops.transform.resize(value=(1.99361, 1.99361, 1.99361), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
#odizberemo vse izbrane točke
bpy.ops.curve.select_all(action='DESELECT')
#izberemo prvo točko
bpy.ops.curve.de_select_first()
#izberemo zadnjo točko
bpy.ops.curve.de_select_last()
#skaliramo te dve točki
bpy.ops.transform.resize(value=(0.682529, 0.682529, 0.682529), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
#naštimamo globino, s tem spremenimo iz 2d v 3d objekt
bpy.context.object.data.bevel_depth = 0.82
#naštimamo resolucijo
bpy.context.object.data.bevel_resolution = 6
#zapremo prvo in zadnjo točko s tranformacijo, da dobimo izgled lune
bpy.ops.transform.transform(mode='CURVE_SHRINKFATTEN', value=(0.0493667, 0, 0, 0), orient_axis='Z', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
#izberemo vse točke
bpy.ops.curve.select_all(action='SELECT')
#gremo nazaj v object mode
bpy.ops.object.editmode_toggle()
#rotiramo našo luno py y osi
bpy.ops.transform.rotate(value=-0.611536, orient_axis='Y', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
#dodamo modifikator površine
bpy.ops.object.modifier_add(type='SUBSURF')
# dodamo modifikator preslikave zaradi površine
bpy.ops.object.modifier_add(type='MIRROR')
#naštimamo da preslikava se v nič
bpy.context.object.modifiers["Mirror"].use_axis[0] = False
#dodamo glajenje senc
bpy.ops.object.shade_smooth()
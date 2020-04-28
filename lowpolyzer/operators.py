import bpy
from bpy.types import Operator


class VIEW3D_lowpolyze(Operator):
    bl_idname = "lowpolyzer.lowpolyze"
    bl_label = "Lowpolyze"
    bl_description = "Apply a low poly style to objects"

    def execute(self, context):
        act = bpy.context.active_object

        for obj in bpy.context.selected_objects:
            if obj.type == "MESH":
                bpy.context.view_layer.objects.active = obj

                bpy.ops.object.modifier_add(type='REMESH')
                bpy.context.object.modifiers["Remesh"].voxel_size = 0.005
                bpy.context.object.modifiers["Remesh"].adaptivity = 1

                bpy.ops.object.modifier_add(type='DECIMATE')
                bpy.context.object.modifiers["Decimate"].ratio = 0.035

        bpy.context.view_layer.objects.active = act

        return {'FINISHED'}


classes = (
    VIEW3D_lowpolyze,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

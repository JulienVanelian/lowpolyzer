import bpy
from bpy.types import Operator


class VIEW3D_lowpolyze(Operator):
    bl_idname = "object.lowpolyze"
    bl_label = "Lowpolyze"
    bl_description = "Apply a low poly style to objects"

    total: bpy.props.IntProperty(name="Resolution", default=5, min=1, max=10)

    def execute(self, context):
        c = bpy.context
        active_obj = c.active_object

        for obj in c.selected_objects:
            if obj.type == "MESH":
                c.view_layer.objects.active = obj
                obj_modifiers = c.object.modifiers
                old_modifier_remesh = obj_modifiers.get("Remesh (Lowpolyzer)")
                old_modifier_decimate = obj_modifiers.get("Decimate (Lowpolyzer)")

                if old_modifier_remesh is None:
                    bpy.ops.object.modifier_add(type='REMESH')
                    obj_modifiers["Remesh"].name = "Remesh (Lowpolyzer)"
                    obj_modifiers["Remesh (Lowpolyzer)"].show_expanded = False

                obj_modifiers["Remesh (Lowpolyzer)"].voxel_size = .007

                if old_modifier_decimate is None:
                    bpy.ops.object.modifier_add(type="DECIMATE")
                    obj_modifiers["Decimate"].name = "Decimate (Lowpolyzer)"
                    obj_modifiers["Decimate (Lowpolyzer)"].show_expanded = False

                obj_modifiers["Decimate (Lowpolyzer)"].ratio = .03

        c.view_layer.objects.active = active_obj

        return {"FINISHED"}


classes = (
    VIEW3D_lowpolyze,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

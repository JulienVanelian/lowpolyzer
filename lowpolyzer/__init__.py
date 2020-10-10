import bpy
from . import operators

bl_info = {
    "name": "Lowpolyzer",
    "author": "Julien Vanélian",
    "version": (0, 2, 0),
    "blender": (2, 90, 0),
    "location": "View3D > Object > Transform",
    "description": "Apply a low poly style to objects",
    "category": "Object",
}


def draw_ui(self, context):
    self.layout.operator(operators.VIEW3D_lowpolyze.bl_idname)


def register():
    operators.register()
    bpy.types.VIEW3D_MT_transform_object.append(draw_ui)


def unregister():
    operators.unregister()
    bpy.types.VIEW3D_MT_transform_object.remove(draw_ui)


if __name__ == "__main__":
    register()

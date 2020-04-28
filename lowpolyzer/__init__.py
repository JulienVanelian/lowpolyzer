bl_info = {
    "name": "Lowpolyzer",
    "author": "Julien Vanelian",
    "version": (0, 1, 0),
    "blender": (2, 81, 0),
    "location": "View3D > Object > Transform",
    "description": "Apply a low poly style to objects",
    "category": "Object",
}

import bpy
from . import operators


def register():
    operators.register()


def unregister():
    operators.unregister()


if __name__ == "__main__":
    register()

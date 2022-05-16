import bpy
from bpy.types import (Operator)
from bpy.props import (FloatProperty)

class VIEW_OT_frame_cursor(Operator):
    bl_label = "Frame Cursor"
    bl_idname = "view.frame_cursor"
    bl_description = "Centers the view around the 3d cursor"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_options = {'REGISTER', 'UNDO'}

    view_distance: bpy.props.FloatProperty(
        name = "Distance",
        default = 2,
        min = 0.1,
        max = 500,
        description = "Distance between the cursor and the viewport camera",
    )

    def execute(self, context):
        selected_obj = bpy.context.selected_objects
        active_obj = bpy.context.active_object

        bpy.ops.mesh.primitive_cube_add(size=(self.view_distance * 2))
        bpy.ops.view3d.view_selected()
        bpy.ops.object.delete(use_global=False, confirm=False)

        if selected_obj:
            for obj in selected_obj:
                obj.select_set(True)
        if active_obj:
            bpy.context.view_layer.objects.active = active_obj

        return {'FINISHED'}

def draw_menu(self, context):
    if bpy.context.mode == 'OBJECT':
        self.layout.separator()
        self.layout.operator(VIEW_OT_frame_cursor.bl_idname)

def register():
    bpy.utils.register_class(VIEW_OT_frame_cursor)
    bpy.types.VIEW3D_MT_view.append(draw_menu)

def unregister():
    bpy.utils.unregister_class(VIEW_OT_frame_cursor)
    bpy.types.VIEW3D_MT_view.remove(draw_menu)
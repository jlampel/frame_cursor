# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name": "Frame Cursor",
    "author": "Jonathan Lampel",
    "version": (1, 0),
    "blender": (3, 1, 0),
    "location": "3D View > View",
    "description": "Orients the view around the 3d cursor",
    "warning": "",
    "wiki_url": "",
    "category": "3D View",
}

from . import frame_cursor

def register():
    frame_cursor.register()

def unregister():
    frame_cursor.unregister()

if __name__ == "__main__":
    register() 
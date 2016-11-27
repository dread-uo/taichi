from taichi_utils import *

class Materials:
    def __init__(self):
        self.materials = {}

    def get_material(self, name):
        '''
        if name not in self.materials:
            self.materials[name] = getattr(self, 'get_material_' + name)()
        return self.materials[name]
        '''
        # Let just waste some memory for easier implementation...
        mat = getattr(self, 'get_material_' + name)()
        return mat

    def get_material_mirror(self):
        material = tc.create_surface_material('pbr')
        material.initialize(P(diffuse_color=(0.0, 0.0, 0.0), specular_color=(1.0, 1.0, 1.0), glossiness=-1, transparent=False))
        return material

    def get_material_gold(self):
        material = tc.create_surface_material('pbr')
        material.initialize(P(diffuse_color=(0.0, 0.0, 0.0), specular_color=(1.0, 0.9, 0.6), glossiness=-1, transparent=False))
        return material

    def get_material_glossy(self):
        material = tc.create_surface_material('pbr')
        material.initialize(P(diffuse_color=(0.0, 0.0, 0.0), specular_color=(0.5, 0.5, 0.3), glossiness=300, transparent=False))
        return material

    def get_material_wall(self):
        tex = tc.create_texture("image")
        tex.initialize(P(filename="C:/tmp/download.jpg"))
        texture_id = tc.register_texture(tex)
        material = tc.create_surface_material('diffusive')
        material.initialize(P(diffuse_map=texture_id))
        return material

    def get_material_glass(self):
        material = tc.create_surface_material('pbr')
        material.initialize(P(diffuse_color=(0, 0, 0), specular_color=(0.0, 0.0, 0.0), glossiness=-1,
                              transparent=True, ior=1.3))
        return material

    def get_material_dark_grey(self):
        material = tc.create_surface_material('pbr')
        material.initialize(P(diffuse_color=(0.3, 0.3, 0.3), specular_color=(0.0, 0.0, 0.0), glossiness=-1,
                              transparent=False))
        return material

    def get_material_interface(self):
        material = tc.create_surface_material('plain_interface')
        material.initialize(P())
        vol = tc.create_volume_material("homogeneous")
        vol.initialize(P(scattering=1, absorption=0))
        material.set_internal_material(vol)
        return material


materials = Materials()
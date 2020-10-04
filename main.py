
from utils.gl_color import color
from utils.gl_math import V2, V3
from gl import Raytracer
from obj import Obj, Texture
from sphere import Sphere, Material,PointLight, AmbientLight
import random

# brick = Material(diffuse = color(0.8, 0.25, 0.25 ), spec = 16)
# stone = Material(diffuse = color(0.4, 0.4, 0.4 ), spec = 32)
# grass = Material(diffuse = color(0.5, 1, 0), spec = 32)
# glass = Material(diffuse = color(0.25, 1, 1), spec = 64)
coal = Material(diffuse = color(0.15,0.15,0.15), spec = 32)
snow = Material(diffuse = color(1, 1, 1), spec = 64)
carrot= Material(diffuse = color(1, 0.54, 0), spec = 64)
eyes= Material(diffuse = color(0.90, 0.90, 0.90),spec = 64)

width = 600
height = 400

r = Raytracer(width,height)
r.pointLight = PointLight(position = (-1,2,0), intensity = 1)
r.ambientLight = AmbientLight(strength = 0.1)

r.scene.append( Sphere(V3(0, -3.1, -10), 2.3, snow) )
r.scene.append( Sphere(V3(0, 0,  -10), 1.8, snow) )
r.scene.append( Sphere(V3(0, 2.9, -10), 1.3, snow) )


r.scene.append( Sphere(V3(0, 2.15, -8), 0.24, carrot) )

r.scene.append( Sphere(V3(0.43, 1.8, -8), 0.1, coal) )
r.scene.append( Sphere(V3(0.15, 1.6, -8), 0.1, coal) )
r.scene.append( Sphere(V3(-0.15, 1.6, -8), 0.1, coal) )
r.scene.append( Sphere(V3(-0.43, 1.8, -8), 0.1, coal) )

r.scene.append( Sphere(V3(0.40, 2.5, -8), 0.12, coal) )
r.scene.append( Sphere(V3(-0.40, 2.5, -8), 0.12, coal) )

r.scene.append( Sphere(V3(0, 0.5, -8.5), 0.26, coal) )
r.scene.append( Sphere(V3(0, -0.8, -8.5), 0.26, coal) )
r.scene.append( Sphere(V3(0, -2.2, -7.5), 0.26, coal) )
r.rtRender()

r.glFinish('output.bmp')


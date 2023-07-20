from gl import Renderer, V2,V3, color
import shaders

width = 1920

height = 1080

rend = Renderer(width,height)

rend.glClearColor(0, 0, 0)
rend.glClear()

rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.fragmentShader

rend.glLoadModel("Dragon.obj", translate = (32, 25,0), scale = (30, 30,0), rotate = (0, 5, 0))

rend.glRender()

rend.glFinish("output.bmp")
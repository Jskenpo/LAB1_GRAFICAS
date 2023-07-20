from gl import Renderer, V2,V3, color
import shaders

width = 1920

height = 1080

rend = Renderer(width,height)

rend.glClearColor(0, 0, 0)
rend.glClear()

rend.glModelMatrix(translate = (width/2, height/2,0))

rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.fragmentShader

rend.glLoadModel("Dragon.obj", translate = (width/2, height/2,0), scale = (5, 5,0), rotate = (0, 0, 0))

rend.glRender()

rend.glFinish("output.bmp")
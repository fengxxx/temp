from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import  time



angle=0.0
x=0.0
y=1.75
z=5.0

lx=0.0
ly=0.0
lz=-1.0



lastx=0
lasty=0
def MouseMotion (x, y):
	global lastx, lasty
	lastx = x*0.1
	lasty = y*0.1
	glutPostRedisplay ()


'''
eyeP=[10.0,10.0,10.0]

glLoadIdentity()
glTranslated(eyeP[0], eyeP[1], eyeP[2])
'''
'''
    def setXRotation(self, angle):
        angle = self.normalizeAngle(angle)
        if angle != self.xRot:
            self.xRot = angle
            self.xRotationChanged.emit(angle)
            self.updateGL()

    def setYRotation(self, angle):
        angle = self.normalizeAngle(angle)
        if angle != self.yRot:
            self.yRot = angle
            self.yRotationChanged.emit(angle)
            self.updateGL()

    def setZRotation(self, angle):
        angle = self.normalizeAngle(angle)
        if angle != self.zRot:
            self.zRot = angle
            self.zRotationChanged.emit(angle)
            self.updateGL()
'''

def click( button, state, x, y ):
	"""Handler for click on the screen"""
	if state == GLUT_UP:
		print "xxxx"

def key_pressed(*args):
	# If escape is pressed, kill everything.
	if args[0] == '\033':
		sys.exit()

def orientMe(ang):
        global angle,x,y, z,lx, ly, lz
        lx = math.sin(ang)
        lz = -math.cos(ang)
        glLoadIdentity()
        gluLookAt(x, y, z, x + lx,y + ly,lz, 0.0,1.0,0.0)
        #glutPostRedisplay ()
def moveMeFlat( direction):
        global angle,x,y, z,lx, ly, lz
        x = x + direction*(lx)*0.1
        z = z + direction*(lz)*0.1
        glLoadIdentity()
        #glPushMatrix ()
        gluLookAt(x, y, z, x + lx,y + ly, lz, 0.0,1.0,0.0)
        #glutPostRedisplay ()
        #glPopMatrix ()
def inputKey( key,  xx,  yy):
        global angle,x,y, z,lx, ly, lz

        while (key):
                if key=="a":
                        angle -= 0.001
                        orientMe(angle)
                        print str(angle)   
                        break
                if key=="d": 
                        angle +=10
                        orientMe(angle)
                        print str(angle)
                        break
                if key=="w":
                        
                        moveMeFlat(10)
                        break
                if key=="s": 
                        moveMeFlat(-0.1)
                        break

def Draw():
    
    PI=3.1415926
    R=0.5
    TR=R-0.05
    glClear(GL_COLOR_BUFFER_BIT)
    genList = glGenLists(1)

    glNewList(1,GL_COMPILE)
    glLineWidth(50)
    glColor3f(0.5,0.1,0.1)
    glBegin(GL_LINE_LOOP)
    for i in range(100):
        glVertex2f(R*math.cos(2*PI/100*i),R*math.sin(2*PI/100*i))
    glEnd()
    glEndList()

    glNewList(2,GL_COMPILE)
    glColor3f(0.1,0.5,0.1)
    glBegin(GL_LINE_LOOP)
    glVertex2f(-0.11,1.2)
    glEnd()
    #gluLookAt(10,10,10,0,0,0,0,0,1)
    #glFrustum(-0.15, +0.15, +0.15, -0.15, 1, 90.0)
    #glRatote(30.0,0,0,1)
    glutSolidCube(1.9)
    glEndList()
    
    glNewList(3,GL_COMPILE)
    glBegin(GL_POLYGON)
    glVertex3f(1,2,1)
    glVertex3f(1,4,2)
    glVertex3f(5,2,3)
    glVertex3f(1,34,1)
    glEnd()
    glEndList()

    glRotatef(30.0,0,0,1)
    glCallList(2)
    glFlush()
glutInit()
glutInitDisplayMode( GLUT_RGBA)


glutInitWindowSize(400, 400)

glutCreateWindow("test")
glViewport(0,0,400,400)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(94.0,1.2,0.1,1200)
gluLookAt(2,2,2,0,0,0,0,1,0)
#gluLookAt(x, y, z, x + lx,y + ly, lz, 0.0,1.0,0.0)
glutDisplayFunc(Draw)
#glutIdleFunc(Update)
#glutSpecialFunc(inputKey)
glutKeyboardFunc(inputKey)#key_pressed)
#glutMotionFunc(MouseMotion)
#glutMouseFunc( click )
glutMainLoop()


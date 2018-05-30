import  pygame, sys, math

def rotate2d(pos,rad):
    x,y=pos
    s,c=math.sin(rad),math.cos(rad)
    return x*c - y*s, y*c + x*s
    #return x,y
class Cam:
    def __init__(self,pos=(0,0,0),rot=(0,0)):
     self.pos = list(pos)
     self.rot = list(rot)
    def events(self,event):
      if event.type == pygame.MOUSEMOTION:
         x,y = event.rel
         x/=200; y/=200
         self.rot[1] -= x; self.rot[0]-= y
         #x/=500; y/=500
         ##print (self.rot[1], self.rot[0]	)
    def update(self,dt,key):
     s=dt*4
     x,y =  s*math.sin(self.rot[1]), s*math.cos(self.rot[1])
    
     if key[pygame.K_q]: self.pos[1]+=s
     if key[pygame.K_e]: self.pos[1]-=s
     if key[pygame.K_w]: self.pos[2]+=y; ##self.pos[0]+=x
     if key[pygame.K_s]: self.pos[2]-=y; ##self.pos[0]-=x
     if key[pygame.K_a]: self.pos[0]-=y;  ##self.pos[2]+=x  
     if key[pygame.K_d]: self.pos[0]+=y; ##self.pos[2]-=x     	 
     ##print(self.pos[0],self.pos[1], self.pos[2]) 
#
#  e1 e2 e2
#  a1 a2 a3 
#  b1 b2 b3 
#  a2*b3 - a3*b2 - (a1*b3 - a3*b1 ) + a1*b2 - a2*b1
#  C a2*b3 - a3*b2 , -  a1*b3 + a3*b1 ,   + a1*b2 - a2*b1
def VectX_3x3 ( A, B):
    C=[[],[],[]]
	
    C[0]=A[1]*B[2] - A[2]*B[1]
    C[1]=-A[0]*B[2] + A[2]*B[0]
    C[2]=A[0]*B[1] - A[1]*B[0]
    R=math.sqrt(C[0]*C[0] + C[1]*C[1] + C[2]*C[2])
    if R > 0:
     C[0]=C[0]/R
     C[1]=C[1]/R
     C[2]=C[2]/R
    return C 
def VectScalarX(A,B):
    C=A[0]*B[0] + A[1]*B[1] + A[2]*B[2]    
    return C

def distMidd(A1,A2,A3,C):
    Xmid=(A2[0] + A1[0])/2
    Ymid=(A3[1] + A2[1])/2
    Zmid=(A3[2] + A1[2])/2
    dist=Xmid*Xmid + Ymid*Ymid + Zmid*Zmid
    return dist
     
     

face_color=(255,0,0), (0,255,0), (0,0,255),(200,0,200), (255,255,25), (120,130,100)
class Cube:
    vertices=(-1,-1,-1),(1,-1,-1),(1,1,-1),(-1,1,-1),(-1,-1,1),(1,-1,1),(1,1,1),(-1,1,1)
    edges=(0,1), (1,2), (2,3), (3,0), (4,5) , (5,6), (6,7),(7,4), (0,4), (1,5),(2,6),(3,7)
    faces=(0,1,2,3),(4,5,6,7),(0,1,5,4),(2,6,7,3),(1,2,6,5),(0,3,7,4)
    
    def __init__(self,pos=(0,0,0)):
        x,y,z = pos
        self.verts= [ (x+ X/2, y+Y/2,z+Z/2 ) for X,Y,Z in self.vertices ]  
	
pygame.init()
w,h=800,600; cx,cy  =  w//2,h//2 
screen= pygame.display.set_mode((w,h))
clock =  pygame.time.Clock()
#  1    2
#     5   6
#  0    3 
#     4    7
radian=0
cam = Cam((0,0,-5))

pygame.event.get();pygame.mouse.get_rel()
pygame.mouse.set_visible(0)
pygame.event.set_grab(1)
pac_points=[(-2,0,1),(-2,0,0.75),(-2,0,0.5),(-2,0,0.25),(-2,0,0),(2,0,1),(2,0,0.75),(2,0,0.5),(2,0,0.25),(2,0,0)]
#,(13,0),(-14,1),(-15,1),(-16,1),(-17,1),(-18,1),(-19,1),(-20,1),(-21,1),(-22,1	)]
#(22,1),(23,2),(24,3),(25,0),(26,0),(26,0),(27,0),(28,0),(29,0),(30,0),(31,0),(32,0),(32,0),(34,0),(35,0),(35,0),(37,0),(38,0),(39,0),(40,0),(41,0),(42,0),(43,0)]

#Cubes = [Cube((x,y,z)) for x,y,z in pac_points]
Cubes=[Cube((-3,0,0)),Cube((-3,0,-0.5)), Cube((-3,0,-1)), Cube((2,0,0)),Cube((2,0,-0.5)),Cube((2,0,-1))]
try:
 while True:
    dt = clock.tick()/3000	
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
      pygame.quit();sys.exit()
    if event.type ==  pygame.KEYDOWN:
       if event.key == pygame.K_ESCAPE:
           pygame.quit();sys.exit()
    if event.type == pygame.MOUSEMOTION:
      cam.events(event)
    screen.fill((0, 0, 0))
    print ("----------")
    cc=0
    allpoly={}
    allvert={}
    s_l=[]
    for obj in Cubes:
     vert_list=[];screen_coords=[]
     #print ("obj.verts:", obj.verts)
     for x,y,z in  obj.verts: 
                
        x-=cam.pos[0]
        y-=cam.pos[1]
        z-=cam.pos[2]
                
        x,z= rotate2d((x,z),cam.rot[1])
        y,z= rotate2d((y,z),cam.rot[0])
            
        vert_list+=[(x,y,z)]
        f=100/z 
        
        x,y=cx+x*f,cy+y*f
        if x<0 : x=0
        if y<0 : y=0
        if x>w : x=w
        if y>h : y=h
        screen_coords += [(x,y,z)]
        
     for f  in range(len(obj.faces)):
        poly=[]
        vert=[]
        face=obj.faces[f]
        on_screen=False
        for i in face:
          x,y=(screen_coords[i][0],screen_coords[i][1])
          if  x>0 and x<w and y>0 and y<h : on_screen = True		  
          poly+=[(x,y)]
          vert+=[(vert_list[i][0],vert_list[i][1],vert_list[i][2])]		
        allpoly[cc]=poly
        #print(vert)
        allvert[cc]=vert
        cc+=1
        ##print (allvert)
        ###pygame.draw.line(screen, (0, 0, 0),poly[0],poly[1],3)   		
        ###pygame.draw.line(screen, (0, 0, 0),poly[1],poly[2],3)   		
        ###pygame.draw.line(screen, (0, 0, 0),poly[2],poly[3],3)   		
        ###pygame.draw.line(screen, (0, 0, 0),poly[3],poly[0],3)
    print (allvert)		
    ###s_l=sorted(range(0,len(allvert)), key=lambda x : allvert[x][0][2]**2 + allvert[x][1][2]**2 + allvert[x][2][2]**2 + allvert[x][3][2]**2,reverse=True)    
    ##s_l=sorted(range(0,len(allvert)), key=lambda x : (allvert[x][0][2]- cam.pos[2])**2 + (allvert[x][2][2]- cam.pos[2])**2 + (allvert[x][3][2]- cam.pos[2])**2 +(allvert[x][1][2]- cam.pos[2])**2,reverse=True)    
    s_l=sorted(range(0,len(allvert)), key=lambda x :  distMidd(allvert[x][0], allvert[x][1] , allvert[x][2],cam.pos),reverse=True)    
    print (s_l )
    if  on_screen == True:
      for l in s_l:
        try: pygame.draw.polygon(screen,face_color[l%6],allpoly[l])
        except: pass
		 

    	   
    pygame.display.flip()
   
    key = pygame.key.get_pressed()
    cam.update(dt,key)	
finally:
    pygame.quit();sys.exit()
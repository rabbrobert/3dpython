
import  pygame, sys, math


w,h=1000,600; cx,cy  =  w//2,h//2 

top=0.4
bottom=-0.4
left=-0.4
right=0.4
near=-0.50
far=-0.75
TANFOV=top/near	
aspect=w/h 
FOV = math.atan(TANFOV)
TANFOV2=math.tan(FOV/2)



def VectX ( A, B):
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
	
def ScalarX(A,B):
    C=A[0]*B[0] + A[1]*B[1] + A[2]*B[2]
	
    return C

def distMidd(A1,A2,A3,C):
    Xmid=(A2[0] + A1[0] + A3[0])/3 - C[0]
    Ymid=(A3[1] + A2[1]  + A1[1])/3 - C[1]
    Zmid=(A3[2] + A1[2] + A2[2])/3  - C[2]
    
    dist=Xmid*Xmid + Ymid*Ymid + Zmid*Zmid
    
    
    return dist
    ##return (math.fabs(A2[0]-A1[0]) + math.fabs(A2[1] - A1[1]) + math.fabs(A3[0]- A1[0]) + math.fabs(A3[1] - A1[1]) +  math.fabs(A3[0]- A2[0]) + math.fabs(A3[1] - A2[1]))	

def calcM4X4(M4X4=([(0,0,0,0)],[(0,0,0,0)],[(0,0,0,0)],[(0,0,0,0)]) ,V1X4=[[],[],[],[]] ):
    RET1X4= [[],[],[],[]]
    
    #x
    RET1X4[0] = M4X4[0][0]*V1X4[0] +  M4X4[0][1]*V1X4[1] + M4X4[0][2]*V1X4[2] +M4X4[0][3]*V1X4[3]
    #y
    RET1X4[1] = M4X4[1][0]*V1X4[0] +  M4X4[1][1]*V1X4[1] + M4X4[1][2]*V1X4[2] +M4X4[1][3]*V1X4[3]
    #z
    RET1X4[2] = M4X4[2][0]*V1X4[0] +  M4X4[2][1]*V1X4[1] + M4X4[2][2]*V1X4[2] +M4X4[2][3]*V1X4[3]
    #w
    RET1X4[3] = M4X4[3][0]*V1X4[0] +  M4X4[3][1]*V1X4[1] + M4X4[3][2]*V1X4[2] +M4X4[3][3]*V1X4[3]
    w=RET1X4[3]
    
    if w == 0 : w=0.001
    RET1X4[0]=RET1X4[0]/w
    RET1X4[1]=RET1X4[1]/w
    RET1X4[2]=RET1X4[2]/w
    RET1X4[3]=RET1X4[3]/w
    return RET1X4

def getVecToCam(Vpos=(0,0,0), Cpos=(0,0,0)):
    VTC=[[],[],[]]
    X= Vpos[0] - Cpos[0]
    Y= Vpos[1] - Cpos[1]
    Z= Vpos[2] - Cpos[2]
    R= math.sqrt(X*X + Y*Y +Z*Z)
    X=X/R
    Y=Y/R
    Z=Z/R
    VTC[0]= X;VTC[1]=Y;VTC[2]=Z
    return VTC
 
def rotate2d(pos,rad):
    x,y=pos
    s,c=math.sin(rad),math.cos(rad)
    return x*c - y*s, y*c + x*s
	
def CheckCollition():
    Collision = False
    possaved = cam.pos
    for i in  range(len(T)): 
     if cam.pos[0] >  T[i].minx and cam.pos[0] <  T[i].maxx  and cam.pos[2] >  T[i].minz and cam.pos[2] <  T[i].maxz : 
#and self.pos[1] < cube1.maxy and self.pos[1] > cube1.minx and self.pos[2] < cube1.maxz and self.pos[2] > cube1.minz:
      
      print(possaved, cam.pos)	
      cam.pos = possaved
      Collision = True
      print(possaved, cam.pos)
    return Collision
	
class Triangle:
  
  #vertices=(0,0,1),(1,0,1),(1,1,1)
  vertices=(0,0,1),(1,1,1),(1,0,1)
  vertices_2=(0,0,1),(0,1,1),(1,1,1)
  #vertices_2=(0,0,1),(1,1,1),(0,1,1)
  vertices_3=(0,0,0),(1,0,0),(1,1,0)
  #vertices_3=(0,0,0),(1,1,0),(1,0,0)
  #vertices_3=(0,0,0),(1,0,0),(1,1,0)
  vertices_4=(0,0,0),(1,1,0),(0,1,0)
  #vertices_4=(0,0,0),(0,1,0),(1,1,0)
  ##vertices_4=(0,0,0),(1,1,0),(0,1,0)
  vertices_5=(0,0,0),(0,0,-1),(0,1,0)
  #vertices_5=(0,0,0),(0,1,0),(0,0,-1)
  vertices_6=(0,1,0),(0,0,-1),(0,1,-1)
  #vertices_6=(0,1,0),(0,1,-1),(0,0,-1)
  vertices_7=(1,0,-1),(1,0,0),(1,1,0)
  #vertices_7=(1,0,0),(1,0,-1),(1,1,0)
  vertices_8=(1,0,-1),(1,1,0),(1,1,-1)
  vertices_9=(0,0,0),(0,0,-1),(1,0,-1)
  #	vertices_9=(0,0,-1),(0,0,0),(1,0,-1)
  vertices_10=(1,0,-1),(1,0,0),(0,0,0)
  #vertices_10=(0,0,0),(1,0,0),(1,0,-1)
  #vertices_11=(0,1,0),(0,1,-1),(1,1,-1)
  vertices_11=(0,1,0),(1,1,-1),(0,1,-1)
  #vertices_12=(1,1,-1),(1,1,0),(0,1,0)
  vertices_12=(1,1,0),(1,1,-1),(0,1,0)
  
  edges=(0,1), (1,2), (2,0) 
  faces=(0,1,2)
    
  def __init__(self,pos=(0,0,0),size=1,color=(0,0,0),type=1):
    x,y,z = pos
    self.size = size
    self.color = color
    self.pos=pos
    self.type=type
    self.V1 = [[],[],[]]
    self.V2 = [[],[],[]]
    self.normV= [[],[],[]]
	
    if type == 1:
      self.verts= [ (x+ size*X/2, y+size*Y/2,z+size*Z/2 ) for X,Y,Z in self.vertices ]
    elif type == 2: 
      self.verts= [ (x+ size*X/2, y+size*Y/2,z+size*Z/2 ) for X,Y,Z in self.vertices_2 ]
    elif type == 3:	  
      self.verts= [ (x+ size*X/2, y+size*Y/2,z+size*Z/2 ) for X,Y,Z in self.vertices_3 ]
    elif type == 4:	  
     self.verts= [ (x+ size*X/2, y+size*Y/2,z+size*Z/2 ) for X,Y,Z in self.vertices_4 ]
    elif type == 5:  
      self.verts= [ (x+ size*X/2, y+size*Y/2,z+size*Z/2 ) for X,Y,Z in self.vertices_5 ]
    elif type == 6:  
      self.verts= [ (x+ size*X/2, y+size*Y/2,z+size*Z/2 ) for X,Y,Z in self.vertices_6 ]
    elif type == 7:  
      self.verts= [ (x+ size*X/2, y+size*Y/2,z+size*Z/2 ) for X,Y,Z in self.vertices_7 ]
    elif type == 8:  
      self.verts= [ (x+ size*X/2, y+size*Y/2,z+size*Z/2 ) for X,Y,Z in self.vertices_8 ]
    elif type == 9:  
      self.verts= [ (x+ size*X/2, y+size*Y/2,z+size*Z/2 ) for X,Y,Z in self.vertices_9 ]
    elif type == 10:  
      self.verts= [ (x+ size*X/2, y+size*Y/2,z+size*Z/2 ) for X,Y,Z in self.vertices_10 ]
    elif type == 11:  
      self.verts= [ (x+ size*X/2, y+size*Y/2,z+size*Z/2 ) for X,Y,Z in self.vertices_11 ]
    elif type == 12:  
      self.verts= [ (x+ size*X/2, y+size*Y/2,z+size*Z/2 ) for X,Y,Z in self.vertices_12 ]
    self.V1 = [ (self.verts[1][0] - self.verts[0][0]),(self.verts[1][1] - self.verts[0][1]), (self.verts[1][2] - self.verts[0][2]) ] 	
    self.V2 = [ (self.verts[2][0] - self.verts[0][0]),(self.verts[2][1] - self.verts[0][1]), (self.verts[2][2] - self.verts[0][2]) ] 	
    ##print (" self.verts[0]:",  self.verts[0] , " self.verts[1]:",  self.verts[1],"self.verts[2]:",self.verts[2])
    self.normV = VectX(self.V1, self.V2)
    print("self.verts:", self.verts)

 
    
class C2D:
  def __init__(self,pos=(0,0),color=(0,0,0), notvisible=0):
    self.pos=pos
    self.color=color
    self.notvisible = notvisible

class Object:
  def __init__ (self, Triangles):	
    self.Triangles=Triangles
    self.maxx=(Triangles[0].verts[0])[0]
    self.maxy=(Triangles[0].verts[1])[1]
    self.maxz=(Triangles[0].verts[2])[2]
    self.minx=(Triangles[0].verts[0])[0]
    self.miny=(Triangles[0].verts[1])[1]
    self.minz=(Triangles[0].verts[2])[2]
    for o in Triangles:
     for (x,y,z) in o.verts:
      if  x < self.minx:    self.minx = x
      if  y < self.miny:    self.miny = y 
      if  z < self.minz:    self.minz = z 
      if  x < self.minx:    self.minx = x
      if  y < self.miny:    self.miny = y 
      if  z < self.minz:    self.minz = z
    ##print("self.minx",self.minx)	  
    ##print("self.miny",self.miny)
    ##print("self.minz",self.minz)	
    ##print("self.maxz",self.minz)	


	
class Cam:
  def __init__(self,pos=(0,0,0),rot=(0,0)):
    self.pos = list(pos)   # camera position
    self.rot = list(rot)
    self.d = self.pos[2] #  screen  z coordinat is the first  z value of camera posotion
    self.rot_grad=(self.rot[0]*180/math.pi , self.rot[1]*180/math.pi )
    self.posa = list(pos)
    self.posb = list(pos)
    self.posa[0] +=1
    self.posb[1]-=1
    self.normV= [[],[],[]]
    self.V1 = [[],[],[]]
    self.V2 = [[],[],[]]
    self.V1= (self.posa[0] - self.pos[0]), (self.posa[1] - self.pos[1]), (self.posa[2]- self.pos[2])     
    self.V2= (self.posb[0] - self.pos[0]), (self.posb[1] - self.pos[1]), (self.posb[2]- self.pos[2])     
    self.normV = VectX(self.V1, self.V2)
    ##x,z=rotate2d((self.normV[0],self.normV[2]),self.rot[0])
    ##self.normV[0]=x; self.normV[2]=z


	
  def update(self,dt,key):
    s=dt*4
    x,y =  s*math.sin(self.rot[1]), s*math.cos(self.rot[1])
    rat=0.015
    ###if key[pygame.K_q]: self.pos[1]+=rat*y ; #self.posa[1]+=rat*y ; self.posb[1]+=rat*y      #;self.pos[1]+=x
    ###if key[pygame.K_e]: self.pos[1]-=rat*y ;  #self.posa[1]-=rat*y ; self.posb[1]-=rat*y   #; self.pos[1]-=x
    possaved = list(self.pos)
	
    if key[pygame.K_UP]: 
       self.pos[2]+=rat*(self.normV[2] ) ; self.pos[0]-=rat*(self.normV[0]  ) ; #self.posa[2]+=rat*y ; self.posb[2]+=rat*y   #; self.pos[0]+=x
    if key[pygame.K_DOWN]:
       self.pos[2]-=rat*(self.normV[2] ); self.pos[0]+=rat*(self.normV[0]  ) ;#self.posa[2]-=rat*y ; self.posb[2]-=rat*y   #self.pos[0]-=x
    
		
    if key[pygame.K_a]: 
        if math.fabs (self.normV[0] ) > math.fabs(self.normV[2]):   self.pos[2]-=rat*(self.normV[0]) ;  #self.posa[0]-=rat*y ; self.posb[0]-=rat*y   #;  self.pos[0]-=x
        else:  	self.pos[0]-=rat#*(self.normV[2])
    if key[pygame.K_d]: 
        if math.fabs (self.normV[0] ) > math.fabs(self.normV[2]):   self.pos[2]+=rat*(self.normV[0]) ;  #self.posa[0]-=rat*y ; self.posb[0]-=rat*y   #;  self.pos[0]-=x
        else:  	self.pos[0]+=rat#*(self.normV[2])	
		        
	
    #if key[pygame.K_d]: 
    #   self.pos[0]+=rat*(self.normV[0]  ); self.pos[2]+=rat*(self.normV[2] ) ; #self.posa[0]+=rat*y ; self.posb[0]+=rat*y    #  self.pos[0]+=x
    
    #if key[pygame.K_w]: self.rot[0] += math.pi/18#; self.rot[1]+=math.pi/9
    #if key[pygame.K_s]: self.rot[0]-= math.pi/18 #; self.rot[1]-= math.pi/9
    if key[pygame.K_LEFT]: self.rot[0] -= math.pi/18#; self.rot[1]+=math.pi/12
    if key[pygame.K_RIGHT]: self.rot[0] += math.pi/18#; self.rot[1]-= math.pi/12

    Collision = False
    xcol =  self.pos[0]# +  self.normV[0]*0.02
    ycol =  self.pos[1]# +  self.normV[1]*0.02
    zcol =  self.pos[2]# +  self.normV[2]*0.02
    ##print (" self.pos[0]:" , self.pos[0], "xcol", xcol, " self.pos[2]", self.pos[2],"zcol:",zcol,"self.normV",self.normV) 
    for i in  range(len(T)):	
     if xcol >  T[i].minx and xcol <  T[i].maxx  and zcol >  T[i].minz and zcol <  T[i].maxz : 
#and self.pos[1] < cube1.maxy and self.pos[1] > cube1.minx and self.pos[2] < cube1.maxz and self.pos[2] > cube1.minz:
      print (cube1.minx ," < ",self.pos[0]," < ",cube1.maxx)
      print(possaved, self.pos)	
      self.pos = possaved
      Collision = True
      print(possaved, self.pos)
    
      
	
    if self.rot[0] > 2*math.pi: self.rot[0] =  self.rot[0] - 2*math.pi   
    if self.rot[1] > 2*math.pi: self.rot[1] =  self.rot[1] - 2*math.pi   
	
    if self.rot[0] < 0: self.rot[0] =  self.rot[0] + 2*math.pi   
    if self.rot[1] < 0: self.rot[1] =  self.rot[1] + 2*math.pi   
	
    self.rot_grad=(self.rot[0]*180/math.pi , self.rot[1]*180/math.pi )
   
    self.posa = list(self.pos)
    self.posb = list(self.pos)
    self.posa[0]+=1
    self.posb[1]-=1
    self.V1= (self.posa[0] - self.pos[0]), (self.posa[1] - self.pos[1]), (self.posa[2]- self.pos[2])     
    self.V2= (self.posb[0] - self.pos[0]), (self.posb[1] - self.pos[1]), (self.posb[2]- self.pos[2])     

    self.normV = VectX(self.V1, self.V2)
    x,z=rotate2d((self.normV[0],self.normV[2]),self.rot[0])
    self.normV[0]=x; self.normV[2]=z
    
# perspective projection
#       x	
#	    |            P
#       |  P'|
#	----0----|-------------------  -z
#       | -d |  
# | 1 0  0   0 |     | x |      |   x   |     | x*-d/z |   
# | 0 1  0   0 |     | y |      |   y   |     | y*-d/z | 
# |´0 0  1   0 |  *  | z |  =   |   z   |  =  | -d     |    
# | 0 0 -1/d 0 |     | 1 |      |  -z/d |     |  1     |
# 
#
#  x= d*x/(d+z)
#  
  def ProjectionTo2D_1(self, p=(0,0,0)):
    xx=p[0]-self.pos[0]
    yy=p[1]-self.pos[1]
    zz=p[2]-self.pos[2]
    d=140
    if zz == 0:  zz=0.01
    m  =  -d/(zz) #self.pos[2]/zz 
    y = yy*m
    x = xx*m
   
    return ((x,y)) 	

# perspective projection 2
#       x	
#	    |            P
#       |  P'|
#	----0----|-------------------  -z
#       | -d |  
# | 1 0  0   0 |     | x |      |   x    |     | x*d/(z+d) |   
# | 0 1  0   0 |     | y |      |   y    |     | y*d/(z+d) | 
# |´0 0  1   d |   * | z |  =   | z +  d |  =  |   d       |          
# | 0 0 1/d  1 |     | 1 |      | z/d +1 |     |   1       |
# 
#
#  x= d*x/(d+z)
#
#d=-50   
#V4x4=[(1,0,0,0), (0,1,0,0), (0,0,1,d), (0,0,1/d, 1)  ] 
 
  def ProjectionTo2D(self, p=(0,0,0)):
    xx=p[0]-self.pos[0]
    yy=p[1]-self.pos[1]
    zz=p[2]-self.pos[2]
   
    d=self.d	
    retc = 0
    r =  math.sqrt(zz*zz + xx*xx +yy*yy )
    if zz == 0 :  zz=0.01	
    m  = d/(zz) 
    
    y = yy*m
    x = xx*m
	
    #public float left = -0.2F;
    #public float right = 0.2F;
    #public float top = 0.2F;
	#pub bottom = -0.2F;
	
	#xm = 2.0F * near / (right - left);
    #ym = 2.0F * near / (top - bottom);
    #am = (right + left) / (right - left);
    #bm = (top + bottom) / (top - bottom);
    #cm = -(far + near) / (far - near);
    #dm = -(2.0F * far * near) / (far - near);
    #em = -1.0F;
    V4x4=[(1,0,0,0), (0,1,0,0), (0,0,1,0), (0,0,-d, 0)  ]
    #V4x4=[(1/(aspect * TANFOV2) ,0,0,0), (0,1/TANFOV2,0,0), (0,0,(near+far)/(near-far),-1), (0,0,(0.02*(near-far))/(near-far), 0)  ]
    ##V4x4=[(1000/( TANFOV) ,0,0,0), (0,1000/TANFOV,0,0), (0,0,-(far)/(near-far),-1), (0,0,-(near*far)/(near-far), 0)  ]
    V4x4=[(5000/(right-left),0,0,0), (0,5000/(top-bottom),500,0),(0,0,-1/(far-near),0), ( -(right+left)/(right-left),-(top+bottom)/(top-bottom),-(far+near)/(far-near), 1)  ]
    V1x4=(xx,yy,zz,1)
    R1x4=[[],[],[],[]]
    R1x4=calcM4X4(V4x4,V1x4)
    ##if p[2]  > d + self.pos[2] : retc =1

    x=R1x4[0]
    y=R1x4[1]
    ##print("p[0]:" ,p[0] , " p[1]:", p[1],  " p[2]:",  p[2] , " xx:", xx , " yy:", yy, " zz:",zz)
    ##print ("V4x4:", V4x4)
    ##print (" p[0] p[1] p[2]:", p[0],p[1],p[2])
   ## print ("y 2. :", y)
    return ((x,y,retc)) 		

	

# perspective projection 2
#       x	
#	    |            P
#       |  P'|
#	----0----|-------------------  -z
#       | -d |  
# | 1 0  0   0 |     | x |      |   x    |     | x*d/(z+d) |   
# | 0 1  0   0 |     | y |      |   y    |     | y*d/(z+d) | 
# |´0 0  0   0 |  *  | z |  =   |   0    |  =  |  0        |    
# | 0 0 1/d  1 |     | 1 |      | (z+d)/d|     |  1        |
# 
#
#  x= d*x/(d+z)
#    
  def ProjectionTo2D_best(self, p=(0,0,0)):
    xx=p[0]-self.pos[0]
    yy=p[1]-self.pos[1]
    zz=p[2] -self.pos[2]
    ##print(self.pos, zz)
    d =  zz
    m  = 1-p[2]/math.fabs(d)  
    y = yy*m
    if zz < 0:
     x = xx*m
    else:
     x = -xx*m
    
    return ((x,y)) 	
	

	
face_color=(255,0,0), (0,255,0), (0,0,255),(200,0,200), (255,255,25), (120,130,100)
##Triangles = [Triangle((-50,-50,100),100,(155,0,0),1), Triangle((-50,-50,100),100,(155,0,0),2), Triangle((-50,-50,200),100,(155,155,0),3)
##,Triangle((-50,-50,200),100,(155,155,0),4) , Triangle((-50,-50,200),100,(155,155,155),5), Triangle((-50,-50,200),100,(155,155,155),6),
##Triangle((-50,-50,200),100,(44,55,155),7),Triangle((-50,-50,200),100,(44,55,155),8), Triangle((-50,-50,200),100,(200,25,5),9),Triangle((-50,-50,200),100,(200,25,5),10),
##Triangle((-50,-50,200),100,(100,205,5),11), Triangle((-50,-50,200),100,(100,205,5),12) ]

##Triangles = [Triangle((-50,-50,-100),-100,(255,0,0),1), Triangle((-50,-50,-100),-100,(255,0,0),2), Triangle((-50,-50,-200),-100,(155,155,0),3)
##,Triangle((-50,-50,-200),-100,(155,155,0),4) , Triangle((-50,-50,-200),-100,(155,155,155),5), Triangle((-50,-50,-200),-100,(155,155,155),6),
##Triangle((-50,-50,-200),-100,(44,55,155),7),Triangle((-50,-50,-200),-100,(44,55,155),8), Triangle((-50,-50,-200),-100,(200,25,5),9),Triangle((-50,-50,-200),-100,(200,25,5),10),
##Triangle((-50,-50,-200),-100,(100,205,5),11), Triangle((-50,-50,-200),-100,(100,205,5),12) ]

Triangles1 = [
Triangle((-0.050,-0.050, -0.100),-0.100,(255,255,255),1), 
Triangle((-0.050,-0.050,-0.100),-0.100,(255,255,255),2), 
Triangle((-0.050,-0.050,-0.200),-0.100,(155,155,0),3),
Triangle((-0.050,-0.050,-0.200),-0.100,(155,155,0),4), 
Triangle((-0.050,-0.050,-0.200),-0.100,(155,0,155),5), 
Triangle((-0.050,-0.050,-0.200),-0.100,(155,0,155),6),
Triangle((-0.050,-0.050,-0.200),-0.100,(44,55,155),7),
Triangle((-0.050,-0.050,-0.200),-0.100,(44,55,155),8), 
Triangle((-0.050,-0.050,-0.200),-0.100,(200,25,200),9),
Triangle((-0.050,-0.050,-0.200),-0.100,(200,25,5),10),
Triangle((-0.050,-0.050,-0.200),-0.100,(10,205,5),11), 
Triangle((-0.050,-0.050,-0.200),-0.100,(10,205,5),12)
]

cube1 = Object(Triangles1)


#Triangle((-0.050,-0.050, -0.100),-0.100,(255,255,255),1),Triangle((-0.050,-0.050, -0.100),-0.100,(255,255,255),1)

Triangles2 = [
 Triangle((0.050,-0.050, -0.100),-0.100,(255,255,255),1), 
 Triangle((0.050,-0.050,-0.100),-0.100,(255,25,25),2), 
 Triangle((0.050,-0.050,-0.200),-0.100,(155,155,0),3),
 Triangle((0.050,-0.050,-0.200),-0.100,(155,155,0),4), 	
 Triangle((0.050,-0.050,-0.200),-0.100,(155,0,155),5), 
 Triangle((0.050,-0.050,-0.200),-0.100,(155,155,155),6),
 Triangle((0.050,-0.050,-0.200),-0.100,(44,55,155),7),
 Triangle((0.050,-0.050,-0.200),-0.100,(44,255,255),8), 
 Triangle((0.050,-0.050,-0.200),-0.100,(200,25,225),9),
 Triangle((0.050,-0.050,-0.200),-0.100,(20,255,50),10),
 Triangle((0.050,-0.050,-0.200),-0.100,(100,205,5),11), 
 Triangle((0.050,-0.050,-0.200),-0.100,(100,205,5),12)
]

Triangles3 = [
Triangle((-0.050,-0.050, -0.200),-0.100,(255,255,255),1), 
Triangle((-0.050,-0.050,-0.200),-0.100,(255,255,255),2), 
Triangle((-0.050,-0.050,-0.300),-0.100,(155,155,0),3),
Triangle((-0.050,-0.050,-0.300),-0.100,(155,155,0),4), 
Triangle((-0.050,-0.050,-0.300),-0.100,(155,155,155),5), 
Triangle((-0.050,-0.050,-0.300),-0.100,(155,155,155),6),
Triangle((-0.050,-0.050,-0.300),-0.100,(44,55,155),7),
Triangle((-0.050,-0.050,-0.300),-0.100,(44,55,155),8), 
Triangle((-0.050,-0.050,-0.300),-0.100,(200,25,5),9),
Triangle((-0.050,-0.050,-0.300),-0.100,(200,25,5),10),
Triangle((-0.050,-0.050,-0.300),-0.100,(100,205,5),11), 
Triangle((-0.050,-0.050,-0.300),-0.100,(100,205,5),12),
]

Triangles4 = [
Triangle((0.050,-0.050, -0.200),-0.100,(255,255,255),1), 
Triangle((0.050,-0.050,-0.200),-0.100,(255,255,255),2), 
Triangle((0.050,-0.050,-0.300),-0.100,(155,155,0),3),
Triangle((0.050,-0.050,-0.300),-0.100,(155,155,0),4), 
Triangle((0.050,-0.050,-0.300),-0.100,(155,155,155),5), 
Triangle((0.050,-0.050,-0.300),-0.100,(155,155,155),6),
Triangle((0.050,-0.050,-0.300),-0.100,(44,55,155),7),
Triangle((0.050,-0.050,-0.300),-0.100,(44,55,155),8), 
Triangle((0.050,-0.050,-0.300),-0.100,(200,25,5),9),
Triangle((0.050,-0.050,-0.300),-0.100,(200,25,5),10),
Triangle((0.050,-0.050,-0.300),-0.100,(100,205,5),11), 
Triangle((0.050,-0.050,-0.300),-0.100,(100,205,5),12)   
]


Route = [
Triangle((0.050,-0.050, -0.200),-0.100,(255,255,255),1), 
Triangle((0.050,-0.050,-0.200),-0.100,(255,255,255),2), 
Triangle((0.050,-0.050,-0.300),-0.100,(155,155,0),3),
Triangle((0.050,-0.050,-0.300),-0.100,(155,155,0),4), 
Triangle((0.050,-0.050,-0.300),-0.100,(155,155,155),5), 
Triangle((0.050,-0.050,-0.300),-0.100,(155,155,155),6),
Triangle((0.050,-0.050,-0.300),-0.100,(44,55,155),7),
Triangle((0.050,-0.050,-0.300),-0.100,(44,55,155),8), 
Triangle((0.050,-0.050,-0.300),-0.100,(200,25,5),9),
Triangle((0.050,-0.050,-0.300),-0.100,(200,25,5),10),
Triangle((0.050,-0.050,-0.300),-0.100,(100,205,5),11), 
Triangle((0.050,-0.050,-0.300),-0.100,(100,205,5),12)   
]


T=[Object(Triangles1)
,Object(Triangles2), Object(Triangles3),Object(Triangles4)]
##Triangles= [ Triangle((-0.050,-0.050,-0.100),0.100,(155,0,0),1), Triangle((-0.050,-0.050,-0.100),0.100,(2,235,5),4)
##,
##Triangle((-50,-50,-200),100,(2,235,5),11) 
##]
pygame.init()

screen= pygame.display.set_mode((w,h))
clock =  pygame.time.Clock()

cam = Cam((-0.05, -0.075, -0.015))

pygame.event.get();pygame.mouse.get_rel()
pygame.mouse.set_visible(0)
pygame.event.set_grab(1)

while True:
   dt = clock.tick()/2000	
   event = pygame.event.wait()
   if event.type == pygame.QUIT:
      pygame.quit();sys.exit()
   if event.type ==  pygame.KEYDOWN:
       if event.key == pygame.K_ESCAPE:
           pygame.quit();sys.exit()
   screen.fill((0, 0, 0))
   all2D=[]
   allvert=[]
   
   retcode=0
   
   if  CheckCollition() == True: print ("Collision")
   ##else: print ("No collition")   
   for t in T:	
    for obj in t.Triangles	:
     poly=[]
     vert=[]
    # print("---")
     retcode=0
     vertcount=0
     alledge=0
     for x,y,z in  obj.verts:
       xreal=x;yreal=y;zreal=z
       xr = x - cam.pos[0]
       yr = y - cam.pos[1]
       zr = z - cam.pos[2]
       
       xr,zr= rotate2d((xr,zr),cam.rot[0])
       #yr,zr=  rotate2d((yr,zr),cam.rot[1])
       x=xr + cam.pos[0]
       z=zr + cam.pos[2]
       y=yr + cam.pos[1] 
              
       xp,yp,ret=cam.ProjectionTo2D((x,y,z))
       ##print ("verts:",x,y,z, "rotate y :" ,  cam.rot_grad[1])
	   
       #if retcode == 1:  pass
       ##print ("pojected to 2D x,y,z:",xp,yp,z)
       xp=cx+xp 
       yp=cy+yp
       poly+=[(xp,yp)]
       vert+=[(x,y,z)]
 
       ##xN1,yN1,r = cam.ProjectionTo2D((cam.pos[0], cam.pos[1],cam.pos[2]))
       ##xN2,yN2,r = cam.ProjectionTo2D((cam.pos[0] + cam.normV[0], cam.pos[1]  + cam.normV[1], cam.pos[2] + cam.normV[2]))
       ##pygame.draw.line(screen, (0, 255, 255), (xN1+cx, yN1+cy), ( xN2+cx, yN2+cy))
       ##print (xN1,yN1, xN2,yN2)
       VtC=getVecToCam((xreal,yreal,zreal), cam.pos)	   
       sk = ScalarX(obj.normV, cam.normV)
       skVtC = ScalarX( cam.normV,VtC)
       radSk = math.asin(sk)*180/math.pi
       if sk <= 0 :  vertcount+=1
       if vertcount == 3:  retcode = 1	  
       #if radSk <= 20 : retcode= 1       
       ##print ("cam.pos:", cam.pos)
       #if z == 0 :  retcode = 1
       if cam.pos[2] <= z : alledge+=1;retcode = 1
       if alledge== 3 :  retcode =1	 
       #if cam.pos[2] - cam.d <  z : retcode=1
       ##print ("obj.normV: ", obj.normV, "obj.type",obj.type , "ScalarX:" , sk, "cube1.minx",cube1.minx,"retcode:", retcode,"z",z,"zreal",zreal)
     ##print ("vert:",vert, "rotate y:" ,  cam.rot_grad[0])
     all2D.append( C2D( poly, obj.color,retcode ) )
     allvert.append(vert)
     #print("obj.verts", obj.verts)
     #print ("cam.pos:", cam.pos,"cam.normV:" , cam.normV)	 
   #s_l=sorted(range(0,len(allvert)), key=lambda x :  distMidd(allvert[x][0], allvert[x][1] , allvert[x][2],cam.pos),reverse=True)
    s_l=sorted(range(0,len(allvert)), key=lambda x :  distMidd(allvert[x][0], allvert[x][1] , allvert[x][2],cam.pos),reverse=True)
   
    for i in s_l:
     ##print (all2D[i].pos)	 
     try: 
       	if all2D[i].notvisible == 0 :
           pygame.draw.polygon(screen,all2D[i].color,all2D[i].pos)
           
     except: pass
       
   pygame.display.flip()
  
   key = pygame.key.get_pressed()
   cam.update(dt,key)
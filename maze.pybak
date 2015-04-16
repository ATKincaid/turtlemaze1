#maze program written by ANDREW KINCAID
setMediaPath('C:\\Users\\Andrew Kincaid\\Documents\\GitHub\\turtlemaze1')
class Maze(object):
  """ solves a maze in JES """
  def __init__(self):
    """initialization"""
    self.image = makePicture('maze.jpg')
    self.w=makeWorld(getWidth(self.image),getHeight(self.image))
    self.w.setPicture(self.image)
    self.t=makeTurtle(self.w)
    penUp(self.t)
    moveTo(self.t,30,190)
    
    
  def colorInFront(self): 
    
    if self.t.getHeading()==0:
      color=getColor(getPixelAt(self.image,getXPos(self.t),getYPos(self.t)-11))
    if self.t.getHeading()==90 or self.t.getHeading()==-270:
      color=getColor(getPixelAt(self.image,getXPos(self.t)+11,getYPos(self.t)))
    if self.t.getHeading()==180 or self.t.getHeading()==-180:
      color=getColor(getPixelAt(self.image,getXPos(self.t),getYPos(self.t)+11))
    if self.t.getHeading()==270 or self.t.getHeading()==-90:
      color=getColor(getPixelAt(self.image,getXPos(self.t)-11,getYPos(self.t)))
    if distance(color,white)<150:
      color=white
    if distance(color,blue)<160:
      color=blue
    if distance(color,green)<150:
      color=green
    if distance(color,red)<150:
      color=red
    if distance(color,yellow)<150:
      color=yellow
    return color
    
  def surroundings(self):
    if self.t.getHeading()==0:
      colorFront=getColor(getPixel(self.image,getXPos(self.t),getYPos(self.t)-11))
      colorRight=getColor(getPixel(self.image,getXPos(self.t)+11,getYPos(self.t)))
      colorLeft=getColor(getPixel(self.image,getXPos(self.t)-11,getYPos(self.t)))
      colorBack=getColor(getPixel(self.image,getXPos(self.t),getYPos(self.t)+11))
      if distance(colorFront,blue)<150:
        colorFront=blue
      if distance(colorRight,blue)<150:
        colorRight=blue
      if distance(colorLeft,blue)<150:
        colorLeft=blue
      if distance(colorBack,blue)<150:
        colorBack=blue
        
      if distance(colorFront,white)<150:
        colorFront=white
      if distance(colorRight,white)<150:
        colorRight=white
      if distance(colorLeft,white)<150:
        colorLeft=white
      if distance(colorBack,white)<150:
        colorBack=white
        
      if distance(colorFront,red)<150:
        colorFront=red
      if distance(colorRight,red)<150:
        colorRight=red
      if distance(colorLeft,red)<150:
        colorLeft=red
      if distance(colorBack,red)<150:
        colorBack=red
        
      if distance(colorFront,yellow)<150:
        colorFront=yellow
      if distance(colorRight,yellow)<150:
        colorRight=yellow
      if distance(colorLeft,yellow)<150:
        colorLeft=yellow
      if distance(colorBack,yellow)<150:
        colorBack=yellow
    if self.t.getHeading()==90 or self.t.getHeading()==-270:
      colorFront=getColor(getPixel(self.image,getXPos(self.t)+11,getYPos(self.t)))
      colorRight=getColor(getPixel(self.image,getXPos(self.t),getYPos(self.t)+11))
      colorLeft=getColor(getPixel(self.image,getXPos(self.t),getYPos(self.t)-11))
      colorBack=getColor(getPixel(self.image,getXPos(self.t)-11,getYPos(self.t)))
      if distance(colorFront,blue)<150:
        colorFront=blue
      if distance(colorRight,blue)<150:
        colorRight=blue
      if distance(colorLeft,blue)<150:
        colorLeft=blue
      if distance(colorBack,blue)<150:
        colorBack=blue
        
      if distance(colorFront,white)<150:
        colorFront=white
      if distance(colorRight,white)<150:
        colorRight=white
      if distance(colorLeft,white)<150:
        colorLeft=white
      if distance(colorBack,white)<150:
        colorBack=white
        
      if distance(colorFront,red)<150:
        colorFront=red
      if distance(colorRight,red)<150:
        colorRight=red
      if distance(colorLeft,red)<150:
        colorLeft=red
      if distance(colorBack,red)<150:
        colorBack=red
        
      if distance(colorFront,yellow)<150:
        colorFront=yellow
      if distance(colorRight,yellow)<150:
        colorRight=yellow
      if distance(colorLeft,yellow)<150:
        colorLeft=yellow
      if distance(colorBack,yellow)<150:
        colorBack=yellow
    if self.t.getHeading()==180 or self.t.getHeading()==-180:
      colorFront=getColor(getPixel(self.image,getXPos(self.t),getYPos(self.t)+11))
      colorRight=getColor(getPixel(self.image,getXPos(self.t)-11,getYPos(self.t)))
      colorLeft=getColor(getPixel(self.image,getXPos(self.t)+11,getYPos(self.t)))
      colorBack=getColor(getPixel(self.image,getXPos(self.t),getYPos(self.t)-11))
      if distance(colorFront,blue)<150:
        colorFront=blue
      if distance(colorRight,blue)<150:
        colorRight=blue
      if distance(colorLeft,blue)<150:
        colorLeft=blue
      if distance(colorBack,blue)<150:
        colorBack=blue
        
      if distance(colorFront,white)<150:
        colorFront=white
      if distance(colorRight,white)<150:
        colorRight=white
      if distance(colorLeft,white)<150:
        colorLeft=white
      if distance(colorBack,white)<150:
        colorBack=white
        
      if distance(colorFront,red)<150:
        colorFront=red
      if distance(colorRight,red)<150:
        colorRight=red
      if distance(colorLeft,red)<150:
        colorLeft=red
      if distance(colorBack,red)<150:
        colorBack=red
        
      if distance(colorFront,yellow)<150:
        colorFront=yellow
      if distance(colorRight,yellow)<150:
        colorRight=yellow
      if distance(colorLeft,yellow)<150:
        colorLeft=yellow
      if distance(colorBack,yellow)<150:
        colorBack=yellow
    if self.t.getHeading()==270 or self.t.getHeading()==-90:
      colorFront=getColor(getPixel(self.image,getXPos(self.t)-11,getYPos(self.t)))
      colorRight=getColor(getPixel(self.image,getXPos(self.t),getYPos(self.t)-11))
      colorLeft=getColor(getPixel(self.image,getXPos(self.t),getYPos(self.t)+11))
      colorBack=getColor(getPixel(self.image,getXPos(self.t)+11,getYPos(self.t)))
      if distance(colorFront,blue)<150:
        colorFront=blue
      if distance(colorRight,blue)<150:
        colorRight=blue
      if distance(colorLeft,blue)<150:
        colorLeft=blue
      if distance(colorBack,blue)<150:
        colorBack=blue
        
      if distance(colorFront,white)<150:
        colorFront=white
      if distance(colorRight,white)<150:
        colorRight=white
      if distance(colorLeft,white)<150:
        colorLeft=white
      if distance(colorBack,white)<150:
        colorBack=white
        
      if distance(colorFront,red)<150:
        colorFront=red
      if distance(colorRight,red)<150:
        colorRight=red
      if distance(colorLeft,red)<150:
        colorLeft=red
      if distance(colorBack,red)<150:
        colorBack=red
        
      if distance(colorFront,yellow)<150:
        colorFront=yellow
      if distance(colorRight,yellow)<150:
        colorRight=yellow
      if distance(colorLeft,yellow)<150:
        colorLeft=yellow
      if distance(colorBack,yellow)<150:
        colorBack=yellow
    array=[colorFront,colorRight,colorLeft,colorBack]
    return array
    
  def forwardd(self,dist):
    """draws green path"""
    for i in range(dist):
      addOvalFilled(self.image,self.t.getXPos()-9,self.t.getYPos()-9,18,18,green)
      self.t.forward(1)
  
    
  def travel2BranchOrWall(self):
    """move straight"""
    if self.surroundings().count(white)>1:
      while self.surroundings().count(white)>1:
        self.forwardd(1)
    
    if self.colorInFront()==white:
      while self.colorInFront()==white and self.surroundings().count(white)==1:
        self.forwardd(10)
  
  def solve(self):
    """solve"""
    if self.colorInFront()==yellow:
      return true
    
      
    
  
  
    
   
          
  def reset(self):
    """reset"""
    self.image=makePicture('maze.jpg')
    self.w.setPicture(self.image)
    self.t.clearPath()
    penUp(self.t)
    moveTo(self.t,30,190)
    self.t.setHeading(90)
    penDown(self.t)
    
    
     
      
      
    
    
#tests follow here
doTests=true
if doTests:
  #Test 1, verify we have a maze
  m=Maze()
  if m.__class__==Maze:
    printNow("Test 1 passed, Maze exists.")
  else:
    printNow("Test 1 failed, Maze does not exists.")
  #Test 2
  if m.image.__class__== Picture:
    printNow("Test 2 passed, image exists.")
  else:
    printNow("Test 2 failed, image does not exist.")
  #Test 3
  try:
    if m.w.__class__==World:
      printNow("Test 3 passed, world exists.")
  except:
    printNow("Test 3 failed, world does not exist.")
  #Test 4
  try:
    if m.w.getPicture().fileName[-8:]=="maze.jpg":
      printNow("Test 4 passed, world picture is maze.jpg.")
    else:
      printNow("Test 4 failed, world picture is " + m.w.getPicture().fileName)
  except:
    printNow("Test 4 failed, world does not have a picture.")
  #Test 5, testing for existence of a turtle
  try:
    if m.t.__class__==Turtle:
      printNow("Test 5 passed, turtle is in maze.")
  except:
     printNow("Test 5 failed, no turtle")
  #Test 6, test for turtle in right location
  if getXPos(m.t)==30 and getYPos(m.t)==190:
    printNow("Test 5 passed, turtle in correct start location.")
  else:
    printNow("Test 5 failed, turtle in wrong start location.")
  #Test 7, check for colorInFront
  if dir(m).index('colorInFront')>0:
    printNow("Test 7 passed, colorInFront exists.")
  else:
    printNow("Test 7 failed, colorInFront does not exists.")
  #Test 8, check what color in front returns
  if m.colorInFront()==white:
    printNow("Test 8 passed, colorInFront returns white.")
  else:
    printNow("Test 8 failed, colorInFront does not return white.")
  #Test 9, check that colorinfront is blue
  if m.colorInFront()==blue:
    printNow("Test 9 passed, colorInFront returns blue.")
  else:
    printNow("Test 9 failed, colorInFront does not return blue.")
  #test 10, check for travel2BranchOrWall
  if dir(m).index('travel2BranchOrWall')>0:
    printNow("Test 10 passed, travel2BranchOrWall exists.")
  else:
    printNow("Test 10 failed, travel2BranchOrWall does not exists.")
  #test 11, test for reset
  if dir(m).index('reset')>0:
    printNow("Test 11 passed, reset exists.")
  else:
    printNow("Test 11 failed, reset does not exists.")
  #Test 12, makes sure maze is in OG condition
  m.reset()
  assert m.t.getXPos()==30, "Test 12 failed, x position is " + str(m.t.getXPos())
  assert m.t.getYPos()==190, "Test 12 failed, y position is " + str(m.t.getYPos())
  assert m.t.getHeading()==90, "Test 12 failed, heading is " + str(m.t.getHeading())
  printNow("Test 12 passed, maze is in original condition")
  #Test 13, check if we move down first path
  m.reset()
  m.travel2BranchOrWall()
  if getXPos(m.t)==108 and getYPos(m.t)==190:
    printNow("Test 13 passed, turtle moved to end of first path")
  else:
    printNow("Test 13 failed, turtle did not move to end of first path")
  #Test 14, check if we stop at branch
  m.reset()
  m.t.setHeading(0)
  m.travel2BranchOrWall()
  if getXPos(m.t)==30 and getYPos(m.t)==106:
    printNow("Test 14 passed, turtle stopped at first crossroads")
  else:
    printNow("Test 14 failed, turtle did not stop at first crossroads. Stopped at "+str(getXPos(m.t))+" , "+str(getXPos(m.t)))
  #Test 15, check for green trail
  m.reset()
  m.forwardd(50)
  m.t.turn(180)
  if m.colorInFront()==green:
    printNow("Test 15 passed, turtle is leaving green trail")
  else:
    printNow("Test 15 failed, color behind turtle is the " + str(m.colorInFront()))
  #Test 16, check value of surroundings
  m.reset()
  if m.surroundings()==[white,blue,white,blue]:
    printNow("Test 16 passed, surroundings array correct")
  else:
    printNow("Test 16 failed, surroundings array incorrect. It is " + str(m.surroundings()))
  #Test 16a, 
  m.reset()
  m.t.setHeading(0)
  
  m.travel2BranchOrWall()
  if m.t.getXPos()==30 and m.t.getYPos()==110:
    printNow("Test 16a passed, turtle stopped at first crossroads")
  else:
    printNow("Test 16a failed, turtle did not stop at first crossroads. Stopped at "+str(m.t.getXPos())+","+str(m.t.getXPos()))
  #Test 17, solve() passes at cheese
  m.reset()
  m.t.penUp()
  m.t.moveTo(390,149)
  m.t.turnToFace(390,160)
  m.solve()
  if m.solve():
    printNow("Test 17 passed, solve() true at cheese")
  else:
    printNow("Test 17 failed, solve() false at cheese")
  #Test 18, return false in impossible location
  m.reset()
  m.t.penUp()
  m.t.moveTo(150,230)
  m.t.turnToFace(150,200)
  m.t.penDown()
  m.solve()
  if m.solve()==false:
    printNow("Test 18 passed, solve() false in impossible locations")
  if m.solve():
    printNow("Test 18 failed, solve() true in impossible locations")
  else:
    printNow("Test 18 failed.")
  
  
  
  
  
  
  
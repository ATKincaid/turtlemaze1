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
    moveTo(self.t,26,185)
    
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
  def travel2BranchOrWall(self):
    """move straight"""
    while self.colorInFront()==white:
      forward(self.t,1)
      
  def reset(self):
    """reset"""
    self.image=makePicture('maze.jpg')
    self.w.setPicture(self.image)
    self.t.clearPath()
    penUp(self.t)
    moveTo(self.t,26,185)
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
  if getXPos(m.t)==26 and getYPos(m.t)==185:
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
  assert m.t.getXPos()==26, "Test 12 failed, x position is " + str(m.t.getXPos())
  assert m.t.getYPos()==185, "Test 12 failed, y position is " + str(m.t.getYPos())
  assert m.t.getHeading()==90, "Test 12 failed, heading is " + str(m.t.getHeading())
  printNow("Test 12 passed, maze is in original condition")
  #Test 13, check if we move down first path
  m.reset()
  m.travel2BranchOrWall()
  if getXPos(m.t)==26 and getYPos(m.t)==185:
    printNow("Test 13 passed, turtle moved to end of first path")
  else:
    printNow("Test 13 failed, turtle did not move to end of first path")
  #Test 14, check if we stop at branch
  #Test 13, check if we move down first path
  m.reset()
  m.t.setHeading(0)
  m.travel2BranchOrWall()
  if getXPos(m.t)==26 and getYPos(m.t)==106:
    printNow("Test 14 passed, turtle stopped at first crossroads")
  else:
    printNow("Test 14 failed, turtle did not stop at first crossroads")
    
  
  
  
  
  
  
  
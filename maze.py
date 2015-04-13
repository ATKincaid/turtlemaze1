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
    turnLeft(self.t)
    forward(self.t,6)
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
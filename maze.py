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
  def colorInFront(self.t):
    """tests to see color in front of turtle"""
      
      
    
    
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
  if colorInFront()=colorInFront():
    printNow("Test 7 passed, colorInFront exists.")
  else:
    printNow("Test 7 failed, colorInFront does not exists.")
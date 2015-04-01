#maze program written by ANDREW KINCAID

class Maze(object):
  """ solves a maze in JES """
  

#tests follow here
doTests=true
if doTests:
  #Test 1, verify we have a maze
  m=Maze()
  if m.__class__==Maze:
    printNow("Test 1 passed, Maze exists.")
  else:
    printNow("Test 1 failed, Maze does not exists.")
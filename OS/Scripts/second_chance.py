#stian var her
class Clock:
  def __init__(self, size) -> None:
      self.pointerPos = 0
      self.clockSize = size
      self.frames = [[0, 0] for _ in range(size)]
      
      self.accessSequence = []
      self.framesHistory = [[] for _ in range(size)]
      self.pointerPosHistory = []
      
  def inc(self):
    self.pointerPos = (self.pointerPos + 1) % self.clockSize
    

  def set(self, page):
    found = False
    for i in range(self.clockSize):
      if self.frames[i][0] == page:
        self.frames[i][1] = 1
        found = True
        break
      
    while not found:
        if self.frames[self.pointerPos][1] == 1:
          self.frames[self.pointerPos][1] = 0
          self.inc()
          continue
        
        self.frames[self.pointerPos] = [page, 1]
        self.inc()
        break
    
    self.accessSequence.append(page)
    self.updateFrameHistory()
    self.pointerPosHistory.append(self.pointerPos)
    
  def updateFrameHistory(self):
    for i in range(self.clockSize):
      self.framesHistory[i].append(self.frames[i][:])

  def pretty_print(self):
    print()
    # print accessSequence
    print("Sequence:", end="\n\t| ")
    for page in self.accessSequence:
      print(page, end=" | ")
    print()

    print("Frames  :" + "-"*4*len(self.accessSequence))
    for frame in range(self.clockSize):

      print("Frame"+str(frame), end="\t| ")
      for i in range(len(self.framesHistory[frame])):
        print(self.framesHistory[frame][i][0], end=" | ")
      print()

    print("Ref bits:" + "-"*4*len(self.accessSequence))
    for frame in range(self.clockSize):

      print("Frame"+str(frame), end="\t| ")
      for i in range(len(self.framesHistory[frame])):
        print(self.framesHistory[frame][i][1], end=" | ")
      print()

    print("P-pos:"+ "-"*4*len(self.accessSequence), end="\n\t| ")
    for pos in self.pointerPosHistory:
      print(pos+1, end=" | ")
    print()
  

  
def main():
  # get accessSequence from user
  userInput = input("Enter the page requests (comma or space separated): ")
  userInput = userInput.replace(",", " ")
  accessSequence = [int(x) for x in userInput.split()]
  
  # get clockSize from user
  clockSize = int(input("Enter the page capacity: "))

  # create clock
  clock = Clock(clockSize)

  # simulate clock
  for page in accessSequence:
    clock.set(page)

  # print clock
  clock.pretty_print()

main()
input("Press enter to quit...")
#######################Arithmetic Logic Unit##########################
class ALU:
  def __init__(self, srcA, srcB,aluopcode):

    self.srcA = srcA
    self.srcB = srcB
    self.aluopcode = aluopcode
    self.map = {2 : self.add, 3 : self.sub, 0 : self.and_, 1 : self.or_, 4 : self.slt}

  def update(self):
    self.map[self.aluopcode]()

  def add(self):
    return self.srcB + self.srcA

  def sub(self):
    return self.srcA - self.srcB

  def and_(self):
    return self.srcA & self.srcB

  def or_(self):
    return self.srcA | self.srcB

  def slt(self):
    if self.srcA < self.srcB:
      return 1
    else:
      return 0
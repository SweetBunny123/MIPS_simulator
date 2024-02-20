###############Program Counter##########################
class ProgramCounter:
  def __init__(self):
      self.pc = 0
      print('PC Initialized to 0')

  def increment(self):
      self.pc += 4
      print('PC after increment: ', self.pc)

  def get_pc(self):
      print('PC is: ', self.pc)
      return self.pc
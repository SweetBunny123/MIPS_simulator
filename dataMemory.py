#######################Data Memory##########################
class DataMemory:
  def __init__(self, size):
      self.memory = [0] * size

  def read_memory(self, address):
      return self.memory[address]

  def write_memory(self, address, value):
      self.memory[address] = value
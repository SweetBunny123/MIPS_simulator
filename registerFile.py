###############Register File##########################
class RegisterFile:
  def __init__(self):
      self.registers = [0] * 32
      print('Initialized Register File (all zeroes)')

  def read_register(self, register_number):
      return self.registers[register_number]

  def write_register(self, register_number, value):
      if register_number != 0:  # Register $zero is hardwired to 0
          self.registers[register_number] = value
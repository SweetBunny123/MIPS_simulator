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

###############Instruction Memory##########################
class InstructionMemory:
  def __init__(self, instructions):
      print('Loaded Instructions into Instruction Memory')
      self.instructions = instructions

  def get_instruction(self, address):
      pass
      #return self.instructions[address]

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
        
#######################Data Memory##########################
class DataMemory:
  def __init__(self, size):
      self.memory = [0] * size

  def read_memory(self, address):
      return self.memory[address]

  def write_memory(self, address, value):
      self.memory[address] = value
    
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
      
#############################Processor#############################
class MIPSProcessor:
  def __init__(self, program):
      self.pc = ProgramCounter()
      self.instruction_memory = InstructionMemory(program)
      self.register_file = RegisterFile()
      self.data_memory = DataMemory(8192)  # Example size

  def fetch_instruction(self):
      instruction = self.instruction_memory.get_instruction(self.pc.get_pc())
      self.pc.increment()
      return instruction

  def decode_and_execute(self, instruction):
      opcode = (instruction & 0xFC000000) >> 26
      rs = (instruction & 0x03E00000) >> 21
      rt = (instruction & 0x001F0000) >> 16
      imm = instruction & 0x0000FFFF

      if opcode == 35:  # Load Word (lw)
          data = self.data_memory.read_memory(self.register_file.read_register(rs) + imm)
          self.register_file.write_register(rt, data)
      elif opcode == 43:  # Store Word (sw)
          self.data_memory.write_memory(self.register_file.read_register(rs) + imm, self.register_file.read_register(rt))
      # Implement other instructions as needed

  def run(self):
      while True:
          instruction = self.fetch_instruction()
          if instruction == 0:  # Assume end of program
              break
          self.decode_and_execute(instruction)

# Example Usage
if __name__ == "__processor__":
  # Example MIPS program
  program = [
      0x8C090000,  # lw $t1, 0($a0)
      0xAC220000,  # sw $v0, 0($s2)
      0x00000000   # End of program
  ]

  # Create and run the MIPS processor
  mips_processor = MIPSProcessor(program)
  mips_processor.run()

  # Display contents of the register file and data memory after execution
  print("Register File:")
  for i in range(32):
      print(f"$t{i}: {mips_processor.register_file.read_register(i)}")

  print("\nData Memory:")
  for i, value in enumerate(mips_processor.data_memory.memory):
      if value != 0:
          print(f"Memory[{i}]: {value}")

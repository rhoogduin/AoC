
"""simple CPU to execute game console boot code"""
class CPU :
    def __init__ (self, program):
        self.PC = 0
        self.acc = 0
        
        self.program = program.copy()
        
        self.prog_len = len(self.program)
        
        """list to check double execution of instructions"""
        self.instruction_executed = [0] * self.prog_len
        
    def clockPulse (self) :
        instruction = self.program[self.PC]
        
        """check if already executed"""
        if self.instruction_executed[self.PC] > 0 :
            print (f" acc = {self.acc}")
            self.PC = self.prog_len
            return
        else :
            self.instruction_executed[self.PC] += 1
        
        op = instruction[0]
        arg = instruction[1]
        
        if op != "jmp" :
            self.PC += 1
        
        self.ALU(op, arg)
    
    def ALU (self, op, arg) :
        
        if op == "acc" :
            self.acc += arg
        
        elif op == "jmp" :
            self.PC += arg
            
    def run (self) :
        while self.PC < self.prog_len :
            self.clockPulse()

"""read input"""
file = open("input.txt", "r")

lines = []

lines = file.read().splitlines()
    
file.close()

"""list that will contain the instructions"""
program = []

"""turn each line into an instruction and add to program"""
for line in lines :
    line = line.split()
    
    operation = line[0]
    argument = int(line[1])
    
    instruction = (operation, argument)
    
    program.append(instruction)

cpu = CPU(program)

cpu.run()
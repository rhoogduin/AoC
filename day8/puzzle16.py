
#simple CPU to execute game console boot code
class CPU :
    def __init__ (self, program):
        self.PC = 0
        self.acc = 0
        
        self.program = program.copy()
        
        self.prog_len = len(self.program)
        
    def clockPulse (self) :
        instruction = self.program[self.PC]
        
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
        while self.PC < self.prog_len:
            self.clockPulse()
        
    def test (self, budget) :
        while self.PC < self.prog_len and budget > 0:
            self.clockPulse()
            budget -= 1
        
        if budget == 0 :
            return False
        return True

#read input
file = open("input.txt", "r")

lines = []

lines = file.read().splitlines()
    
file.close()

#list that will contain the instructions
program = []

#turn each line into an instruction and add to program
for line in lines :
    line = line.split()
    
    operation = line[0]
    argument = int(line[1])
    
    instruction = (operation, argument)
    
    program.append(instruction)

#try to find broken instruction
for i in range( len(program) ) :
    original = program[i]
    
    #if nop, replace with jump and try executing
    if program[i][0] == "nop" :
        program[i] = ("jmp", program[i][1])
        
        #try altered program
        cpu = CPU(program)
        if cpu.test(1000) :
            print (f"Found faulty nop at {i}: {original}.")
            instr_pos = i
            instr = ("jmp", program[i][1])
            break 
    
    #if jump, replace with nop and try executing
    elif program[i][0] == "jmp" :
        program[i] = ("nop", program[i][1])
        
        #try altered program
        cpu = CPU(program)
        if cpu.test(1000) :
            print (f"Found faulty jmp at {i}: {original}.")
            instr_pos = i
            instr = ("nop", program[i][1])
            break
            
    program[i] = original
    
print ("Fixing program!")

program[instr_pos] = instr

cpu = CPU(program)

cpu.run()

print (f"Accumulator value after execution of fixed program: {cpu.acc}.")
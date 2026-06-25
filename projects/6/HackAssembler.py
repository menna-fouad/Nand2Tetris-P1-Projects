import sys
from Parser import initial_parsing, parse_a_ins, parse_c_ins
from Coder import code_a_instruction, code_c_instruction

# File I/O
in_name = sys.argv[1] # Input file name
out_name = in_name.replace("asm", "hack") # Output file name (replace 'asm' with 'hack')

in_file = open(in_name, 'r') # Open input file in read mode
out_file = open(out_name, 'w') # Open output file in write mode to overwrite already existing files with the same name

# Intiialize the symbol_table with predefined symbols
symbol_table = {
    "R0" : 0,
    "R1" : 1,
    "R2" : 2,
    "R3" : 3,
    "R4" : 4,
    "R5" : 5,
    "R6" : 6,
    "R7" : 7,
    "R8" : 8,
    "R9" : 9,
    "R10" : 10,
    "R11" : 11,
    "R12" : 12,
    "R13" : 13,
    "R14" : 14,
    "R15" : 15,
    "SCREEN" : 16384,
    "KBD" : 24576,
    "SP" : 0,
    "LCL" : 1,
    "ARG" : 2,
    "THIS" : 3,
    "THAT" : 4
}
# Set the next free space to store a variable to 16
unique_address = 16

# First pass
instructions = []
for line in in_file:
    # For every line in the file, we pass it through the initial parsing
    curr = initial_parsing(line)
    # If the line is a comment, curr is an empty string therefore we do nothing
    # If curr is not empty, there is an instruction
    if curr:
        # If the first character is a '(', the instruction is a label
        if curr[0] == '(':
            # label is the result of parsing curr to remove the '(' and ')' at the beginning and the end
            label = curr[1 : -1]
            # The label is appended to the symbol_table along with the address of the next instruction
            # This is the length of the instructions array since the address of the instructions already appended ranges from 0 to len(instructions) - 1
            # Therefore, the next instruction is at address len(instructions) - 1 + 1 = len(instructions)
            symbol_table[label] = len(instructions)
        else:
            # curr is not a lable, it is a valid instruction appended to the list of instructions
            instructions.append(curr)

# Second pass
for i, ins in enumerate(instructions):
    if ins[0] == '@':
        # The instruction is an A instruction functions that parse and code the A instruction are called
        value = parse_a_ins(ins)
        translated, symbol_table, unique_address = code_a_instruction(value, symbol_table, unique_address)
    else:
        # The instruction is a C instruction functions that parse and code the C instruction are called
        dest, comp, jump = parse_c_ins(ins)
        translated = code_c_instruction(dest, comp, jump)
    
    # The translated instruction is written to the output (.hack) file
    if i < len(instructions) - 1:
        translated += '\n'
    out_file.write(translated)

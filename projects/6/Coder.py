# Map of comp field to its binary value
comp_bits = {
    '0':   '101010',
    '1':   '111111',
    '-1':  '111010',
    'D':   '001100',
    'A':   '110000', 'M':   '110000',
    '!D':  '001101',
    '!A':  '110001', '!M':  '110001',
    '-D':  '001111',
    '-A':  '110011', '-M':  '110011',
    'D+1': '011111',
    'A+1': '110111', 'M+1': '110111',
    'D-1': '001110',
    'A-1': '110010', 'M-1': '110010',
    'D+A': '000010', 'D+M': '000010',
    'D-A': '010011', 'D-M': '010011',
    'A-D': '000111', 'M-D': '000111',
    'D&A': '000000', 'D&M': '000000',
    'D|A': '010101', 'D|M': '010101',
}

# Map of jump field to its binary value
jump_bits = {
    None : '000',
    'JGT' : '001',
    'JEQ' : '010',
    'JGE' : '011',
    'JLT' : '100',
    'JNE' : '101',
    'JLE' : '110',
    'JMP' : '111'
}

def code_a_instruction(value, symbol_table, unique_address):
    '''
    Parses a instruction
    '''
    if not value.isdigit():
        # If the value is not a digit, it is a symbol or label that must be stored in the symbol table
        if value not in symbol_table:
            # If the value is not in the symbol table, 
                # It is not a label, since they were appended to the symbol table during the first pass
                # It is a variable not seen before, and is assigned the next free space in the memory
            symbol_table[value] = unique_address
            unique_address += 1 # The unique address is incremented to point to the next free space
        
        # The value is now assigned to its corresponding number in the symbol table
        # This number is guaranteed to be defined
        value = symbol_table[value]
        
    binary = bin(int(value))[2 : ] # The value is converted to its binary value and parsed to remove the leading '0b'
    # The A instruction is now formed with the following fields
        # An initial 0 to indicate that it is an A instruction
        # The binary value of the address specified
        # 0s in the middle to pad the instruction to 15 bits
    machine_language = '0' + '0' * (14 - len(binary)) + binary

    # The updated symbol_table and unique_address must be returned to the main program that manages them
    return machine_language, symbol_table, unique_address

def code_c_instruction(dest, comp, jump):
    '''
    Parses a instruction
    '''

    # The C instruction starts with a 1 to indicate that it is a C instruction 
    # The next 2 unused bits are set to 1
    machine_language = '111'

    # If one of the operands is 'M' the a bit is set to 1, otherwise it is set to 0
    machine_language += '1' if 'M' in comp else '0'
    
    # The comp bits come next, which are found in the comp_bits look up table
    machine_language += comp_bits[comp]

    # The dest bits come next
    if dest:
        # Each dest bit is independent of the other 
        # They are set to 0 or 1 depending on the prescence of the destination register they represent in the dest field
        machine_language += '1' if 'A' in dest else '0'
        machine_language += '1' if 'D' in dest else '0'
        machine_language += '1' if 'M' in dest else '0'
    else:
        # They are set to 0 if the destination is None
        machine_language += '000'
    
    # The jump bits come next, which are found in the comp_bits look up table
    machine_language += jump_bits[jump]

    return machine_language # The final machine language instruction is returned

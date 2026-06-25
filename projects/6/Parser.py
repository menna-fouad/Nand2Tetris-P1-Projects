def initial_parsing(ins):
    '''
    Removes white spaces and comments
    '''
    ins = ins.strip() # Removes leading and trailing white spaces
    ins = ins.replace(" ", "") # Replaces spaces with an empty string 
    # This is done so as to not include them in the parsed fields when parsing the instruction

    if '//' in ins:
        # If a comment is present, it is after an instruction
        # If the comment makes up the entire line, then the instruction becomes an empty string
        # If a comment is present, we find its index and remove it from the instruction
        index = ins.index('/')
        ins = ins[ : index]
    
    return ins

def parse_c_ins(ins):
    '''
    Parses a C instruction and outputs the 
    '''
    dest, jump = None, None # The dest and jump fields are optional so we intiialize them to None
    if '=' in ins:
        # If there is an '=' sign, there is a dest field specified at the beginning
        # We split the instruction at the '=' to the dest field, and the rest of the instruction
        dest, ins = ins.split('=')
        # If the dest field is specified but it is set to 'null' the dest field is set to None
        # This is done to treat both the explicit and implicit specification of not storing the final result the same
        dest = None if dest == 'null' else dest
    if ';' in ins:
        # If there is a ';', there is a jump field specified at the end
        # The instruction is split into the comp and jump fields
        comp, jump = ins.split(';')
        jump = None if jump == 'null' else jump
    else:
        # If no jump is specified, then the comp field makes up the intire instruction
        comp = ins
    
    return dest, comp, jump

def parse_a_ins(ins):
    # The '@' symbol is truncated
    # The value (or label/symbol in the case of a word) is returned
    return ins[1 : ]

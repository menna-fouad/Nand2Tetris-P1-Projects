# Project 6 Notes

The Assembler translates the Hack assembly language into machine language in the following steps:

1. The `HackAssembler.py` program first reads the input file name from the command-line and prepares the input `.asm` file and output `.hack` file.
2. It then reads the assembly file line by line to do the following:
    1. Remove comments and white spaces.
    2. Add labels to the symbol table.
3. During the second pass, it identifies the instruction type and calls the appropriate parser and coder function.

### First pass

During the first pass, each line goes through an initial parse to remove white spaces and comments. This is done so that we can cleanly parse the instruction in the second pass without any special handling.

If the line is purely a comment, the initial parsing returns an empty string, which is not added to the list of instructions that go through the second pass. If the line is a label (it starts with a `(`), the label and the instruction that follows it are added to the symbol table. The label is also not added to the list of instructions processed during the second pass.

If the line is an instruction, the initial parsing removed any spaces at the start, middle, and end of the instruction along with any comment that follows the instruction. It is then added to the list of instructions.

### Second Pass

If the first character is an `@`, the instruction is an A type instruction, otherwise, it is a C type instruction.

**Parsing**

The `HackAssembler.py` program calls the appropriate parser function defined in `Parser.py` to break down the instruction to its underlying fields.

* In the case of an A instruction, the `@` is simply removed and the remaining value is returned. This value can be a number, label, or variable.
* In the case of a C instruction, the instruction is split into the `dest`, `comp`, and `jump` fields.
    * The `dest` and `jump` fields are initially assigned to `None` since they are optional
    * If there is an `=` sign, there is a `dest` field specified and we split the instruction at the `=` sign to the `dest` field and the rest of the instruction. The `dest` field is assigned to None if it was explicitly defined as `null` to treat it the same as if no `dest` field was specified.
    * If there is a `;` sign, there is a `jump` field specified. The instruction is split at the `;` to the `comp` and `jump` field. If there was no `jump` field specified, then the `comp` field makes up the instruction.

**Translating**

At this stage, the instruction has been parsed into its underlying fields, which are each translated then merged to form the final instruction.

* In the case of an A instruction:
    * If the value is non-numeric, it is either a variable or a label whose value is obtained by consulting the symbol table. If the value is not in the symbol table, it is a variable not seen before, so it is assigned to the next free address in memory and appended to the symbol table. We now assign the value its numeric value.
    * Regardless of whether the value is a variable, label, or number, we are now dealing with its numeric value, which is encoded into its binary value and the instruction is formed by adding a `0` at the beginning, then adding `0`s as padding to fill the instruction, then the binary value is added. The number of `0`s added as padding depends on the number of bits used to encode the binary value.
* In the case of a C instruction:
    * We first deal with the `a` bit, which is set to `1` if the `M` register is one of the operands, otherwise it is set to `0`.
    * Next, the `comp` field is translated into binary by using the `comp_bits` lookup table.
    * The `dest` field come next. Each `dest` bit is independent of the other and they are set to 0 or 1 depending on the prescence of the destination register they represent in the `dest` field. The 1st `dest` bit represents the `A` register, the 2nd `dest` bit represents the `D` register, and the 3rd `dest` bit represents the `M` register.
    * Finally, the `jump` field is translated into binary by using the `jump_bits` lookup table.

The parsing and translation are done on every instruction after the initial parsing and stored in the output Hack binary file.

# Nand2Tetris Part 1 Solutions

This repo contains my solutions to the projects of the first part of the [Nand2Tetris](https://www.nand2tetris.org/) course, which covers the hardware principles of building a modern computer. I will begin with logic gates, then work my way towards building a working ALU, memory, a CPU, and assembler.

## Projects

The projects folder goes from `projects/1` through `projects/6`, each with their own `Notes.md` file discussing concepts and tips. The code in each project has been tested using the test and compare files the course provided, which I have not shared in my repo due to copyright.

---
### Project 1 - Boolean Logic

Through project 1, I implemented elementary logic gates, their 16 bit variants, and their multi-way variants.

| Elementary | 16-bit variants | Multi-way variants |
| --- | --- | --- |
| Not | Not16 | Or8Way |
| And | And16 | Mux4Way16 |
| Or | Or16 | Mux8Way16 |
| Xor | Mux16 | DMux4Way |
| Mux |  | DMux8Way |
| DMux |  |  |

---
### Project 2 - Boolean Arithmetic and ALU

Through project 2, I implemented arithmetic chips, and built a fully functional ALU.

| Chip | Description |
| --- | --- |
| HalfAdder | Adds two bits, outputs sum and carry |
| FullAdder | Adds three bits (two inputs + carry-in), outputs sum and carry |
| Add16 | Adds two 16-bit numbers by chaining one half adder and fifteen full adders |
| Inc16 | Increments a 16-bit number by 1 |
| ALU | Computes one of 18 functions on two 16-bit inputs based on 6 control bits |

The ALU is built ontop of these chips. It takes two 16-bit inputs `x` and `y` and six control bits and pre-processes the inputs, selects between addition and bitwise AND, and post-processes the output. It also outputs two status bits: `ng` indicating whether or not the output is negative, and `zr` which detects whether the output is 0 or not.

---
### Project 3 - Memory

In project 3, I started to implement sequential logic, where the output depends on the previous input. I started with a `Bit` that utilizes a DFF (Data Flip Flop) that outputs the input from the previous cycle. The 16-bit register is built on top of this `Bit`. I built the RAM using this register. There are 5 different RAM chips, which differ by the number of registers they contain. I also built a PC (Program Counter) that is built upon chips built in project 2, such as the incrementor.

 Sequential Logic | RAM Chips |
| --- | --- |
| Bit | RAM8 |
| Register | RAM64 |
| PC | RAM512 |
| | RAM4K (4,096 registers) |
| | RAM16K (16,384 registers) |

---
### Project 4 - Machine Language

In project 4, I wrote two programs directly in Hack assembly language to understand the Hack ISA before building the assembler in project 6. The Hack ISA has only two instruction types: A-instructions (@value) for loading constants and selecting memory addresses, and C-instructions (dest=comp;jump) for computation, memory writes, and control flow.

| Program | Description |
| --- | --- |
| Multi.asm | Multiplies R0 and R1 by using repetitive addition and stores result in R2. |
| Fill.asm | Probes the keyboard in an infite loop, filling the screen black if a key is pressed, white otherwise |

---
### Project 5 - HACK Computer

In project 5, I used previously implemented chips, along with built-in chips (primarily for the GUI side effect), to build the `Memory`, `CPU` chip, and integrate everything into the final `Computer`.

| Chip | Description |
| --- | --- |
| `Memory` | This is where the RAM along with the screen and keyboard memory map are implemented. The memory decides which part the address refers to using a `DMux`, and selects the output using a `Mux16` |
| `CPU` | This implements the core processing logic, handling the `A`, `D`, and `M` registers, along with computation using the `ALU`, and the final storage in the required memory locations |
| `Computer` | Connects the built-in `ROM32K`, and the implemented `Memory` and `CPU` chips into a working computer |

---
### Project 6 - Assembler

The final project of part 1 of the course involved building an assembler that bridges between the programs written in HACK assembly language during project 4, and the `Computer` I built in project 5 that only handles binary code.

I wrote a python program to translate the `.asm` files given in the project to `.hack` program that runs on the HACK `Computer`. This is known as cross-assembly where the assembler runs on one computer and produces machine language for another computer.

| Program | Description |
| --- | --- |
| `Parser.py` | Defines the `initial_parser` for the first pass of defining the labels and unpacks the instructions into their underlying fields in the second pass |
| `Code.py` | Translates each field into its corresponding binary value and merges them into the final binary instruction |
| `HackAssembler.py` | The main program that manages the symbol table, file I/O, and drives the process by calling the functions in the mentioned programs in the correct order |

---

This completes Part 1 of the course, starting from a single NAND gate and building up through logic gates, an ALU, memory, a CPU, a working computer that integrates everything, and finally an assembler to program it.

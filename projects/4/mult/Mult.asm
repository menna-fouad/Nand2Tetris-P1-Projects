// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
// The algorithm is based on repetitive addition.

@i
M=0 // i = 0
@res
M=0 // res = 0

// The program will add R1 to the result R0 times, which is the equivalent of R1 x R0

(LOOP)
    @i
    D=M // D = i
    @R0
    D=D-M // D = i - R0
    @DONE
    D;JGE // If i - R0 ≥ 0 (i.e. i ≥ R0), terminate the loop

    @R1
    D=M // D = R1
    @res
    M=D+M // res = res + R1
    @i
    M=M+1 // i++

    @LOOP
    0;JMP // Jump back to the beginning of the loop

(DONE)
@res
D=M // D = res
@R2
M=D // R2 = res (copy the final result to R2)

(END)
@END
0;JMP

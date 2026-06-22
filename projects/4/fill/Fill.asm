// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, 
// the screen should be cleared.

// The screen is 256 x 512 and each word represents 16 pixels
// Therefore, the number of words is 256 x 512 / 16 = 8192
@8192
D=A
@words
M=D

(LOOP)
    // Initialize addr to the base address of the screen
    @SCREEN
    D=A
    @addr
    M=D

    @i
    M=0 // i = 0

    @KBD // A = KBD
    D=M // D = Memory[KBD] (the screen code of the current key pressed, 0 if no key is pressed)

    @BLACK
    D;JNE // if D != 0 (a key is pressed), jump to the loop that fills the screen with black (1)

    (WHITE)
        @i
        D=M // D = i
        @words
        D=D-M // D = i - words
        @LOOP
        0;JGE  // if i - words ≥ 0 (i.e. i ≥ words), the screen is filled with 0s, jump to the next iteration of the main loop

        @addr
        A=M // A = address of current word
        M=0 // word = 0

        @i
        M=M+1 // i++
        @addr
        M=M+1 // addr++

        @WHITE
        0;JMP // Jump back to the beggining of the white loop

    (BLACK)
        @i
        D=M // D = i
        @words
        D=D-M // D = i - words
        @LOOP
        0;JEQ // if i - words ≥ 0 (i.e. i ≥ words), the screen is filled with 0s, jump to the next iteration of the main loop

        @addr
        A=M // A = address of current word
        M=-1 // set all pixels of the word to 1

        @i
        M=M+1 // i++
        @addr
        M=M+1 // addr++

        @BLACK
        0;JMP // Jump back to the beggining of the black loop

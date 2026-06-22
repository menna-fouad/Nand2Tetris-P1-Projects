# Project 4 Notes

## ISA Overview

The Hack ISA has three registers:

* `A` - Stores the address of a place in memory, or a 16-bit value depending on the context
* `M` - The register in memory pointed to by the address in register `A`
* `D` - Stored a 16-bit value

It also has 2 types of instructions

* **A Instruction** (`@value`) - loads the value into the A register, and the value of the register pointed to by that address is stored in M. This instruction is always required before accessing memory.
* **C Instruction** (`dest=comp;jump`) - computes something and stores in it memory and/or jumps to a specific instruction based on a comparison between the value computed and 0. Either dest or jump can be omitted.

## Mult.asm

Multiplies R0 and R1 via repetitive addition (adds R1 to a running total R0 times) and stores the result in R2. Uses a counter `i` that increments each iteration and the loop is terminated when `i ≥ R0` (`i - R0 ≥ 0`).

## Fill.asm

Probes the keyboard register (KBD) in an infinite loop. If a key is pressed (KBD != 0), the loop fills all 8192 screen words with -1 (black). If no key is pressed, the loop fills all 8192 screen words with 0 (white).

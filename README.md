# Nand2Tetris Part 1 Solutions

This repo contains my solutions to the projects of the first part of the [Nand2Tetris](https://www.nand2tetris.org/) course, which covers the hardware principles of building a modern computer. I will begin with logic gates, then work my way towards building a working ALU, memory, a CPU, and assembler.

## Projects

The projects folder goes from `projects/1` through `projects/6`, each with their own `Notes.md` file discussing concepts and tips. The code in each project has been tested using the test and compare files the course provided, which I have not shared in my repo due to copyright.

---
### Project 1

Through project 1, I implemented elementary logic gates, their 16 bit variants, and their multi-way variants.


| Elementary | 16-bit variants | Multi-way variants |
| --- | --- | --- |
| Not | Not16 | Or8Way |
| And | And16 | Mux4Way16 |
| Or | Or16 | Mux8Way16 |
| Xor | Mux16 | DMux4Way |
| Mux |  | DMux8Way |
| DMux |  |  |

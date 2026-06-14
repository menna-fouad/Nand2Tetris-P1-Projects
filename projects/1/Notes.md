# Project 1 Notes

## General Approach
All chips in this project are built from Nand gates (directly or via higher-level chips). 
Nand is also known as a universal gate since any Boolean function can be expressed using only Nand gates.

## Basic Gates (Not, And, Or, Xor, Mux, DMux)

**Not**

$\overline{A} = \overline{A \cdot A} = A \text{ NAND } A$

**And**

Nand followed by Not.

$A \cdot B = \overline{\overline{A \cdot B}}$

We previously established that the negation of an expression is equivalent to that expression NANDed with itself.

$A \cdot B = \overline{A \cdot B} \text{ NAND } \overline{A \cdot B}$

**Or**

Apply Not to both inputs, then Nand the results (De Morgan's law).

$A + B = \overline{\overline{A} \cdot \overline{B}}$

**Xor**

The output is 1 if the inputs do not equal each other.

$A \text{ XOR } B = A \cdot \overline{B} + \overline{A} \cdot B$

**Mux**

It chooses one of the inputs to be the output depending on the selection bit (sel). Therefore, sel is essentially a switch that outputs a if equal to 0, and outputs b if equal to 1. In boolean algebra:

$\text{out} = \overline{\text{sel}} \cdot A + \text{sel} \cdot B$

If $\text{sel} = 0$ then:
$\text{out} = 1 \cdot A + 0 \cdot B = A$

If $\text{sel} = 1$ then:
$\text{out} = 0 \cdot A + 1 \cdot B = B$

**DMux**

Inverse of Mux. Routes a single input to one of two outputs based on sel.

$A = \overline{\text{sel}} \cdot in$

$B = \text{sel} \cdot in$

## Multi-bit Gates (Not16, And16, Or16, Mux16)
Just 16 parallel copies of the 1-bit version, one per bit. Same logic implemented over a wider bus.

## Multi-way Gates (Mux4Way16, Mux8Way16, DMux4Way, DMux8Way)
Built as binary trees of simpler chips, using one selector bit per level.

**Mux4Way16** uses 2 levels of Mux16 (3 instances total).

The first level uses sel[0] to narrow 4 inputs down to 2 — selecting between a and b, and independently between c and d. The second level uses sel[1] to make the final selection between those two results.

**Mux8Way16** extends the same pattern with a third level.

We use sel[0] to pair up all 8 inputs into 4 results, sel[1] narrows those to 2, and sel[2] makes the final selection. 3 levels, 7 Mux16 instances total.

**DMux4Way** is the mirror image of Mux4Way16. 

Sel[1] first decides which pair of outputs (a/b or c/d) will receive the signal, then sel[0] routes it to the exact output within that pair.

**DMux8Way** adds a third level.

Sel[2] splits the signal into two halves, sel[1] splits each half into pairs, and sel[0] makes the final routing decision. 3 levels, 7 DMux instances total.

In general, an N-way chip requires $log_2 N$ levels and $2N-1$ instances of the base chip.
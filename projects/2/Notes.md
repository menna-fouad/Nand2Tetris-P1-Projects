# Project 2 Notes

## Addition Components

### Half Adder

A half adder adds two bits and outputs the `sum` and `carry` bits. 

The sum is 1 when only one of the 2 bits is equal to 1, therefore implemented using the XOR gate and the carry is 1 when both inputs are 1, therefore implemented using the AND gate.

$\text{sum} = A \text{ XOR } B$

$\text{carry} = A \text{ AND } B$

### Full Adder

A full adder adds three bits and outputs their sum and carry. The sum is 1 when an odd number of the three inputs are 1, which is XOR across all three. The carry is 1 when at least two of the three inputs are 1.

$\text{sum} = A \text{ XOR } B \text{ XOR } C$

$\text{carry} = A \cdot B + \text{C} \cdot (A \text{ XOR } B)$

The first term handles the case where `A` and `B` are both 1, which means there must be a carry output regardless of `C` input. The second term handles the case where exactly one of `A` and `B` is 1, represented by XOR, and the `C` input must be a 1 in order for there to be a carry. `A XOR B` is already computed for the sum line, so it is reused here at no extra cost.

### Add16

Add16 performs 16-bit addition by chaining one half adder and fifteen full adders. The half adder handles bit 0, since there is no carry coming in at the least significant position. Each subsequent bit uses a full adder that takes the carry-out of the previous stage as its carry in. The carry-out of the most significant bit is discarded, meaning overflow is ignored.

## ALU

### Overview

The ALU takes two 16-bit inputs `x` and `y` and six control bits (`zx`, `nx`, `zy`, `ny`, `f`, `no`) that determine which of 18 functions of interest to perform. We first process `x`, then process `y`, then compute the function, and handle the output.

### Stage 1 — Pre-process x

The `x` input is conditionally zeroed and/or negated before any computation.

`zx` is fed into a Mux16 that selects between the original `x` and the constant `false` (all zeros). If `zx = 1`, `x` becomes zero.

The result is then passed through a Not16 to produce its bitwise complement. A second Mux16 selects between the unmodified result and its complement based on `nx`. If `nx = 1`, `x` is negated.

### Stage 2 — Pre-process y

Identical structure to Stage 1, using `zy` and `ny` to zero and/or negate `y`.

### Stage 3 — Compute f

The processed `x` and `y` are fed into both an Add16 and an And16 in parallel. A Mux16 selects between the two results based on `f`. If `f = 1`, the output is `x + y`. If `f = 0`, the output is `x & y`.

### Stage 4 — Post-process output

The result from Stage 3 is passed through a Not16. A Mux16 selects between the unmodified result and the complement based on `no`. If `no = 1`, the output is negated.

The final Mux16 fans out to three destinations simultaneously using HDL multi-output syntax:
- `out` — the 16-bit result
- `out[15]`, `out[0..7]`, and `out[8..15]`

### Stage 5 — Status bits

**ng** is taken directly from `out[15]` since in two's complement the MSB is 1 only if the value is negative

**zr** requires checking whether all 16 output bits are zero. Two Or8Way gates reduce each byte to a single bit, which is 1 if any bit in that byte is 1. An Or gate combines the two results into a single bit that indicates if any of the output bits is equal to 1. This is then negated with a Not gate to produce `zr = 1` when all bits are 0.
# Project 3 Notes

## Overview

This project builds the entire memory hierarchy, from a single bit of state up to a 16K-register RAM, and the Program Counter. The main concept is *sequential* logic, where the output of a chip depends on a clock and on its own previous output, rather than being a pure combinational function that only depends on current inputs.

The project is split into two parts:

- **Storage**: `Bit` -> `Register` -> `RAM8` -> `RAM64` -> `RAM512` -> `RAM4K` -> `RAM16K`
- **Program Counter**: `PC` (built on top of `Register` and Project 2's `Inc16`)

## Storage

### 1 Bit

If `load = 1`, store `in`. Otherwise, hold the value from the previous clock cycle.
In order to implement this, we use a `DFF` (data flip-flop), which outputs whatever was on its input one clock cycle ago. Then we use a `Mux` to either hold the `DFF` output or load `in` depending on `load`.

### Register

A 16-bit register. Same load/hold behavior as `Bit`, but for a 16-bit bus. I instantiated 16 independent `Bit` chips, one per
bit position, all sharing the same `load` signal so either they are all updated, or none of them are updated.

### RAM

This is the main part of Project 3. Each layer of RAM is always built only from the layer immediately below it, except RAM8, which is the lowest layer, and is built using 8 `Register` chips.

| Chip    | Registers | Built from | Address bits |
|---|---|---|---|
| RAM8 | 8 | 8 x `Register` | 3 |
| RAM64 | 64 | 8 x `RAM8` | 6 |
| RAM512 | 512 | 8 x `RAM64` | 9 |
| RAM4K | 4096 | 8 x `RAM512` | 12 |
| RAM16K | 16,384 | 4 x `RAM4K` | 14 |

At every layer, I used a `DMux8Way` (`DMux4Way` for `RAM16K`, since it's made up of 4 x `RAM4K`) where the upper 3 bits (2 for `RAM16K`) are the selection bits to decide which sub-block to route `load` to. Each sub-block uses the lower n - 3 (2 in the case of `RAM16K`) where n is the number of address bits to select their respective output. A `Mux8Way16` (`Mux4Way16` for `RAM16K`) is then used to select which sub-block's output to be the final output, which is stored in `out`.

## Program Counter

A 16-bit counter where `reset` overrides `load`, which overrides `inc`, which overrides holding, and the result is stored in a `Register` with `load` hardwired to `true`.

**Steps:**

- `Inc16` computes `out + 1` from the register's current output (fed back, same idea as `Bit`'s `DFF` feedback).
- A chain of 3 `Mux16`s applies priority, built from lowest to highest priority: `inc` first, then `load` overrides it, then `reset` overrides everything.
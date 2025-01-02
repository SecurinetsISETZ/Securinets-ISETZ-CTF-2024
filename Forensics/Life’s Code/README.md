# Task: Life’s Code

## Description
> My boss handed me this file, saying it’s critical to figure out what it means.  
> No further instructions were given.  
> Can you help me make sense of it?

> Author: ADX2K

The challenge provides a file containing a pattern for Conway’s Game of Life. Your mission is to interpret the pattern and figure out its significance using a simulator.

---

## Solution

### Step 1: Understand the Problem
The provided file contains a pattern formatted for Conway’s Game of Life, a cellular automaton devised by mathematician John Conway. The file itself encodes readable text that can be directly imported into a simulator to reveal the hidden message.

To solve the challenge, simply load the pattern into a Conway’s Game of Life simulator and observe the output.

---
### Step 2: Pattern Symbols
The provided pattern uses the **Run Length Encoded (RLE) format**, which describes the grid for Conway’s Game of Life. Here’s a brief explanation of the symbols used:

- **`b`**: Represents a dead cell (blank space).  
- **`o`**: Represents a live cell.  
- **`$`**: Indicates the end of a row and moves to the next line of the grid.  
- **`!`**: Marks the end of the pattern.

### Step 3: Use an Online Simulator
For this task, you can use the online Conway’s Game of Life simulator available at [copy.sh/life](https://copy.sh/life/). Follow these steps:

1. Open the simulator at [https://copy.sh/life/](https://copy.sh/life/).
2. Click on the **import** and import the file.
3. Once the pattern is loaded, the simulator will immediately display a message.


### Step 3: Analyze the Output
The loaded pattern will directly render readable text, but the flag is still not found. 

Upon examining the pattern, we notice that there are two **`!`** symbols, which indicate two separate ends of the pattern. This suggests that a part of the pattern was not simulated.

After removing the extra **`!`**, the simulator processes the entire pattern, and we can finally find the flag.


``Securinets{D0_Y0u_Kn0w_RLE}``

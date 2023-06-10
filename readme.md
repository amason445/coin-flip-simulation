# Coin Flip Simulation
## Summary
I wrote a simple script that simulates a fair coin being fliped and compared the expected success rate to the realized success rate.  I also attempted to package the trials as Python bytearrays which are sequences fo bytes stored in memory because I thought it would help with speed and performance.

## Methodolgy
- I encoded the flips into byte objects and then counted the success rate each expirement.
- An expirement is a sequence of flips that contains a number of trial flips.
- Since the expected number of success is equal to the trials multiplied by the theoretical success rate, the realized success rate is equal to the number of success divided by the number of trials
- Once this was completed, I packaged this information into the below visualization

## Output
![alt text](output_plot.png)

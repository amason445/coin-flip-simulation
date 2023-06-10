# Coin Flip Simulation
## Summary
I wrote a simple script that simulates a fair coin being fliped and compared the expected success rate to the realized success rate.  I also attempted to package the trials as Python bytearrays which are sequences fo bytes stored in memory because I thought it would help with speed and performance.

## Methodolgy
- I encoded the flips into byte objects and then counted the success rate each expirement.
- An expirement is a sequence of flips that contains a number of trial flips.
- Since the expected number of success is equal to the trials multiplied by the theoretical success rate, the realized success rate is equal to the number of success divided by the number of trials
- Once this was completed, I packaged this information into the below visualization

## Formulas

### Mean of the Binomial Distribution
$$\mu = {Number\\of\\Trials}\cdot {Theoretical\\Success\\Rate}$$

### Realized Success Rate
$${Realized\\Success\\Rate} = \frac{Success\\Rate}{Number\\of\\Trials}$$

### Distance from Theoretical Success Rate and Realized Success Rate
$$\Delta = \vert{\mu - Realized\\Success\\Rate}\vert$$

## Output
![alt text](output_plot.png)

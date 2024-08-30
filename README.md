# mppt_project
Simulation of MPPT using matlab and python
//////////////_CODE EXPLANATION_//////////////////////
line 5-10 is Parameters of the Flower pollination algorithm
line 13-15 is PV Parameters
line 18-21 is Initialize pollen (duty cycles)
line 24-25 is Function to calculate power based on duty cycle
line 28,29 Store data for plotting
line 34 Calculates fitness values for each pollen
line 38,39 Determines the best fitness value and corresponding duty cycle
line 42-44 Updates global optimum if current best is better
line 47-48 Stores current duty cycles and powers for plotting
line 51-57 Updates duty cycle based on conversion probability, local search, global search
line 66-68 To Update current duty cycle and fitness if new fitness is better
line 71,72 Checks termination condition
line 75-78 Outputs the best result
line 81 Initiates plotting
line 84-89 PV Voltage vs. Duty Cycle
line 92-98PV Current vs. Duty Cycle
line 101-106 Output Power vs. Duty Cycle
line 109-116 Duty Cycle over Iterations
line 118,119 Ends plotting
///////////////_TERMINAL RUNNING CONDITION_//////////////
Matlab is a Mathmatical simulation software, It is also developed to run in python compiler
with proper extensions.For the developed python code choose cmd in terminal, create environment to 
install Library extensions locally to this file. Once the installation is complete choose file 
location and run the Program.

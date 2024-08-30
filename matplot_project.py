import numpy as np
import matplotlib.pyplot as plt


max_iterations = 5          
pollen_population = 3
duty_cycle_min = 0.2        
duty_cycle_max = 0.8         
conversion_probability = 0.8 
termination_threshold = 0.005 


P_voc = 30            
I_sc = 10              
V_oc = np.linspace(0, P_voc, 100)


duty_cycles = duty_cycle_min + (duty_cycle_max - duty_cycle_min) * np.random.rand(pollen_population)
fitness_values = np.zeros(pollen_population)
global_optimal_duty_cycle = duty_cycles[0]
global_optimal_power = -np.inf


def objective_function(duty_cycle):
    return duty_cycle * (P_voc - duty_cycle)  


duty_cycle_history = np.zeros((max_iterations, pollen_population))
power_history = np.zeros((max_iterations, pollen_population))


for iter in range(max_iterations):
    
    fitness_values = np.array([objective_function(d) for d in duty_cycles])
    
    
    current_best_fitness = np.max(fitness_values)
    best_idx = np.argmax(fitness_values)
    current_best_duty_cycle = duty_cycles[best_idx]
    
    
    if current_best_fitness > global_optimal_power:
        global_optimal_power = current_best_fitness
        global_optimal_duty_cycle = current_best_duty_cycle
    

    duty_cycle_history[iter, :] = duty_cycles
    power_history[iter, :] = fitness_values
    
    
    for i in range(pollen_population):
        if np.random.rand() < conversion_probability:

            new_duty_cycle = duty_cycles[i] + (np.random.rand() - 0.5) * (duty_cycle_max - duty_cycle_min)
        else:
            
            new_duty_cycle = global_optimal_duty_cycle + (np.random.rand() - 0.5) * (duty_cycle_max - duty_cycle_min)
        
        
        new_duty_cycle = np.clip(new_duty_cycle, duty_cycle_min, duty_cycle_max)
        

        new_fitness = objective_function(new_duty_cycle)
        
        
        if new_fitness > fitness_values[i]:
            duty_cycles[i] = new_duty_cycle
            fitness_values[i] = new_fitness
    
    
    if abs(global_optimal_duty_cycle - duty_cycles[best_idx]) < termination_threshold:
        break


print('Optimal duty cycle:')
print(global_optimal_duty_cycle)
print('Optimal power:')
print(global_optimal_power)


plt.figure(figsize=(10, 8))


plt.subplot(2, 2, 1)
plt.plot(duty_cycle_history.flatten(), objective_function(duty_cycle_history.flatten()), 'o-')
plt.title('PV Voltage vs. Duty Cycle')
plt.xlabel('Duty Cycle')
plt.ylabel('Power Output')
plt.grid(True)


plt.subplot(2, 2, 2)
plt.plot(duty_cycle_history.flatten(), (P_voc - duty_cycle_history.flatten()), 'o-')
plt.title('PV Current vs. Duty Cycle')
plt.xlabel('Duty Cycle')
plt.ylabel('PV Current')
plt.grid(True)


plt.subplot(2, 2, 3)
plt.plot(duty_cycle_history.flatten(), power_history.flatten(), 'o-')
plt.title('Output Power vs. Duty Cycle')
plt.xlabel('Duty Cycle')
plt.ylabel('Output Power')
plt.grid(True)


plt.subplot(2, 2, 4)
for i in range(pollen_population):
    plt.plot(range(1, iter + 2), duty_cycle_history[:iter + 1, i], label=f'Pollen {i + 1}')
plt.title('Duty Cycle over Iterations')
plt.xlabel('Iteration')
plt.ylabel('Duty Cycle')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
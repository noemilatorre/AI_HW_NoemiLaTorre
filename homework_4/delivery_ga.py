# delivery_ga.py

import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple
import math

# Problem Constants
DELIVERY_LOCATIONS = [
    (2, 3),   # Location 1
    (5, 1),   # Location 2
    (1, 7),   # Location 3
    (8, 4),   # Location 4
    (4, 6)    # Location 5
]

TIME_WINDOWS = [
    (30, 60),    # Location 1: deliver between 30-60 minutes
    (45, 90),    # Location 2: deliver between 45-90 minutes
    (20, 50),    # Location 3: deliver between 20-50 minutes
    (60, 100),   # Location 4: deliver between 60-100 minutes
    (40, 80)     # Location 5: deliver between 40-80 minutes
]

TRAFFIC_MULTIPLIERS = {
    "morning": 1.5,    # 7am - 9am
    "normal": 1.0,     # Other times
    "evening": 1.3     # 4pm - 6pm
}

AVERAGE_SPEED = 30  # km/h
SERVICE_TIME = 5    # minutes per delivery
DEPOT_LOCATION = (0, 0)

class DeliveryOptimizer:
    """Base class for delivery route optimization using Genetic Algorithm."""
    
    def __init__(
        self,
        population_size: int = 50,
        max_generations: int = 100,
        mutation_rate: float = 0.01,
        crossover_rate: float = 0.8,
        elitism: bool = True
    ):
        """Initialize the genetic algorithm parameters."""
        self.population_size = population_size
        self.max_generations = max_generations
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.elitism = elitism
        
        # Will be set in child class
        self.chromosome_length = None
        
        # Setup visualization
        #plt.style.use('seaborn')  NO
        plt.style.use('ggplot')
        #plt.style.use('classic')
        self.fig, (self.ax1, self.ax2) = plt.subplots(1, 2, figsize=(15, 5))
        
    def _select_parents(self, fitness_values: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """Tournament selection for parent selection."""
        tournament_size = 3
        tournament_indices = np.random.choice(self.population_size, size=tournament_size, replace=False)
        tournament_fitness = fitness_values[tournament_indices]
        winner_idx = tournament_indices[np.argmax(tournament_fitness)]
        return self.population[winner_idx]
    
    def _crossover(self, parent1: np.ndarray, parent2: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """Perform two-point crossover."""
        if np.random.random() < self.crossover_rate:
            points = sorted(np.random.choice(self.chromosome_length - 1, size=2, replace=False) + 1)
            offspring1 = np.concatenate([
                parent1[:points[0]],
                parent2[points[0]:points[1]],
                parent1[points[1]:]
            ])
            offspring2 = np.concatenate([
                parent2[:points[0]],
                parent1[points[0]:points[1]],
                parent2[points[1]:]
            ])
            return offspring1, offspring2
        return parent1.copy(), parent2.copy()
    
    def _mutate(self, chromosome: np.ndarray) -> np.ndarray:
        """Perform bit-flip mutation."""
        mutation_mask = np.random.random(self.chromosome_length) < self.mutation_rate
        if mutation_mask.any():
            chromosome = chromosome.copy()
            chromosome[mutation_mask] = 1 - chromosome[mutation_mask]
        return chromosome
    
    def _plot_route(self, route: List[int]):
        """Plot the current best route."""
        self.ax1.clear()
        
        # Plot locations
        locations = [DEPOT_LOCATION] + DELIVERY_LOCATIONS
        x_coords = [loc[0] for loc in locations]
        y_coords = [loc[1] for loc in locations]
        
        # Plot depot
        self.ax1.scatter([DEPOT_LOCATION[0]], [DEPOT_LOCATION[1]], 
                        c='red', marker='s', s=100, label='Depot')
        
        # Plot delivery locations
        self.ax1.scatter(x_coords[1:], y_coords[1:], c='blue', marker='o', label='Deliveries')
        
        # Add location labels
        for i, (x, y) in enumerate(DELIVERY_LOCATIONS, 1):
            self.ax1.annotate(f'L{i}', (x, y), xytext=(5, 5), 
                            textcoords='offset points')
        
        # Plot route
        route = [0] + route + [0]  # Add depot at start and end
        for i in range(len(route) - 1):
            start = locations[route[i]]
            end = locations[route[i + 1]]
            self.ax1.plot([start[0], end[0]], [start[1], end[1]], 'r--', alpha=0.7)
        
        self.ax1.set_title('Current Best Route')
        self.ax1.grid(True)
        self.ax1.legend()
        
        # Set fixed axes with some padding
        max_x = max(x_coords) + 1
        max_y = max(y_coords) + 1
        self.ax1.set_xlim(-1, max_x)
        self.ax1.set_ylim(-1, max_y)
    
    def optimize(self):
        """Run the genetic algorithm optimization."""
        if self.chromosome_length is None:
            raise ValueError("Chromosome length must be set before optimization")
        
        # Create initial population
        self.population = np.random.randint(2, size=(self.population_size, self.chromosome_length))
        
        best_fitness_history = []
        avg_fitness_history = []
        
        for generation in range(self.max_generations):
            # Calculate fitness for all chromosomes
            fitness_values = np.array([self.calculate_fitness(chrom) for chrom in self.population])
            
            # Store best and average fitness
            best_fitness = np.max(fitness_values)
            avg_fitness = np.mean(fitness_values)
            best_fitness_history.append(best_fitness)
            avg_fitness_history.append(avg_fitness)
            
            # Plot current best route
            best_route = self.decode_chromosome(self.population[np.argmax(fitness_values)])
            self._plot_route(best_route)
            
            # Create new population
            new_population = []
            
            # Elitism
            if self.elitism:
                elite_idx = np.argmax(fitness_values)
                new_population.append(self.population[elite_idx].copy())
            
            # Create rest of new population
            while len(new_population) < self.population_size:
                parent1 = self._select_parents(fitness_values)
                parent2 = self._select_parents(fitness_values)
                
                offspring1, offspring2 = self._crossover(parent1, parent2)
                
                offspring1 = self._mutate(offspring1)
                offspring2 = self._mutate(offspring2)
                
                new_population.extend([offspring1, offspring2])
            
            # Trim population to correct size
            new_population = new_population[:self.population_size]
            self.population = np.array(new_population)
            
            # Update fitness plot
            self.ax2.clear()
            self.ax2.plot(best_fitness_history, 'r-', label='Best Fitness')
            self.ax2.plot(avg_fitness_history, 'b-', label='Average Fitness')
            self.ax2.set_xlabel('Generation')
            self.ax2.set_ylabel('Fitness')
            self.ax2.set_title('Fitness Evolution')
            self.ax2.legend()
            self.ax2.grid(True)
            
            # Display generation info
            print(f"\rGeneration {generation + 1}/{self.max_generations} "
                  f"| Best Fitness: {best_fitness:.2f} "
                  f"| Avg Fitness: {avg_fitness:.2f}", end="")
            
            plt.pause(0.1)
        
        print("\nOptimization completed!")
        plt.show()
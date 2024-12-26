import sys

sys.dont_write_bytecode = True

from my_delivery_optimizer import MyDeliveryOptimizer
from rich import print

def main():
    """Run the delivery route optimization."""
    optimizer = MyDeliveryOptimizer(
        population_size=50,
        max_generations=100,
        mutation_rate=0.01,
        crossover_rate=0.8,
        elitism=True
    )
    
    # Print configuration
    print("Delivery Route Optimization")
    print("=" * 50)
    print("Configuration:")
    print(f"Population Size: {optimizer.population_size}")
    print(f"Max Generations: {optimizer.max_generations}")
    print(f"Mutation Rate: {optimizer.mutation_rate}")
    print(f"Crossover Rate: {optimizer.crossover_rate}")
    print(f"Elitism: {optimizer.elitism}")
    print("=" * 50)
    
    # Run optimization
    print("Starting optimization...")
    optimizer.optimize()

if __name__ == "__main__":
    main()
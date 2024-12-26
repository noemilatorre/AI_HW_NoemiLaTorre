from delivery_ga import DeliveryOptimizer, DELIVERY_LOCATIONS, AVERAGE_SPEED, SERVICE_TIME, TIME_WINDOWS, TRAFFIC_MULTIPLIERS
import numpy as np

class MyDeliveryOptimizer(DeliveryOptimizer):
    """Optimized implementation of the delivery route optimizer."""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Chromosome length: Each location is assigned a priority
        self.chromosome_length = len(DELIVERY_LOCATIONS)
    
    def decode_chromosome(self, chromosome: np.ndarray) -> list:
        """
        Decode chromosome into a delivery route.
        
        Args:
            chromosome: Binary array representing the solution
            
        Returns:
            list: Delivery route (indices of locations in order)
        """
        # Sort locations by their assigned priority in the chromosome
        #return np.argsort(chromosome) + 1  # Convert 0-based to 1-based indexing

        # Ordina le località in base alla priorità del cromosoma (0-based)
        route = np.argsort(chromosome) + 1  # Converto in indici 1-based
        return list(route)

    def calculate_fitness(self, chromosome: np.ndarray) -> float:
        """
        Calculate fitness as a combination of total travel distance and time penalties.

        Args:
            chromosome: Array representing the solution priorities.

        Returns:
            float: Fitness value (higher is better).
        """
        # Decodifica del cromosoma
        route = self.decode_chromosome(chromosome)

        total_distance = 0
        total_time_penalty = 0
        current_pos = (0, 0)  # Posizione iniziale: deposito

        # Mi serve per orario di arrivo e penalità
        arrival_times = self._calculate_arrival_times(route)

        for i, location_idx in enumerate(route):
            next_pos = DELIVERY_LOCATIONS[location_idx - 1]

            # Distanza dal prossimo punto
            distance_to_next = np.linalg.norm(np.array(next_pos) - np.array(current_pos))
            total_distance += distance_to_next

            # Aggiorno posizione corrente
            current_pos = next_pos

            # Applico delle penalità se arrivo fuori dalla finestra temporale:

            # Recupero i limiti temporali della località
            min_time, max_time = TIME_WINDOWS[location_idx - 1]
            # Orario di arrivo previsto
            arrival_time = arrival_times[i]

            # Calcolo delle penalità per arrivi fuori orario
            early_penalty = max(0, min_time - arrival_time)
            late_penalty = max(0, arrival_time - max_time)
            total_time_penalty += early_penalty + late_penalty

        # Ritorno al deposito
        return_to_depot = np.linalg.norm(np.array((0, 0)) - np.array(current_pos))
        total_distance += return_to_depot

        # Calcolo dei fattori della fitness
        distance_factor = 1000 / (total_distance + 1)
        time_penalty_factor = 1 / (total_time_penalty + 1)

        # Fitness totale
        fitness = distance_factor + time_penalty_factor

        return fitness

    def _calculate_arrival_times(self, route: list) -> list:
        """
        Calculate arrival times at each location.
        
        Args:
            route: List of location indices
            
        Returns:
            list: Arrival times at each location (in minutes)
        """
        current_time = 0
        current_pos = (0, 0)  # Start at depot
        arrival_times = []
        
        for location_idx in route:

            next_pos = DELIVERY_LOCATIONS[location_idx - 1]
            travel_time = (np.linalg.norm(np.array(next_pos) - np.array(current_pos)) / AVERAGE_SPEED) * 60
            current_time += travel_time + SERVICE_TIME
            arrival_times.append(current_time)
            current_pos = next_pos
        
        return arrival_times

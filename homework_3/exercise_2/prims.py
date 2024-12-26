from heapq import heappush, heappop
from typing import Dict, List, Set, Tuple, Optional
import matplotlib.pyplot as plt
import numpy as np


class PowerStation:
    def __init__(self, name: str, location: Tuple[float, float]):
        self.name = name
        self.location = location
        self.connections: Dict[str, float] = {}


class PowerGrid:
   def __init__(self):
      self.stations: Dict[str, PowerStation] = {
         'Downtown': PowerStation('Downtown', (0, 0)),
         'Northside': PowerStation('Northside', (2, 4)),
         'Westpark': PowerStation('Westpark', (-3, 1)),
         'Eastville': PowerStation('Eastville', (4, 0)),
         'Southend': PowerStation('Southend', (1, -3)),
         'Industrial': PowerStation('Industrial', (-1, -2))
      }
      self.setup_connection_costs()

   def setup_connection_costs(self):
      """Initialize possible connections between stations with costs"""
      connections = [
         ('Downtown', 'Northside', 8500),
         ('Downtown', 'Westpark', 6200),
         ('Downtown', 'Eastville', 7800),
         ('Downtown', 'Southend', 5400),
         ('Northside', 'Westpark', 9100),
         ('Northside', 'Eastville', 6700),
         ('Westpark', 'Southend', 8300),
         ('Eastville', 'Southend', 7200),
         ('Southend', 'Industrial', 4800),
         ('Downtown', 'Industrial', 5900)
      ]
      
      for station1, station2, cost in connections:
         self.stations[station1].connections[station2] = cost
         self.stations[station2].connections[station1] = cost

   def optimize_connections(self) -> List[Tuple[str, str, float]]:
       """Find minimum spanning tree using Prim's algorithm"""
       start_station = 'Downtown'  # Nodo di partenza arbitrario
       mst = []  # Lista degli archi nell'albero di copertura minimo
       visited = set()  # Nodi già inclusi nell'MST
       min_heap = []  # Coda di priorità per selezionare l'arco di costo minimo

       # Inizializza la coda con gli archi collegati al nodo di partenza
       visited.add(start_station)
       for neighbor, cost in self.stations[start_station].connections.items():
           heappush(min_heap, (cost, start_station, neighbor))

       # Costruisce l'MST
       while min_heap:
           cost, station1, station2 = heappop(min_heap)
           if station2 not in visited:
               visited.add(station2)
               mst.append((station1, station2, cost))

               # Aggiunge gli archi collegati al nuovo nodo
               for next_neighbor, next_cost in self.stations[station2].connections.items():
                   if next_neighbor not in visited:
                       heappush(min_heap, (next_cost, station2, next_neighbor))

       return mst


   def get_total_cost(self, mst: List[Tuple[str, str, float]]) -> float:
       """Calculate total cost of power line installation"""
       # TODO: Implement this method
       # pass
       total_cost = 0
       for _, _, cost in mst:
           total_cost += cost
       return total_cost

   def display_network(self, mst: List[Tuple[str, str, float]]):
      """Display the optimized power grid network"""
      # TODO: Implement this method
      #pass
      for station1, station2, cost in mst:
          print(f"Connection between {station1} and {station2} with cost €{cost:,.0f}")
     
   def visualize(self, mst: List[Tuple[str, str, float]] = None):
        """
        Visualize the power grid network using matplotlib.
        If MST is provided, it will be shown in green, other connections in gray.
        """
        fig, ax = plt.subplots(figsize=(12, 8))
        
        # Plot stations as points
        x_coords = [station.location[0] for station in self.stations.values()]
        y_coords = [station.location[1] for station in self.stations.values()]
        
        # Plot all possible connections in light gray
        for station_name, station in self.stations.items():
            for neighbor, cost in station.connections.items():
                neighbor_station = self.stations[neighbor]
                ax.plot([station.location[0], neighbor_station.location[0]],
                       [station.location[1], neighbor_station.location[1]],
                       'lightgray', zorder=1, linewidth=1, alpha=0.5,
                       label='Possible Connection' if station_name == 'Downtown' else "")
        
        # Plot MST connections if provided
        if mst:
            mst_connections = set()
            for station1, station2, _ in mst:
                # Add both directions to avoid duplicate plotting
                mst_connections.add((station1, station2))
                mst_connections.add((station2, station1))
                
                # Plot MST connection
                station1_loc = self.stations[station1].location
                station2_loc = self.stations[station2].location
                ax.plot([station1_loc[0], station2_loc[0]],
                       [station1_loc[1], station2_loc[1]],
                       'green', zorder=2, linewidth=2,
                       label='Optimal Connection' if (station1, station2) == mst[0] else "")
        
        # Plot stations
        ax.scatter(x_coords, y_coords, c='red', s=100, zorder=3, label='Power Station')
        
        # Add station labels
        for station_name, station in self.stations.items():
            ax.annotate(station_name, (station.location[0], station.location[1]),
                       xytext=(5, 5), textcoords='offset points')
        
        # Add costs to MST connections if provided
        if mst:
            for station1, station2, cost in mst:
                station1_loc = self.stations[station1].location
                station2_loc = self.stations[station2].location
                midpoint = np.array(station1_loc) + (np.array(station2_loc) - np.array(station1_loc)) * 0.5
                ax.annotate(f'€{cost:,.0f}', 
                           (midpoint[0], midpoint[1]),
                           bbox=dict(facecolor='white', edgecolor='none', alpha=0.7))
        
        # Customize plot
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.title('Power Grid Network')
        plt.xlabel('Distance (km)')
        plt.ylabel('Distance (km)')
        
        # Add legend
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        
        plt.tight_layout()
        plt.show()

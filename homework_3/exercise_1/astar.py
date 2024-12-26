from heapq import heappush, heappop
import matplotlib.pyplot as plt
import numpy as np
from typing import List, Tuple, Optional


class Node:
    def __init__(self, position: Tuple[int, int], parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Cost from start to current node
        self.h = 0  # Estimated cost from current node to goal
        self.f = 0  # Total cost (g + h)

    def __lt__(self, other):
        return self.f < other.f


class MuseumEvacuation:
    def __init__(self):
        self.layout = [
            ['0', '0', '1', '0', 'E'],
            ['0', '1', '0', '1', '0'],
            ['P', '0', '0', '0', '0'],
            ['0', '1', '1', '1', '0'],
            ['0', '0', '0', '0', 'E']
        ]
        self.rows = len(self.layout)
        self.cols = len(self.layout[0])

    def find_person_and_exits(self) -> Tuple[Tuple[int, int], List[Tuple[int, int]]]:
        """Find person's position and all emergency exits"""
        # TODO: Implement this method
        #pass

        person_position = None
        exits = []

        for i in range(self.rows):
            for j in range(self.cols):
                if self.layout[i][j] == 'P':  # P è la posizione della persona
                    person_position = (i, j)
                elif self.layout[i][j] == 'E':  # E è la posizione delle uscite
                    exits.append((i, j))

        if person_position is None:
            raise ValueError("Non è stata trovata nessuna persona in questa posizione nella griglia.")

        return person_position, exits

    def manhattan_distance(self, pos1: Tuple[int, int], pos2: Tuple[int, int]) -> int:
        """Calculate Manhattan distance between two points"""
        # TODO: Implement this method
        #pass
        # somma del valore assoluto delle differenze delle due coordinate

        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    def get_neighbors(self, position: Tuple[int, int]) -> List[Tuple[int, int]]:
        """Get valid neighboring positions"""
        # TODO: Implement this method
        #pass
        x, y = position
        neighbors = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Mi posso muovere solo: su, giù, sinistra, destra

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if (0 <= nx < self.rows
                    and 0 <= ny < self.cols
                    and self.layout[nx][ny] != '1'):  # '1' è un muro (ostacolo)
                neighbors.append((nx, ny))

        return neighbors


    def find_evacuation_path(self) -> Optional[List[Tuple[int, int]]]:
        """Find shortest path to nearest emergency exit"""
        # TODO: Implement this method
        # pass
        # coda di priorità per selezionare
        # il nodo con il valore f più basso e iterare fino a trovare un percorso

        start, exits = self.find_person_and_exits()
        open_list = []  # è la coda di priorità
        closed_list = set()

        # Nodo iniziale
        start_node = Node(start)
        start_node.g = 0
        start_node.h = min(self.manhattan_distance(start, exit) for exit in exits)
        start_node.f = start_node.g + start_node.h
        heappush(open_list, start_node)

        while open_list:
            current_node = heappop(open_list)

            # Controllo se è una delle uscite
            if current_node.position in exits:
                path = []
                while current_node:
                    path.append(current_node.position)
                    current_node = current_node.parent
                path.reverse()  # Inverto il percorso per mostrarlo dall'inizio alla fine
                return path

            closed_list.add(current_node.position)

            # Espando tutti i vicini
            for neighbor_pos in self.get_neighbors(current_node.position):
                if neighbor_pos in closed_list:
                    continue

                neighbor = Node(neighbor_pos, current_node)
                neighbor.g = current_node.g + 1  # Costo tra nodi adiacenti unitario (1)
                neighbor.h = min(self.manhattan_distance(neighbor.position, exit) for exit in exits)
                neighbor.f = neighbor.g + neighbor.h

                # Devo verificare se il vicino è già nella lista di open con un percorso migliore
                if not any(neighbor.position == n.position and neighbor.f >= n.f for n in open_list):
                    heappush(open_list, neighbor)

        return None  # Nessun percorso trovato

    def display_path(self, path: List[Tuple[int, int]]):
        """Display the evacuation path on the museum layout"""
        # TODO: Implement this method
        #pass
        for (i, j) in path:
            if self.layout[i][j] != 'E':
                self.layout[i][j] = '→'     #segno il percorso con una freccia, tranne sulle uscite
    
    def visualize(self, path: List[Tuple[int, int]] = None):
        """
        Visualize the museum layout with matplotlib.
        If path is provided, it will be shown in green.
        """
        # Create figure with smaller size and better cell proportion
        fig, ax = plt.subplots(figsize=(6, 6))
        
        # Create color map with distinct colors
        cmap = plt.cm.colors.ListedColormap(['#FFFFFF', '#404040', '#FF4444', '#4444FF', '#FFCC00'])
        
        # Convert layout to numeric array for visualization
        numeric_layout = np.zeros((self.rows, self.cols))
        text_annotations = []  # Store text annotations for cells
        
        for i in range(self.rows):
            for j in range(self.cols):
                if self.layout[i][j] == '1':  # Wall
                    numeric_layout[i][j] = 1
                    text_annotations.append((i, j, ''))
                elif self.layout[i][j] == 'E':  # Exit
                    numeric_layout[i][j] = 2
                    text_annotations.append((i, j, 'EXIT'))
                elif self.layout[i][j] == 'P':  # Person
                    numeric_layout[i][j] = 3
                    text_annotations.append((i, j, 'P'))
                else:  # Free space
                    text_annotations.append((i, j, ''))
        
        # Add path if provided
        if path:
            for row, col in path[1:-1]:  # Skip start and end positions
                numeric_layout[row][col] = 4
                text_annotations.append((row, col, '→'))

        # Plot the layout
        im = ax.imshow(numeric_layout, cmap=cmap)
        
        # Add cell borders
        for i in range(self.rows + 1):
            ax.axhline(i - 0.5, color='black', linewidth=1)
        for j in range(self.cols + 1):
            ax.axvline(j - 0.5, color='black', linewidth=1)
        
        # Add text annotations
        for i, j, text in text_annotations:
            if text:  # Only add non-empty text
                color = 'white' if numeric_layout[i,j] in [1, 2, 3] else 'black'
                ax.text(j, i, text, ha='center', va='center', color=color, 
                       fontweight='bold', fontsize=10)
        
        # Remove ticks but keep grid lines
        ax.set_xticks([])
        ax.set_yticks([])
        
        # Add legend with smaller patches
        from matplotlib.patches import Patch
        legend_elements = [
            Patch(facecolor='#FFFFFF', edgecolor='black', label='Free Space'),
            Patch(facecolor='#404040', edgecolor='black', label='Wall'),
            Patch(facecolor='#FF4444', edgecolor='black', label='Exit'),
            Patch(facecolor='#4444FF', edgecolor='black', label='Person'),
        ]
        if path:
            legend_elements.append(Patch(facecolor='#FFCC00', edgecolor='black', label='Path'))
            
        ax.legend(handles=legend_elements, 
                 loc='center left',
                 bbox_to_anchor=(1.05, 0.5),
                 title='Legend',
                 frameon=True,
                 fontsize='small')
        
        plt.title('Museum Layout', pad=10)
        plt.tight_layout()
        plt.show()
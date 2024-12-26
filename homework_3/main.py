import sys

sys.dont_write_bytecode = True

from exercise_1.astar import MuseumEvacuation
from exercise_2.prims import PowerGrid


def test_museum_evacuation():
    """
    Test the MuseumEvacuation class
    """
    museum = MuseumEvacuation()
    path = museum.find_evacuation_path()
    if path:
        print("Emergency evacuation path found!")
        museum.display_path(path)
    else:
        print("No evacuation path available!")


def test_power_grid():
    """
    Test the PowerGrid class
    """
    grid = PowerGrid()
    mst = grid.optimize_connections()
    if mst:
        print("Optimal power grid design found!")
        grid.display_network(mst)
        print(f"Total installation cost: ${grid.get_total_cost(mst):,.2f}")
    else:
        print("Could not find valid power grid configuration!")


def main():
    print("1. Testing Museum Evacuation System")
    print("===================================")
    museum = MuseumEvacuation()
    
    print("\nInitial Museum Layout:")
    museum.visualize()  
    
    path = museum.find_evacuation_path()
    if path:
        print("\nEvacuation path found!")
        museum.display_path(path)
        museum.visualize(path)
    else:
        print("No evacuation path available!")

    print("\n2. Testing Power Grid Optimization")
    print("===================================")
    grid = PowerGrid()
    
    print("\nInitial Power Grid Network:")
    grid.visualize()  
    
    mst = grid.optimize_connections()
    if mst:
        print("\nOptimal Power Grid Configuration:")
        grid.display_network(mst)  
        grid.visualize(mst)
    else:
        print("Could not find valid power grid configuration!")

if __name__ == "__main__":
    main()
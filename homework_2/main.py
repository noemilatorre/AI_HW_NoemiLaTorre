import numpy as np 
import pandas as pd 
from src.signal_processing import analyze_signal 
from src.score_analysis import analyze_scores 
from src.weather_analysis import analyze_weather 
from src.traffic_analysis import analyze_traffic 
from utils.data_generator import DataGenerator 
 

def main():
    """
    Main function to run all homework exercises.
    Each exercise demonstrates the use of NumPy, Pandas, and Matplotlib.
    
    The exercises are:
    1. Signal Processing: Demonstrates NumPy array operations and signal manipulation
    2. Score Analysis: Shows NumPy statistical operations
    3. Weather Analysis: Uses Pandas for data manipulation and analysis
    4. Traffic Analysis: Demonstrates Pandas time series capabilities
    """
    
    # Initialize data generator
    data_gen = DataGenerator()
    
    # Exercise 1: Signal Processing with NumPy
    print("\n=== Exercise 1: Signal Processing ===")
    time_array, clean_signal, noisy_signal = data_gen.generate_signal_data(
        duration=5,
        num_points=500,
        noise_std=0.2
    )
    
    analyze_signal(time_array, clean_signal, noisy_signal)
    
    # Exercise 2: Student Scores with NumPy
    print("\n=== Exercise 2: Student Score Analysis ===")
    scores = data_gen.generate_score_data(
        num_students=10,
        num_subjects=5,
        min_score=60,
        max_score=100
    )
    
    analyze_scores(scores)
    
    # Exercise 3: Weather Analysis with Pandas
    print("\n=== Exercise 3: Weather Analysis ===")
    weather_data = data_gen.generate_weather_data()
    
    analyze_weather(weather_data)
    
    # Exercise 4: Traffic Analysis with Pandas
    print("\n=== Exercise 4: Website Traffic Analysis ===")
    traffic_data = data_gen.generate_traffic_data()
    
    analyze_traffic(traffic_data)
 
if __name__ == "__main__": 
    main() 

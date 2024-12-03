"""Data Generator for Exercises""" 
import numpy as np 
import pandas as pd 
 
 
class DataGenerator:
    """
    Class responsible for generating data for all exercises.
    Provides methods to create synthetic data for testing and analysis.
    """
    
    def generate_signal_data(self, duration, num_points, noise_std):
        """
        Generate signal data for signal processing exercise.
        
        Parameters:
        -----------
        duration : float
            Duration of the signal in seconds
        num_points : int
            Number of data points to generate
        noise_std : float
            Standard deviation of the noise to add
            
        Returns:
        --------
        tuple
            (time_array, clean_signal, noisy_signal)
        """
        t = np.linspace(0, duration, num_points)
        clean = np.sin(2 * 2 * np.pi * t) + np.cos(2 * np.pi * t)
        noise = np.random.normal(0, noise_std, num_points)
        noisy = clean + noise
        return t, clean, noisy


    def generate_score_data(self, num_students, num_subjects, min_score, max_score):
        """
        Generate random student scores for score analysis exercise.
        
        Parameters:
        -----------
        num_students : int
            Number of students
        num_subjects : int
            Number of subjects
        min_score : int
            Minimum possible score
        max_score : int
            Maximum possible score
            
        Returns:
        --------
        numpy.ndarray
            2D array of scores (students × subjects)
        """
        return np.random.randint(min_score, max_score + 1, 
                               size=(num_students, num_subjects))


    def generate_weather_data(self):
        """
        Generate weather data for weather analysis exercise.
        Creates a DataFrame with monthly temperature and precipitation data.
        
        Returns:
        --------
        pandas.DataFrame
            DataFrame with columns: Month, Temperature, Precipitation
        """
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        
        data = {
            'Month': months,
            'Temperature': np.random.uniform(-5, 35, 12),
            'Precipitation': np.random.uniform(0, 100, 12)
        }
        return pd.DataFrame(data)


    def generate_traffic_data(self):
        """
        Generate website traffic data for traffic analysis exercise.
        Creates a DataFrame with daily visitors and bounce rate data.
        
        Returns:
        --------
        pandas.DataFrame
            DataFrame with columns: Date, Visitors, Bounce_Rate
        """
        dates = pd.date_range(start='2024-01-01', periods=30)
        data = {
            'Date': dates,
            'Visitors': np.random.randint(100, 1000, 30),
            'Bounce_Rate': np.random.uniform(20, 60, 30)
        }
        return pd.DataFrame(data)

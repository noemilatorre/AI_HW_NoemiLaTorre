"""Weather Analysis Exercise""" 
import pandas as pd 
import matplotlib.pyplot as plt 
 
def analyze_weather(df):
    """
    Exercise 3: Weather Data Analysis with Pandas
    ------------------------------------------
    Task: Analyze temperature and precipitation patterns.
    
    Required steps:
    1. Calculate basic statistics:
       - Monthly temperature averages
       - Total precipitation by month
       - Seasonal patterns
       - Temperature-precipitation correlation
    
    2. Create seasonal analysis:
       - Group data by seasons
       - Calculate seasonal averages
       - Identify extreme weather months
    
    3. Create visualizations:
       - Dual-axis plot for temperature and precipitation
       - Seasonal temperature averages
       - Temperature distribution
       - Temperature vs precipitation scatter plot
    
    Parameters:
    -----------
    df : pandas.DataFrame
        DataFrame with columns:
        - Month: month names
        - Temperature: temperature values in Celsius
        - Precipitation: precipitation values in mm
    
    Expected Output:
    --------------
    1. Four-panel figure showing:
       - Temperature and precipitation trends
       - Seasonal averages
       - Temperature distribution
       - Correlation scatter plot
    2. Dictionary with weather statistics
    
    Hint: Use pd.cut for seasonal grouping
    """
    #pass

#Colonna 'Stagione' basata sul mese

    Season = {
        'Dec': 'Winter', 'Jan': 'Winter', 'Feb': 'Winter',
        'Mar': 'Spring', 'Apr': 'Spring', 'May': 'Spring',
        'Jun': 'Summer', 'Jul': 'Summer', 'Aug': 'Summer',
        'Sep': 'Autumn', 'Oct': 'Autumn', 'Nov': 'Autumn'
    }

    df['Season'] = df['Month'].map(Season)
    print(df['Season'].unique())
    print(df[['Month', 'Temperature']])

#  Medie temp stagionali e somma totale delle precipitazioni stagionali
    media_temp_stagionale = df.groupby('Season')['Temperature'].mean()
    print(media_temp_stagionale)

    totale_precip_stagionale = df.groupby('Season')['Precipitation'].sum()

# Media di temp e somma totale precipitazioni mensili
    media_temp_mensile = df.groupby('Month')['Temperature'].mean()
    totale_precip_mensile = df.groupby('Month')['Precipitation'].sum()

# Correlazione tra temperatura e precipitazioni
    correlazione_temp_precip = df['Temperature'].corr(df['Precipitation'])

 # Mesi con temperature estreme (max e min)
    mese_max_temp = df.loc[df['Temperature'].idxmax(), 'Month']
    mese_min_temp = df.loc[df['Temperature'].idxmin(), 'Month']

# Grafici con subplot 4
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('Analisi Meteo', fontsize=16)

# 1) Dual-axis plot: Temperature e Precipitazioni mensili, ho fatto bar plot
    axes[0, 0].bar(media_temp_mensile.index, media_temp_mensile.values, color='blue', label='Temperatura Media (°C)')
    axes[0, 0].set_ylabel('Temperatura Media (°C)')
    axes[0, 0].set_xlabel('Mese')
    axes[0, 0].set_title('Andamento Mensile di Temperatura e Precipitazioni')
    axes[0, 0].legend()
    axes[0, 0].tick_params(axis='y')
#secondo plot sovrapposto, l'ho messo come e linear plot, perchè bar plot sovrapposto non si leggeva
    ax2 = axes[0, 0].twinx() #per aggiungere ulteriore scala su asse y
    ax2.plot(totale_precip_mensile.index, totale_precip_mensile.values, color='red', alpha=0.6,
            label='Precipitazione Totale (mm)')
    ax2.set_ylabel('Precipitazione Totale (mm)')
    ax2.legend()
    ax2.tick_params(axis='y')

# 2) Media stagionale della temperatura

    ordine_stagioni = ['Winter', 'Spring', 'Summer', 'Autumn']
    media_temp_stagionale = media_temp_stagionale.reindex(ordine_stagioni)

    axes[0, 1].bar(
        media_temp_stagionale.index,
        media_temp_stagionale.values,
        color=['blue', 'orange', 'green', 'red'],
        alpha=0.7
    )
    axes[0, 1].set_title('Media Stagionale della Temperatura')
    axes[0, 1].grid(True, alpha=0.3)
    axes[0, 1].set_xlabel('Stagione')
    axes[0, 1].set_ylabel('Temperatura Media (°C)')

 # 3) Istogramma della distribuzione delle temperature
    axes[1, 0].hist(
        df['Temperature'],bins=15, color='green', edgecolor='black')
    axes[1, 0].set_title('Distribuzione delle Temperature')
    axes[0, 1].grid(True, alpha=0.3)
    axes[1, 0].set_xlabel('Temperatura (°C)')
    axes[1, 0].set_ylabel('Frequenza')

# 4) Scatter plot: Temperatura vs Precipitazioni
    axes[1, 1].scatter(
        df['Temperature'], df['Precipitation'], color='red', alpha=0.8)
    axes[1, 1].set_title('Temperatura vs Precipitazioni')
    axes[0, 1].grid(True, alpha=0.3)
    axes[1, 1].set_xlabel('Temperatura (°C)')
    axes[1, 1].set_ylabel('Precipitazione (mm)')

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()


 # Dictionary
    risultati_analisi = {
        #converto prima in dizionario
        'media_temp_mensile': media_temp_mensile.to_dict(),
        'totale_precip_mensile': totale_precip_mensile.to_dict(),
        'media_temp_stagionale': media_temp_stagionale.to_dict(),
        'totale_precip_stagionale': totale_precip_stagionale.to_dict(),
        'correlazione_temp_precip': correlazione_temp_precip,
        'mese_max_temp': mese_max_temp,
        'mese_min_temp': mese_min_temp
    }

    print(risultati_analisi)

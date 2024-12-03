"""Traffic Analysis Exercise""" 
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np


def analyze_traffic(df):
    """
    Exercise 4: Website Traffic Analysis with Pandas
    --------------------------------------------
    Task: Analyze website traffic patterns and bounce rates.
    
    Required steps:
    1. Time series analysis:
       - Calculate daily traffic patterns
       - Compute moving averages (3-day and 7-day)
       - Identify weekly patterns
    
    2. Bounce rate analysis:
       - Calculate average bounce rates
       - Correlate bounce rates with traffic
       - Identify high/low bounce rate periods
    
    3. Create visualizations:
       - Traffic trends with moving averages
       - Daily traffic patterns
       - Bounce rate trends
       - Traffic vs bounce rate correlation
    
    Parameters:
    -----------
    df : pandas.DataFrame
        DataFrame with columns:
        - Date: datetime index
        - Visitors: daily visitor count
        - Bounce_Rate: daily bounce rate percentage
    
    Expected Output:
    --------------
    1. Four-panel figure showing:
       - Traffic trends with moving averages
       - Average daily traffic patterns
       - Bounce rate trend
       - Correlation scatter plot
    2. Dictionary with traffic statistics
    
    Hint: Use df.rolling for moving averages
    """
    #pass
   # print(df) #Ho Date, Visitors, Bound Rate

# 1. Calcolo delle statistiche di traffico giornaliere e medie

    # (0) lunedi (1) martedì (2) mercoledì (3) giovedì (4) venerdì (5)sabato (6) domenica
    daily_pattern = df['Visitors'].groupby(df['Date'].dt.dayofweek).mean()


# 2. Calcolo delle medie mobili  (3 giorni e 7 giorni)
    df['3_day_avg'] = df['Visitors'].rolling(window=3).mean()
    df['7_day_avg'] = df['Visitors'].rolling(window=7).mean()


# 3. Tassi di rimbalzo medi
    average_bounce_rate = df['Bounce_Rate'].mean()

# 4. Correlazione tra traffico e bounce rate (rimbalzi medi)
    correlation = df['Visitors'].corr(df['Bounce_Rate'])

 # 5. Identificare i periodi di tasso di rimbalzo alto/basso
    high_bounce_periods = df[df['Bounce_Rate'] > average_bounce_rate]
    low_bounce_periods = df[df['Bounce_Rate'] < average_bounce_rate]

# Subplot 4
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Analisi Traffico', fontsize=16)


# Trend dei visitatori con medie mobili tutto con linear plot
# Metto tutti sullo stesso grafico
    axes[0,0].plot(df['Date'], df['Visitors'], label='Daily Traffic', color='blue')
    axes[0,0].plot(df['Date'], df['3_day_avg'], label='3-Day Avg', color='green')
    axes[0,0].plot(df['Date'], df['7_day_avg'], label='7-Day Avg', color='red')
    axes[0,0].set_title('Trend del Traffico con Medie Mobili')
    axes[0,0].set_xlabel('Data')
    axes[0,0].set_ylabel('Numero di Visitatori')
    axes[0,0].legend()

# Pattern di traffico giornaliero (barplot)
    axes[0, 1].bar(daily_pattern.index, daily_pattern, color='orange')
    axes[0, 1].set_title('Pattern di Traffico Giornaliero Medio')
    axes[0, 1].set_xlabel('Giorno della Settimana')
    axes[0, 1].set_ylabel('Visitatori Medi')

# Trend del tasso di rimbalzo (linear plot)
    axes[1, 0].plot(df['Date'], df['Bounce_Rate'], color='green')
    axes[1, 0].set_title('Trend del Tasso di Rimbalzo')
    axes[1, 0].set_xlabel('Data')
    axes[1, 0].set_ylabel('Tasso di Rimbalzo (%)')

# Correlazione tra traffico e tasso di rimbalzo (scatter plot)
    axes[1, 1].scatter(df['Visitors'], df['Bounce_Rate'], alpha=0.6)
    axes[1, 1].set_title('Correlazione Traffico e Tasso di Rimbalzo')
    axes[1, 1].set_xlabel('Numero di Visitatori')
    axes[1, 1].set_ylabel('Tasso di Rimbalzo (%)')
 #metto la correlazione visibile dal grafico
    axes[1, 1].text(0.5, 0.1, f'Correlazione: {correlation:.2f}', ha='center', va='center', fontsize=12)

    # Layout e visualizzazione
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()

# Dictionary
    traffic_analysis_results = {
#per media mobile a 3 e a 7 giorni alcuni valori sono nan perchè non ho abbastanza valori precedenti
        '3_day_avg': df['3_day_avg'].to_dict(),
        '7_day_avg': df['7_day_avg'].to_dict(),
        'daily_pattern': daily_pattern.to_dict(), #(0) lunedì - (6) domenica
        'high_bounce_periods': high_bounce_periods[['Date', 'Bounce_Rate']].to_dict(),
        'low_bounce_periods': low_bounce_periods[['Date', 'Bounce_Rate']].to_dict(),
        'correlation': correlation
    }

    print(traffic_analysis_results)
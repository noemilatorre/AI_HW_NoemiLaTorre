"""Signal Processing Exercise""" 
import numpy as np 
import matplotlib.pyplot as plt 
 
 
def analyze_signal(time, clean, noisy):
    """
    Exercise 1: Signal Processing with NumPy
    ---------------------------------------
    Task: Analyze and visualize a signal with noise.
    
    Required steps:
    1. Calculate basic signal statistics:
       - Mean and standard deviation
       - Maximum and minimum values
       - Signal-to-noise ratio
    
    2. Process the signal:
       - Apply a moving average filter (window size = 5)
       - Perform frequency analysis using FFT
    
    3. Create visualizations:
       - Plot original clean signal
       - Plot noisy signal
       - Plot filtered signal
       - Show frequency spectrum
    
    Parameters:
    -----------
    time : numpy.ndarray
        Time points for the signal
    clean : numpy.ndarray
        Original clean signal values
    noisy : numpy.ndarray
        Signal with added noise
    
    Expected Output:
    --------------
    1. Two subplot figure showing:
       - Time domain: clean, noisy, and filtered signals
       - Frequency domain: frequency spectrum
    2. Dictionary with signal statistics
    
    Hint: Use np.fft for frequency analysis
    """

    mean = np.mean(noisy)
    standard_dev = np.std(noisy)
    max_val = np.max(noisy)
    min_val = np.min(noisy)

    snr = np.mean(clean ** 2) / np.mean((clean - noisy) ** 2)

    print("Mean", mean)
    print("Standard Dev", standard_dev)
    print("Max val", max_val)
    print("Min val", min_val)
    print("SNR", snr)

    # Filtro a media mobile di dim (5)
    win_size = 5

    #filtered = np.convolve(noisy, np.ones(win_size) / win_size, mode='same')
    filtered = np.convolve(noisy, np.ones(win_size),"same")/win_size

    # Analisi in frequenza uso FFT
    freq = np.fft.fftfreq(len(time), d=(time[1] - time[0]))
    fft_values = np.fft.fft(noisy)

    # Plot
    fig, axes = plt.subplots(2, 1, figsize=(14, 8))

    # Grafico dei 3 segnali sovrapposti
    axes[0].plot(time, clean, label='Segnale Pulito', color='blue')
    axes[0].plot(time, noisy, label='Segnale Rumoroso', color='red',linestyle='--', alpha=0.5)
    axes[0].plot(time, filtered, label='Segnale Filtrato', color='green', alpha=0.6)
    axes[0].grid(True)
    axes[0].set_xlabel("Tempo")
    axes[0].set_ylabel("Ampiezza")
    axes[0].set_title("Analisi segnali dominio del tempo")
    axes[0].legend()

    # Spettro di frequenza plot
    # solo freq pos
    axes[1].plot(freq[:len(freq) // 2], np.abs(fft_values[:len(fft_values) // 2]), color='red')
    axes[1].set_xlabel("Frequenza (Hz)")
    axes[1].set_ylabel("Ampiezza")
    axes[1].set_title("Analisi in frequenza")

    plt.show()

#Dictionary
    signal_statistics = {
        "mean": mean,
        "std_dev": standard_dev,
        "max": max_val,
        "min": min_val,
        "SNR": snr
    }


    print(signal_statistics)

    #pass


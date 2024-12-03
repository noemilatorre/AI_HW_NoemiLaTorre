"""Score Analysis Exercise""" 
import numpy as np 
import matplotlib.pyplot as plt 
 
def analyze_scores(scores):
    """
    Exercise 2: Student Score Analysis with NumPy
    ------------------------------------------
    Task: Analyze student performance across multiple subjects.
    
    Required steps:
    1. Calculate statistics for:
       - Each student's average performance
       - Each subject's average scores
       - Overall class performance

       
    2. Analyze score distribution:
       - Calculate standard deviation
       - Identify highest and lowest performing students
       - Determine score ranges for each subject
    
    3. Create visualizations:
       - Bar plot of student averages with error bars
       - Subject performance comparison
       - Score distribution histogram
       - Box plot for each subject
    
    Parameters:
    -----------
    scores : numpy.ndarray
        2D array with shape (num_students, num_subjects)
        Each row represents a student
        Each column represents a subject
    
    Expected Output:
    --------------
    1. Four-panel figure showing:
       - Student performance bar plot
       - Subject averages bar plot
       - Score distribution histogram
       - Box plot by subject
    2. Dictionary with statistical analysis
    
    Hint: Use np.mean, np.std for calculations
    """

# scores deve essere array 2D
    scores = np.array(scores)

 # axis=0 student (righe) e  axis=1 subject (colonne)

    # colonna rappresenta la materia
    # riga lo studente

    student_averages = np.mean(scores, axis=1)
    subject_averages = np.mean(scores, axis=0)
    class_average = np.mean(scores)
# Deviazione standard di ogni studente e per ogni materia
    student_std_dev = np.std(scores, axis=1)
    subject_std_dev = np.std(scores, axis=0)
    class_std = np.std(scores)

# Studente migliore e peggiore
    highest_performing_student = np.argmax(student_averages)
    lowest_performing_student = np.argmin(student_averages)

# Voto massimo e min per ciascuna materia
    #min_scores = np.min(scores, axis=0)
    #max_scores = np.max(scores, axis=0)
    subject_ranges = np.ptp(scores, axis=0)

#Visualizzazione con subplot a 4
    fig, axes = plt.subplots(2, 2, figsize=(14, 12))
    fig.suptitle('Analisi Voti Studenti', fontsize=16)


 # 1. Bar plot della media degli studenti con error bar

    bars = axes[0, 0].bar(
        range(len(student_averages)),
        student_averages,
        yerr=student_std_dev,
        capsize=5,
        color='skyblue',
    )
    axes[0, 0].set_title("Media delle Performance degli Studenti")
    axes[0, 0].set_xlabel("Studenti")
    axes[0, 0].set_ylabel("Media Voti")
    for bar in bars:
        height = bar.get_height()
        axes[0, 0].text(bar.get_x() + bar.get_width() / 2., height, f'{height:.2f}', ha='center', va='bottom')

 # 2. Bar plot della media per materia
    bars = axes[0, 1].bar(
        range(len(subject_averages)),
        subject_averages,
        yerr=subject_std_dev,
        capsize=5,
        color='lightgreen'
    )
    axes[0, 1].set_title('Media delle Performance per Materia')
    axes[0, 1].set_xlabel('Materia')
    axes[0, 1].set_ylabel('Media Voti')
    axes[0, 1].grid(True, alpha=0.3)
    axes[0, 1].set_xticks(range(len(subject_averages)))
    axes[0, 1].set_ylim(0, max(subject_averages + subject_std_dev) + 5)
    for bar in bars:
        height = bar.get_height()
        axes[0, 1].text(bar.get_x() + bar.get_width() / 2., height, f'{height:.2f}', ha='center', va='bottom',
                        fontsize=8)

# 3. Istogramma per la distribuzione dei voti
    axes[1, 0].hist(
        scores.flatten(),bins=10, color='orange', alpha=0.7)
# asse verticale per la media della classe
    axes[1, 0].axvline(class_average, color='blue', linestyle='--', label='Media della Classe')
    axes[1, 0].set_title("Distribuzione dei Voti")
    axes[1, 0].set_xlabel("Voto")
    axes[1, 0].set_ylabel("Numero di studenti")
    axes[1, 0].legend()
    axes[1, 0].grid(True, alpha=0.3)

 # 4. Box plot verticale, per materia
    axes[1, 1].boxplot(scores, patch_artist=True, boxprops=dict(facecolor="lightcoral", color="red"))
    axes[1, 1].set_title("Box Plot per Materia")
    axes[1, 1].set_xlabel("Materia")
    axes[1, 1].set_ylabel("Voti")

 #aumento per titolo attaccato
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()

# Dictionary
    class_statistics = {
        "student_averages": student_averages,
        "subject_averages": subject_averages,
        "class_average": class_average,
        "student_std": student_std_dev,
        "subject_std": subject_std_dev,
        "class_std": class_std,
        "highest_performing_student": highest_performing_student,
        "lowest_performing_student": lowest_performing_student,
        "subject_ranges": subject_ranges,
    }

    print(class_statistics)




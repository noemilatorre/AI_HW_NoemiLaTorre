import string
import re
from collections import Counter

def count_words(text: str) -> dict:
    """
    Count frequency of each word in text
    Args:
        text: Input string
    Returns:
        Dictionary with word frequencies
    """
    # Rimuovo la punteggiatura con regex
    text_no_punctuation = re.sub(r'[^\w\s]', '', text)

    text_lower = text_no_punctuation.lower()

    # Uso Counter per contare le occorrenze
    word_counts = Counter(text_lower.split())

    print("Parole Totali:", sum(word_counts.values()))

    return word_counts



def find_longest_word(text: str) -> str:
    """
    Find the longest word in text
    Args:
        text: Input string
    Returns:
        Longest word found
    """
    # Rimuovo la punteggiatura nel testo xon regex
    cleaned_text = re.sub(r'[^\w\s]', '', text)

    # Splitto il testo in parole
    words = cleaned_text.split()

    # Verifico se ho percorso tutte le parole
    if not words:
        return ""

    return max(words, key=len)


def format_sentences(text: str) -> list:
    """
    Split text into sentences and capitalize first letter
    Args:
        text: Input string
    Returns:
        List of formatted sentences
    """

    # Rimuovo le nuove linee
    text = text.replace("\n", "")

    # Sostituisco spazi multipli con un singolo spazio
    text = re.sub(r"\s\s+", " ", text)

    # Divido il testo in frasi
    sentence_pattern = r'[^.!?]*[.!?]'  # uso un pattern per le frasi che terminano così
    sentences = re.findall(sentence_pattern, text)

    # Capitalizzo la prima lettera di ogni frase
    formatted_sentences = []
    for sentence in sentences:
    # Rimuovo ulteriori spazi laterali
        stripped_sentence = sentence.strip()
        capitalized_sentence = stripped_sentence.capitalize()
        formatted_sentences.append(capitalized_sentence)

    return formatted_sentences






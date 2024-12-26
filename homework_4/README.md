# Homework 4
## Progetto di Algoritmi Genetici

### Descrizione del Problema
Un servizio di consegna cibo deve ottimizzare i suoi percorsi di consegna. Il problema include:
- 5 punti di consegna con coordinate specifiche
- Una cucina centrale (deposito) in posizione (0,0)
- Finestre temporali per ogni consegna
- Condizioni del traffico variabili durante il giorno

### Obiettivo
Sviluppare un algoritmo genetico che trovi il percorso ottimale per minimizzare:
- Distanza totale percorsa
- Violazioni delle finestre temporali
- Impatto del traffico

### Struttura del Progetto
```
delivery_optimization/
├── delivery_ga.py           # Implementazione base dell'algoritmo genetico
├── my_delivery_optimizer.py # File da modificare (implementazione studente)
└── main.py                 # Script principale per l'esecuzione
```

### File da Modificare
Nel file `my_delivery_optimizer.py`, dovrai implementare:
1. `decode_chromosome()`: Converti il cromosoma binario in un percorso
2. `calculate_fitness()`: Calcola il valore di fitness della soluzione

### Dati Forniti
- Coordinate delle consegne
- Finestre temporali per ogni consegna
- Moltiplicatori del traffico per diverse fasce orarie
- Velocità media del veicolo
- Tempo di servizio per consegna

### Suggerimenti per l'Implementazione

#### Rappresentazione del Cromosoma
1. Considera di utilizzare:
   - Bits per ordinare le località
   - Bits per rappresentare i tempi di partenza
   - Una lunghezza appropriata del cromosoma

#### Funzione Fitness
1. Fattori da considerare:
   - Distanza totale del percorso
   - Penalità per consegne fuori dalla finestra temporale
   - Effetto delle condizioni del traffico
   - Tempo totale del percorso

#### Suggerimenti Generali
- Inizia con una rappresentazione semplice e poi migliorala
- Testa il codice con percorsi brevi
- Usa i metodi helper forniti
- Verifica che le soluzioni rispettino i vincoli

### Note Aggiuntive
- Il codice base gestisce già:
  - Selezione dei genitori
  - Crossover
  - Mutazione
  - Visualizzazione
  - Evoluzione della popolazione

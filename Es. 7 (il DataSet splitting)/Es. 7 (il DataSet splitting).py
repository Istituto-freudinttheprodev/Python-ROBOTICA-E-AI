#!/usr/bin/env python
# coding: utf-8

# Per poter iniziare questa esercitazione, è necessario installare la libreria "numpy" attraverso il comando qui sotto incollandolo sul terminale di Windows (CMD) per Python "classico" o su una cella di Notebook Jupyter se si sta programmando Python lì, questa libreria permette di gestire diverse operazioni matematiche che di norma Python non riuscirebbe ad eseguire.

# In[ ]:


pip install numpy


# # L'APERTURA E LA LETTURA DI UN FILE CSV (COMMA SEPARATED VALUES)

# In questo codice viene mostrato come importare da una cartella specifica del PC un file CSV e poi successivamente come leggerlo (tramite la funzione "pd.read_csv"). Infine il programma stampa anche le prime righe del DataFrame utilizzando il metodo "(df.head())" e attraverso l'attributo "shape" si possono visualizzare le proprietà del file, cioè il numero di righe (1017) e il numero di colonne (18). Inoltre quando si parla di DataFrame i rispettivi termini di colonna e riga rappresentano le Feature e le istanze.

# In[1]:


import pandas as pd # per la gestione dei DataFrame
import numpy as np  # per la gestione delle diverse operazioni matematiche
import matplotlib.pyplot as plt # per la creazione di grafici

# Specificare il percorso del file CSV
percorsofilecsv="C:\\Users\\matte\\OneDrive - Scuola Paritaria S. Freud SRL\\Desktop\\FREUD\\2D\\QUADERNI E ALTRO\\ROBOTICA ED AI\\ESERCIZI IN CLASSE PYTHON\\pokemons.csv"
# Leggere il file CSV in un DataFrame
df=pd.read_csv(percorsofilecsv) # per i file CSV si scrive "csv" nel pd.read
# Mostrare le prime righe del DataFrame
print(df.head()) # (df.head()) stampa solo le prime righe (istanze) del DataFrame 
df.shape # visualizza le proprietà del DataFrame, quindi il numero totale di righe (istanze) e di colonne (Feature)


# # L'APERTURA E LA LETTURA DI UN FILE XLSX (FILE "ORIGINALE" DI EXCEL)

# Questo codice è equivalente a quello precedente tranne il fatto che in questo caso si sta importando un file XLSX (file classico di un Cartel di Excel).
# In questo programma viene inserito anche il parametro "sheet_name" della funzione "pd.read_excel" che permette di leggere un particolare foglio del Cartel in questione, in questo caso il foglio di nome "09-10".

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Specificare il percorso del file XLSX
percorsofileExcel="C:\\Users\\matte\\OneDrive - Scuola Paritaria S. Freud SRL\\Desktop\\FREUD\\2D\\QUADERNI E ALTRO\\ROBOTICA ED AI\\ESERCIZI IN CLASSE PYTHON\\serieA.xlsx"
# Leggere il file XLSX in un DataFrame
df=pd.read_excel(percorsofileExcel, sheet_name='09-10') # per i file XLSX si scrive "excel" nel pd.read, il nome del programma
# Mostrare le prime righe del DataFrame
print(df.head())


# Qui sotto vengono mostrare tutte le righe dell'ultimo DataFrame importato usando "df".

# In[4]:


# Stampare tutte le righe del DataFrame
df


# Per poter continuare con questa esercitazione, è necessario installare la libreria "os" attraverso il comando qui sotto incollandolo sul terminale di Windows (CMD) per Python "classico" o su una cella di Notebook Jupyter se si sta programmando Python lì, questa libreria permette di gestire i path di sistema (percorsi file)

# In[ ]:


pip install os


# # L'APERTURA E LA LETTURA DI UNA CARTELLA E DI UN COLLEGAMENTO FILE

# In questo programma viene spiegato come aprire e leggere i diversi file all'interno di una cartella (in questo caso solo CSV) per poi poterli unire in un unico DataFrame. Inizialmente viene creata una lista di cui conterrà tutti i DataFrame dei file CSV (un DataFrame per ogni CSV), poi successivamente viene specificato il percorso della cartella (path). A questo punto per automatizzare al meglio il processo di unione dei file CSV in unico DataFrame viene usato un ciclo for con una condizione al suo interno. Nel dettaglio il ciclo for in questione crea una "lista" (non salvata in una variabile) con tutti i nomi dei file nella cartella con la funzione "os.listdir()", in modo che ad ogni iterazione l'indice "nomedelfile" assume un diverso nome di file. Prima che "nomedelfile" assume un nuovo valore, il ciclo for segue una condizione: se "nomedelfile" finisce con ".csv" allora quest'ultimo viene letto e aggiunto alla lista "listadataframes" creata all'inizio del codice appositamente. 

# In[5]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Creare variabile della lista dei DataFrame
listadataframes=[]
# Specificare il percorso della cartella
percorsofilecartella="C:\\Users\\matte\\OneDrive - Scuola Paritaria S. Freud SRL\\Desktop\\FREUD\\2D\\QUADERNI E ALTRO\\ROBOTICA ED AI\\ESERCIZI IN CLASSE PYTHON\\serieAnuovo"
for nomedelfile in os.listdir(percorsofilecartella): # os.listdir crea una lista contenente tutti i nomi dei file
    # Si inserisce una condizione che permette di selezionare solo un determinato file all'interno di una cartella
    if nomedelfile.endswith(".csv"): # endswith(".csv") significa che il file deve terminare con .csv, quindi tutti e solo i file della cartella che terminano con questa estensione file
        percorsofilecsv=os.path.join(percorsofilecartella, nomedelfile)#join unisce entrambe le variabili dentro la parentesi
        df=pd.read_csv(percorsofilecsv)
        listadataframes.append(df)
print(listadataframes)


# # IL CONTEGGIO DEI DATI DI UN DATAFRAME 

# Il comando qui sotto permette di sapere il numero di DataFrame presenti nella lista "listadataframes". Len è l'acronimo di "length" cioè lunghezza.

# In[15]:


len(listadataframes)


# Il comando "len(listadataframes[23])" permette al programma di contare il numero di istanze (righe) all'interno del DataFrame n°23.

# In[16]:


len(listadataframes[23])


# Invece il comando "len(listadataframes[23].columns)" permette al programma di contare il numero di colonne (Feature) all'interno del DataFrame n°23. Quindi riassumendo: se si desidera sapere il numero istanze basta indicare il nome della lista e il numero del singolo DataFrame, invece se si desidera sapere il numero di Feature bisogna aggiungere l'attributo ".columns".

# In[17]:


len(listadataframes[23].columns)


# Il comando sottostante legge il DataFrame scelto dall'utente via input. Bisogna sottolineare il fatto che su Python l'indice (cioè la numerazione) parte dal numero 0 infatti sono 23 gli effettivi DataFrame e non 24 come stampava l'output di un codice precedente, in ogni caso il numero 24 è giusto se si inizia a contare dal numero 1 e non dallo 0.

# In[23]:


DataFramescelto=int(input("Quale DataFrame si desidera visualizzare? "))
print("Eccolo qua!!!")
listadataframes[DataFramescelto]


# Infatti se si prova ad inserire un numero pari a 24 o superiore il programma darà errore durante la ricerca del DataFrame. L'errore in questione è: "IndexError: list index out of range" cioè che per l'appunto l'indice è fuori portata della lista (in questo caso si riferisce alla lista "listadataframes").

# In[24]:


DataFramescelto=int(input("Quale DataFrame si desidera visualizzare? "))
print("Eccolo qua!!!")
listadataframes[DataFramescelto]


# Per poter continuare questa esercitazione, è necessario installare la libreria "sklearn" attraverso il comando qui sotto incollandolo sul terminale di Windows (CMD) per Python "classico" o su una cella di Notebook Jupyter se si sta programmando Python lì, questa libreria permette di gestire diverse operazioni di Machine Learning.

# In[ ]:


pip install sklearn


# # LO SPLITTING DATASET E LE VISUALIZZAZIONI DEI DATI IN GRAFICI

# Questo codice è un vero e proprio esempio di "Dataset Splitting". Quest'ultimo incomincia con l'importazione delle librerie "numpy" e "sklearn", nel dettaglio quando si importa la libreria "sklearn" viene usata una formattazione particolare: from viene utilizzato per indicare il nome della libreria mentre con il comando import viene importata una sola parte della libreria. Nella vera parte di codice invece viene prima definito il random seed, che crea dei dati randomici che non cambiano ad ogni esecuzione del codice poichè il seme (per l'appunto il seed) è impostato a 0 altrimenti se non fosse specificato cambierebbe di volta in volta e si genererebbero così numeri casuali ogni volta diversi. Poi nella riga sotto vengono creati i veri e propri dati randomici (usando sempre np.random.) delle altezze usando una distribuzione Gaussiana (o normale) con il valore medio di 160 cm (picco della Gaussiana) e con la deviazione standard di 10 cm (cioè che permette di definire il range ad alta probabilità del valore delle altezze, quindi nel range ci sono solo i valori più comuni che sono: da 150 cm a 170 cm). Infine viene anche indicato il numero 100 che definisce il numero di dati totali che dovranno essere generati casualmente dal programma. Nella riga successiva viene indicata la formula con cui vengono calcolati i dati dei pesi, in quest'ultima viene sempre usata la distribuzione normale per generare dei dati randomici nello stesso modo di prima ma con valori diversi. È importante sottolineare il fatto che i valori sia delle altezze che dei pesi fanno parte adesso di un unico DataSet creato. A questo punto non rimane altro che iniziare a splittare (dividere in due parti non uguali) sia i valori delle altezze che quelli dei pesi, questo perchè è necessario avere un dataset di Training (70%) e uno di Test (30%). La differenza tra i dati Training e i dati di Test è che i primi vengono esclusivamente utilizzati per allenare il modello finale, invece quelli di Test svolgono il compito di testare il modello (usando per l'appunto valori diversi dalla fase di Training). Alla fine per riassumere un po' il tutto vengono stampate le dimensioni dei dati di Training e di Test.

# In[2]:


import numpy as np
from sklearn.model_selection import train_test_split # in questo caso viene solo importata una parte di libreria poichè è strettamente necessaria quella determinata funzione

# Creare dati casuali per altezze: variabile indipendente = input (cioè quello che mi serve per fare delle previsioni) e sono le Feature nel DataSet 
# Pesi sono la variabile dipendente = output (cioè ciò che voglio prevedere) del DataSet
np.random.seed(0)
altezze = np.random.normal(160, 10, 100) # la variabile "altezze" è indipendente, cioè non ha una formula in cui viene denominata un'altra variabile
# Formula di esempio:
pesi = 0.5 * altezze + np.random.normal(0, 5, 100) # la variabile "pesi" è dipendente, cioè ha una formula in cui viene denominata un'altra variabile

# Previsione del modello: dal valore delle altezze prevedere il peso

# Suddividere il dataset in training set (70%) e test set (30%) formando due DataSet
X_train, X_test, y_train, y_test = train_test_split(altezze, pesi, test_size=0.3, random_state=42) # riprendendo la formula di prima: le X sono i valori delle altezze perchè sono le Feature del DataSet, cioè l'input. Invece le Y sono gli output del DataSet, cioè i valori dei pesi. "test_size=0.3" vuol dire che il DataSet di Test è il 30% di quello totale mentre random_state sceglie in modo randomico i valori del DataSet per il Training e il Test
# Stampare le dimensioni dei training set e test set
print("Dimensioni del Training Set (altezze e pesi):", X_train.shape, y_train.shape) # shape = dimensione dei DataSet di Training
print("Dimensioni del Test Set (altezze e pesi):", X_test.shape, y_test.shape) # shape = dimensione dei DataSet di Test


# Questo output particolare qui sotto non è altro che l'array di tutti i 100 valori che rappresentano altezze generate casualmente secondo la distribuzione Gaussiana nel codice di prima, con una media di 160 cm e una deviazione standard di 10 cm. Ogni valore dell'array corrisponde all'altezza di una persona esempio nel dataset. Inoltre nel codice per fare la "prova del 9" in fondo alla stampa dell'array è stato fatto stampare il numero totale di elementi dell'array tramite il comando "shape" che infatti è pari a 100, come descritto all'inizio.

# CURIOSITÀ: il comando "shape" stampa sempre un valore all'interno di una parentesi tonda insieme ad una virgola posta sempre alla fine del numero prima della chiusura della parentesi finale. Questo perchè a dir la verità il comando "shape" è stato progettato per le matrici e non per gli array. Le matrici sono degli array ma che si sviluppano non solo in larghezza (asse x) ma anche in altezza (asse y), definendo così più valori contemporaneamente. Si può e solitamente si usa questo comando anche per gli array perchè funziona correttamente, con il fatto però che quando Python non trova i dati dell'asse y lascierà uno spazio vuoto mantenendo così la virgola. Gli array si possono quindi definire unidimensionali mentre le matrici bidimensionali.

# In[22]:


# Stampare l'array delle altezze
print("Array delle altezze:")
print(altezze)
# Dimensione dell'array
dimensione = altezze.shape
print("La grandezza dell'array delle altezze è di:", dimensione)


# Il codice sottostante è un'altro esempio di Dataset Splitting. La struttura è perlopiù identica al codice precedente riguardo la creazione dei dati e il Dataset Splitting. L'unica differenza con il codice precedente è il grafico finale sulla relazione tra le visite del sito e l'importo delle vendite. Da come si può notare, c'è una relazione di tipo lineare. Ovviamente si può subito notare come ci sia più o meno una diretta proporzionalità tra la variabile dipendente (visite al sito) e quella indipendente (importo vendite), infatti all'aumentare delle visite al sito aumenta anche l'importo delle vendite. Il fatto che non sia perfettamente lineare è dovuto al rumore generato dalla gaussiana nella formula finale (cioè quella dell'importo vendite). Il rumore è quel "disturbo" o variazione imprevista nei dati sull'importo delle vendite (in questo caso), è come un'imprevista interferenza che può rendere l'andamento dei dati meno lineare, in questo caso è proprio "np.random.normal()" a creare questa interferenza creando dei dati randomici attraverso una distribuzione Gaussiana

# In[6]:


import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Creazione di dati casuali per visite al sito web e importo delle vendite
# Creare dati casuali per le visite al sito: variabile indipendente = input (cioè quello che mi serve per fare delle previsioni) e sono le Feature nel DataSet 
# L'importo delle vendite sono la variabile dipendente = output (cioè ciò che voglio prevedere) del DataSet
np.random.seed(0)
visite_al_sito = np.random.randint(100, 1000, 1000) # la variabile "visite al sito" è indipendente, cioè non ha una formula in cui viene denominata un'altra variabile. "np.random.randint(100, 1000, 1000)" vuol dire che vengono creati dei valori randomici, sempre attraverso la libreria numpy. Si legge: il primo parametro (100) indica il valore minimo che può assumere il numero mentre il secondo parametro (1000) indica il valore massimo, infine il terzo parametro (1000) indica il numero di valori da generare
importo_vendite = 50 + 0.2 * visite_al_sito + np.random.normal(0, 10, 1000) # la variabile "importo delle vendite" è dipendente, cioè ha una formula in cui viene denominata un'altra variabile
# Suddivisione del dataset in training set (70%) e test set (30%)
X_train, X_test, y_train, y_test = train_test_split(visite_al_sito, importo_vendite, test_size=0.3, random_state=42) # riprendendo la formula di prima: le X sono i valori delle visite al sito perchè sono le Feature del DataSet, cioè l'input. Invece le Y sono gli output del DataSet, cioè i valori degli importi vendite. "test_size=0.3" vuol dire che il DataSet di Test è il 30% di quello totale mentre random_state sceglie in modo randomico i valori del DataSet per il Training e il Test

# Previsione del modello: dal valore delle visite al sito prevedere l'importo vendite

# Creazione di un grafico a dispersione
plt.figure(figsize=(10, 6)) # dimensione del grafico
plt.scatter(X_train, y_train, label='Training Set', color='blue', alpha=0.7) # label è il nome della legenda, alpha è il valore della trasparenza: più è vicino ad 0 come valore i pallini del grafico saranno più trasparenti
plt.scatter(X_test, y_test, label='Test Set', color='orange', alpha=0.7)
plt.xlabel('Numero di Visite al Sito')
plt.ylabel('Importo delle Vendite')
plt.title('Relazione tra Visite al Sito e Importo delle Vendite')
plt.legend()
plt.grid(True)
plt.show()
# Stampare le dimensioni dei training set e test set
print("Dimensioni del Training Set (visite al sito e importo delle vendite):", X_train.shape, y_train.shape)
print("Dimensioni del Test Set (visite al sito e importo delle vendite):", X_test.shape, y_test.shape)


# Il codice sottostante è un'altro esempio di Dataset Splitting. La struttura è perlopiù identica al codice precedente riguardo la creazione dei dati e il Dataset Splitting. L'unica differenza con il codice precedente è il grafico finale sulla relazione tra i mesi trascorsi e peso corporeo. Da come si può notare, c'è una relazione sempre di tipo lineare ma ben diversa dal codice precedente. Infatti si può subito notare come ci sia più o meno una proporzionalità diretta ma negativa, quindi non inversa come si può pensare. Rispetto al codice di prima l'output viene stampato in maniera decrescente ma è pur sempre lineare, infatti non viene un'iperbole. Quindi il grafico va letto nel modo in cui all'aumentare della variabile indipendente (mesi trascorsi) diminuisce la variabile dipendente (peso corporeo). Il fatto che non sia perfettamente lineare è dovuto al rumore, generato dalla gaussiana nella formula finale (cioè quella del peso corporeo).

# In[9]:


import numpy as np #da sistemare
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Creazione di dati casuali per mesi trascorsi e peso corporeo
# Creare dati casuali per i mesi trascorsi: variabile indipendente = input (cioè quello che serve per fare delle previsioni) e sono le Feature nel DataSet 
# Il peso corporeo è la variabile dipendente = output (cioè ciò che bisogna prevedere) del DataSet
np.random.seed(0)
n=120 # è un parametro, non è una variabile ed è molto comodo in quanto se si cambia quello si cambia tutto ciò "collegato" ad esso
mesi_trascorsi = np.arange(1, n+1) #la variabile "visite al sito" è indipendente, cioè non ha una formula in cui viene denominata un'altra variabile. "np.arange(1, n+1)" serve per generare un array di numeri interi da 1 a n, inclusi, che rappresentano i singoli mesi nel periodo di osservazione.
peso_corporeo = 70 - 0.2 * mesi_trascorsi + np.random.normal(0, 2, n)

# Suddivisione del dataset in training set (75%) e test set (25%)
X_train, X_test, y_train, y_test = train_test_split(mesi_trascorsi, peso_corporeo, test_size=0.25, random_state=42)

# Creazione di un grafico a linee
plt.figure(figsize=(10, 6)) #dimesioni del grafico
plt.plot(X_train, y_train, label='Training Set', marker='o', color='blue', linestyle='', markersize=8,alpha=0.7) # label è il nome della legenda, alpha è il valore della trasparenza: più è vicino ad 0 come valore i pallini del grafico saranno più trasparenti
plt.plot(X_test, y_test, label='Test Set', marker='s', color='orange', linestyle='', markersize=8,alpha=0.7)
plt.xlabel('Mesi Trascorsi')
plt.ylabel('Peso Corporeo (kg)')
plt.title('Analisi dei Dati di Fitness')
plt.legend()
plt.grid(True)
plt.show()

# Stampare le dimensioni dei training set e test set
print("Dimensioni del Training Set (mesi trascorsi e peso corporeo):", X_train.shape, y_train.shape)
print("Dimensioni del Test Set (mesi trascorsi e peso corporeo):", X_test.shape, y_test.shape)


# Nel codice sottostante vengono creati direttamente due DataSet: uno di Training e uno di Test. Entrambi i dataset vengono creati con valori randomici nella prima parte del codice. Poi nella seconda parte vengono creati i due grafici, quello blu rappresenta la distribuzione di età nel Training Set e quello arancione rappresenta la distrubuzione di età nel Test Set. Per creare grafici viene usata la libreria "matplotlib".

# In[10]:


import numpy as np
import matplotlib.pyplot as plt

# Creazione di dati casuali per età
np.random.seed(0)
eta_training_set = np.random.randint(18, 60, 300)#"np.random.randint(100, 1000, 1000)" vuol dire che vengono creati dei valori randomici, sempre attraverso la libreria numpy. Si legge: il primo parametro (100) indica il valore minimo che può assumere il numero mentre il secondo parametro (1000) indica il valore massimo, infine il terzo parametro (1000) indica il numero di valori da generare
eta_test_set = np.random.randint(18, 60, 100)
# Confronto delle distribuzioni di età
# Primo grafico
plt.figure(figsize=(12, 6)) #dimesioni del grafico
plt.subplot(1, 2, 1) # permette di creare all'interno di una figura più plot
plt.hist(eta_training_set, bins=20, color='blue', alpha=0.7) # crea un istogramma, bins vuole indicare la barre verticali cioè i cosidetti "bins"
plt.title('Distribuzione di Età nel Training Set')
plt.xlabel('Età')
plt.ylabel('Frequenza')
# Secondo grafico
plt.subplot(1, 2, 2)
plt.hist(eta_test_set, bins=20, color='orange', alpha=0.7)
plt.title('Distribuzione di Età nel Test Set')
plt.xlabel('Età')
plt.ylabel('Frequenza')
plt.tight_layout()
plt.show()


# # LO SPLITTING DATASET CON LE CLASSI

# Questo codice è molto simile a quelli mostrati sopra, infatti vengono inserite le librerie numpy e sklearn e poi vengono generati in maniera randomica i valori di x e y. Questo codice introduce il concetto di classi, infatti l'array y ha presente ben due classi.  Le classi sono le categorie a cui appartengono i dati, come "cane" o "gatto", in questo codice le classi sono A e B. Lo "split stratificato" è come dividere i dati in modo da mantenere la stessa proporzione di categorie in entrambe le parti. Questo è importante quando ci sono più di una categoria come in questo caso e così ci si può assicurare che il modello le impari da entrambi, quindi sia dalla classe A che quella B. Uno split normale non tiene conto di questo, quindi potrebbe dare al modello un'idea sbagliata delle categorie. Quindi, lo split stratificato aiuta il modello a imparare meglio perchè assicura che ciascuna categoria sia rappresentata in modo equo sia nel set di dati di addestramento che in quello di test. Ciò significa che il modello avrà l'opportunità di imparare da esempi di entrambe le categorie, migliorando la sua capacità di generalizzazione e di prendere decisioni accurate su nuovi dati. Infatti nei dati stampati alla fine i valori sono simili perchè lo split stratificato ha "equiparato" all'incirca le proporzioni tra il Test e il Training

# In[2]:


from sklearn.model_selection import train_test_split
import numpy as np

np.random.seed(3)
# Supponiamo di avere un dataset con feature X e target y
X = np.random.rand(100, 2)  # Dati del dataset (100 campioni, 2 feature)
y = np.random.choice(['A', 'B'], size=100)  # Etichette di classi casuali (categorie), size è la grandezza
print("I valori di x sono:")
print(X)
print("I valori di y sono:")
print(y)

# Calcola le proporzioni delle classi nel dataset originale
proporzione_classe_A = sum(y == 'A') / len(y)
proporzione_classe_B = 1 - proporzione_classe_A

# Eseguire uno split stratificato con una proporzione specificata
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Calcola le proporzioni delle classi nel training set e nel test set
proporzione_classe_A_train = sum(y_train == 'A') / len(y_train)
proporzione_classe_B_train = 1 - proporzione_classe_A_train

proporzione_classe_A_test = sum(y_test == 'A') / len(y_test)
proporzione_classe_B_test = 1 - proporzione_classe_A_test

# Stampa delle proporzioni
print("Proporzione Classe A nel Data Set:", proporzione_classe_A)
print("Proporzione Classe B nel Data Set:", proporzione_classe_B)
print("Proporzione Classe A nel Training Set:", proporzione_classe_A_train)
print("Proporzione Classe B nel Training Set:", proporzione_classe_B_train)
print("Proporzione Classe A nel Test Set:", proporzione_classe_A_test)
print("Proporzione Classe B nel Test Set:", proporzione_classe_B_test)


# Nel grafico sottostante vengono stampati i valori del DataSet, anche qua infatti si può notare un equiparazione dovuta allo split stratificato:

# In[27]:


import matplotlib.pyplot as plt
# Etichette delle classi
labels=["Classe A", "Classe B"]
# Colori delle fette del grafico
colors = ['gold', 'lightcoral']
# Crea un grafico a torta con etichette
plt.pie([proporzione_classe_A, proporzione_classe_B], labels=labels, colors=colors, autopct='%1.1f%%')#si usa pie perchè in questo caso è un grafico a torta
plt.title('Proporzione delle Classi nel DataSet')
plt.show()


# Il grafico qui sotto riguarda invece il Training Set:

# In[3]:


import matplotlib.pyplot as plt
# Etichette delle classi
labels=["Classe A", "Classe B"]
# Colori delle fette del grafico
colors = ['gold', 'lightcoral']
# Crea un grafico a torta con etichette
plt.pie([proporzione_classe_A_train, proporzione_classe_B_train], labels=labels, colors=colors, autopct='%1.0f%%')#si usa pie perchè in questo caso è un grafico a torta
plt.title('Proporzione delle Classi nel Training Set')
plt.show()


# Il grafico qui sotto riguarda invece il Test Set:

# In[32]:


# Crea un grafico a torta con etichette
plt.pie([proporzione_classe_A_test, proporzione_classe_B_test], labels=labels, colors=colors, autopct='%1.1f%%')#si usa pie perchè in questo caso è un grafico a torta
plt.title('Proporzione delle Classi nel Test Set')
plt.show()


# Il codice sottostante genera un grande DataSet di dati contenente 24 milioni di numeri casuali compresi tra 0 e 100. Dopodiché, viene estratto un campione casuale di dimensione circa il 30% del totale. Successivamente, calcola la media e la deviazione standard di questo campione casuale. La media è il valore medio dei numeri nel campione, mentre la deviazione standard indica quanto i numeri nel campione si discostano dalla media. Infine, calcola la media e la deviazione standard per l'intero dataset. La media è il valore medio di tutti i numeri nel dataset, mentre la deviazione standard indica quanto i numeri nel dataset si discostano dalla media. Alla fine il codice stampa i seguenti risultati: la media e la deviazione standard del campione casuale, e la media e la deviazione standard del dataset completo.

# In[33]:


import random
import numpy as np

dataset=[]
# Creazione di un dataset di 1000 elementi (ad esempio, dati casuali)
popolazione =24000000
for i in range(popolazione):
    dataset.append(random.randint(0, 100000))
    
campione = int(round(0.3 * popolazione))# Estrazione di un campione casuale semplice dal dataset
campione_casuale = random.sample(dataset, campione)

# Calcolo della media e della deviazione standard del campione
media_campione = np.mean(campione_casuale)
deviazione_standard_campione = np.std(campione_casuale)

# Calcolo della media e della deviazione standard del dataset completo
media_dataset = np.mean(dataset)
deviazione_standard_dataset = np.std(dataset)

print(f"Media del campione casuale: {media_campione: .2f}")
print(f"Deviazione standard del campione casuale: {deviazione_standard_campione: .2f}")
print(f"Media del dataset completo: {media_dataset: .2f}")
print(f"Deviazione standard del dataset completo: {deviazione_standard_dataset: .2f}")


# Questo codice utilizza la libreria pandas per creare un DataFrame contenente una colonna chiamata "ColonnaAB" con una distribuzione specificata tra le categorie 'A' e 'B'. Per prima cosa, il codice imposta un seed per la riproducibilità dei risultati. Poi, definisce il numero totale di elementi nel DataFrame (100.000) e la percentuale di elementi della categoria 'A' (0.7). Successivamente, utilizza la funzione np.random.choice per generare una colonna di lunghezza num_elementi con distribuzione desiderata tra le categorie 'A' e 'B', specificata attraverso il parametro p, dove p è una lista di probabilità associate a ciascuna categoria. Infine, crea il DataFrame utilizzando la libreria pandas, assegnando alla colonna il nome 'ColonnaAB' e la visualizza.

# In[34]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Impostare il seed per la riproducibilità
np.random.seed(42)
# Numero totale di elementi nel DataFrame
num_elementi = 100000
# Percentuale di "A"
percentuale_A = 0.7
# Generare la colonna con distribuzione desiderata
colonna = np.random.choice(['A', 'B'], size=num_elementi, p=[percentuale_A, 1 - percentuale_A])

# Creare il DataFrame
df = pd.DataFrame({'ColonnaAB': colonna})
df


# Questo codice crea tre sottoinsiemi (subset) del DataFrame originale, ciascuno con dimensioni simili.
# 
# Per prima cosa, crea subset1 e lo inizializza estraendo casualmente un terzo dei dati dal DataFrame originale utilizzando il metodo sample(frac=1/3). Successivamente, rimuove gli indici dei dati presenti in subset1 dal DataFrame originale utilizzando il metodo drop(). Poi, crea subset2 e ripete il processo, estraendo casualmente la metà dei dati rimasti nel DataFrame originale e rimuovendoli dal DataFrame. Infine, subset3 è costituito dai dati rimanenti nel DataFrame originale dopo aver creato subset1 e subset2.

# In[37]:


# Creare tre subset di dimensioni simili
subset1 = df.sample(frac=1/3)
df = df.drop(subset1.index)

subset2 = df.sample(frac=1/2)
df = df.drop(subset2.index)

subset3 = df  # L'ultimo subset con il rimanente


# Qua sotto vengono stampati i grafici esplicativi:

# In[38]:


# Calcolare le percentuali di "A" e "B" per ogni subset
percentuali_subset1 = subset1['ColonnaAB'].value_counts(normalize=True)
percentuali_subset2 = subset2['ColonnaAB'].value_counts(normalize=True)
percentuali_subset3 = subset3['ColonnaAB'].value_counts(normalize=True)

# Creare i grafici a torta
fig, axs = plt.subplots(3, 1, figsize=(6, 12))

# Subset 1
axs[0].pie(percentuali_subset1, labels=percentuali_subset1.index, autopct='%1.1f%%', startangle=90)
axs[0].set_title('Subset 1')

# Subset 2
axs[1].pie(percentuali_subset2, labels=percentuali_subset2.index, autopct='%1.1f%%', startangle=90)
axs[1].set_title('Subset 2')

# Subset 3
axs[2].pie(percentuali_subset3, labels=percentuali_subset3.index, autopct='%1.1f%%', startangle=90)
axs[2].set_title('Subset 3')

# Mostrare il grafico
plt.show()


# In[39]:


# Dividere ciascun subset in training set e test set
train_subset1, test_subset1 = train_test_split(subset1, test_size=0.2, random_state=42)
train_subset2, test_subset2 = train_test_split(subset2, test_size=0.2, random_state=42)
train_subset3, test_subset3 = train_test_split(subset3, test_size=0.2, random_state=42)

# Creare il grafico con 6 torte
fig, axs = plt.subplots(3, 2, figsize=(10, 12))

# Funzione per disegnare una torta con etichette
def draw_pie(ax, data, title):
    ax.pie(data, labels=data.index, autopct='%1.1f%%', startangle=90)
    ax.set_title(title)

# Prima riga di torte (Subset 1)
draw_pie(axs[0, 0], train_subset1['ColonnaAB'].value_counts(normalize=True), 'Train Subset 1')
draw_pie(axs[0, 1], test_subset1['ColonnaAB'].value_counts(normalize=True), 'Test Subset 1')

# Seconda riga di torte (Subset 2)
draw_pie(axs[1, 0], train_subset2['ColonnaAB'].value_counts(normalize=True), 'Train Subset 2')
draw_pie(axs[1, 1], test_subset2['ColonnaAB'].value_counts(normalize=True), 'Test Subset 2')

# Terza riga di torte (Subset 3)
draw_pie(axs[2, 0], train_subset3['ColonnaAB'].value_counts(normalize=True), 'Train Subset 3')
draw_pie(axs[2, 1], test_subset3['ColonnaAB'].value_counts(normalize=True), 'Test Subset 3')

# Regolare lo spaziamento tra i subplots
plt.tight_layout()

# Mostrare il grafico
plt.show()


# In[40]:


np.random.seed(41)

# Creare il DataFrame originale
num_elementi = 1000
percentuale_A = 0.7
colonna = np.random.choice(['A', 'B'], size=num_elementi, p=[percentuale_A, 1 - percentuale_A])
df = pd.DataFrame({'ColonnaAB': colonna})

# Creare tre subset di dimensioni simili
subset1 = df.sample(frac=1/3)
df = df.drop(subset1.index)

subset2 = df.sample(frac=1/2)
df = df.drop(subset2.index)

subset3 = df  # L'ultimo subset con il rimanente

# Dividere ciascun subset in training set e test set
train_subset1, test_subset1 = train_test_split(subset1, test_size=0.2, stratify=subset1['ColonnaAB'], random_state=42)
train_subset2, test_subset2 = train_test_split(subset2, test_size=0.2, stratify=subset2['ColonnaAB'], random_state=42)
train_subset3, test_subset3 = train_test_split(subset3, test_size=0.2, stratify=subset3['ColonnaAB'], random_state=42)

# Creare il grafico con 6 torte
fig, axs = plt.subplots(3, 2, figsize=(10, 12))

# Funzione per disegnare una torta con etichette
def draw_pie(ax, data, title):
    ax.pie(data, labels=data.index, autopct='%1.1f%%', startangle=90)
    ax.set_title(title)

# Prima riga di torte (Subset 1)
draw_pie(axs[0, 0], train_subset1['ColonnaAB'].value_counts(normalize=True), 'Train Subset 1')
draw_pie(axs[0, 1], test_subset1['ColonnaAB'].value_counts(normalize=True), 'Test Subset 1')

# Seconda riga di torte (Subset 2)
draw_pie(axs[1, 0], train_subset2['ColonnaAB'].value_counts(normalize=True), 'Train Subset 2')
draw_pie(axs[1, 1], test_subset2['ColonnaAB'].value_counts(normalize=True), 'Test Subset 2')

# Terza riga di torte (Subset 3)
draw_pie(axs[2, 0], train_subset3['ColonnaAB'].value_counts(normalize=True), 'Train Subset 3')
draw_pie(axs[2, 1], test_subset3['ColonnaAB'].value_counts(normalize=True), 'Test Subset 3')

# Regolare lo spaziamento tra i subplots
plt.tight_layout()

# Mostrare il grafico
plt.show()


# In[41]:


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns

# Impostare il seed per la riproducibilità
np.random.seed(41)

# Creare il DataFrame originale
num_elementi = 1000
percentuale_A = 0.7
colonna = np.random.choice(['A', 'B'], size=num_elementi, p=[percentuale_A, 1 - percentuale_A])
df = pd.DataFrame({'ColonnaAB': colonna})

# Numero di subset desiderato
num_subset = 5

# Creare i subset di dimensioni simili
subset_list = []
for i in range(num_subset):
    subset = df.sample(frac=1/num_subset)
    df = df.drop(subset.index)
    subset_list.append(subset)

# Creare il grafico con 2 torte per ognuno dei N subset
fig, axs = plt.subplots(num_subset, 2, figsize=(10, 2*num_subset))

# Iterare attraverso i subset e disegnare le torte
for i, subset in enumerate(subset_list):
    # Dividere ciascun subset in training set e test set
    train_set, test_set = train_test_split(subset, test_size=0.2, random_state=42) # posso aggiungere stratify=subset['ColonnaAB']

    # Prima colonna: Training Set
    draw_pie(axs[i, 0], train_set['ColonnaAB'].value_counts(normalize=True), f'Train Subset {i + 1}')

    # Seconda colonna: Test Set
    draw_pie(axs[i, 1], test_set['ColonnaAB'].value_counts(normalize=True), f'Test Subset {i + 1}')

# Regolare lo spaziamento tra i subplots
plt.tight_layout()

# Mostrare il grafico
plt.show()


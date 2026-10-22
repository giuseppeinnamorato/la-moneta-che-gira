# La moneta che gira

**Viaggio al centro del computer quantistico**
di Giuseppe Innamorato · prima edizione, novembre 2026

Prendi una moneta, mettila in piedi sul tavolo e falla girare. Finché gira non è né testa né croce: è un'altra cosa, che i fisici hanno impiegato un secolo a capire. Su quella cosa si sta costruendo il computer quantistico.

Questo libro è un viaggio verso il fondo del «lampadario», la macchina dorata che tiene i qubit a quindici millesimi di grado sopra lo zero assoluto. Un piano alla volta, senza formule difficili, scoprirai come si fanno girare le monete, che cosa può fare davvero un computer quantistico e che cosa no, e come riconoscere le promesse gonfiate.

Per studenti delle superiori, curiosi di ogni età e chiunque voglia capire che cosa c'è dietro i titoli dei giornali.

## Scarica il libro

📖 **[Scarica il libro in PDF](https://github.com/giuseppeinnamorato/la-moneta-che-gira/releases/latest/download/La.moneta.che.gira.pdf)** (9 MB)

📦 **[Scarica libro e materiali in un unico file zip](https://github.com/giuseppeinnamorato/la-moneta-che-gira/releases/latest/download/la-moneta-che-gira.zip)** (7 MB, consigliato): dentro ci sono il PDF e la cartella `materiali`, già sistemati. Estrai lo zip e apri il PDF: i riquadri «Prova tu» aprono il simulatore con un clic.

Tutte le versioni sono nella pagina delle [Release](https://github.com/giuseppeinnamorato/la-moneta-che-gira/releases).

## Una copia di carta?

Il libro è e resterà gratuito in digitale. Se però ti piacerebbe averlo anche su carta, da sfogliare, sottolineare o lasciare in biblioteca a scuola, fammelo sapere: se le richieste saranno abbastanza, lo pubblicherò su Amazon in versione cartacea, al prezzo più basso possibile.

Scrivimi a ginnamorato1961@gmail.com, oppure lascia una ⭐ al repository: per me è un segnale che il libro è servito.

## Il simulatore

🪙 **[Apri il simulatore online](https://giuseppeinnamorato.github.io/la-moneta-che-gira/materiali/simulatore.html)**, senza scaricare niente, anche dal telefono.

Fa girare fino a tre monete quantistiche con le mosse X, H, Z e CNOT, mostra le freccette prima della mano, ferma le monete da 10 a 1.000 volte e ha un cursore per il disturbo. Ogni capitolo ha il suo esperimento pronto.

Nella versione scaricata il simulatore è il file `materiali/simulatore.html`: si apre con un doppio clic, funziona anche senza connessione, e nei riquadri «Prova tu» del libro basta un clic per arrivare all'esperimento giusto. Il pulsante «Torna al libro», in alto, riapre il PDF alla pagina da cui eri partito; nel simulatore online diventa «Apri il libro». Con Chrome conviene il Ctrl-clic (⌘-clic sul Mac), così il simulatore si apre in una nuova scheda.

Perché tutto funzioni, il PDF e la cartella `materiali` devono stare uno accanto all'altra, e il PDF non va rinominato.

## Il programma del capitolo 12

`materiali/gemelli.py` è l'«Hello World» dei computer quantistici: la ricetta dei gemelli scritta con [Qiskit](https://www.ibm.com/quantum/qiskit).

```
pip install qiskit qiskit-aer
python gemelli.py
```

Dovresti vedere qualcosa come `{'00': 507, '11': 493}`: i numeri cambiano ogni volta, le coppie diverse non compaiono mai.

## Il viaggio

| Piano | Temperatura | Parte |
|---|---|---|
| 1 | 300 K | La moneta sul tavolo |
| 2 | 50 K | Le mosse |
| 3 | 4 K | Il mondo reale |
| 4 | 800 mK | La lingua dei qubit |
| 5 | 100 mK | La guerra al rumore |
| 6 | 15 mK | Il fondo |

Diciassette capitoli, 136 domande di verifica con le risposte, glossario, cronologia e una cassetta degli attrezzi per continuare.

## Licenza

Il libro e i materiali sono distribuiti con licenza [Creative Commons Attribuzione – Non commerciale – Non opere derivate 4.0 Internazionale](https://creativecommons.org/licenses/by-nc-nd/4.0/deed.it) (CC BY-NC-ND 4.0): vedi [LICENSE.md](LICENSE.md).

In parole semplici: puoi leggerlo, copiarlo e passarlo a chi vuoi, e puoi usarlo liberamente in attività didattiche e formative gratuite, a condizione di citare l'autore. Non puoi usarlo per scopi commerciali, né distribuirne versioni modificate. Per usi diversi (un corso a pagamento, una traduzione, un adattamento) basta chiedere all'autore: ginnamorato1961@gmail.com

**Come citarlo:** Giuseppe Innamorato, *La moneta che gira. Viaggio al centro del computer quantistico*, 2026. Licenza CC BY-NC-ND 4.0.

## Dello stesso autore

*[Dentro la macchina](https://archive.org/details/dentro-la-macchina-21-settembre-2026)*, 2026: il primo viaggio, dentro un modello linguistico. Si legge gratuitamente su archive.org.

# Sveglia
Una semplice sveglia fatta tramite libraria time e pygame.
Organizzata in due funzioni:
 1. **def suono_sveglia(filepath)** prende il filepath del suono e tramite la libreria pygame lo apre e lo avvia
 2. **def sveglia(filepath)** riceve come argomento il filepath dell'audio mp3,successivamente prende minuti e ora
      in input e controlla se sono validi, dopodichè li unisce in una stringa f"{ora}:{minuti}".
      Con la libreria time prende l'ora attuale e la converte nel formato HH:MM, e se l'ora locale è uguale a all'ora precedentemente
      impostata, richiamo la funzione suono_sveglia(filepath) e faccio suonare la sveglia per 45 secondi  

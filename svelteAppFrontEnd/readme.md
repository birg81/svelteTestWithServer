# svelte app

Questo è un project template per app [Svelte](https://svelte.dev).
Può essere scaricato dal sito [https://github.com/sveltejs/template/](https://github.com/sveltejs/template/).

È stato creato partendo dal template [degit](https://github.com/Rich-Harris/degit):

## Cosa fa questa WebApp

Questa WebApp ha lo scopo di mostrare il funzionamento di Svelte e mostrare come questi dialoga con i diversi back-end attraverso webAPI.
Nello specifico sono stati sviluppati due back-end, uno in FastAPI (sulla porta ```4000```) e un altro in Java Sprint Web (sulla porta ```3000```); (ed inultima istanza è stato creato anche un altro di tipo Stream Socket sulla porta ```12345```), questi mettono a disposizione una rotta all'indirizzo ```/api/people``` la quale restituisce a sua volta una risposta in formato JSON del tipo

```json
	[
	{
		"firstname": "Jhon",
		"lastname": "Doe",
		"gender": "male"
	},
	{
		"firstname": "Jhane",
		"lastname": "Doe",
		"gender": "female"
	}
]
```

Ricevuti questi dati la pagina principale stampa i nominativi riceuti.

### Attenzione!

Per far si che le richieste verso i back-end vadano a buon fine, bisogna questi abbiano abialitato i [CORS](https://it.wikipedia.org/wiki/Cross-origin_resource_sharing), per far ciò bisogna configurare opportunamente i codici affinché nel header della risposta siano bene presenti queste autorizzazioni.

Gli esempi sono già configurati in modo da aver abilitata questa funzionalità.

## Come Testare il progetto?

In primo luogo è necessario avviare sia il back-end in Spring che quello in FastAPI (opzionalmente lo stream socket) e solo successivamente Svelte (vedi come nelle prossime righe).
Nel caso in cui Svelte non riuscirà a comunicare col back-end verrà mostrato un elenco di 4 persone (2 maschi e 2 femmine), nel caso invece stia comunicando col back-end in Spring scaricherà i nominativi di 4 uomini, se sta comunicando con FastAPI scaricherà i nominativi di 5 donne (se invece sta comunicando col server socket in python scaricherà l'elendo di alcuni giocatori della SSC NAPOLI).
Per impostare che il back-end con qual quale Svelte deve comunicare basta recarsi nel file [App.svelte](./svelteAppFrontEnd/src/App.svelte) e alla riga

```javascript
const response = await fetch('http://localhost:3000/api/people');
```

sostituire il valore della porta con
* ```3000``` in caso di **Spring**
* ```4000``` in caso di **FastAPI**
* (```12345``` di socket server in *Python*)

## Da dove scaricare lo starterpack

Premesso che per creare una webApp è necessario aver installato [Node.js](https://nodejs.org/), attravero questi sarà possibile creare una webApp semplicemente lanciando il comando

```bash
npm create svelte@latest svelte-app
```

o alternativamente

```bash
npx degit sveltejs/template svelte-app
cd svelte-app
```

dove svelte-app il nome della cartella scelta per la creazione dell'app

Questo però portarà dietro con se diverse dipendenze e moltissimi file che di certo potranno confondere un novello sviluppatore; per tanto in maniera alternativa, potrebbe essere una buona soluzione scaricare un template iniziale dal seguente percorso [https://github.com/sveltejs/template/](https://github.com/sveltejs/template/)

Successivamente bisognerà solo avviare la webApp.

## Come avviare l'applicazione

Per avviare l'applicazione basta semplicemente digitare i seguenti comandi

```bash
npm install
npm run dev
```
che servono rispettivamente a:

```bash
npm install
```

Scarica tutte le dipendenze, mentre

```bash
npm run dev
```

avvia l'applicazione.

La configurazione predefinita del template prevede che sulla porta ```8080``` venga avviata la webApp; tale porta potrebbe già essere occupata da altri servizi, per cui potrebbe essere una buona idea modificare il valore della porta predefinita recandosi nel file ```package.json``` e alla riga contenente la proprietà start modificarla nella seguente ```"sirv public --no-clear --host 0.0.0.0 --port 5000"``` in modo da avviare ad esempio l'applicazione sulla porta ```5000``` o volendo direttamente con un qualsiasi valore sceldo dall'utente.
Potrebbe ad esempio essere una buona idea impostare come valore della porta ```80``` o ```443```.
Si faccia però attenzione e si controlli se la porta scelta non è già occupata

### Curiostità:

Grazie allo template scaricato, non bisognerà riavviare Svelte ad ogni modifica del codice del front-end, in quanto ad ogni modifica, il progetto si riavvierà automaticamente!

## Come tenere pulito il progetto?

Prima di effettuare un Push su github eliminare le seguenti cartelle e i seguenti file

```bash
./node_modules
./public/build
./package-lock.json
```

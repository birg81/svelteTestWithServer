# svelte app

Questo è un project template per app [Svelte](https://svelte.dev).
Può essere scaricato dal sito [https://github.com/sveltejs/template/](https://github.com/sveltejs/template/).

È stato creato partendo dal template [degit](https://github.com/Rich-Harris/degit):


## Da dove scaricare lo starterpack

Per creare un'applicazione svelte si può semplicemente lanciare il comando

```bash
npm create svelte@latest svelte-app
```

o alternativamente

```bash
npx degit sveltejs/template svelte-app
cd svelte-app
```

dove svelte-app il nome della cartella scelta per la creazione dell'app

Questo però porta dietro diverse dipendenze e moltissimi file che possono confondere, in maniera alternativa e decisamente più compatta si può scaricare un template iniziale dal seguente percorso ([https://github.com/sveltejs/template/]https://github.com/sveltejs/template/)

## Come avviare l'applicazione

```bash
npm install
npm run dev
```

De default ciò avvia la SPA su una porta predefinita, la porta ```8080```, per modificarla basta recarsi nel file ```package.json``` e relativamente alla riga contenente la proprietà start modificarla nella seguente ```"sirv public --no-clear --host 0.0.0.0 --port 5000"``` in modo da avviare ad esempio l'applicazione sulla porta 5000 o volendo direttamente sulla porta ```80``` o ```443```

## Come funziona?

```bash
npm install
```

Scarica tutte le dipendenze, mentre

```bash
npm run dev
```

avvia l'applicazione.

Grazie allo starterpack scaricato, non bisognerà riavviare svelte ad ogni modifica del codice, in quanto modificando i file, il progetto si riavvierà da solo!


## Come tenere pulito il progetto?

Prima di effettuare un Push su github eliminare le seguenti cartelle e i seguenti file

```bash
./node_modules
./public/build
./package-lock.json
```
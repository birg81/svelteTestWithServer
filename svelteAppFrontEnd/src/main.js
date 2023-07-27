import App from './App.svelte';

const app = new App({
	target: document.body,
	props: {
		// proprietà
		author: 'Biagio Rosario Greco'
	}
});

export default app;
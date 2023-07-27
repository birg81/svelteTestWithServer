<script>
	import { onMount } from 'svelte';
	export let author;
	export let plist = [
		{
			firstname: 'Gennaro',
			lastname: 'Esposito',
			gender: 'male'
		},
		{
			firstname: 'Antonella',
			lastname: 'Ricciardi',
			gender: 'female'
		},
		{
			firstname: 'Salvatore',
			lastname: 'Sorrentino',
			gender: 'male'
		},
		{
			firstname: 'Marianna',
			lastname: 'De Simone',
			gender: 'female'
		}
	];
	onMount(async () => {
		const response = await fetch('http://localhost:3000/api/people');
		plist = await response.json();
		console.log(plist);
	})
</script>

<main>
	{#each plist as p}
	<p>
		<i>{p.firstname}</i>
		{p.lastname}
		<b>{p.gender == 'male' ? '♂️' : '♀️'}</b>
	</p>
	{/each}
	<h1>Hello {author}!</h1>
	<p>Visit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn how to build Svelte apps.</p>
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}
	h1 {
		color: #547eda;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 250;
	}
	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>
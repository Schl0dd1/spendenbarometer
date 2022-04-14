<script context="module">
	export async function load({ fetch, params }) {
		const id = params.id;
		const res = await fetch(`http://localhost:8000/api/konten/${id}`);
		const konto = await res.json();
		//console.log(konto);
		if (res.ok) {
			return {
				props: {
					konto
				}
			};
		}
		return {
			status: res.status,
			error: new Error('Konto nicht gefunden')
		};
	}
</script>

<script>
	import Buchung from '../components/Buchung.svelte';
	import BuchungForm from '../components/BuchungForm.svelte';
	import Button from '../components/Button.svelte';
	import { goto } from '$app/navigation';

	export let konto;

	let showAll = false;

	//funktioniert:
	const deleteKonto = async (konto_id) => {
		console.log(konto_id);
		let text = 'Willst du dieses Konto unwiderruflich löschen?';
		if (confirm(text) === true) {
			// filteredKonten = filteredKonten.filter((konto) => konto.id != konto_id);
			// console.log(filteredKonten);
			const res = await fetch(`http://localhost:8000/api/konten/${konto_id}/`, {
				method: 'DELETE',
				headers: {
					'Content-Type': 'application/json'
					// 'Access-Control-Allow-Origin': '*'
				},
				body: JSON.stringify({
					konto_id
				})
			});
			await goto('/');
			return;
			// location.reload();
		}
	};

	export const createBuchung = async (e) => {
		let data = e.detail;
		console.log(e);
		console.log(data);
		const res = await fetch('http://localhost:8000/api/buchungen/', {
			method: 'POST',
			credentials: 'include',
			headers: {
				'Content-Type': 'application/json'
				// 'Access-Control-Allow-Origin': '*'
			},
			body: JSON.stringify({
				data
			})
		});
		console.log('went thgrouh');
		//location.reload();
	};
</script>

<h1 class="text-3xl font-bold">{konto.kontoname}</h1>
<h1 class="text-3xl font-bold text-right">{konto.kontostand} €</h1>
<h2 class="text-xl font-bold">Neuer Eintrag:</h2>
<BuchungForm {konto} on:create-buchung={createBuchung} />
{#each konto.buchungen as buchung, i}
	{#if !showAll}
		{#if i < 3}
			<Buchung {buchung} index={buchung.id} />
		{/if}
	{/if}
	{#if showAll}
		<Buchung {buchung} index={buchung.id} />
	{/if}
{/each}
<Button text="show All" color="bg-green-400" on:click={() => (showAll = !showAll)} />
<Button text="delete Account" on:click={() => deleteKonto(konto.id)} />

<script context="module">
	export async function load({ fetch, params }) {
		const id = params.id;
		const res = await fetch(`http://localhost:8000/api/konten/${id}`, {
			headers: {
				'Access-Control-Allow-Origin': '*'
			}
		});
		const konto = await res.json();
		if (res.ok) {
			return {
				props: {
					konto
				}
			};
		}
		return {
			status: 301,
			//error: new Error('Konto nicht gefunden')
			redirect: '/'
		};
	}
</script>

<script>
	import Buchung from '../components/Buchung.svelte';
	import BuchungForm from '../components/BuchungForm.svelte';
	import Button from '../components/Button.svelte';
	import { goto } from '$app/navigation';
	import Graph from '../components/graph.svelte';

	export let konto;

	let showAll = false;

	//funktioniert:
	const deleteKonto = async (konto_id) => {
		console.log(konto_id);
		let text = 'Willst du dieses Konto unwiderruflich löschen?';
		if (confirm(text) === true) {
			// filteredKonten = filteredKonten.filter((konto) => konto.id != konto_id);
			// console.log(filteredKonten);
			const res = await fetch(`http://localhost:8000/api/konten/${konto_id}`, {
				method: 'DELETE',
				headers: {
					'Content-Type': 'application/json',
					'Access-Control-Allow-Origin': '*'
				},
				body: JSON.stringify({
					konto_id
				})
			});
			await goto('/');
			return;
		}
	};

	//funktioniert:
	export const createBuchung = async (e) => {
		let data = e.detail;
		console.log(e);
		console.log(data);
		const res = await fetch('http://localhost:8000/api/buchungen/', {
			method: 'POST',
			credentials: 'include',
			headers: {
				'Content-Type': 'application/json',
				'Access-Control-Allow-Origin': '*'
			},
			body: JSON.stringify({
				data
			})
		});
		location.reload();
	};

	//geht das auch kürzer?
	const kontostand = () => {
		let e_list = konto.buchungen.filter((buchung) => buchung.einnahme === true);
		let e = e_list
			.map((buchung) => buchung.betrag)
			.reduce((prev, curr) => parseFloat(prev) + parseFloat(curr), 0);
		let a_list = konto.buchungen.filter((buchung) => buchung.einnahme === false);
		let a = a_list
			.map((buchung) => buchung.betrag)
			.reduce((prev, curr) => parseFloat(prev) + parseFloat(curr), 0);
		let sum = (e - a).toFixed(2);
		return sum;
	};
</script>

<div class="text-right"><Button on:click={() => goto('/')} text="<< zur Übersicht" /></div>
<div class="flex justify-between my-5">
	<h1 class="text-3xl font-bold">{konto.kontoname}</h1>
	<h1 class="text-3xl font-bold text-right">{kontostand()} €</h1>
</div>

<h2 class="text-xl font-bold">Neuer Eintrag:</h2>
<BuchungForm {konto} on:create-buchung={createBuchung} />
<div class="my-25"><Graph kontostand={kontostand()} /></div>

{#each konto.buchungen.reverse() as buchung, i}
	{#if !showAll}
		{#if i < 3}
			<Buchung {buchung} index={buchung.id} />
		{/if}
	{/if}
	{#if showAll}
		<Buchung {buchung} index={buchung.id} />
	{/if}
{/each}
<Button text="alle Einträge" color="bg-green-500" on:click={() => (showAll = !showAll)} />
<Button text="Konto löschen" on:click={() => deleteKonto(konto.id)} />

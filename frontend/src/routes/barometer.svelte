<script>
	import { buchungen, konten } from '../stores/data_store';
	import Graph from '../components/graph.svelte';
	import BuchungForm from '../components/BuchungForm.svelte';
	// import { konto } from './[id].svelte';

	let handleSubmit = () => {
		console.log('submit');
	};
	let betrag;
	let memberId;

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
	const kontostand = (konto) => {
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

{#each $konten as konto}
	<div class="text-center ">
		<Graph kontostand={kontostand(konto.id)} text="geplante Direktkredite" />
		<BuchungForm konto={konto.id} on:create-buchung={createBuchung} />
	</div>
{/each}

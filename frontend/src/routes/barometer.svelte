<script>
	import { buchungen, konten } from '../stores/data_store';
	import Graph from '../components/graph.svelte';
	import BuchungForm from '../components/BuchungForm.svelte';
	// import { konto } from './[id].svelte';

	//let konto;
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
	const kontostand = (k) => {
		// 	let e_list = k.buchungen.filter((buchung) => buchung.einnahme === true);
		// 	let e = e_list
		// 		.map((buchung) => buchung.betrag)
		// 		.reduce((prev, curr) => parseFloat(prev) + parseFloat(curr), 0);
		// 	let a_list = k.buchungen.filter((buchung) => buchung.einnahme === false);
		// 	let a = a_list
		// 		.map((buchung) => buchung.betrag)
		// 		.reduce((prev, curr) => parseFloat(prev) + parseFloat(curr), 0);
		// 	let sum = (e - a).toFixed(2);
		// 	return sum;
		return 'Kontostand';
	};
</script>

<h1 class="text-4xl m-auto mb-6 text-center">Spendenbarometer</h1>
<div class="flex justify-around">
	{#each $konten as konto}
		<div class="text-center ">
			<Graph kontostand={kontostand(konto)} text={konto.kontoname} />
			<BuchungForm konto={konto.id} on:create-buchung={createBuchung} />
		</div>
	{/each}
</div>

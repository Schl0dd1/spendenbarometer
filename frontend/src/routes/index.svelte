<script>
	import KontoCard from '../components/KontoCard.svelte';
	import CreateNewAccount from '../components/createNewAccount.svelte';

	import { konten, buchungen } from '../stores/data_store';

	// fetch data from data_store:
	let filteredKonten = [...$konten];
	let filteredBuchungen = [...$buchungen];

	//neue Buchung in db anlegen:
	const createBuchung = async (e) => {
		let data = e.detail; //Object{id:,buchungsbetrag:,einnahme:}
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
	};

	//kontostand in db updaten:

	//Konto löschen
	const deleteKonto = async (e) => {
		let konto_id = e.detail;
		console.log(konto_id);
		let text = 'Willst du dieses Konto unwiderruflich löschen?';
		if (confirm(text) == true) {
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
			location.reload();
		}
	};

	//Neues Konto anlegen:
	//fetch erzeugen, dass ein post auf api-konten macht
	const createKonto = async (e) => {
		let data = e.detail;
		console.log(data); // Object { kontoname: "inputvalue"}
		const res = await fetch('http://localhost:8000/api/konten/', {
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
		location.reload();
	};

	//kontostand in db updaten:
</script>

<svelte:head><title>Taschengeldapp</title></svelte:head>
<main>
	<div
		class="flex flex-col items-center justify-center h-screen bg-gradient-to-br from-blue-500 to-green-700"
	>
		<h1 class="text-4xl text-center text-white my-6 uppercase">Taschengeldapp</h1>
		<!-- md:grid-cols-1 to -2/-3 angabe, wie viel container in einer reihe sein sollen -->
		<div class="py-4 grid gap-4 md:grid-cols-1 grid-cols-1">
			{#each $konten as konto (konto.id)}
				<KontoCard
					kontoname={konto.kontoname}
					kontostand={konto.kontostand}
					{konto}
					on:delete-konto={deleteKonto}
					on:update-konto={createBuchung}
				/>
			{/each}
		</div>

		<CreateNewAccount on:create-konto={createKonto} />
	</div>
</main>

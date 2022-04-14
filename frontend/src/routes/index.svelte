<script>
	import KontoCard from '../components/KontoCard.svelte';
	import CreateNewAccount from '../components/createNewAccount.svelte';
	import { konten, buchungen } from '../stores/data_store';
	import KontoListElement from '../components/KontoListElement.svelte';
	import BuchungenList from '../components/BuchungenList.svelte';

	// fetch data from data_store:
	let filteredKonten = [...$konten];
	let filteredBuchungen = [...$buchungen];

	//kontostand in db updaten:

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
</script>

<svelte:head><title>Taschengeldapp</title></svelte:head>
<main>
	<div
		class=" relative overflow-hidden items-center justify-center h-screen -my-8 bg-gradient-to-br from-blue-500 to-green-700"
	>
		<h1 class="text-4xl text-center text-white uppercase py-5">Taschengeldapp</h1>
		<div class="flex justify-center">
			{#each $konten as konto}
				<a href={`/${konto.id}`}>
					<li
						class="flex items-center px-10 mx-5 justify-center shadow-sm shadow-white text-white text-xl border-2 border-white  rounded-lg my-2 py-2 px-4"
					>
						{konto.kontoname}
					</li>
				</a>
			{/each}
		</div>

		<CreateNewAccount on:create-konto={createKonto} />
	</div>
</main>

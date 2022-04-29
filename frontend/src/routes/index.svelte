<script>
	import CreateNewAccount from '../components/createNewAccount.svelte';
	import { buchungen, konten } from '../stores/data_store';

	const createKonto = async (e) => {
		let data = e.detail;
		console.log(data); // Object { kontoname: "inputvalue"}
		const res = await fetch('http://localhost:8000/api/konten/', {
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
</script>

<svelte:head><title>Spendenbarometer</title></svelte:head>
<main>
	<div
		class=" relative overflow-hidden items-center justify-center h-screen -my-8 bg-gradient-to-br from-blue-500 to-green-700"
	>
		<h1 class="text-4xl text-center text-white uppercase py-20">Taschengeld app</h1>
		<h2 class="text-xl text-white text-center py-5">deine Konten:</h2>
		<div class="flex justify-center">
			{#each $konten as konto}{/each}
		</div>

		<CreateNewAccount on:create-konto={createKonto} />
	</div>
</main>

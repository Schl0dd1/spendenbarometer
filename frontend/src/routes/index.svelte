<script>
	import KontoCard from '../components/KontoCard.svelte';
	import CreateNewAccount from '../components/createNewAccount.svelte';

	//durch daten aus datenbank ersetzen:
	let konten = [
		{
			id: 1,
			kontoname: 'Hanni',
			kontostand: 0,
			src_img: '/img/the-bear.webp',
			alle_buchungen: [
				{ id: 1, betrag: 20, beschreibung: 'Taschengeld' },
				{ id: 2, betrag: -1.2, beschreibung: 'Kaugummis' },
				{ id: 3, betrag: -5.0, beschreibung: 'Kino' }
			]
		},
		{
			id: 2,
			kontoname: 'Nanni',
			kontostand: 30,
			src_img: '/img/the-cat.webp',
			alle_buchungen: []
		}
	];

	const deleteKonto = (e) => {
		let konto_id = e.detail;
		let text = 'Willst du dieses Konto unwiderruflich löschen?';
		if (confirm(text) == true) {
			konten = konten.filter((konto) => konto.id != konto_id);
		}
	};

	const createKonto = (e) => {
		let neuesKonto = e.detail;
		neuesKonto.id = konten.length + 1;
		konten = [e.detail, ...konten];
		console.log(konten);
	};
</script>

<h1 class="text-4xl text-center my-8 uppercase">Taschengeldapp</h1>
<svelte:head><title>Taschengeldapp</title></svelte:head>

<div class="py-4 grid gap-4 md:grid-cols-2 grid-cols-1">
	{#each konten as konto (konto.id)}
		<KontoCard
			kontoname={konto.kontoname}
			kontostand={konto.kontostand}
			src={konto.src_img}
			alle_buchungen={konto.alle_buchungen}
			{konto}
			on:delete-konto={deleteKonto}
		/>
	{/each}
</div>

<CreateNewAccount on:create-konto={createKonto} />

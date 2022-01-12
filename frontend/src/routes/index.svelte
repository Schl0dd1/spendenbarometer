<script>
	import KontoCard from '../components/KontoCard.svelte';

	//durch daten aus datenbank ersetzen:
	let k1 = {
		kontoname: 'Hanni',
		kontostand: 0,
		src_img: '../img/the-bear.webp'
	};
	let k2 = {
		kontoname: 'Nanni',
		kontostand: 30,
		src_img: '../img/the-the-cat.webp'
	};
</script>

<h1 class="text-4xl text-center my-8 uppercase">Taschengeldapp</h1>
<svelte:head><title>Taschengeldapp</title></svelte:head>

<div class="py-4 grid gap-4 md:grid-cols-2 grid-cols-1">
	<!-- wird später durch each as ersetzt -->
	<KontoCard kontoname={k1.kontoname} kontostand={k1.kontostand} src={k1.src_img} />
	<KontoCard kontoname={k2.kontoname} kontostand={k2.kontostand} src={k2.src_img} />
</div>

<script>
	import KontoCard from '../components/KontoCard.svelte';

	let k1 = {
		kontoname: 'Hanni',
		kontostand: 0
	};
	let k2 = {
		kontoname: 'Nanni',
		kontostand: 30
	};
</script>

<h1 class="text-4xl text-center my-8 uppercase">Taschengeldapp</h1>
<svelte:head><title>Taschengeldapp</title></svelte:head>

<div class="py-4 grid gap-4 md:grid-cols-2 grid-cols-1">
	<!-- wird später durch each as ersetzt -->
	<KontoCard kontoname={k1.kontoname} kontostand={k1.kontostand} />
	<KontoCard kontoname={k2.kontoname} kontostand={k2.kontostand} />
</div>

<script>
	import KontoCard from '../components/KontoCard.svelte';
</script>

<h1 class="text-4xl text-center my-8 uppercase">Taschengeldapp</h1>
<svelte:head><title>Taschengeldapp</title></svelte:head>

<div class="py-4 grid gap-4 md:grid-cols-2 grid-cols-1">
	<!-- wird später durch each as ersetzt -->
	<KontoCard kontoname="Hanni" kontostand="0,00€" />
	<KontoCard kontoname="Nanni" kontostand="20,00€" />
</div>

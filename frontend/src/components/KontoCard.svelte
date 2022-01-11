<script>
	export let kontoname;
	export let kontostand;
	import { fade } from 'svelte/transition';
</script>

<a
	class="list-none p-6 bg-gray-100 text-gray-800 text-center rounded-md shadow-sm hover:shadow-md flex flex-col items-center"
	href={``}
	transition:fade
>
	<img class="h-40" src="../img/the-bird.webp" alt="Foto" />
	<h1 class="uppercase text-2xl">{kontoname}</h1>
	<h2 class="uppercase text-1xl">{kontostand}</h2>
</a>

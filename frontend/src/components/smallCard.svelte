<script>
	export let konto;
	export let kontoname;
	export let kontostand;

	import { createEventDispatcher } from 'svelte';

	const dispatch = createEventDispatcher();
	const toggle = (kontoId) => {
		dispatch('toggle', kontoId);
	};
</script>

<div
	class="list-none p-6 bg-gray-100 text-gray-800 text-center rounded-md shadow-sm hover:shadow-md flex flex-row items-center justify-between border"
>
	<p class="uppercase text-2xl">{kontoname}</p>
	<p class="uppercase text-2xl">{kontostand} €</p>

	<button class="mx-1 text-lg w-6 hover:shadow-md">
		<img
			class="opacity-50"
			src="/icons/pencil.svg"
			alt=""
			on:click={() => toggle(konto.id)}
		/></button
	>
</div>

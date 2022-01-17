<script>
	export let konto;
	import { createEventDispatcher } from 'svelte';

	const dispatch = createEventDispatcher();
	const handleDelete = (kontoId) => {
		dispatch('delete-konto', kontoId);
	};
</script>

<nav class="flex justify-end w-full mx-8 my-4">
	<button class="mx-1 text-lg w-6 hover:shadow-md"> <img src="/icons/pencil.svg" alt="" /></button>
	<button class="mx-3 text-lg w-6 hover:shadow-md">
		<img src="/icons/list-numbered.svg" alt="uebersicht aus- und einnahmen" /></button
	>
	<button class="mx-1 text-lg w-6 hover:shadow-md" on:click={() => handleDelete(konto.id)}>
		<img src="/icons/bin.svg" alt="" /></button
	>
</nav>

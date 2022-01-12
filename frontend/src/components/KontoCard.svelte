<script>
	export let kontoname;
	export let kontostand;
	export let betrag;
	import { fade } from 'svelte/transition';

	function handleClick() {
		kontostand += betrag;
	}
</script>

<div
	class="list-none p-6 bg-gray-100 text-gray-800 text-center rounded-md shadow-sm hover:shadow-md flex flex-col items-center"
	href={``}
	transition:fade
>
	<img class="h-40" src="../img/the-bird.webp" alt="Foto" />
	<div class="mb-3 xl:w-96">
		<label for="exampleNumber0" class="form-label inline-block mb-2 text-gray-700"
			>Gib einen Betrag in € ein:</label
		>
		<input
			type="number"
			class="
            form-control
            block
            w-full
            px-3
            py-1.5
            text-base
            font-normal
            text-gray-700
            bg-white bg-clip-padding
            border border-solid border-gray-300
            rounded
            transition
            ease-in-out
            m-0
            focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none
          "
			id="betrag"
			placeholder="0.00"
			bind:value={betrag}
		/>
	</div>
	<button
		on:click={handleClick}
		class="my-4 bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded"
	>
		Eintrag hinzufügen
	</button>
	<h1 class="uppercase text-2xl">{kontoname}</h1>
	<h2 class="uppercase text-1xl">{kontostand} €</h2>
</div>

<script>
	import { createEventDispatcher } from 'svelte';

	export let konto;
	export let kontoname;
	export let kontostand;
	export let betrag;

	//responsive variable style Kontostand rot-schwarz
	$: style = kontostand < 0 ? 'uppercase text-2xl text-rose-600 mx-4' : 'uppercase text-2xl mx-4';
	let einnahme = null;

	//Delete-Button löscht Konto
</script>

<div
	class=" py-3 bg-gray-100 text-grey-800 text-center rounded-md shadow-sm col-start-2 col-span-10"
>
	<div class=" text-center flex items-center justify-between">
		<p class="uppercase text-2xl mx-5">{kontoname}</p>
		<p class={style}>{kontostand} €</p>

		<button class="mx-2 text-lg w-5 hover:shadow-md" on:click={() => handleDelete(konto.id)}>
			<img class="opacity-50" src="/icons/bin.svg" alt="" /></button
		>
	</div>

	<form on:submit|preventDefault={handleSubmit} class="">
		<label for="betrag" class="mr-5">Neue Buchung:</label>

		<input
			type="number"
			step="0.01"
			class="
					form-control
					flex-auto
					w-1/3
					px-3
					py-1.5
					text-center
					font-normal
					text-grey-700
					bg-white bg-clip-padding
					border border-solid border-gray-300
					rounded
					transition
					ease-in-out
					m-0
					focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none
			  		"
			id="betrag"
			placeholder="Betrag in €"
			bind:value={betrag}
		/>

		<button
			on:click={() => (einnahme = false)}
			type="submit"
			class="my-4 bg-transparent hover:bg-rose-500 text-rose-700 font-semibold hover:text-white py-2 px-4 border border-rose-600 hover:border-transparent rounded"
		>
			Ausgabe
		</button>
		<button
			on:click={() => (einnahme = true)}
			type="submit"
			class="my-4 bg-transparent hover:bg-green-500 text-green-700 font-semibold hover:text-white py-2 px-4 border border-green-600 hover:border-transparent rounded"
		>
			Einnahme
		</button>
	</form>
</div>

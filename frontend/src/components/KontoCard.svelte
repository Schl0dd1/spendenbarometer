<script>
	import Nav from '../components/nav.svelte';
	export let konto;
	export let kontoname;
	export let kontostand;
	export let src;
	export let betrag;
	export let alle_buchungen = [];
	import { fade } from 'svelte/transition';
	import { createEventDispatcher } from 'svelte';
	import { v4 as uuidv4 } from 'uuid';

	const dispatch = createEventDispatcher();
	const handleDelete = (kontoId) => {
		dispatch('delete-konto', kontoId);
	};

	let style = 'uppercase text-2xl';
	let einnahme = false; // let einnahme für spätere datenbankspeicherung:

	let handleUpdate = (e) => {
		const neuerEintrag = {
			id: uuidv4(), //wird überschrieben
			betrag: betrag,
			kontostand: 0,
			beschreibung: '',
			date: Date.now()
		};
		alle_buchungen = [neuerEintrag, ...alle_buchungen];
		betrag = 0;
		style = kontostand < 0 ? 'uppercase text-2xl text-rose-600' : 'uppercase text-2xl';
	};

	function handleClickAusgabe() {
		if (isNaN(betrag)) {
			alert('Gib eine Zahl ein!');
		} else {
			einnahme = false;
			if (betrag < 0) {
				betrag = betrag * -1;
			}
			kontostand -= betrag;
			kontostand = Math.round(kontostand * 100) / 100;
		}
	}

	function handleClickEinnahme() {
		if (isNaN(betrag)) {
			alert('Gib eine Zahl ein!');
		} else {
			einnahme = true;

			if (betrag < 0) {
				betrag = betrag * -1;
			}
			kontostand += betrag;
			kontostand = Math.round(kontostand * 100) / 100;
		}
	}
</script>

<div
	class="list-none p-6 bg-gray-100 text-gray-800 text-center rounded-md shadow-sm hover:shadow-md flex flex-col items-center"
	href={``}
	transition:fade
>
	<nav class="flex justify-end w-full mx-8 my-4">
		<button class="mx-1 text-lg w-6 hover:shadow-md">
			<img class="opacity-50" src="/icons/pencil.svg" alt="" /></button
		>
		<button class="mx-3 text-lg w-6 hover:shadow-md">
			<img
				class="opacity-50"
				src="/icons/list-numbered.svg"
				alt="uebersicht aus- und einnahmen"
			/></button
		>
		<button class="mx-1 text-lg w-6 hover:shadow-md" on:click={() => handleDelete(konto.id)}>
			<img class="opacity-50" src="/icons/bin.svg" alt="" /></button
		>
	</nav>

	<h1 class="uppercase text-2xl">{kontoname}</h1>
	<img class="h-20 mb-4" {src} alt="Foto" />
	<form on:submit|preventDefault={handleUpdate}>
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
				placeholder="0.00"
				bind:value={betrag}
			/>
		</div>
		<div>
			<button
				on:click={handleClickAusgabe}
				type="submit"
				class="my-4 bg-transparent hover:bg-rose-500 text-rose-700 font-semibold hover:text-white py-2 px-4 border border-rose-600 hover:border-transparent rounded"
			>
				Ausgabe
			</button>
			<button
				on:click={handleClickEinnahme}
				type="submit"
				class="my-4 bg-transparent hover:bg-green-500 text-green-700 font-semibold hover:text-white py-2 px-4 border border-green-600 hover:border-transparent rounded"
			>
				Einnahme
			</button>
		</div>

		<h2 class={style}>{kontostand} €</h2>
	</form>
</div>

<style>
</style>

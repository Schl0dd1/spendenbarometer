<script>
	export let konto;
	export let kontoname;
	export let kontostand;
	//export let src;
	export let betrag;
	// export let buchungen = [];
	import { fade } from 'svelte/transition';
	import { createEventDispatcher } from 'svelte';
	//import { v4 as uuidv4 } from 'uuid';

	let style = kontostand < 0 ? 'uppercase text-2xl text-rose-600 mx-4' : 'uppercase text-2xl mx-4';
	let einnahme = null; // let einnahme für spätere datenbankspeicherung:

	const dispatch = createEventDispatcher();
	const handleDelete = (kontoId) => {
		dispatch('delete-konto', kontoId);
	};

	//add eintrag in einträge-array speichern
	const handleSubmit = (e) => {
		const newBuchung = {
			id: konto.id,
			buchungsbetrag: betrag,
			einnahme: einnahme
		};
		dispatch('update-konto', newBuchung);

		if (isNaN(betrag)) {
			alert('Gib eine Zahl ein!');
		} else {
			if (betrag < 0) {
				betrag = betrag * -1; //korrektur, sollte der user "-" mit eintippen
			}
			//kontostand-update:
			einnahme = einnahme ? (kontostand += betrag) : (kontostand -= betrag);
			kontostand = Math.round(kontostand * 100) / 100;
			//zurücksetzten des betrags auf 0, eingegebener betrag beleibt in neuerEintrag gespeichert:
			betrag = null;
			//kontostand rot, sollte er sich im Minus befinden:
			style = kontostand < 0 ? 'uppercase text-2xl text-rose-600 mx-4' : 'uppercase text-2xl mx-4';
		}
	};

	//Pencil-button: eingabefeld zeigen/verstecken:
	let show = false;
	const toggle = () => {
		show = show ? false : true;
	};
</script>

<div
	class=" list-none p-6 bg-gray-100 text-grey-800 text-center rounded-md shadow-sm flex flex-col"
>
	<div class=" text-center flex flex-row items-center justify-between">
		<p class="uppercase text-2xl mx-2">{kontoname}</p>
		<p class={style}>{kontostand} €</p>

		<nav class="flex">
			<button class="mx-2 text-lg w-5 hover:shadow-md">
				<img class="opacity-50" src="/icons/pencil.svg" alt="" on:click={toggle} /></button
			>
			<button class="mx-2 text-lg w-5 hover:shadow-md">
				<img
					class="opacity-50"
					src="/icons/list-numbered.svg"
					alt="uebersicht aus- und einnahmen"
				/></button
			>
			<button class="mx-2 text-lg w-5 hover:shadow-md" on:click={() => handleDelete(konto.id)}>
				<img class="opacity-50" src="/icons/bin.svg" alt="" /></button
			>
		</nav>
	</div>

	{#if show === true}
		<form on:submit|preventDefault={handleSubmit}>
			<div class="mb-3 mt-4 xl:w-96 flex flex-col">
				<label for="betrag" class="form-label text-gray-700 ">Neue Buchung:</label>

				<input
					type="number"
					step="0.01"
					class="
            form-control
			flex-auto
			w-full
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
			</div>
			<div>
				<button
					on:click={() => {
						einnahme = false;
					}}
					type="submit"
					class="my-4 bg-transparent hover:bg-rose-500 text-rose-700 font-semibold hover:text-white py-2 px-4 border border-rose-600 hover:border-transparent rounded"
				>
					Ausgabe
				</button>
				<button
					on:click={() => {
						einnahme = true;
					}}
					type="submit"
					class="my-4 bg-transparent hover:bg-green-500 text-green-700 font-semibold hover:text-white py-2 px-4 border border-green-600 hover:border-transparent rounded"
				>
					Einnahme
				</button>
			</div>
		</form>
	{/if}

	<!-- <div>
		<ul>
			{#each buchungen as buchung}
				<li>{buchung.betrag}}</li>{/each} 
		</ul>
	</div> -->
</div>

<style>
	.glass {
		box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
		backdrop-filter: blur(5px);
		border-radius: 10px;
	}

	/* h1 {
		@apply text-red-500;
	} */
</style>

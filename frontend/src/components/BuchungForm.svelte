<script>
	import { createEventDispatcher } from 'svelte';
	const dispatch = createEventDispatcher();

	export let konto;
	let betrag = null;
	let beschreibung = '';

	const handleSubmit = (e) => {
		const newBuchung = {
			kontoId: konto.id,
			beschreibung: beschreibung,
			betrag: betrag,
			einnahme: true,
			buchungsdatum: Date.now()
		};
		console.log(newBuchung);
		dispatch('create-buchung', newBuchung);

		if (isNaN(betrag)) {
			alert('Gib eine Zahl ein!');
		} else {
			if (betrag < 0) {
				betrag = betrag * -1;
			}
			betrag = null;
			beschreibung = '';
		}
	};
</script>

<form on:submit|preventDefault={handleSubmit}>
	<div class="flex flex-col text-sm mt-10">
		<label class="mb-1 mt-4">Betrag hinzufügen:</label>
		<input
			bind:value={betrag}
			type="number"
			step="100"
			name="betrag"
			placeholder="type in here..."
			class="appearance-none shadow-sm border border-gray-200 p-2 focus:outline-1 focus:border-gray-500 m-auto sm:w-1/4"
		/>
		<label class="mt-4 mb-1">MitgliedsNummer/Name Externe:</label>
		<input
			bind:value={beschreibung}
			type="text"
			name="beschreibung"
			placeholder="type in here..."
			class="appearance-none shadow-sm border border-gray-200 p-2 focus:outline-1 focus:border-gray-500 m-auto sm:w-1/4"
		/>

		<div>
			<button
				type="submit"
				class="py-2 px-6 text-white font-bold text-lg  py-2 my-2 bg-violet-500 shadow-xl rounded"
			>
				Submit
			</button>
		</div>
	</div>
</form>

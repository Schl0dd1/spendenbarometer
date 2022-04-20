<script>
	import { createEventDispatcher } from 'svelte';
	const dispatch = createEventDispatcher();

	export let konto;
	let kontostand;
	let betrag = null;
	let beschreibung = '';
	let einnahme = false;

	const handleSubmit = (e) => {
		const newBuchung = {
			kontoId: konto.id,
			beschreibung: beschreibung,
			betrag: betrag,
			einnahme: einnahme,
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
	<div class="flex flex-col text-sm mb-10">
		<label for="betrag" class="mb-1 mt-4">Betrag:</label>
		<input
			bind:value={betrag}
			type="number"
			step="0.01"
			name="betrag"
			placeholder="type in here..."
			class="appearance-none shadow-sm border border-gray-200 p-2 focus:outline-1 focus:border-gray-500 sm:w-1/3"
		/>
		<label for="todo" class="mt-4 mb-1">Verwendungszweck:</label>
		<input
			bind:value={beschreibung}
			type="text"
			name="beschreibung"
			placeholder="type in here..."
			class="appearance-none shadow-sm border border-gray-200 p-2 focus:outline-1 focus:border-gray-500 md:w-1/2"
		/>
		<div class="mt-2 mb-3">
			<label>
				<input type="radio" bind:group={einnahme} name="scoops" value={false} />
				Ausgabe
			</label>

			<label>
				<input type="radio" bind:group={einnahme} name="scoops" value={true} />
				Einnahme
			</label>
		</div>
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

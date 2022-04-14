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
		<label for="betrag" class="mb-1">Betrag:</label>
		<input
			bind:value={betrag}
			type="number"
			step="0.01"
			name="betrag"
			placeholder="type in here..."
			class="appearance-none shadow-sm border border-gray-200 p-2 focus:outline-1 focus:border-gray-500"
		/>
		<label for="todo" class="mt-2 mb-1">Verwendungszweck:</label>
		<input
			bind:value={beschreibung}
			type="text"
			name="beschreibung"
			placeholder="type in here..."
			class="appearance-none shadow-sm border border-gray-200 p-2 focus:outline-1 focus:border-gray-500"
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

		<button type="submit" class="w-1/4 py-2 my-2 bg-violet-400 shadow-xl rounded"> Submit </button>
	</div>
</form>

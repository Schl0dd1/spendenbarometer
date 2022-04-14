<script>


	import {deleteBuchung} from "../stores/BuchungStore.js";

	export let buchung;

	$: chooose_bgcolor = () => {
		let color;
		if (buchung.einnahme) {
			color = 'bg-green-300';
		} else if (!buchung.einnahme) {
			color = 'bg-rose-300';
		} else {
			color = 'bg-white';
		}
		return color;
	};
</script>

<li
	class={`${chooose_bgcolor()} flex items-center shadow-sm border border-gray-200 rounded-lg my-2 py-2 px-4`}
>
	<span class="flex-1 text-gray-800">
		{buchung.betrag} €
	</span>
	<span class="flex-1 text-gray-800">
		{buchung.beschreibung}
	</span>
	<button
		type="button"
		class="text-sm bg-red-500 hover:bg-red-600 text-white py-1 px-2 rounded focus:outline-none focus:shadow-outline"
		on:click={() => deleteBuchung(buchung.id)}
	>
		Delete
	</button>
</li>

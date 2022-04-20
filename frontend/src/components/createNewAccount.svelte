<script>
	import { v4 as uuidv4 } from 'uuid';
	import { createEventDispatcher } from 'svelte';
	let btnDisabled = true;
	let message = null;
	export let text = '';
	const handleInput = () => {
		if (text.length <= 2) {
			message = 'Name muss mindestens 3 Zeichen haben';
			btnDisabled = true;
		} else {
			message = null;
			btnDisabled = false;
		}
	};
	const dispatch = createEventDispatcher();
	const handleSubmit = (e) => {
		if (text.trim().length > 2) {
			const newKonto = {
				kontoname: text
			};
			dispatch('create-konto', newKonto);
		}
		text = null;
	};
</script>

<form on:submit|preventDefault={handleSubmit}>
	<div
		class="glass py-20 bg-gray-100 text-gray-800 text-center shadow-sm hover:shadow-md absolute bottom-0 w-full"
	>
		<input
			type="text"
			on:input={handleInput}
			bind:value={text}
			placeholder="Kontoname"
			class="
		w-1/3
        px-3
        py-1.5
        text-center
        font-normal
        text-grey-700
        bg-white bg-clip-padding
        border border-solid border-gray-300
        m-3
      "
		/>
		<button
			type="submit"
			disabled={btnDisabled}
			class="bg-transparent hover:bg-blue-500 text-white font-semibold hover:text-blue-500 py-2 px-4 border border-white hover:border-transparent hover:bg-white rounded"
			>Neues Konto anlegen</button
		>
	</div>
	{#if message}
		<div class="message">{message}</div>
	{/if}
</form>

<style>
	.glass {
		background: rgba(255, 235, 233, 0.15);
		box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
		backdrop-filter: blur(5px);
	}
</style>

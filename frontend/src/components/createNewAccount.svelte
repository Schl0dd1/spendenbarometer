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
				id: uuidv4(), //wird überschrieben
				kontoname: text,
				kontostand: 0,
				src_img: '',
				alle_buchungen: []
			};
			dispatch('create-konto', newKonto);
		}
		text = null;
	};
</script>

<form on:submit|preventDefault={handleSubmit}>
	<div
		class="input-group list-none p-6 bg-gray-100 text-gray-800 text-center rounded-md shadow-sm hover:shadow-md flex flex-col items-center"
		href={``}
	>
		<input
			type="text"
			on:input={handleInput}
			bind:value={text}
			placeholder="Kontoname"
			class="
        form-control
        block
        w-2/3
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
        m-3
        focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none
      "
		/>
		<button
			type="submit"
			disabled={btnDisabled}
			class="bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded"
			>Neues Konto anlegen</button
		>
	</div>
	{#if message}
		<div class="message">{message}</div>
	{/if}
</form>

<style>
	/* @tailwind utilities;
	@tailwind base;
	@tailwind components;


	.btn-create {
		@apply .bg-transparent .hover:bg-blue-500 .text-blue-700 .font-semibold .hover:text-white .py-2 .px-4 .border-blue-500 .hover:border-transparent .rounded; 
	}*/
</style>

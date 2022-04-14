<script>

	export let kontostand;
	export let kontoname;
	export let id;
	export let konto_active = null;

	$: style = kontostand < 0 ? 'uppercase text-xl text-rose-600 mx-4' : 'uppercase text-xl mx-4';

	let active = () => {
		konto_active = id
		console.log(konto_active)
	}

</script>

<div
	class=" py-3 bg-gray-100 text-grey-800 text-center rounded-md shadow-sm col-start-2 col-span-4"
>
	<div class=" text-center flex flex-row items-center justify-between">
		<p class="uppercase text-xl mx-2">{kontoname}</p>
		<p class={style}>{kontostand} €</p>
		<button class="mx-5 text-lg w-5 hover:shadow-md">
			<img class="opacity-50" src="/icons/pencil.svg" alt="" on:click={() => active()}>
		</button>

	</div>
</div>
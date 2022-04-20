<script>
	export let text = '';
	export let color = 'bg-violet-500';
</script>

<button
	type="submit"
	on:click
	class={`w-auto py-1 px-4 my-2 ${color} shadow-xl rounded text-white font-bold text-lg `}
>
	{text}
</button>

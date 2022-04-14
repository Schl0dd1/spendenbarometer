<script>
	export let text = '';
	export let color = 'bg-violet-400';
</script>

<button type="submit" on:click class={`w-auto py-2 px-3 my-2 ${color} shadow-xl rounded`}>
	{text}
</button>
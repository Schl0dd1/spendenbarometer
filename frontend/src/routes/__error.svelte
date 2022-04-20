<script context="module">
	export function load({ error }) {
		return {
			props: { message: error.message }
		};
	}
</script>

<script>
	export let message;
</script>

<div class="text-4xl text-blue-500">
	Was ist da los? <a href="/" class="font-bold">Hier</a> gehts zurück zur Übersicht
</div>

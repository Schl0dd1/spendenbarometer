<script context="module">
	import mapTouchToMouseFor from 'svelte-touch-to-mouse';
</script>

<script>
	import ArrowLeft from './icons/ArrowLeft.svelte';

	mapTouchToMouseFor('.mouse');
	const goal = 2000;
	export let text;
	export let kontostand;
	let prozent = (kontostand / (2000 / 100)).toFixed().toString();
	console.log(prozent);
	let fill = `h-[${prozent}%]`;
	fill = 'h-[25%]';
	console.log(fill);

	$: showKontostand = false;
	//$: position = '';

	function showDiv(event) {
		kontostand = true;
		let x = event.clientX;
		let y = event.clientY;
		document.getElementById('mouse').style.marginLeft = x + 'px';
		document.getElementById('mouse').style.marginTop = y + 'px';
	}
</script>

<div class="container text-center ">
	<div class="flex justify-center relative">
		<div class="my-3.5">
			<div class="w-24 items-center m-auto  h-[600px] border relative">
				<div
					on:mousemove={showDiv}
					on:mouseout={() => {
						showKontostand = false;
					}}
					class="w-full bg-green-200 absolute bottom-0 {fill}"
				>
					{#if showKontostand}
						<div id="mouse" class={` absolute`}>{kontostand} €</div>
					{/if}
				</div>
			</div>
		</div>
		<div class="relative h-[600px] w-24 text-sm">
			<div class="absolute left-2 bottom-[548px] font-bold"><ArrowLeft />6.000.000 €</div>
			<div class="absolute left-2 bottom-[448px]"><ArrowLeft /> 5.000.000 €</div>
			<div class="absolute left-2 bottom-[348px]"><ArrowLeft /> 4.000.000 €</div>
			<div class="absolute left-2 bottom-[248px]"><ArrowLeft /> 3.000.000 €</div>
			<div class="absolute left-2 bottom-[148px]"><ArrowLeft /> 2.000.000 €</div>
			<div class="absolute left-2 bottom-[48px]"><ArrowLeft /> 1.000.000 €</div>
		</div>
	</div>
	<div class="mt-6 font-bold text-xl">{text}</div>
</div>

<style>
	.mouse {
		-webkit-touch-callout: none;
		-ms-touch-action: none;
		touch-action: none;
	}
</style>

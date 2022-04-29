<script>
	import ArrowLeft from './icons/ArrowLeft.svelte';

	const goal = 2000;
	export let text;
	export let kontostand;
	let prozent = (kontostand / (2000 / 100)).toFixed().toString();
	console.log(prozent);
	let fill = `h-[${prozent}%]`;
	fill = 'h-[25%]';
	console.log(fill);

	$: showKontostand = false;
</script>

<div class="container text-center ">
	<div class="flex justify-center relative">
		<div class="my-3.5">
			<div class="w-24 items-center m-auto  h-[600px] border relative">
				<div
					on:mouseover={() => {
						showKontostand = true;
					}}
					on:mouseout={() => {
						showKontostand = false;
					}}
					class="w-full bg-green-200 absolute bottom-0 {fill}"
				>
					{#if showKontostand}
						<div class="absolute left-1/3 top-2">{kontostand} €</div>
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

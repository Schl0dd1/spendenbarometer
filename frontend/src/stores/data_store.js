import { writable } from 'svelte/store';

export const konten = writable([]);
const fetchKonten = async () => {
	const url = 'http://127.0.0.1:8000/api/konten/';
	const res = await fetch(url);
	const data = await res.json();
	console.log(data);
	const loadedKonten = data.objects.map((data) => {
		return {
			id: data.id,
			kontoname: data.kontoname,
			kontostand: data.kontostand
		};
	});
	konten.set(loadedKonten);
};

fetchKonten();

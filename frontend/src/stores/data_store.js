import { browser } from '$app/env';
import { writable } from 'svelte/store';

export const konten = writable([]);
const fetchKonten = async () => {
	const url = 'http://localhost:8000/api/konten/';
	const res = await fetch(url, { credentials: 'include' });
	const data = await res.json();
	//console.log(data);
	const loadedKonten = data?.objects?.map((data) => {
		return {
			id: data.id,
			kontoname: data.kontoname,
			kontostand: +data.kontostand
		};
	});
	konten.set(loadedKonten);
};

if (browser) fetchKonten();

export const buchungen = writable([]);
const fetchBuchungen = async () => {
	const url = 'http://localhost:8000/api/buchungen/';
	const res = await fetch(url, { credentials: 'include' });
	const data = await res.json();
	//console.log(data);
	const loadedBuchungen = data?.objects?.map((data) => {
		return {
			id: data.id,
			kontoId: data.kontoId,
			beschreibung: data.beschreibung,
			betrag: data.betrag
		};
	});
	buchungen.set(loadedBuchungen);
};

if (browser) fetchBuchungen();

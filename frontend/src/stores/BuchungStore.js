//neue Buchung in db anlegen:

//Buchung löschen
export const deleteBuchung = async (e) => {
	let buchung_id = e.detail;
	const res = await fetch(`http://localhost:8000/api/buchungen/${buchung_id}/`, {
		method: 'DELETE',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({
			buchung_id
		})
	});
	location.reload();
};

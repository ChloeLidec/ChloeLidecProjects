export async function load() {
	await new Promise((fulfil) => {
		setTimeout(fulfil, 1000);
	});
}
import { games } from './data.js';

export function load() {
	return {
		summaries: games.map((game) => ({
			name: game.name,
			system: game.system,
			year: game.year,
			cover: game.cover
		}))
	};
}

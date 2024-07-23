export async function load() {
	await new Promise((fulfil) => {
		setTimeout(fulfil, 1000);
	});
}
import { characters } from './data.js';

export function load() {
	return {
		summaries: characters.map((character) => ({
			name: character.name,
			story: character.story,
			firstSeenGame: character.firstSeenGame,
			picture: character.picture,
			colors: character.colors
		}))
	};
}
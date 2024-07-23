import { error } from '@sveltejs/kit';
import { games } from '../data.js';

export function load({ params }) {
	const game = games.find((game) => game.name === params.name);

	if (!game) throw error(404);

	return {
		game
	};
}
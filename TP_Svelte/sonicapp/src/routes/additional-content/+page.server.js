export async function load() {
	await new Promise((fulfil) => {
		setTimeout(fulfil, 1000);
	});
}
import { links } from './data.js';

export function load() {
	return {
		summaries: links.map((link) => ({
			name: link.name,
			url: link.url
		}))
	};
}
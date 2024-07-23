<script>
	import Button from "@smui/button";
	import TopAppBar, { Row, Section, Title } from "@smui/top-app-bar";
	let darkTheme = false;

	let prominent = false;
	let dense = false;
	let secondaryColor = false;
</script>

<svelte:head>
	<!-- Dark and Lightmode CSS change-->
	<!-- SMUI Styles -->

	{#if darkTheme}
		<link rel="stylesheet" href="/smui.css" />
		<link rel="stylesheet" href="/smui-dark.css" media="screen" />
	{:else}
		<link rel="stylesheet" href="/smui.css" />{/if}
</svelte:head>
<div class="flexy">
	<div class="top-app-bar-container flexor">
		<TopAppBar
			variant="static"
			{prominent}
			{dense}
			color={secondaryColor ? "secondary" : "primary"}
			style="background-color: blue !important;"
		>
			<Row>
				<Section>
					<Title>Sonic</Title>
					<a class="m-2" href="/"
						><button type="button" class="btn btn-primary"
							>Home</button
						></a
					>
					<a class="m-2" href="/characters" data-sveltekit-preload-data
						><button type="button" class="btn btn-primary"
							>Characters</button
						></a
					>
					<a class="m-2" href="/games" data-sveltekit-preload-data
						><button type="button" class="btn btn-primary"
							>Games</button
						></a
					>
					<a
						class="m-2"
						href="/additional-content"
						data-sveltekit-preload-data
						><button type="button" class="btn btn-primary"
							>Additional Content</button
						></a
					>
				</Section>
				<Section align="end">
					{#if darkTheme}
						<Button on:click={() => (darkTheme = !darkTheme)}
							><svg
								xmlns="http://www.w3.org/2000/svg"
								width="16"
								height="16"
								fill="currentColor"
								class="bi bi-lightbulb"
								viewBox="0 0 16 16"
							>
								<path
									d="M2 6a6 6 0 1 1 10.174 4.31c-.203.196-.359.4-.453.619l-.762 1.769A.5.5 0 0 1 10.5 13a.5.5 0 0 1 0 1 .5.5 0 0 1 0 1l-.224.447a1 1 0 0 1-.894.553H6.618a1 1 0 0 1-.894-.553L5.5 15a.5.5 0 0 1 0-1 .5.5 0 0 1 0-1 .5.5 0 0 1-.46-.302l-.761-1.77a2 2 0 0 0-.453-.618A5.98 5.98 0 0 1 2 6m6-5a5 5 0 0 0-3.479 8.592c.263.254.514.564.676.941L5.83 12h4.342l.632-1.467c.162-.377.413-.687.676-.941A5 5 0 0 0 8 1"
								/>
							</svg></Button
						>
					{:else}
						<Button on:click={() => (darkTheme = !darkTheme)}
							><svg
								xmlns="http://www.w3.org/2000/svg"
								width="16"
								height="16"
								fill="currentColor"
								class="bi bi-moon"
								viewBox="0 0 16 16"
							>
								<path
									d="M6 .278a.77.77 0 0 1 .08.858 7.2 7.2 0 0 0-.878 3.46c0 4.021 3.278 7.277 7.318 7.277q.792-.001 1.533-.16a.79.79 0 0 1 .81.316.73.73 0 0 1-.031.893A8.35 8.35 0 0 1 8.344 16C3.734 16 0 12.286 0 7.71 0 4.266 2.114 1.312 5.124.06A.75.75 0 0 1 6 .278M4.858 1.311A7.27 7.27 0 0 0 1.025 7.71c0 4.02 3.279 7.276 7.319 7.276a7.32 7.32 0 0 0 5.205-2.162q-.506.063-1.029.063c-4.61 0-8.343-3.714-8.343-8.29 0-1.167.242-2.278.681-3.286"
								/>
							</svg></Button
						>
					{/if}
				</Section>
			</Row>
		</TopAppBar>
	</div>
</div>
<slot />

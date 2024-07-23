<script>
    import Souris from "../Souris.svelte"
    import GameCard from "./GameCard.svelte"
    export let data;
</script>
<Souris />

<div class="d-flex flex-row flex-wrap m-3 justify-content-center">
	{#each data.summaries as { name, system,year,cover }}
    <GameCard name={name} year={year} system={system} cover={cover}/>
	{/each}
    </div>
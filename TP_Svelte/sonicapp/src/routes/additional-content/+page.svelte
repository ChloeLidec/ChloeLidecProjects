<script>
    import Souris from "../Souris.svelte"
    import Iframe from "./Iframe.svelte";
    export let data;
</script>
<h1>Videos about Sonic (mostly SA2B)</h1>
<div class="d-flex m-2 justify-content-center align-items-center flex-wrap" style="93vh">
{#each data.summaries as { name, url }}
    <Iframe name={name} url={url}/>
	{/each}</div>

<style>
    h1{
        margin: 2%;
        padding: 2%;
        color: rgb(2, 0, 92);
        border: solid;
        border-radius: 25px;
        background-color:rgb(165, 11, 0);
    }
</style>
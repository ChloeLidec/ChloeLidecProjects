<script>
	export let data;
</script>
<div class="d-flex flex-column justify-content-around m-5 w-100 h-100 align-items-center">
<div class="d-flex flex-row justify-content-around">
<div id="title" class="d-flex flex-column align-self-center m-3">
<h1>{data.game.name}</h1>
<h2>System : {data.game.system}</h2>
<h2>Year : {data.game.year}</h2></div>
<img class="imgcover" src="/src/lib/images/{data.game.cover}" alt="{data.game.name}"/>
</div>
<div id="plot" class="d-flex flex-column m-3 w-75 align-self-center justify-content-center">{@html data.game.plot}</div>
</div>
<style>
	#title{
		padding: 2%;
		background-color: rgb(0, 9, 131);
		border: 0.3em solid;
		border-radius: 25px;
		border-color: rgb(170, 170, 170);
	}
	.imgcover{
		height: 10%;
		width: auto;
	}
	#plot{
		padding: 2%;
		color: rgb(0, 0, 105);
		font-family: Avantgarde, TeX Gyre Adventor, URW Gothic L, sans-serif;
		font-size: larger;
		background-color: rgb(196, 0, 0);
		border: 0.3em solid;
		border-radius: 25px;
		border-color: rgb(63, 63, 63);
	}
</style>
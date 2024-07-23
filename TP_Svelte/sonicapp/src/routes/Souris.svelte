<script>
   import SonicIcon from "$lib/images/sanic.webp"
	import { spring } from 'svelte/motion';

	let coords = spring({ x: 100, y: 100 }, {
		stiffness: 0.1,
		damping: 0.25
	});

	let size = spring(20);

</script>

  
<svg
	id="svgsanic"
	on:mousemove={(e) => {
		coords.set({ x: e.clientX, y: e.clientY });
	}}
	on:mousedown={(e) => {size.set(60);
		if (e.clientY < 30){
			document.getElementById("svgsanic").style = "pointer-events:none;";
			document.getElementById("imagesanic").style = "pointer-events:fill;";
		}
		else{
			document.getElementById("svgsanic").style = "";
			document.getElementById("imagesanic").style = "";
		}
		}
	}
	on:mouseup={() => size.set(20)}
	role="presentation"
	>
	<defs>
		<clipPath id="circleView">
			<circle cx={$coords.x} cy={$coords.y} r=200 fill="#FFFFFF" />
		</clipPath>
	</defs>
	<image 
	id="imagesanic"
	width={$size} 
	height="{$size}"
	x={$coords.x}
	y={$coords.y}
	xlink:href={SonicIcon}
	clip-path="url(#circleView)"
	/>
	
</svg>
<style>
	svg {
		position: absolute;
		width: 100%;
		height: 100%;
		left: 0;
		top: 0;
	}
</style>
<script>
    import Button, { Label } from '@smui/button';
    import Checkbox from '@smui/checkbox';
  import FormField from '@smui/form-field';
    import Souris from "./Souris.svelte"
    import { fade } from 'svelte/transition';
    import { elasticOut } from 'svelte/easing';
    let size = 500;

    let visible = true;

    function spin(node, { duration }) {
        return {
            duration,
            css: (t) => {
                const eased = elasticOut(t);

                return `
                    transform: scale(${eased}) rotate(${eased * 1080}deg);
                    color: hsl(
                        ${Math.trunc(t * 360)},
                        ${Math.min(100, 1000 * (1 - t))}%,
                        ${Math.min(50, 500 * (1 - t))}%
                    );`;
            }
        };
    }
</script>
<main>
<Souris />
<div class="d-flex flex-row" id="divacc">
    <div class="d-flex flex-column m-5 w-50 align-self-center">
        
        <FormField>
            <Checkbox bind:checked={visible} />
            <span slot="label">Sonic</span>
          </FormField>
        {#if visible}
            <div
                class="centered"
                in:spin={{ duration: 8000 }}
                out:fade
            >
                <span id="transition">Sonic! It's no use!</span>
            </div>
        {/if}
    </div>
    <div class="d-flex flex-row m-5 w-50 h-100">
    <div class="d-flex m-2 flex-column">
    <Button on:click={() => {size+=5;}}>
      <Label>Chaos.... BLAST!</Label>
    </Button>
    <Button on:click={() => {size-=5;}}>
        <Label>Chaos.... CONTROL!</Label>
      </Button>
    </div>
      <div id="shadow" style='--size:{size};'></div></div>
</div>
</main>
<style>
    main{
        width: 100%;
        height: 93vh;
        background-image: url("../lib/images/bggreenhill.png");
        background-size:cover;
        background-repeat: no-repeat;
        
    }
    
    #shadow{
		width : calc( var(--size) * 1px );
		height : calc( var(--size) * 1px );
		background-image: url("../lib/images/shadow.png");
        background-repeat: no-repeat;
        background-size:contain;
        opacity:1;
	}
    #transition{
        font-size: 10vh;
    }
    #divacc{
        width: 100%;
        height: 93vh;
    }
</style>
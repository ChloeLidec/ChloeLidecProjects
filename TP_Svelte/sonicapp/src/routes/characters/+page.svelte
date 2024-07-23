<script>
    import Souris from "../Souris.svelte"
    import Character from "./Character.svelte"
    import Drawer, {
      AppContent,
      Content,
      Header,
      Title,
      Subtitle,
    } from '@smui/drawer';
    import Button, { Label } from '@smui/button';
    import List, { Item, Text } from '@smui/list';
    export let data;
   
    let open = false;
    let active = data.summaries[0].name;
   
    function setActive(value) {
      active = value;
    }
</script>
<div class="drawer-container">
    <Drawer variant="dismissible" bind:open>
      <Header>
        <Title>Characters</Title>
        <Subtitle>All the main characters and their story</Subtitle>
      </Header>
      <Content>
        <List>
          {#each data.summaries as { name, story,firstSeenGame,picture,colors }}
          <Item
            href="javascript:void(0)"
            on:click={() => {let namejs = {name}.name; setActive(namejs)}}
            activated={active == {name}.name}
          >
            <Text>{name}</Text>
          </Item>
          {/each}
        </List>
      </Content>
    </Drawer>
   
    <AppContent class="app-content">
      <div>
        <Button on:click={() => (open = !open)}
          ><Label><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-list" viewBox="0 0 16 16">
            <path fill-rule="evenodd" d="M2.5 12a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5m0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5m0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5"/>
          </svg></Label></Button
        >
        {#each data.summaries as { name, story,firstSeenGame,picture,colors }}
            {#if active==name}
            <Character name={name} story={story} firstSeenGame={firstSeenGame} picture={picture} colors={colors} />
            {/if}
          {/each}
        </div>
    </AppContent>
  </div>


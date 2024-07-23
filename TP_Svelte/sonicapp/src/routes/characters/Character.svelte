<script>
  export let name;
  export let story;
  export let firstSeenGame;
  export let picture;
  export let colors;
  let first = colors.first;
  let second = colors.second;
  let third = colors.third;
</script>
<div class="d-flex justify-content-center">
<div class="card-container">
    <div class="card" style="--first:{first};--second:{second};--third:{third}">
    <div class="front-content h-100 w-100 d-flex flex-column align-items-center justify-content-center">
      <p class="m-2 text-center">{name}</p>
      <p class="m-2 text-center">First apparition : {firstSeenGame}</p>
    </div>
    <div class="content">
      <p class="heading">{name}</p>
      <img src="/src/lib/images/{picture}" alt="{name}" style="height: 40%; width:auto;" />
      <div>{@html story}</div>
    </div>
  </div>
  </div></div>
  <style>
    .card-container {
        width: 50%;
        height: 80vh;
        border-radius: 10px;
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
        overflow: hidden;
        margin: 2%;
    }

.card {
  width: 100%;
  height: 100%;
  border-radius: inherit;
  background-color: var(--third);
}

.card .front-content {
  transition: all 0.6s cubic-bezier(0.23, 1, 0.320, 1)
}

.card .front-content p {
  font-size: 32px;
  font-weight: 700;
  opacity: 1;
  background: linear-gradient(-45deg, var(--first) 0%, var(--second) 100% );
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  transition: all 0.6s cubic-bezier(0.23, 1, 0.320, 1)
}

.card .content {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  gap: 10px;
  background: linear-gradient(-45deg, var(--first) 0%, var(--second) 100% );
  color: #e8e8e8;
  padding: 20px;
  line-height: 1.5;
  border-radius: 5px;
  pointer-events: none;
  transform: translatex(96%);
  transition: all 0.6s cubic-bezier(0.23, 1, 0.320, 1);
}

.card .content .heading {
  font-size: 32px;
  font-weight: 700;
}

.card:hover .content {
  transform: translateY(0);
}

.card:hover .front-content {
  transform: translateX(20%);
}

.card:hover .front-content p {
  opacity: 0;
}


  </style>
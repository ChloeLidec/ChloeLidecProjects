<script>
    export let name;
    export let cover;
    export let system;
    export let year;
</script>

 <div class="myCard">
        <div class="innerCard">
            <div class="frontSide">
                <p class="title">{name}</p>
                <p>{year}</p>
            </div>
            <div class="backSide">
              <img class="coverimg" src="/src/lib/images/{cover}" alt="{name}"/>
              <p>{system}</p>
              <a
						class="m-2"
						href="/games/{name}"
						data-sveltekit-preload-data
						><button type="button" class="btn btn-danger"
							>More...</button
						></a
					>
            </div>
        </div>
    </div>
<style>
  .coverimg{
    height:50%;
    width: auto;
  }
.myCard {
  background-color: transparent;
  width: 15%;
  height: 40vh;
  perspective: 1000px;
  margin: 1%;
}

.title {
  font-size: x-large;
  text-align: center;
  margin: 0;
  color: rgb(3, 3, 168);
}

.innerCard {
  position: relative;
  width: 100%;
  height: 100%;
  text-align: center;
  transition: transform 0.8s;
  transform-style: preserve-3d;
  cursor: pointer;
}

.myCard:hover .innerCard {
  transform: rotateY(180deg);
}

.frontSide,
.backSide {
  position: absolute;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-evenly;
  width: 100%;
  height: 100%;
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden;
  border: 1px solid rgba(255, 255, 255, 0.8);
  border-radius: 1rem;
  color: white;
  box-shadow: 0 0 0.3em rgba(255, 255, 255, 0.5);
  font-weight: 700;
}

.frontSide,
.frontSide::before {
  background: linear-gradient(43deg, rgb(65, 88, 208) 0%, rgb(200, 80, 192) 46%, rgb(255, 204, 112) 100%);
}

.backSide,
.backSide::before {
  background-image: linear-gradient(160deg, #0093E9 0%, #80D0C7 100%);
}

.backSide {
  transform: rotateY(180deg);
}

.frontSide::before,
.backSide::before {
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  content: '';
  width: 110%;
  height: 110%;
  position: absolute;
  z-index: -1;
  border-radius: 1em;
  filter: blur(20px);
  animation: animate 5s linear infinite;
}

@keyframes animate {
  0% {
    opacity: 0.3;
  }

  80% {
    opacity: 1;
  }

  100% {
    opacity: 0.3;
  }
}
</style>
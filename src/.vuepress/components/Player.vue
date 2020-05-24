<template>
  <div v-if="play">
    <a-player
      :options="{
              audio: [
                  {
                  name: title,
                  artist: 'terapyon',
                  url: audio_url,
                  cover: image_href
                  }
              ]
              }"
    />
  </div>
  <div v-else>
    <button v-on:click="showPlayer()" class="play-button">
      <i class="fas fa-play-circle"></i>
      <span class="button-text">Play</span>
      <img :src="image_href" width="30px" />
    </button>
  </div>
</template>
<script>
export default {
  name: "Player",
  props: ["title", "audio_url", "image_href"],
  data: function() {
    return {
      play: false
    };
  },
  methods: {
    showPlayer() {
      console.log("showPlayer");
      this.play = true;
    }
  }
};
</script>

<style scoped>
.play-button {
  position: relative;
  display: inline-block;
  padding: 0.25em 0.5em;
  text-decoration: none;
  color: #fff;
  background: #0083be;
  border-radius: 1px;
  border: 1px dashed #fff;
  box-shadow: 0 0 0 2px #0083be;
  font-weight: bold;
  width: 100%;
  height: 66px;
  text-align: center;
  margin: 5px 0;
  cursor: pointer;
}

.play-button:hover {
  box-shadow: 0 0 4px #0083be;
}

.button-text {
  display: inline-block;
  vertical-align: center;
  margin: 0 10px;
  font-size: 120%;
}
</style>

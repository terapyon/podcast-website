<template>
  <v-card>
    <v-row>
      <v-col cols="12" md="10">
        <h3>
          <router-link :to="page.path">{{page.title || 'No Title'}}</router-link>
        </h3>
      </v-col>
      <v-col cols="12" md="2" class="episode-date">
        <DisplayDate :dateStr="page.frontmatter.date"></DisplayDate>
        <DisplaySeason :season="page.frontmatter.season" :topic="page.frontmatter.number" />
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <div
          v-if="page.frontmatter.description"
          class="article-description"
        >{{page.frontmatter.description}}...</div>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <Player
          :title="page.title"
          :audio_url="page.frontmatter.audio_url"
          :image_href="page.frontmatter.image_href"
        />
      </v-col>
    </v-row>
  </v-card>
</template>

<script>
export default {
  name: "Episode",
  props: ["page"],
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
h3 {
  font-size: 1.5rem;
  padding: 0 15px;
}
.article-description {
  padding: 0 10px;
}
.play-button {
  position: relative;
  display: inline-block;
  padding: 0.25em 0.5em;
  text-decoration: none;
  color: #fff;
  background: #307df8;
  border-radius: 4px;
  box-shadow: inset 0 2px 0 rgba(255, 255, 255, 0.2),
    inset 0 -2px 0 rgba(0, 0, 0, 0.05);
  font-weight: bold;
  border: solid 2px #0004d2;
  width: 50%;
  height: 66px;
  text-align: center;
  margin: 5px 0;
  cursor: pointer;
}

.play-button:active {
  box-shadow: 0 0 2px rgba(0, 0, 0, 0.3);
}
</style>

<template>
  <div>
    <div v-for="page in filteredPages" class="box-episode" v-if="!page.frontmatter.exclude">
      <div class="episode-title">
        <h3 class="article-title">
          <router-link :to="page.path">{{page.title || 'No Title'}}</router-link>
        </h3>
        <div class="episode-date">
          <DisplayDate :dateStr="page.frontmatter.date"></DisplayDate>
          <DisplaySeason :season="page.frontmatter.season" :topic="page.frontmatter.number" />
        </div>
      </div>
      <div class="tag-container">
        <i class="fas fa-tags tag-icon"></i>
        <div v-for="c in page.frontmatter.category" class="tag">{{c}}</div>
      </div>
      <div
        v-if="page.frontmatter.description"
        class="article-description"
      >{{page.frontmatter.description}}</div>
      <a-player
        :options="{
            audio: [
                {
                name: page.title,
                artist: 'terapyon',
                url: page.frontmatter.audio_url,
                cover: page.frontmatter.image_href
                }
            ]
            }"
      />
    </div>
  </div>
</template>

<script>
export default {
  name: "Articles",
  props: ["pages", "prefix"],
  computed: {
    filteredPages() {
      return this.pages
        .filter(page => page.path.includes(this.prefix || ""))
        .reverse();
    }
  }
};
</script>

<style scoped>
.box-episode {
  padding: 0.5em 1em;
  margin: 2em 0;
  color: #5d627b;
  background: white;
  border-top: solid 5px #5d627b;
  box-shadow: 0 3px 5px rgba(0, 0, 0, 0.22);
}
.box-episode p {
  margin: 0;
  padding: 0;
}

.article-title {
  display: inline-block;
  text-align: left;
  vertical-align: top;
  width: 590px;
  margin: 10px 0;
}
.episode-date {
  display: inline-block;
  text-align: right;
}
</style>
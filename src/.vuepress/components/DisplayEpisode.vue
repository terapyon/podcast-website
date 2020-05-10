<template>
  <div>
    <div class="episode-title">
      <h3 class="article-title">
        <router-link :to="page.path">{{page.title || 'No Title'}}</router-link>
      </h3>
      <div class="episode-date">
        <DisplayDate :dateStr="page.frontmatter.date"></DisplayDate>
        <DisplaySeason :season="page.frontmatter.season" :topic="page.frontmatter.number" />
      </div>
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
</template>

<script>
export default {
  name: "Episode",
  props: ["page"]
};
</script>

<style scoped>
.article-title {
  display: inline-block;
  text-align: left;
  vertical-align: top;
  width: 83%;
  margin: 10px 0;
}
.episode-date {
  display: inline-block;
  text-align: right;
}
</style>

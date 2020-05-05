<template>
  <div>
    <div v-for="page in filteredPages" class="box-episode" v-if="!page.frontmatter.exclude">
      <h3 class="article-title">
        <router-link :to="page.path">{{page.title || 'No Title'}}</router-link>
      </h3>
      <div>{{page.frontmatter.date}}</div>
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

    <div class="entry-date date first">
      <time pubdate datetime="2017-01-29T09:44:54Z" title="2017-01-29T09:44:54Z">
        <span class="date-year">2017</span>
        <span class="hyphen">-</span>
        <span class="date-month">01</span>
        <span class="hyphen">-</span>
        <span class="date-day">29</span>
      </time>
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
/*  */
/* // add */
/* 日付手縫いステッチ風 */
.entry-header .date {
  position: absolute;
  left: -105px;
  padding: 8px 6px;
  width: 62px;
  background: #47a89c;
  border-radius: 1px;
  border: 1px dashed #fff;
  box-shadow: 0 0 0 4px #47a89c;
  text-align: center;
  line-height: 1;
}
.date time {
  font-family: "Montserrat", san-serif;
  color: #050505;
  text-decoration: none;
  font-size: 26px;
}
.hyphen {
  display: none;
}

.date-year {
  display: block;
}
.date-year {
  font-size: 14px;
}
.date-day,
.date-month {
  display: inline-block;
}
.date-month::after {
  content: "/";
}
</style>
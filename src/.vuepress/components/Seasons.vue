<template>
  <v-container>
    <v-row v-for="page in filteredPages" class="box-episode" v-if="!page.frontmatter.exclude">
      <DisplayEpisode :page="page" />
    </v-row>
  </v-container>
</template>
<script>
import moment from "moment";
export default {
  name: "Articles",
  props: ["pages", "prefix", "season"],
  computed: {
    filteredPages() {
      return this.pages
        .filter(page => page.path.includes(this.prefix || ""))
        .filter(page => page.frontmatter.season == this.season || 0)
        .sort(function(a, b) {
          return moment(a.frontmatter.date) - moment(b.frontmatter.date);
        });
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
</style>
<template>
  <div>
    <div v-for="page in filteredPages" class="box-episode" v-if="!page.frontmatter.exclude">
      <DisplayEpisode :page="page" />
    </div>
  </div>
</template>
<script>
export default {
  name: "Articles",
  props: ["pages", "prefix", "limit"],
  computed: {
    filteredPages() {
      return this.pages
        .filter(page => page.path.includes(this.prefix || ""))
        .reverse()
        .slice(0, (this.limit || 10) + 1);
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
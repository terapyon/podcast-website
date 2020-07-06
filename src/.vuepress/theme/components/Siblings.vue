<template>
  <v-container>
    <v-row class="siblings">
      <v-col>
        <v-btn v-show="isPrevious" text rounded small>
          <RouterLink :to="previous.path">&lt; {{shortTitle(previous.title)}}</RouterLink>
        </v-btn>
      </v-col>
      <v-col>
        <v-btn text rounded small>
          <RouterLink to="/episodes/">Episode List</RouterLink>
        </v-btn>
      </v-col>
      <v-col>
        <v-btn v-show="isNext" text rounded small>
          <RouterLink :to="next.path">{{shortTitle(next.title)}} &gt;</RouterLink>
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
import moment from "moment";
export default {
  name: "Siblings",
  data() {
    return {
      isPrevious: false,
      isNext: false
    };
  },

  methods: {
    shortTitle(s) {
      const maxString = 15;
      if (s.length > maxString) {
        return s.substring(0, maxString) + "...";
      } else {
        return s;
      }
    }
  },

  computed: {
    episodedList() {
      const prefix = "/episodes/";
      return this.$site.pages
        .filter(
          page => page.path.includes(prefix || "") && page.path !== "/episodes/"
        )
        .sort(function(a, b) {
          return moment(a.frontmatter.date) - moment(b.frontmatter.date);
        });
    },
    hasSiblings() {
      const path = this.$page.path;
      const episodes = this.episodedList;
      const episode_paths = episodes.map(x => x.path);
      if (episode_paths.includes(path)) {
        const ix = episode_paths.indexOf(path);

        if (ix > 1) {
          this.isPrevious = true;
        } else {
          this.isPrevious = false;
        }
        if (ix < episode_paths.length - 1) {
          this.isNext = true;
        } else {
          this.isNext = false;
        }
        return ix;
      } else {
        return -1;
      }
    },
    previous() {
      const episodes = this.episodedList;
      const ix = this.hasSiblings;
      if (this.isPrevious) {
        return episodes[ix - 1];
      } else {
        return { path: "", title: "" };
      }
    },
    next() {
      const episodes = this.episodedList;
      const ix = this.hasSiblings;
      if (this.isNext) {
        return episodes[ix + 1];
      } else {
        return { path: "", title: "" };
      }
    }
  }
};
</script>
<style scoped>
button {
  background-color: lightskyblue;
}
button a {
  text-decoration: none;
  color: black;
}
.siblings {
  font-size: 50%;
}
</style>
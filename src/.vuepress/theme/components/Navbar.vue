<template>
  <v-app-bar
    :collapse="!collapseOnScroll"
    :collapse-on-scroll="collapseOnScroll"
    app
    color="primary"
    dark
  >
    <v-app-bar-nav-icon @click="drawer = true">
      <!-- <NavLinks class="can-hide" /> -->
    </v-app-bar-nav-icon>

    <RouterLink :to="$localePath">
      <v-row>
        <v-col>
          <v-img
            v-if="$site.themeConfig.logo"
            class="logo"
            width="50px"
            :src="$withBase($site.themeConfig.logo)"
            :alt="$siteTitle"
          />
        </v-col>
        <v-toolbar-title>
          <v-col class="site-title">{{ $siteTitle }}</v-col>
        </v-toolbar-title>
      </v-row>
    </RouterLink>

    <v-spacer></v-spacer>
    <!-- <SearchBox v-if="$site.themeConfig.search !== false && $page.frontmatter.search !== false" /> -->
    <!-- <NavLinks /> -->
    <!-- <v-btn v-if="collapseOnScroll" text rounded @click="toggleTheme">Toggle Theme</v-btn> -->
    <v-navigation-drawer v-model="drawer" fixed temporary>
      <v-list nav dense>
        <v-list-item-group>
          <v-list-item>
            <v-list-item-title>HOME</v-list-item-title>
          </v-list-item>
          <v-list-item>
            <v-list-item-title>ABOUT</v-list-item-title>
          </v-list-item>
          <v-list-item>
            <v-list-item-title>WORK</v-list-item-title>
          </v-list-item>
          <v-list-item>
            <v-list-item-title>SERVICE</v-list-item-title>
          </v-list-item>
          <v-list-item>
            <v-list-item-title>BLOG</v-list-item-title>
          </v-list-item>
          <v-list-item>
            <v-list-item-title>ACCESS</v-list-item-title>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
  </v-app-bar>
</template>

<script>
import SearchBox from "@vuepress/plugin-search/SearchBox";
import NavLinks from "@theme/components/NavLinks.vue";

export default {
  name: "Navbar",

  components: {
    NavLinks,
    SearchBox
  },

  data() {
    return {
      linksWrapMaxWidth: null,
      collapseOnScroll: true,
      drawer: false
    };
  },

  computed: {},

  mounted() {}
};
</script>
<style scoped>
.site-title {
  color: #ffff;
  font-size: 1.5em;
}
</style>
<template>
  <v-card>
    <v-app-bar
      :collapse="!collapseOnScroll"
      :collapse-on-scroll="collapseOnScroll"
      app
      color="primary accent-4"
      dark
    >
      <!-- <v-app-bar-nav-icon @click="drawer = true" class="main-menu"></v-app-bar-nav-icon> -->
      <v-app-bar-nav-icon @click.stop="drawer = !drawer">></v-app-bar-nav-icon>

      <v-img
        v-if="!collapseOnScroll"
        class="logo"
        width="50px"
        :src="$withBase($site.themeConfig.logo)"
        :alt="$siteTitle"
      />

      <v-toolbar-title>
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
            <v-col class="site-title">{{ $siteTitle }}</v-col>
          </v-row>
        </RouterLink>
      </v-toolbar-title>
      <!-- <v-spacer></v-spacer> -->
      <!-- <SearchBox v-if="$site.themeConfig.search !== false && $page.frontmatter.search !== false" /> -->
      <!-- <v-toolbar-items>
      <NavLinks />
      </v-toolbar-items>-->
      <!-- <v-btn v-if="collapseOnScroll" text rounded @click="toggleTheme">Toggle Theme</v-btn> -->

      <v-spacer></v-spacer>

      <v-checkbox v-model="collapseOnScroll" color="white" hide-details></v-checkbox>
    </v-app-bar>
    <v-navigation-drawer v-model="drawer" app color="blue" dark>
      <v-list nav dense>
        <v-list-item-group v-model="group" active-class="deep-purple--text text--accent-4">
          <NavLinks />
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
  </v-card>
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
      drawer: false,
      group: null
    };
  },

  watch: {
    group() {
      this.drawer = false;
    }
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
/* .main-menu {
  color: #fff;
  z-index: 100;
  border-color: #fff;
} */
</style>
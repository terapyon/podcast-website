<template>
  <v-card>
    <v-app-bar app color="primary accent-4" dark>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" class="material-icons" v-show="isMobile"></v-app-bar-nav-icon>
      <v-toolbar-title>
        <RouterLink :to="$localePath">
          <v-row>
            <v-col v-show="!isMobile">
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
      <v-spacer></v-spacer>
      <SearchBox v-if="$site.themeConfig.search !== false && $page.frontmatter.search !== false" />
      <NavLinks v-show="!isMobile" :isList="false" />
    </v-app-bar>
    <v-navigation-drawer v-model="drawer" app color="blue" dark v-show="isMobile">
      <v-list nav dense>
        <v-list-item-group v-model="group" active-class="deep-purple--text text--accent-4">
          <NavLinks :isList="true" />
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

  computed: {
    isMobile() {
      return this.$vuetify.breakpoint.mdAndDown;
    }
  },

  mounted() {}
};
</script>
<style lang="stylus" scoped>
.site-title {
  color: #ffff;
  font-size: 1.5em;
}

@media (max-width: $MQMobile) {
  .site-title {
    font-size: 1em;
    padding: 0;
  }
}
</style>
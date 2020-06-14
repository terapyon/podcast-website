<template>
  <v-app>
    <Navbar v-if="shouldShowNavbar" @toggle-sidebar="toggleSidebar" />
    <!-- <v-app-bar app color="primary" dark>
      <v-toolbar-title>サイト名</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn text rounded>ホーム</v-btn>
      <v-btn text rounded>ログイン</v-btn>
    </v-app-bar>-->
    <v-main>
      <v-card width="1000" class="mx-auto mt-5">
        <Content />
      </v-card>
    </v-main>
    <v-footer color="primary lighten-1" padless>
      <v-row justify="center" no-gutters>
        <v-btn v-for="link in links" :key="link" color="white" text rounded class="my-2">{{ link }}</v-btn>
        <v-col class="primary lighten-2 py-4 text-center white--text" cols="12">
          {{ new Date().getFullYear() }} —
          <strong>terapyon</strong>
        </v-col>
      </v-row>
    </v-footer>
  </v-app>
</template>
<script>
import Navbar from "@theme/components/Navbar.vue";

export default {
  name: "Layout",
  components: {
    Navbar
  },
  data() {
    return {
      isSidebarOpen: false
    };
  },
  computed: {
    shouldShowNavbar() {
      const { themeConfig } = this.$site;
      const { frontmatter } = this.$page;
      if (frontmatter.navbar === false || themeConfig.navbar === false) {
        return false;
      }
      return (
        this.$title ||
        themeConfig.logo ||
        themeConfig.repo ||
        themeConfig.nav ||
        this.$themeLocaleConfig.nav
      );
    },
    pageClasses() {
      const userPageClass = this.$page.frontmatter.pageClass;
      return [
        {
          "no-navbar": !this.shouldShowNavbar,
          "sidebar-open": this.isSidebarOpen,
          "no-sidebar": !this.shouldShowSidebar
        },
        userPageClass
      ];
    }
  },
  methods: {
    // side swipe
    onTouchStart(e) {
      this.touchStart = {
        x: e.changedTouches[0].clientX,
        y: e.changedTouches[0].clientY
      };
    },
    onTouchEnd(e) {
      const dx = e.changedTouches[0].clientX - this.touchStart.x;
      const dy = e.changedTouches[0].clientY - this.touchStart.y;
      if (Math.abs(dx) > Math.abs(dy) && Math.abs(dx) > 40) {
        if (dx > 0 && this.touchStart.x <= 80) {
          this.toggleSidebar(true);
        } else {
          this.toggleSidebar(false);
        }
      }
    }
  }
};
</script>
<template>
  <v-app class="overflow-hidden">
    <Navbar />

    <v-main id="main-content">
      <component id="scrolling-techniques" class="overflow-y-auto" :is="layout" />
    </v-main>
    <Footer />
    <!-- </v-sheet> -->
  </v-app>
</template>
<script>
import Home from "./Home.vue";
import Episode from "./Episode";
import Page from "./Page.vue";
import Navbar from "@theme/components/Navbar.vue";
import Footer from "@theme/components/Footer.vue";

export default {
  name: "Layout",
  components: {
    Home,
    Episode,
    Page,
    Navbar,
    Footer
  },
  data() {
    return {
      isSidebarOpen: false
    };
  },
  computed: {
    layout() {
      const { path } = this.$page;
      if (path === "/") {
        return "Home";
      } else if (path.match(/\/episodes\/\d+\.html$/)) {
        return "Episode";
      } else {
        return "Page";
      }
    }
    // shouldShowNavbar() {
    //   const { themeConfig } = this.$site;
    //   const { frontmatter } = this.$page;
    //   if (frontmatter.navbar === false || themeConfig.navbar === false) {
    //     return false;
    //   }
    //   return (
    //     this.$title ||
    //     themeConfig.logo ||
    //     themeConfig.repo ||
    //     themeConfig.nav ||
    //     this.$themeLocaleConfig.nav
    //   );
    // },
    // pageClasses() {
    //   const userPageClass = this.$page.frontmatter.pageClass;
    //   return [
    //     {
    //       "no-navbar": !this.shouldShowNavbar,
    //       "sidebar-open": this.isSidebarOpen,
    //       "no-sidebar": !this.shouldShowSidebar
    //     },
    //     userPageClass
    //   ];
    // }
  },
  methods: {
    // side swipe
    onTouchStart(e) {
      this.touchStart = {
        x: e.changedTouches[0].clientX,
        y: e.changedTouches[0].clientY
      };
    }
    // onTouchEnd(e) {
    //   const dx = e.changedTouches[0].clientX - this.touchStart.x;
    //   const dy = e.changedTouches[0].clientY - this.touchStart.y;
    //   if (Math.abs(dx) > Math.abs(dy) && Math.abs(dx) > 40) {
    //     if (dx > 0 && this.touchStart.x <= 80) {
    //       this.toggleSidebar(true);
    //     } else {
    //       this.toggleSidebar(false);
    //     }
    //   }
    // }
  }
};
</script>
<style lang="stylus"></style>
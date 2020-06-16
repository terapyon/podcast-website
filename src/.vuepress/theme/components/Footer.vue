<template>
  <v-footer color="primary lighten-1" padless>
    <v-row justify="center" no-gutters>
      <NavLinks class="can-hide" />
      <!-- <v-btn v-for="link in links" :key="link" color="white" text rounded class="my-2">{{ link }}</v-btn> -->
      <v-col class="primary lighten-2 py-4 text-center white--text" cols="12">
        {{ new Date().getFullYear() }} —
        <strong>terapyon</strong>
      </v-col>
    </v-row>
  </v-footer>
</template>
<script>
import NavLinks from "@theme/components/NavLinks.vue";
export default {
  name: "Footer",

  components: {
    NavLinks
  }
};
</script>

<style lang="stylus" scope>
.links {
  padding-left: 1.5rem;
  box-sizing: border-box;
  background-color: white;
  white-space: nowrap;
  font-size: 0.9rem;
  position: absolute;
  right: $navbar-horizontal-padding;
  top: $navbar-vertical-padding;
  display: flex;
}
</style>
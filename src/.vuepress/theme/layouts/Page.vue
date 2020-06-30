<template>
  <v-container>
    <v-row>
      <Content />
    </v-row>
    <v-row>
      <ShareLink />
    </v-row>
  </v-container>
</template>
<script>
import ShareLink from "@theme/components/ShareLink.vue";
export default {
  name: "Page",

  components: {
    ShareLink
  }
};
</script>
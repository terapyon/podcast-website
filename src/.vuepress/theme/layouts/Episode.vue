<template>
  <v-container>
    <v-row>
      <Siblings />
    </v-row>
    <v-row>
      <Content />
    </v-row>
    <v-row>
      <ShareLink />
    </v-row>
  </v-container>
</template>
<script>
import Siblings from "@theme/components/Siblings.vue";
import ShareLink from "@theme/components/ShareLink.vue";
export default {
  name: "Episode",

  components: {
    Siblings,
    ShareLink
  }
};
</script>
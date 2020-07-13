<template>
  <v-container>
    <v-row style="font-size: 2rem;">
      <v-spacer></v-spacer>
      <v-col cols="auto">
        <ShareNetwork
          network="facebook"
          :url="shareUrl"
          :title="shareTitle"
          hashtags="terapyon_channel"
        >
          <i class="fab fa-facebook-square"></i>
        </ShareNetwork>
      </v-col>
      <v-col cols="auto">
        <ShareNetwork
          network="twitter"
          :url="shareUrl"
          :title="shareTitle"
          hashtags="terapyon_channel"
        >
          <i class="fab fa-twitter-square"></i>
        </ShareNetwork>
      </v-col>
      <v-spacer></v-spacer>
    </v-row>
  </v-container>
</template>
<script>
export default {
  name: "ShareLink",

  computed: {
    shareTitle() {
      return "Podcast terapyon channel 「" + this.$page.title + "」を共有";
    },
    shareUrl() {
      return window.location.toString();
    }
  }
};
</script>
<style scoped>
</style>
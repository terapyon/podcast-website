<template>
  <v-container>
    <v-col>
      <ShareNetwork
        network="facebook"
        :url="shareUrl"
        title="'Podcast terapyon channel ' + this.$page.title + ' を共有'"
        hashtags="terapyon_channel"
      >Share on Facebook</ShareNetwork>
    </v-col>
    <v-col>
      <ShareNetwork
        network="twitter"
        :url="shareUrl"
        :title="'Podcast terapyon channel ' + this.$page.title + ' を共有'"
        hashtags="terapyon_channel"
      >Share on twitter</ShareNetwork>
    </v-col>
  </v-container>
</template>
<script>
export default {
  name: "ShareLink",

  data() {
    return {
      // shareTitle: "Podcast terapyon channel " + this.$page.title + " を共有"
      shareUrl: window.location.toString()
    };
  }
};
</script>
<template>
  <v-container>
    <v-row>
      <v-col>
        <h1 :class="$vuetify.breakpoint.mdAndUp? 'left': 'center'">terapyon channel podcast Top page</h1>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12" md="7">
        <v-img class="main-image" src="/terada-uspycon2019.jpg" />
      </v-col>
      <v-col cols="12" md="5">
        <v-card :shaped="true">
          <v-card-text>
            <div>いずれかのサービスでサブスクライブ</div>
            <p class="display-1 text--primary">Podcastサービス</p>
            <p>登録は以下のいずれかのサービスからお願いします。</p>
          </v-card-text>
          <v-card-actions>
            <v-btn text color="deep-purple accent-4">Learn More</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <Content />
      </v-col>
    </v-row>
    <v-row v-intersect="showMoreContents">
      <v-col>
        <h2>最近のエピソード</h2>最近のエピソードを5件
      </v-col>
    </v-row>
    <v-row v-if="loadNewContents">
      <v-col>
        <RecentEpisodes :pages="this.$site.pages" :prefix="'/episodes/'" :limit="limitNumber" />
      </v-col>
    </v-row>
    <a href="/episodes/" v-intersect="addContents">すべて見る</a>
  </v-container>
</template>
<script>
export default {
  name: "Home",

  data() {
    return {
      loadNewContents: false,
      limitNumber: 5
    };
  },
  methods: {
    showMoreContents(entries) {
      //   console.log(entries[0].isIntersecting);
      if (!this.loadNewContents) {
        this.loadNewContents = entries[0].isIntersecting;
      }
    },
    addContents(entries) {
      //   console.log(this.limitNumber);
      this.limitNumber += 5;
    }
  }
};
</script>
<style scoped>
h1 {
  font-size: 3em;
}
h1.center {
  text-align: center;
  font-size: 2em;
}
.display-1 {
  font-size: 0.7em;
}
</style>

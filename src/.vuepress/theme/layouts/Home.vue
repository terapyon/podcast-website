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
        <v-card :shaped="true" class="card-box">
          <v-card-text>
            <div>いずれかのサービスでサブスクライブ</div>
            <p class="display-1 text--primary">Podcastサービス</p>
            <p>登録は以下のいずれかのサービスからお願いします。</p>
          </v-card-text>
          <v-card-text class="podcast-servicies">
            <v-chip-group v-model="selection" column>
              <v-chip>
                <a
                  href="https://open.spotify.com/show/3F1JJCqbBzmNQhSibjvzKZ"
                  title="Spotifyプレミアアカウントの方におすすめ"
                >
                  <i class="fab fa-spotify fa-lg"></i>&nbsp;Spotify
                </a>
              </v-chip>
              <v-chip>
                <a
                  href="https://podcasts.apple.com/jp/podcast/manabu-terada/id1501371621"
                  title="iPhoneなどスマホに取り込みやすい"
                >
                  <i class="fas fa-podcast fa-lg"></i>&nbsp;Apple Podcasts
                </a>
              </v-chip>
              <v-chip>
                <a
                  href="https://www.google.com/podcasts?feed=aHR0cHM6Ly9hbmNob3IuZm0vcy8xNDQ4MGUwNC9wb2RjYXN0L3Jzcw=="
                  title="Googleのサービス"
                >
                  <i class="fab fa-google fa-lg"></i>&nbsp;Google Podcasts
                </a>
              </v-chip>
              <v-chip>
                <a
                  href="https://anchor.fm/terapyon"
                  title="このPodcastの配信ベースとなっているサービス(配信タイミングが一番早い)"
                >Anchor</a>
              </v-chip>
            </v-chip-group>
          </v-card-text>
        </v-card>
        <v-card :shaped="true">
          <v-card-text>
            <div>個人のTwitterアカウント</div>
            <p class="display-1 text--primary">Twitter</p>
            <p>フォローをお願いします。</p>
          </v-card-text>
          <v-card-text class="podcast-servicies">
            <v-chip-group v-model="selection" column>
              <v-chip>
                <a href="https://twitter.com/terapyon">
                  <i class="fab fa-twitter fa-lg"></i>&nbsp;terapyon個人アカウント
                </a>
              </v-chip>
              <v-chip>
                <a
                  href="https://twitter.com/hashtag/terapyon_channel?src=hashtag_click&f=live"
                >#terapyon_channel (ハッシュタグ)</a>
              </v-chip>
            </v-chip-group>
          </v-card-text>
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
        <h2>最近のエピソード</h2>
      </v-col>
    </v-row>
    <v-row v-if="loadNewContents">
      <v-col>
        <RecentEpisodes :pages="this.$site.pages" :prefix="'/episodes/'" :limit="limitNumber" />
      </v-col>
    </v-row>
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
.podcast-servicies a {
  text-decoration: none;
  color: black;
  vertical-align: middle;
}
.card-box {
  margin: 3px 0;
}
</style>

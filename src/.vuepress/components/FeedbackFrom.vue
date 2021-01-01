<template>
  <v-container>
    <form name="feedback" method="POST" netlify>
      <v-row>
        <v-col cols="12" md="6">
          <v-text-field
            name="name"
            label="お名前またはラジオネーム"
            required
          ></v-text-field>
        </v-col>
        <v-col cols="12" md="6">
          <v-text-field
            name="email"
            label="メールアドレス"
            required
          ></v-text-field>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12" md="6">
          <v-text-field
            name="sns-name"
            label="SNSアカウントネーム"
          ></v-text-field>
        </v-col>
        <v-col cols="12" md="6">
          <v-select
            :items="snsItems"
            label="SNSタイプ"
          ></v-select>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
        <v-textarea
          outlined
          name="message"
          label="メッセージ内容"
        ></v-textarea>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <v-checkbox
            name="allow-public"
            label="内容の公開を許可"
          ></v-checkbox>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <v-btn
            width="100%"
            class="mr-4"
            color="primary"
            type="submit"
          >
            投稿
          </v-btn>
        </v-col>
      </v-row>
    </form>
  </v-container>
</template>
<script>
export default {
  name: "FeedbackFrom",
  props: [],
  data: () => {
    return {
      snsItems: ["Twitter", "Facebook", "Github", "Instagram"]
    };
  },
  computed: {}
};
</script>

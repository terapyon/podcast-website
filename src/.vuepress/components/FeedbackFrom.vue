<template>
  <v-container>
    <form name="ask-question" netlify>
      <v-row>
        <v-col cols="12" md="6">
          <v-text-field
            v-model="name"
            name="name"
            label="お名前またはラジオネーム"
            required
          ></v-text-field>
        </v-col>
        <v-col cols="12" md="6">
          <v-text-field
            v-model="email"
            name="email"
            label="メールアドレス"
            required
          ></v-text-field>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12" md="6">
          <v-text-field
            v-model="snsName"
            name="sns-name"
            label="SNSアカウントネーム"
          ></v-text-field>
        </v-col>
        <v-col cols="12" md="6">
          <v-select
            v-model="snsType"
            name="sns-type"
            :items="snsItems"
            label="SNSタイプ"
          ></v-select>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
        <v-textarea
          outlined
          v-model="message"
          name="message"
          label="メッセージ内容"
        ></v-textarea>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <v-checkbox
            v-model="allow"
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
            @click="handleSubmit"
          >
            投稿
          </v-btn>
        </v-col>
      </v-row>
    </form>
  </v-container>
</template>
<script>
import axios from "axios";

export default {
  name: "FeedbackFrom",
  props: [],
  data: () => {
    return {
      snsItems: ["Twitter", "Facebook", "Github", "Instagram"],
      name: null,
      email: null,
      snsName: null,
      snsType: null,
      message: null,
      allow: null
    };
  },
  computed: {},
  methods: {
    encode (data) {
      return Object.keys(data)
        .map(
          key => `${encodeURIComponent(key)}=${encodeURIComponent(data[key])}`
        )
        .join('&')
    },
    handleSubmit () {
      const axiosConfig = {
        header: { 'Content-Type': 'application/x-www-form-urlencoded' }
      }
      console.log(this.name)
      axios.post(
          '/',
          this.encode({
            'form-name': 'contact',
            name: this.name,
            email: this.email,
            snsName: this.snsName,
            snsType: this.snsType,
            message: this.message,
            allow: this.allow
          }),
          axiosConfig
        )
    }
  }
};
</script>

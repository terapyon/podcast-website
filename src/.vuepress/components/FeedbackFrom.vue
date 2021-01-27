<template>
  <v-container>
    <form
      name="ask-question"
      method="post"
      data-netlify="true"
      >
      <input type="hidden" name="form-name" value="ask-question" />
      <v-row>
        <v-col cols="12" md="6">
          <v-text-field
            v-model="name"
            name="name"
            label="お名前またはラジオネーム（必須）"
            required
          ></v-text-field>
        </v-col>
        <v-col cols="12" md="6">
          <v-text-field
            v-model="email"
            name="email"
            label="メールアドレス（必須）"
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
            required
          ></v-select>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
        <v-textarea
          outlined
          v-model="message"
          name="message"
          label="メッセージ内容（必須）"
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
        <!-- <v-col>
          <button @click="recaptcha">Execute recaptcha</button>
        </v-col> -->
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
    <v-snackbar
      v-model="snackbar"
      timeout=10000
    > {{ snackbarText }}
      <template v-slot:action="{ attrs }">
        <v-btn
          color="blue"
          text
          v-bind="attrs"
          @click="closeSnackbar"
        >
          閉じる
        </v-btn>
      </template>
    </v-snackbar>
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
      requiredChk: false,
      name: null,
      email: null,
      snsName: null,
      snsType: null,
      message: null,
      allow: false,
      snackbar: false,
      snackbarText: null
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
    async handleSubmit () {
      console.log(this.name)
      if (this.name && this.email && this.message ) {
        this.requiredChk = true
      }
      const axiosConfig = {
        header: { 'Content-Type': 'application/x-www-form-urlencoded' }
      }
      if (this.requiredChk) {
        this.snackbarText = "フィードバックが投稿されました。（テスト中のため送信できませんできた）"
        const res = await axios.post(
            "/",
            this.encode({
              'form-name': 'ask-question',
              name: this.name,
              email: this.email,
              snsName: this.snsName,
              snsType: this.snsType,
              message: this.message,
              allow: this.allow
            }),
            axiosConfig
          )
        console.log(res)
        this.name = null
        this.email = null
        this.snsName = null
        this.snsType = null
        this.message = null
        this.allow = false
        this.requiredChk = false
      } else {
        this.snackbarText = "エラーがありました。必要情報（お名前、メールアドレス、内容）を入力してください。"
      }
      this.snackbar = true
    },
    closeSnackbar () {
      if (this.requiredChk) {
        //
      }
      this.snackbar = false
    },
    // recaptcha() {
    //   // (optional) Wait until recaptcha has been loaded.
    //   this.$recaptchaLoaded()
    //   // Execute reCAPTCHA with action "login".
    //   const token = this.$recaptcha('login')
    //   // Do stuff with the received token.
    // }
  }
};
</script>

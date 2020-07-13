<template>
  <SWUpdatePopup v-slot="{ enabled, reload, message, buttonText }">
    <v-alert v-if="enabled" prominent type="info">
      <v-row align="center">
        <v-col class="grow">{{ message }}</v-col>
        <v-col class="shrink">
          <v-btn dark @click="reload">{{ buttonText }}</v-btn>
        </v-col>
      </v-row>
    </v-alert>
  </SWUpdatePopup>
</template>

<script>
import SWUpdatePopup from "@vuepress/plugin-pwa/lib/SWUpdatePopup.vue";

export default {
  components: { SWUpdatePopup }
};
</script>
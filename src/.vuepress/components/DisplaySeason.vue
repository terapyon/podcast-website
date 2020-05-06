<template>
  <div id="display-season">
    <div class="season">
      <span class="label">Season:</span>
      <span class="number">{{season}}</span>
    </div>
    <div class="topic">
      <span class="label">Topic:</span>
      <span class="number">{{topic}}</span>
    </div>
  </div>
</template>

<script>
import moment from "moment";

export default {
  name: "display-season",
  props: ["season", "topic"]
};
</script>

<style>
#display-season {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  margin: 10px 0 10px 0px;
  padding: 8px 5px;
  width: 100px;
  line-height: 1;
  text-align: center;
  color: #fff;
  background: #01c211;
  border-radius: 1px;
  border: 1px dashed #fff;
  box-shadow: 0 0 0 4px #01c211;
}
.season,
.topic {
  display: inline;
}
.label {
  font-size: 8px;
}
.number {
  font-size: 14px;
  font-weight: bold;
}
</style>
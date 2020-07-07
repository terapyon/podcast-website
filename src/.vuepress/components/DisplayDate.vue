<template>
  <div id="display-date">
    <time pubdate :datetime="dateStr | moment" :title="dateStr | moment">
      <span class="date-year">{{dateStr | moment("YYYY")}}</span>
      <span class="hyphen">-</span>
      <span class="date-month">{{dateStr | moment("MMM")}}</span>
      <span class="hyphen">-</span>
      <span class="date-day">{{dateStr | moment("Do")}}</span>
      <span class="hyphen">-</span>
      <span class="date-week">{{dateStr | moment("ddd")}}</span>
    </time>
  </div>
</template>

<script>
import moment from "moment";

export default {
  name: "display-date",
  props: ["dateStr"],
  filters: {
    moment(value, format) {
      moment.locale("ja");
      return moment(value).format(format);
    }
  }
};
</script>

<style  lang="stylus" scoped>
#display-date {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  margin: 0;
  padding: 8px 5px;
  width: 100%;
  line-height: 1;
  text-align: center;
  color: #fff;
  background: #0083be;
  border-radius: 1px;
  border: 1px dashed #fff;
  box-shadow: 0 0 0 4px #0083be;
}

.hyphen {
  display: none;
}

.date-year {
  display: block;
}

.date-year {
  font-size: 14px;
}

.date-day {
  display: inline-block;
  font-weight: bold;
}

.date-month {
  display: inline-block;
  font-weight: bold;
}

/* .date-month::after {
  content: "/";
} */
.date-week {
  font-size: 10px;
}

.date-week::before {
  content: '(';
}

.date-week::after {
  content: ')';
}

@media (max-width: $MQNarrow) {
  #display-date {
    width: 30%;
  }
}
</style>
<script setup>

import Tierlist from "./Tierlist.vue";
import {Star} from "@element-plus/icons-vue";
</script>

<template>
 <Tierlist></Tierlist>
  <div class="Info__nameRow">
    <h3> Summoner Name #EUW </h3>
    <el-button  :icon="Star" class="Info__addToFavoritesButton" />
  </div>
</template>

<style scoped lang="scss">
.Info {
  &__nameRow {
    display: flex;
  }

  &__addToFavoritesButton {
    width: 20px;
    margin-left: 10px;
    font-size: 20px !important;

  }
}
</style>
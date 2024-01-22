
<template>
<section>
  <el-row :gutter="30" >
    <el-col :span="6" class="HeaderProfileInfo__imageColumn">
      <ProfilePic></ProfilePic>
      <ElBadge :value="level.summonerLevel" max="9999" class="HeaderProfileInfo__badge"></ElBadge>
    </el-col>
    <el-col :span="18">
      <Info></Info>
    </el-col>
  </el-row>
</section>
</template>


<script setup>
import Info from "./Info.vue";
import ProfilePic from "./ProfilePic.vue";
import axios from "axios";
import { ref, onMounted } from "vue";

const level = ref("")

const getSummonerLevel = () => {
  const path = 'http://localhost:5001/ping';
  axios.get(path)
      .then((res) => {
        console.log(res.data)
        level.value = res.data;
      })
      .catch((error) => {
        console.error(error);
      });
}

onMounted(() =>  {
  getSummonerLevel()
})
</script>


<style lang="scss">

.HeaderProfileInfo {
  &__imageColumn  {
    display: flex !important;
    flex-direction: column;
    align-items: center;
  }

  &__badge {
    margin-top: -11px;
    .el-badge__content--danger {
      background: #202D37;
      border: none;
    }
  }

}



</style>
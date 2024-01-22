
<template>
<section>
  <el-row gutter="30" >
    <el-col :span="6">
      <ProfilePic></ProfilePic>
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
</script>


<style scoped>



</style>
<script setup>

</script>

<template>
 <div class="Tierlist">
   <div class="Tierlist__container">
       <ul class="Tierlist__list">
         <li>
           S2023 S2 Silver 3
         </li>
         <li>
           S2023 S1 Bronze 1
         </li>
         <li>
           S2022 Silver 4
         </li>
       </ul>
   </div>
 </div>
</template>

<style scoped lang="scss">
.Tierlist {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 32px;

  &__container {
    position: relative;
    display: flex;
  }

  &__list {
    display: flex;
  }

  ul {
    padding: 0;
    list-style: none;
  }

  li {
    line-height: 18px;
    padding: 0px 4px;
    border-radius: 2px;
    font-size: 11px;
    color: #9AA4AF;
    background-color: #ebeef1;
    text-transform: capitalize;
    margin-right: 5px;
  }
}
</style>
<template>
  <div>
    test
    <p>{{ msg }}</p>

  </div>
</template>

<script setup >
import axios from 'axios';
import { ref, onMounted } from "vue";


const msg = ref("")

const getMessage = () => {
  const path = 'http://localhost:5001/ping';
  axios.get(path)
      .then((res) => {
        msg.value = res.data;
      })
      .catch((error) => {

        console.error(error);
      });
}

onMounted(() => {
  getMessage()
})

</script>
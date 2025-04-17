<template>
  <div>
    <h2 class="text-2xl font-bold">Input the VIN of the car</h2>
    <SInput v-model="globalStore.vin" placeholder="VIN" />
  </div>
</template>

<script setup>
import { useGlobalStore } from '@/store/global'

const globalStore = useGlobalStore()
</script>

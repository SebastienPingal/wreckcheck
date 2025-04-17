import { defineStore } from 'pinia'

export const useGlobalStore = defineStore('global', () => {
  const vin = ref('')

  function $reset() {
    vin.value = ''
  }

  return {
    vin,
    $reset,
  }
})

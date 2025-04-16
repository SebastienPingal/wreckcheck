<template>
  <div class="flex flex-col gap-4">
    <h1 class="text-2xl font-bold">Upload an image</h1>
    <SImageInput v-model="selectedImage" />
    <div v-if="selectedImage" class="mt-2 p-3 bg-gray-100 rounded-md shadow-sm flex justify-between">
      <div class="flex items-center gap-2">
        <div class="text-blue-600">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
          </svg>
        </div>
        <div>
          <div class="font-medium">{{ selectedImage.name }}</div>
          <div class="text-xs text-gray-500">{{ formatSize(selectedImage.size) }}</div>
        </div>
      </div>
      <SButton @click="uploadImage" variant="outline">Upload</SButton>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const selectedImage = ref(null)

const formatSize = (bytes) => {
  if (bytes < 1024) return bytes + ' bytes'
  else if (bytes < 1048576) return (bytes / 1024).toFixed(1) + ' KB'
  else return (bytes / 1048576).toFixed(1) + ' MB'
}

const uploadImage = () => {
  console.log(selectedImage.value)
}
</script>

<style scoped></style>

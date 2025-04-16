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
      <SButton v-if="!isLoading" @click="uploadImage" variant="outline">Upload</SButton>
      <SButton v-else variant="outline" class="relative">
        <span class="opacity-0">Upload</span>
        <div class="absolute inset-0 flex items-center justify-center">
          <div class="flex space-x-1">
            <div class="h-2 w-2 bg-primary rounded-full animate-bounce" style="animation-delay: 0ms"></div>
            <div class="h-2 w-2 bg-primary rounded-full animate-bounce" style="animation-delay: 150ms"></div>
            <div class="h-2 w-2 bg-primary rounded-full animate-bounce" style="animation-delay: 300ms"></div>
          </div>
        </div>
      </SButton>
    </div>
    <div v-if="damageAnalysis" class="mt-2 p-3 bg-gray-100 rounded-md shadow-sm">
      <div class="text-sm font-medium">Damage Analysis</div>
      <div class="text-sm">{{ damageAnalysis }}</div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const isLoading = ref(false)
const damageAnalysis = ref(null)
const selectedImage = ref(null)

const formatSize = (bytes) => {
  if (bytes < 1024) return bytes + ' bytes'
  else if (bytes < 1048576) return (bytes / 1024).toFixed(1) + ' KB'
  else return (bytes / 1048576).toFixed(1) + ' MB'
}

const uploadImage = () => {
  isLoading.value = true
  console.log('🖼️ Selected image:', selectedImage.value)

  // Call the API to upload the image
  const formData = new FormData()
  formData.append('image', selectedImage.value)

  fetch('/api/wreckcheck', {
    method: 'POST',
    body: formData
  })
    .then(response => response.json())
    .then(data => {
      console.log('✅ Upload successful:', data)
      damageAnalysis.value = data.damage_analysis
    })
    .catch(error => {
      console.error('❌ Upload failed:', error)
    })
    .finally(() => {
      isLoading.value = false
    })
}
</script>

<style scoped></style>

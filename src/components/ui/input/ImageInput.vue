<script setup lang="ts">
import { ref, watch } from 'vue'
import { cn } from '@/lib/utils'
import type { HTMLAttributes } from 'vue'

const props = defineProps<{
  modelValue?: File
  class?: HTMLAttributes['class']
}>()

const emits = defineEmits<{
  (e: 'update:modelValue', payload: File): void
}>()

const fileInput = ref<HTMLInputElement | null>(null)
const previewUrl = ref<string | null>(null)

const handleFileChange = (event: Event) => {
  const target = event.target as HTMLInputElement
  const file = target.files?.[0]
  
  if (file) {
    emits('update:modelValue', file)
    
    // Create a preview URL
    if (previewUrl.value) {
      URL.revokeObjectURL(previewUrl.value)
    }
    previewUrl.value = URL.createObjectURL(file)
  }
}

// Clean up object URL when component is unmounted
watch(
  () => props.modelValue,
  (newFile, oldFile) => {
    if (oldFile && previewUrl.value) {
      URL.revokeObjectURL(previewUrl.value)
      previewUrl.value = null
    }
    
    if (newFile && !previewUrl.value) {
      previewUrl.value = URL.createObjectURL(newFile)
    }
  }
)
</script>

<template>
  <div class="flex flex-col gap-2 w-full">
    <input
      ref="fileInput"
      type="file"
      accept="image/*"
      @change="handleFileChange"
      class="hidden"
    />
    
    <div 
      @click="fileInput?.click()"
      :class="cn(
        'border-input flex min-h-[150px] w-full items-center justify-center rounded-md border bg-transparent px-3 py-2 text-sm cursor-pointer hover:bg-muted/50 transition-colors',
        'focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-[3px]',
        props.class,
      )"
    >
      <div v-if="!previewUrl" class="flex flex-col items-center justify-center text-muted-foreground">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="mb-2">
          <rect width="18" height="18" x="3" y="3" rx="2" ry="2" />
          <circle cx="9" cy="9" r="2" />
          <path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21" />
        </svg>
        <span>Click to upload an image</span>
      </div>
      
      <img 
        v-else 
        :src="previewUrl" 
        alt="Preview" 
        class="max-h-[300px] max-w-full object-contain rounded-md"
      />
    </div>
  </div>
</template> 
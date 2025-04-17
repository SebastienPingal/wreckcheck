<template>
  <div>
    <component :is="VueMarkdown" :source="source" />
  </div>
</template>

<script setup>
import VueMarkdown from 'vue-markdown-render'

defineProps({
  source: {
    type: String,
    required: true
  }
})
</script>

<style scoped>
/* Markdown base styling */
:deep(h1), :deep(h2), :deep(h3), :deep(h4), :deep(h5), :deep(h6) {
  margin-top: 1.5rem;
  margin-bottom: 1rem;
  font-weight: 600;
  line-height: 1.25;
}

:deep(h1) {
  font-size: 2rem;
}

:deep(h2) {
  font-size: 1.5rem;
}

:deep(h3) {
  font-size: 1.25rem;
}

:deep(p) {
  margin-top: 0;
  margin-bottom: 1rem;
  line-height: 1.6;
}

:deep(a) {
  color: #0366d6;
  text-decoration: none;
}

:deep(a:hover) {
  text-decoration: underline;
}

:deep(code) {
  padding: 0.2em 0.4em;
  margin: 0;
  font-size: 85%;
  background-color: rgba(27,31,35,0.05);
  border-radius: 3px;
}

:deep(pre) {
  margin-top: 0;
  margin-bottom: 1rem;
  padding: 1rem;
  overflow: auto;
  font-size: 85%;
  line-height: 1.45;
  background-color: #f6f8fa;
  border-radius: 3px;
}

:deep(blockquote) {
  padding: 0 1rem;
  margin-left: 0;
  color: #6a737d;
  border-left: 0.25rem solid #dfe2e5;
}

:deep(ul), :deep(ol) {
  padding-left: 2rem;
  margin-top: 0;
  margin-bottom: 1rem;
}

:deep(ul) {
  list-style-type: disc;
}

:deep(ul ul) {
  list-style-type: circle;
}

:deep(ul ul ul) {
  list-style-type: square;
}

:deep(ol) {
  list-style-type: decimal;
}

:deep(ol ol) {
  list-style-type: lower-alpha;
}

:deep(ol ol ol) {
  list-style-type: lower-roman;
}

:deep(li) {
  margin-top: 0.25rem;
  padding-left: 0.25rem;
}

:deep(li::marker) {
  color: #6a737d;
}

:deep(table) {
  border-collapse: collapse;
  width: 100%;
  margin-bottom: 1rem;
}

:deep(th), :deep(td) {
  padding: 0.5rem;
  border: 1px solid #dfe2e5;
}

:deep(img) {
  max-width: 100%;
  height: auto;
}
</style>
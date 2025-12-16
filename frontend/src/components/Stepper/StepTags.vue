<script setup lang="ts">
const props = defineProps<{
  modelValue: string[];
  title: string;
  label: string;
  placeholder: string;
  color?: string;
}>();

const emit = defineEmits(['update:modelValue']);
</script>

<template>
  <v-container>
    <h3 class="text-h6 mb-4">{{ title }}</h3>
    <v-combobox
      :model-value="modelValue"
      @update:model-value="emit('update:modelValue', $event)"
      :label="label"
      :placeholder="placeholder"
      chips
      multiple
      closable-chips
      variant="outlined"
      :color="color"
      hint="Press enter to add multiple items"
      persistent-hint
    />
  </v-container>
</template>
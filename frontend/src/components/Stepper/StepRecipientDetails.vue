<script setup lang="ts">
  import type { GiftRequest } from '@/types/GiftRequests';

  const props = defineProps<{ modelValue: GiftRequest }>();
</script>

<template>
  <v-container>
    <h3 class="text-h6 mb-4">The Recipient</h3>
    <v-row>
      <v-col cols="12" md="4">
        <v-text-field
          v-model.number="props.modelValue.recipientAge"
          label="Age"
          type="number"
          variant="outlined"
        />
      </v-col>

      <v-col cols="12" md="8">
        <v-select
          v-model="props.modelValue.relationship"
          label="Relationship"
          :items="['Friend', 'Spouse', 'Parent', 'Sibling', 'Colleague', 'Child']"
          variant="outlined"
        />
      </v-col>

      <v-col cols="12">
        <v-text-field
          v-model="props.modelValue.location"
          label="Location"
          placeholder="City, State or Country"
          variant="outlined"
        />
      </v-col>
    </v-row>
  </v-container>
</template>
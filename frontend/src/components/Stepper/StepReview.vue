<script setup lang="ts">
import type { GiftRequest } from '@/types/GiftRequests';

const props = defineProps<{ data: GiftRequest }>();
</script>

<template>
  <v-container>
    <h3 class="text-h6 mb-4 text-center">Is everything correct?</h3>

    <v-card variant="tonal" class="pa-4">
      <v-table density="compact">
        <tbody>
          <tr><th class="text-left">Occasion</th><td>{{ data.occasion }} ({{ data.date }})</td></tr>
          <tr><th class="text-left">Budget</th><td>{{ data.maxBudget }}</td></tr>
          <tr><th class="text-left">Recipient</th><td>{{ data.relationship }} (Age: {{ data.recipientAge }})</td></tr>
          <tr><th class="text-left">Location</th><td>{{ data.location }}</td></tr>
          <tr><th class="text-left">Interests</th><td>{{ data.interests.join(', ') || 'None listed' }}</td></tr>
          <tr><th class="text-left">Dislikes</th><td>{{ data.dislikes.join(', ') || 'None listed' }}</td></tr>
        </tbody>
      </v-table>
    </v-card>
  </v-container>
</template>
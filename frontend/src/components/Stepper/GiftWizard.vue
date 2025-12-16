<script setup lang="ts">
import { ref, reactive } from 'vue';
import { GiftRequest, initialGiftRequest } from '@/types/GiftRequests';

// Step components
import StepEventDetails from './StepEventDetails.vue';
import StepRecipientDetails from './StepRecipientDetails.vue';
import StepTags from './StepTags.vue';
import StepReview from './StepReview.vue';

// State
const step = ref(1);
const loading = ref(false);
const formData = reactive<GiftRequest>({ ...initialGiftRequest });

// Step definitions for the UI
const steps = ['Occasion', 'Recipient', 'Interests', 'Dislikes', 'Review'];

// Submit logic
const submitData = async () => {
  loading.value = true;

  try {
    const response = await fetch('http://localhost:5000/api/generate-gift-ideas', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(formData),
    });

    if (!response.ok) throw new Error('Network response was not ok');

    const result = await response.json()
    console.log('Suggestions received:', result);
    // TODO: Navigate to results page (create results page)
  } catch (error) {
    console.error('Error submitting form:', error);
  } finally {
    loading.value = false;
  }
};
</script>

<template>
  <v-container class="fill-height justify-center">
    <v-card width="100%" max-width="800">
      <v-toolbar color="primary" title="Supimpa Gift Wizard" />

      <v-stepper v-model="step" :items="steps" hide-actions>
        <template v-slot:item.1>
          <step-event-details v-model="formData" />
        </template>

        <template v-slot:item.2>
          <step-recipient-details v-model="formData" />
        </template>

        <template v-slot:item.3>
          <step-tags
            v-model="formData.interests"
            title="What are they into?"
            label="Add Interests"
            placeholder="e.g. Hiking, Sci-Fi, Coffee"
            color="success"
          />
        </template>

        <template v-slot:item.4>
          <step-tags
            v-model="formData.dislikes"
            title="What should we avoid?"
            label="Add Dislikes"
            placeholder="e.g. Plastic, Spicy Food"
            color="error"
          />
        </template>

        <template v-slot:item.5>
          <step-review :data="formData" />
        </template>

        <v-card-actions class="justify-space-between pa-4">
          <v-btn
            v-if="step > 1"
            variant="text"
            @click="step--"
          >
            Back
          </v-btn>
          <v-spacer v-else />

          <v-btn
            v-if="step < 5"
            color="primary"
            variant="flat"
            @click="step++"
          >
            Next
          </v-btn>

          <v-btn
            v-if="step === 5"
            color="success"
            variant="flat"
            :loading="loading"
            @click="submitData"
          >
            Get Suggestions!
          </v-btn>
        </v-card-actions>
      </v-stepper>
    </v-card>
  </v-container>
</template>
<script setup lang="ts">
    import type { GiftRequest } from '@/types/GiftRequests';

    // Accepts the form data object
    const props = defineProps<{
        modelValue: GiftRequest
    }>();

    const emit = defineEmits(['update:modelValue']);

    // Rules for validation
    const required = (v: any) => !!v || 'Field is required';
</script>

<template>
    <v-container>
        <h3 class="text-h6 mb-4">The Occasion</h3>
        <v-row>
            <v-col cols="12">
                <v-text-field
                    v-model="props.modelValue.occasion"
                    label="What's the occasion?"
                    placeholder="e.g. Birthday, Anniversary, Christmas"
                    :rules="[required]"
                    variant="outlined"
                />
            </v-col>
            
            <v-col cols="12" md="6">
                <v-text-field
                    v-model.number="props.modelValue.maxBudget"
                    label="Maximum Budget ($)"
                    type="number"
                    prefix="$"
                    :rules="[required]"
                    variant="outlined"
                />
            </v-col>
        </v-row>
    </v-container>
</template>
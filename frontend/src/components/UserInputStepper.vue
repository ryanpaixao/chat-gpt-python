<template>
  <v-stepper :items="['Step 1', 'Step 2', 'Step 3', 'Step 4', 'Step 5']">
    <template v-slot:item.1>
      <v-card title="Occasion Info" flat>
        1) What's the occasion?
        2) What's the date?
        3) What's the maximum budget?
      </v-card>
    </template>

    <template v-slot:item.2>
      <v-card title="Gift Recipient Info" flat>
        1) What's the recipient's age?
        2) What's the relationship with the recipient?
        3) What's their location?
      </v-card>
    </template>

    <template v-slot:item.3>
      <v-card title="Gift Recipient's Interests" flat>
        1) What are their interests?
      </v-card>
    </template>

    <template v-slot:item.4>
      <v-card title="Gift Recipient's Dislikes" flat>
        1) What are their dislikes?
      </v-card>
    </template>

    <template v-slot:item.5>
      <v-card title="Verify Info" flat>
        ~User Input Data~
        Verify Data is correct.
      </v-card>
    </template>
  </v-stepper>
</template>
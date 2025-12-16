export interface GiftRequest {
    // Step 1
    occasion: string;
    date: string; // YYYY-MM-DD
    maxBudget: number | null;

    // Step 2
    recipientAge: number | null;
    relationship: string;
    location: string;

    // Step 3 & 4
    interests: string[];
    dislikes: string[];
};

export const initialGiftRequest: GiftRequest = {
    occasion: '',
    date: '',
    maxBudget: null,
    recipientAge: null,
    relationship: '',
    location: '',
    interests: [],
    dislikes: [],
};

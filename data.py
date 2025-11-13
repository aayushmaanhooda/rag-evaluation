# ============================================================================
# EVALUATION TEST DATASET
# ============================================================================
# This file contains test questions with ground truth answers for evaluating
# the RAG system. Each example includes:
# - question: The query to test the RAG system with
# - ground_truth: The correct/expected answer based on the source document
#
# These examples are used to measure how well the RAG system retrieves
# relevant information and generates accurate responses.
# NOTE: TO GENERATE SUCH DATASET YOU WILL ALWAYS NEED A DOMAIN EXPERT
# ============================================================================

examples = [
    {
        "question": "Who founded The Ember & Oak Kitchen and what is their background?",
        "ground_truth": "Maria Elena Santiago founded The Ember & Oak Kitchen in March 2019. She has a 15-year career in culinary arts, with degrees from Le Cordon Bleu Paris and Cornell University, and was a James Beard Foundation Rising Star Chef Semifinalist in 2014.",
    },
    {
        "question": "What are the restaurant's hours of operation?",
        "ground_truth": "The Ember & Oak Kitchen is open Tuesday-Thursday 5:00-10:00 PM, Friday-Saturday 5:00-11:00 PM, and Sunday 5:00-9:00 PM for dinner. Weekend brunch is available Saturday-Sunday 10:00 AM-2:00 PM. The restaurant is closed on Mondays.",
    },
    {
        "question": "What is the restaurant's sourcing philosophy?",
        "ground_truth": "The restaurant maintains direct relationships with 23 local farms and producers within a 150-mile radius. Currently, 78% of ingredients are sourced locally, with all seafood vetted through Monterey Bay Aquarium Seafood Watch and all beef and pork from pasture-raised, hormone-free sources.",
    },
    {
        "question": "What is the average check per person at The Ember & Oak Kitchen?",
        "ground_truth": "The average check per person is $65-85 including beverages. The restaurant positions itself as mid-to-high range fine casual dining.",
    },
    {
        "question": "What are the restaurant's sustainability initiatives?",
        "ground_truth": "The restaurant diverts 85% of waste through composting partnerships, uses LED lighting and low-flow water fixtures, sources 78% of ingredients within 150 miles, and plans to install solar panels in 2026. They aim for less than 5% food waste by 2026.",
    },
    {
        "question": "How many employees does the restaurant have and what benefits do they offer?",
        "ground_truth": "The restaurant has 38 total employees (18 kitchen staff and 20 front of house). Full-time employees receive health insurance with 70% premiums paid by the company, 401(k) with 3% match, 10-15 days PTO, 6 paid holidays, and a $500 annual professional development stipend.",
    },
    {
        "question": "What are the restaurant's expansion plans?",
        "ground_truth": "Short-term plans include launching a chef's counter experience, installing solar panels in 2025, and adding outdoor patio seating in 2026. Mid-term goals include opening a second location in 2027 and launching a retail product line in 2028. Long-term vision includes potential expansion to Seattle or Vancouver.",
    },
    {
        "question": "What is the cancellation policy for reservations?",
        "ground_truth": "The restaurant requires 24-hour notice for cancellations or charges a $25 per person fee. No-shows are charged $50 per person. Parties of 7 or more require a credit card to hold the reservation.",
    },
]

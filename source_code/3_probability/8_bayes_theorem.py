def bayes(prior, sensitivity, specificity):
    """
    Calculates your updated chance of having a disease after a positive test.
    
    :param prior: Your original chance of having the disease before testing
    :param sensitivity: How often the test is correct when you DO have the disease
    :param specificity: How often the test is correct when you DO NOT have the disease
    """
    true_positives = sensitivity * prior
    false_positives = (1 - specificity) * (1 - prior)
    
    # True Positives / Total Positives
    return true_positives / (true_positives + false_positives)


# --- Single Test Calculation ---
p1 = bayes(0.01, 0.95, 0.95)      # After 1st positive

print(round(p1, 3))               # Output: 0.161
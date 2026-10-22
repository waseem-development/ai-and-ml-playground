def bayes(prior, sensitivity, specificity):
    # Probability of testing positive if you DO have the disease
    true_positives = sensitivity * prior
    
    # Probability of testing positive if you DO NOT have the disease (False Positive)
    false_positives = (1 - specificity) * (1 - prior)
    
    # Bayes' Theorem: True Positives / Total Positives
    return true_positives / (true_positives + false_positives)


# --- Sequential Testing ---
p1 = bayes(0.01, 0.95, 0.95)      # After 1st positive
p2 = bayes(p1, 0.95, 0.95)        # After 2nd positive

print(round(p1, 3))               # Output: 0.161
print(round(p2, 3))               # Output: 0.785s
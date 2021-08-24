def compute_classification_accuracy(true_positive: int,
                                    false_positive: int,
                                    false_negative: int,
                                    true_negative: int) -> float:
    return (true_positive + true_negative) / \
           (true_positive + true_negative + false_positive + false_negative)


accuracy = compute_classification_accuracy(true_positive=2,
                                           false_positive=2,
                                           false_negative=11,
                                           true_negative=985)
print(f"Classification accuracy: {accuracy}")

def compute_classification_accuracy(total_predictions: int,
                                    correct_predictions: int) -> float:
    return correct_predictions / total_predictions


accuracy = compute_classification_accuracy(total_predictions=365,
                                           correct_predictions=300)
print(f"Classification accuracy: {accuracy * 100:.2f} %")

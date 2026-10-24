def calculate_average(grades: list[float]) -> float:
    if not grades:
        raise ValueError("Список оцінок не може бути порожнім")
    return sum(grades) / len(grades)

def get_highest_grade(grades: list[float]) -> float:
    if not grades:
        raise ValueError("Список оцінок не може бути порожнім")
    return max(grades)

def is_passing(average_score: float, threshold: float = 60.0) -> bool:
    return average_score > threshold

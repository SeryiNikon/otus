def get_pow(*numbers, power=2):
    results = []
    for num in numbers:
        results.append(num ** power)
    return results



def savings_calculator():
    print("--- Калькулятор накопичень ---")
    try:
        monthly_amount = float(input("Введіть суму, яку ви відкладаєте щомісяця (грн): "))
        months = int(input("Введіть кількість місяців: "))
    except ValueError:
        print("Помилка: Будь ласка, введіть коректні числа.")
        return
    current_balance = 0
    print("\nРезультат накопичень:")
    for i in range(1, months + 1):
        current_balance += monthly_amount
        print(f"Місяць {i}: {current_balance} грн")
if __name__ == "__main__":
    savings_calculator()
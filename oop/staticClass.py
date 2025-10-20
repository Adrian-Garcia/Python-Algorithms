
class MathUtils:
    # Static method (does not depend on instance or class state)
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

# Call static methods directly on the class (no instance needed)
sum_result = MathUtils.add(5, 3)
product_result = MathUtils.multiply(4, 6)

print(f"Sum: {sum_result}")
print(f"Product: {product_result}")

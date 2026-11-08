# Using walrus operator
if (n := len([1, 2, 3, 4, 5])) > 3:  # ye list ki length ko n mai store kry or or condition true hony pr if loop chly ga
    print(f"List is too long ({n} elements, expected <= 3)")
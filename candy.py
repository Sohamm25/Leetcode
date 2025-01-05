# Problem: Distribute minimum candies such that:
# - Each child gets at least 1 candy.
# - A child with a higher rating than their neighbor gets more candies.

# Step 1: Initialize variables
ratings = []  # Input list of children's ratings
n = len(ratings)  # Number of children
candies = [1] * n  # Start by giving 1 candy to each child

# Step 2: Traverse from left to right
# - If the current child's rating is higher than the previous child's, give more candies than the previous child.
for i in range(1, n):
    if ratings[i] > ratings[i - 1]:  # Higher rating than the left neighbor
        candies[i] = candies[i - 1] + 1  # Assign one more candy than the left neighbor

# Step 3: Traverse from right to left
# - Ensure that each child still has more candies than their right neighbor if their rating is higher.
for i in range(n - 2, -1, -1):
    if ratings[i] > ratings[i + 1]:  # Higher rating than the right neighbor
        candies[i] = max(candies[i], candies[i + 1] + 1)  # Assign the maximum required candies

# Step 4: Output the total candies required
print(sum(candies))  # Sum up all candies to get the final result

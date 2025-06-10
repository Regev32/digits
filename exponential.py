from uniform import generate_uniform_numbers, plot_histogram
import numpy as np


def generate_exponential_numbers(seed, list_size, lambda_value=1.0):
    # Apply the inverse CDF for the Exponential distribution
    uniform_numbers = generate_uniform_numbers(seed=seed, list_size=list_size)
    exp_numbers = -np.log(uniform_numbers) / lambda_value
    return exp_numbers


if __name__ == '__main__':
    # Example Usage
    seed_50 = 50  # Choose a seed
    size = 10000  # Number of random numbers to generate
    lambda_val = 1.0
    exponential_numbers = generate_exponential_numbers(seed_50, size, lambda_val)
    distribution = f"Exp({lambda_val})"
    # Plot the histogram to check uniformity
    plot_histogram(exponential_numbers, distribution, size)

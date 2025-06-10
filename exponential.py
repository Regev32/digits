from uniform import generate_uniform_numbers
import numpy as np
import matplotlib.pyplot as plt


def generate_exponential_numbers(seed, size, lambda_value=1.0):
    """
    Generate exponential random numbers using the inverse CDF method.

    :param uniform_numbers: List of Uniform[0, 1] random numbers.
    :param lambda_value: The rate parameter (λ) of the exponential distribution.
    :return: A list of exponential random numbers.
    """
    # Apply the inverse CDF for the Exponential distribution
    uniform_numbers = generate_uniform_numbers(seed=seed, size=size)
    exponential_numbers = -np.log(uniform_numbers) / lambda_value
    return exponential_numbers


def plot_histogram(uniform_numbers):
    """Plot the histogram of the generated uniform numbers."""
    plt.figure(figsize=(8, 6))  # Set figure size for better readability
    plt.hist(uniform_numbers, bins=50, density=True, color='skyblue', alpha=0.7, edgecolor='black')
    plt.title('Histogram of Exp(λ) Numbers', fontsize=16, fontweight='bold')
    plt.xlabel('Value', fontsize=14)
    plt.ylabel('Density', fontsize=14)
    plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    # Example Usage
    seed = 50  # Choose a seed
    size = 10000  # Number of random numbers to generate
    exponential_numbers = generate_exponential_numbers(seed, size)

    # Plot the histogram to check uniformity
    plot_histogram(exponential_numbers)

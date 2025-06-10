import matplotlib.pyplot as plt


class MersenneTwister:
    def __init__(self, seed):
        self.w = 32  # Word size in bits
        self.n = 624  # Degree of recurrence
        self.m = 397  # Middle word
        self.r = 31  # Separation point (lower bitmask size)
        self.a = 0x9908B0DF  # Coefficients for the twist transformation
        self.u = 11  # Tempering shift
        self.s = 7  # Tempering shift
        self.t = 15  # Tempering shift
        self.l = 18  # Tempering shift
        self.b = 0x9D2C5680  # Mask for tempering
        self.c = 0xEF600000  # Mask for tempering

        # Initialize the state vector with 624 elements
        self.state = [0] * self.n
        self.index = self.n  # The index for the state vector
        self.initialize_state(seed)

    def initialize_state(self, seed):
        """Initialize the state vector based on the seed."""
        self.state[0] = seed
        for i in range(1, self.n):
            self.state[i] = (1812433253 * (self.state[i - 1] ^ (self.state[i - 1] >> (self.w - 2))) + i) & 0xFFFFFFFF

    def next_random(self):
        """Generate the next random number from the state."""
        if self.index >= self.n:
            # Generate the next state
            self.twist()

        # Temper the value and return it
        y = self.state[self.index]
        self.index += 1

        # Apply tempering
        y ^= (y >> self.u)
        y ^= ((y << self.s) & self.b)
        y ^= ((y << self.t) & self.c)
        y ^= (y >> self.l)

        return y & 0xFFFFFFFF  # Return as a 32-bit number

    def twist(self):
        """Twist the state vector to generate new values."""
        for i in range(self.n):
            y = (self.state[i] & 0x80000000) | (self.state[(i + 1) % self.n] & 0x7FFFFFFF)
            self.state[i] = self.state[(i + self.m) % self.n]
            # Apply tempering to the new value
            y ^= (y >> self.u)
            y ^= ((y << self.s) & self.b)
            y ^= ((y << self.t) & self.c)
            y ^= (y >> self.l)
            self.state[i] = y & 0xFFFFFFFF  # Store back the transformed value

        self.index = 0  # Reset the index to start generating new values


    def generate_uniform(self):
        """Generate a uniform random number in the range [0, 1]."""
        # Get the next 32-bit random number and normalize it
        return self.next_random() / float(2 ** 32)


def generate_uniform_numbers(seed, list_size):
    """Generate a list of uniform [0, 1] numbers."""
    mt = MersenneTwister(seed)
    return [mt.generate_uniform() for _ in range(list_size)]


def plot_histogram(numbers, dist, num_samples):
    """Plot the histogram of the generated uniform numbers."""
    plt.figure(figsize=(8, 6))  # Set figure size for better readability
    plt.hist(numbers, bins=50, density=True, color='skyblue', alpha=0.7, edgecolor='black')
    plt.title(f"Histogram of {num_samples} {dist} Numbers", fontsize=16, fontweight='bold')
    plt.xlabel('Value', fontsize=14)
    plt.ylabel('Density', fontsize=14)
    plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    # Example Usage
    seed_42 = 42  # The answer to everything
    size = 1000000  # Number of random numbers to generate
    uniform_numbers = generate_uniform_numbers(seed_42, size)
    distribution = "Uniform[0, 1]"
    # Plot the histogram to check uniformity
    plot_histogram(uniform_numbers, distribution, size)

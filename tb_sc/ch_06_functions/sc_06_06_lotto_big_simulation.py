# File: sc_06_06_lotto_big_simulation.py
"""
Lotto Simulation: Demonstrating Equal Probability and Trends
Simulates 1 million lotto draws with 34 numbers to show:
1. All numbers have equal probability of being drawn
2. Trends can occur even with equal probability
3. Large sample sizes approach theoretical probability
"""

import random
import statistics
from collections import Counter

def simulate_lotto_draws(num_draws=1_000_000, max_number=34):
    """
    Simulate lotto draws and track frequency of each number.
    
    Args:
        num_draws: Number of draws to simulate (default: 1 million)
        max_number: Highest number in lotto (default: 34)
    
    Returns:
        Tuple of (Counter object with frequency, list of recent draws, list of all draws)
    """
    print(f"Simulating {num_draws:,} lotto draws with numbers 1-{max_number}...")
    
    # Track frequency of each number
    number_frequency = Counter()
    
    # Track all draws for rolling window analysis
    all_draws = []
    
    # Track trends - store last 1000 draws for trend analysis
    recent_draws = []
    trend_window = 1000
    
    for draw in range(num_draws):
        # Draw a random number between 1 and max_number
        drawn_number = random.randint(1, max_number)
        number_frequency[drawn_number] += 1
        all_draws.append(drawn_number)
        
        # Track recent draws for trend analysis
        recent_draws.append(drawn_number)
        if len(recent_draws) > trend_window:
            recent_draws.pop(0)
        
        # Print progress every 100,000 draws
        if (draw + 1) % 100_000 == 0:
            print(f"  Progress: {draw + 1:,} draws completed")
    
    return number_frequency, recent_draws, all_draws

def analyze_distribution(frequency_data, total_draws, max_number):
    """
    Analyze the distribution of drawn numbers.
    
    Args:
        frequency_data: Counter with frequency of each number
        total_draws: Total number of draws performed
        max_number: Highest number in lotto
    """
    print(f"\n=== DISTRIBUTION ANALYSIS ===")
    print(f"Total draws: {total_draws:,}")
    print(f"Numbers range: 1-{max_number}")
    
    # Expected frequency for each number (theoretical)
    expected_frequency = total_draws / max_number
    print(f"Expected frequency per number: {expected_frequency:,.1f}")
    
    # Get actual frequencies
    frequencies = [frequency_data[i] for i in range(1, max_number + 1)]
    
    # Statistics
    min_freq = min(frequencies)
    max_freq = max(frequencies)
    mean_freq = statistics.mean(frequencies)
    std_dev = statistics.stdev(frequencies)
    
    print(f"\nACTUAL FREQUENCIES:")
    print(f"  Minimum frequency: {min_freq:,}")
    print(f"  Maximum frequency: {max_freq:,}")
    print(f"  Mean frequency: {mean_freq:,.1f}")
    print(f"  Standard deviation: {std_dev:.1f}")
    
    # Show deviation from expected
    deviation = abs(mean_freq - expected_frequency)
    deviation_percent = (deviation / expected_frequency) * 100
    print(f"  Deviation from expected: {deviation:.1f} ({deviation_percent:.3f}%)")
    
    return frequencies, expected_frequency

def analyze_rolling_window_trends(all_draws, window_size=50, max_number=34):
    """
    Analyze trends in a rolling window to find numbers that appear frequently
    within short consecutive periods.
    
    Args:
        all_draws: List of all drawn numbers
        window_size: Size of rolling window (default: 50)
        max_number: Highest number in lotto
    """
    print(f"\n=== ROLLING WINDOW TREND ANALYSIS (Window: {window_size} draws) ===")
    
    # Track how often each number appears as "hot" in rolling windows
    hot_number_count = Counter()
    total_windows = 0
    significant_trends = []  # Store windows with significant trends
    
    # Slide window through all draws
    for i in range(len(all_draws) - window_size + 1):
        window = all_draws[i:i + window_size]
        window_frequency = Counter(window)
        
        # Expected frequency in window (uniform distribution)
        expected_in_window = window_size / max_number
        
        # Find numbers that appear significantly more than expected
        for number, count in window_frequency.items():
            # Consider "hot" if appears more than 2x expected frequency
            if count >= expected_in_window * 2:
                hot_number_count[number] += 1
                
                # Store significant trends (3+ appearances in 50 draws)
                if count >= 3:
                    significant_trends.append({
                        'window_start': i,
                        'window_end': i + window_size - 1,
                        'number': number,
                        'count': count,
                        'percentage': (count / window_size) * 100
                    })
        
        total_windows += 1
        
        # Progress indicator for large datasets
        if (i + 1) % 100_000 == 0:
            print(f"  Analyzed {i + 1:,} rolling windows...")
    
    # Report numbers that frequently appear as "hot"
    print(f"\nNumbers that frequently appear as 'hot' in rolling windows:")
    print(f"(Analyzed {total_windows:,} windows of {window_size} draws each)")
    
    most_trending = hot_number_count.most_common(10)
    for number, hot_count in most_trending:
        percentage = (hot_count / total_windows) * 100
        print(f"  Number {number}: appeared as 'hot' in {hot_count:,} windows ({percentage:.2f}%)")
    
    # Show most significant individual trends
    print(f"\nMost significant individual trends (3+ occurrences in {window_size} draws):")
    significant_trends.sort(key=lambda x: x['count'], reverse=True)
    
    for i, trend in enumerate(significant_trends[:10]):  # Top 10
        print(f"  #{i+1}: Number {trend['number']} appeared {trend['count']} times "
              f"({trend['percentage']:.1f}%) in draws {trend['window_start']:,}-{trend['window_end']:,}")
    
    return hot_number_count, significant_trends

def find_trends(frequency_data, recent_draws, max_number, all_draws=None):
    """
    Identify trends in the lottery data.
    
    Args:
        frequency_data: Counter with overall frequency
        recent_draws: List of recent draws for trend analysis
        max_number: Highest number in lotto
        all_draws: List of all draws for rolling window analysis
    """
    print(f"\n=== TREND ANALYSIS ===")
    
    # Overall trends - most and least frequent numbers
    most_common = frequency_data.most_common(5)
    least_common = frequency_data.most_common()[-5:]
    
    print("OVERALL TRENDS (all draws):")
    print("Most frequently drawn numbers:")
    for number, count in most_common:
        percentage = (count / sum(frequency_data.values())) * 100
        print(f"  Number {number}: {count:,} times ({percentage:.2f}%)")
    
    print("\nLeast frequently drawn numbers:")
    for number, count in reversed(least_common):
        percentage = (count / sum(frequency_data.values())) * 100
        print(f"  Number {number}: {count:,} times ({percentage:.2f}%)")
    
    # Recent trends - last 1000 draws
    recent_frequency = Counter(recent_draws)
    recent_most_common = recent_frequency.most_common(3)
    
    print(f"\nRECENT TRENDS (last {len(recent_draws)} draws):")
    print("Hot numbers (most frequent recently):")
    for number, count in recent_most_common:
        percentage = (count / len(recent_draws)) * 100
        print(f"  Number {number}: {count} times ({percentage:.1f}%)")
    
    # Cold numbers (haven't appeared recently)
    all_numbers = set(range(1, max_number + 1))
    recent_numbers = set(recent_draws)
    cold_numbers = all_numbers - recent_numbers
    
    if cold_numbers:
        print(f"\nCold numbers (not drawn in last {len(recent_draws)} draws):")
        for number in sorted(cold_numbers):
            print(f"  Number {number}")
    else:
        print(f"\nAll numbers appeared in last {len(recent_draws)} draws")
    
    # Rolling window analysis if all draws provided
    if all_draws:
        analyze_rolling_window_trends(all_draws, 50, max_number)

def demonstrate_equal_probability(frequencies, expected_frequency, max_number):
    """
    Demonstrate that despite trends, all numbers have equal probability.
    
    Args:
        frequencies: List of actual frequencies
        expected_frequency: Theoretical expected frequency
        max_number: Highest number in lotto
    """
    print(f"\n=== EQUAL PROBABILITY DEMONSTRATION ===")
    
    # Calculate how close we are to equal probability
    deviations = [abs(freq - expected_frequency) for freq in frequencies]
    max_deviation = max(deviations)
    max_deviation_percent = (max_deviation / expected_frequency) * 100
    
    print(f"Maximum deviation from expected frequency: {max_deviation:.1f}")
    print(f"Maximum deviation percentage: {max_deviation_percent:.2f}%")
    
    # Show that deviations are within expected range for random sampling
    # For large samples, standard error ≈ sqrt(np(1-p)) where p = 1/max_number
    total_draws = sum(frequencies)
    probability = 1 / max_number
    expected_std_error = (total_draws * probability * (1 - probability)) ** 0.5
    
    print(f"\nExpected standard error for random sampling: {expected_std_error:.1f}")
    print(f"Actual standard deviation: {statistics.stdev(frequencies):.1f}")
    
    # Count numbers within 1, 2, and 3 standard deviations
    within_1_std = sum(1 for freq in frequencies if abs(freq - expected_frequency) <= expected_std_error)
    within_2_std = sum(1 for freq in frequencies if abs(freq - expected_frequency) <= 2 * expected_std_error)
    within_3_std = sum(1 for freq in frequencies if abs(freq - expected_frequency) <= 3 * expected_std_error)
    
    print(f"\nNumbers within 1 std dev: {within_1_std}/{max_number} ({within_1_std/max_number*100:.1f}%)")
    print(f"Numbers within 2 std dev: {within_2_std}/{max_number} ({within_2_std/max_number*100:.1f}%)")
    print(f"Numbers within 3 std dev: {within_3_std}/{max_number} ({within_3_std/max_number*100:.1f}%)")
    
    print("\nExpected for normal distribution:")
    print("  ~68% within 1 std dev")
    print("  ~95% within 2 std dev")
    print("  ~99.7% within 3 std dev")

def display_detailed_results(frequency_data, max_number):
    """
    Display detailed frequency results for all numbers.
    
    Args:
        frequency_data: Counter with frequency of each number
        max_number: Highest number in lotto
    """
    print(f"\n=== DETAILED FREQUENCY TABLE ===")
    total_draws = sum(frequency_data.values())
    expected = total_draws / max_number
    
    print(f"{'Number':<6} {'Frequency':<10} {'Percentage':<10} {'Deviation':<10}")
    print("-" * 46)
    
    for number in range(1, max_number + 1):
        freq = frequency_data[number]
        percentage = (freq / total_draws) * 100
        deviation = freq - expected
        
        print(f"{number:<6} {freq:<10,} {percentage:<10.2f} {deviation:<+10.0f}")

def main():
    """Main function to run the lotto simulation."""
    print("LOTTO SIMULATION: Equal Probability and Trends")
    print("=" * 50)
    
    # Set random seed for reproducible results (optional)
    # random.seed(42)  # Uncomment for reproducible results
    
    # Simulation parameters
    NUM_DRAWS = 1_000_000
    MAX_NUMBER = 34
    
    # Run simulation
    frequency_data, recent_draws, all_draws = simulate_lotto_draws(NUM_DRAWS, MAX_NUMBER)
    
    # Analyze results
    frequencies, expected_freq = analyze_distribution(frequency_data, NUM_DRAWS, MAX_NUMBER)
    find_trends(frequency_data, recent_draws, MAX_NUMBER, all_draws)
    demonstrate_equal_probability(frequencies, expected_freq, MAX_NUMBER)
    
    # Show detailed results
    display_detailed_results(frequency_data, MAX_NUMBER)
    
    print(f"\n=== CONCLUSION ===")
    print("This simulation demonstrates that:")
    print("1. All numbers have equal probability in the long run")
    print("2. Trends and 'hot/cold' numbers are natural random variations")
    print("3. Large sample sizes converge to theoretical probability")
    print("4. Past draws do not influence future draw probabilities")

if __name__ == "__main__":
    main()

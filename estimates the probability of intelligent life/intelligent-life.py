def probability_of_intelligent_life(years_after_big_bang):
    # Constants in years (converted to billions for simplicity)
    current_time = 13.8 # Current time after the Big Bang in billion years
    end_of_stars = 1_000_000 # When most stars will die in billion years

    # Convert input years to billion years
    t = years_after_big_bang / 1_000_000_000  

    if t < 0:
        return 0.0 # No intelligent life before the Big Bang
    elif t <= current_time:
        # Linearly increase probability from 0% to 100%
        return t / current_time * 100
    elif t <= end_of_stars:
        # Linearly decrease probability from 100% to 0%
        return max(0, 100 - ((t - current_time) / (end_of_stars - current_time) * 100))
    else:
        return 0.0 # No intelligent life after stars die

# Example usage
years = [0, 1e9, 5e9, 13.8e9, 50e9, 500e9, 1e12, 2e12]
for year in years:
    prob = probability_of_intelligent_life(year)
    print(f"Years after Big Bang: {year:.1e}, Probability of Intelligent Life: {prob:.2f}%")

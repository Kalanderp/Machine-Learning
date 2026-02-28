def find_s(training_data):
    hypothesis = training_data[0][:-1]
    for example in training_data:
        if example[-1] == "Yes":  
            for i in range(len(hypothesis)):
                if hypothesis[i] != example[i]:
                    hypothesis[i] = "?"
    return hypothesis
data = [
    ["Sunny", "Warm", "Normal", "Strong", "Warm", "Same", "Yes"],
    ["Sunny", "Warm", "High", "Strong", "Warm", "Same", "Yes"],
    ["Rainy", "Cold", "High", "Strong", "Warm", "Change", "No"],
    ["Sunny", "Warm", "High", "Strong", "Cool", "Change", "Yes"]
]
final_hypothesis = find_s(data)
print("Final Hypothesis:")
print(final_hypothesis)

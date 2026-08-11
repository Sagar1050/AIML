# Candidate Elimination Algorithm
# Experiment: Implementation of Candidate Elimination Algorithm

# Training Dataset
data = [
    ["Sunny", "Warm", "Normal", "Strong", "Yes"],   # D1
    ["Sunny", "Warm", "High", "Strong", "Yes"],     # D2
    ["Rainy", "Cold", "High", "Strong", "No"],      # D3
    ["Sunny", "Warm", "High", "Weak", "Yes"]        # D4
]

# Attributes
attributes = ["Sky", "AirTemp", "Humidity", "Wind"]

# Most Specific Boundary
S = ["Ø", "Ø", "Ø", "Ø"]

# Most General Boundary
G = [["?", "?", "?", "?"]]


# Function to check if a hypothesis covers an instance
def covers(hypothesis, instance):
    for h, value in zip(hypothesis, instance):
        if h != "?" and h != value:
            return False
    return True


# Function to generalize S
def generalize_S(S, instance):
    new_S = S.copy()

    for i in range(len(S)):
        if S[i] == "Ø":
            new_S[i] = instance[i]
        elif S[i] != instance[i]:
            new_S[i] = "?"

    return new_S


# Function to specialize G
def specialize_G(G, instance, S):
    new_G = []

    for hypothesis in G:
        for i in range(len(instance)):
            if hypothesis[i] == "?":
                if S[i] != "?" and S[i] != "Ø":
                    new_hypothesis = hypothesis.copy()
                    new_hypothesis[i] = S[i]

                    if not covers(new_hypothesis, instance):
                        new_G.append(new_hypothesis)

    return new_G


# Remove hypotheses from G that do not cover positive instance
def remove_inconsistent_G(G, instance):
    return [h for h in G if covers(h, instance)]


# Remove hypotheses from S that do not cover positive instance
def remove_inconsistent_S(S, instance):
    if covers(S, instance):
        return S
    return S


# -------------------------------
# Candidate Elimination Algorithm
# -------------------------------

print("=" * 60)
print("       CANDIDATE ELIMINATION ALGORITHM")
print("=" * 60)

print("\nInitial Boundaries:")
print("S =", S)
print("G =", G)

for step, row in enumerate(data, start=1):

    instance = row[:-1]
    target = row[-1]

    print("\n" + "-" * 60)
    print("Processing D" + str(step))
    print("Instance :", instance)
    print("Target   :", target)

    # ---------------------------
    # Positive Instance
    # ---------------------------
    if target == "Yes":

        # Generalize S to cover positive example
        S = generalize_S(S, instance)

        # Remove hypotheses from G that don't cover positive example
        G = remove_inconsistent_G(G, instance)

    # ---------------------------
    # Negative Instance
    # ---------------------------
    else:

        # Specialize G to exclude negative example
        G = specialize_G(G, instance, S)

    print("\nAfter processing D" + str(step) + ":")
    print("S =", S)
    print("G =", G)


# -------------------------------
# Final Version Space
# -------------------------------

print("\n" + "=" * 60)
print("             FINAL VERSION SPACE")
print("=" * 60)

print("\nSpecific Boundary (S):")
print(S)

print("\nGeneral Boundary (G):")
for hypothesis in G:
    print(hypothesis)

print("\n" + "=" * 60)
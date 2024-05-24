# Define the weights for each skill
health_weight = 0.2
agility_weight = 0.3
charisma_weight = 0.1
knowledge_weight = 0.05
energy_weight = 0.05
resourcefulness_weight = 0.3


# Define the function to calculate the score for each skill
def calculate_score(skill_value, skill_weight):
    return round(6 * (int(skill_value) * skill_weight)) + 10


# Define the function to calculate the overall value
def calculate_overall_value(
    health, agility, charisma, knowledge, energy, resourcefulness
):
    return round(
        5
        * (
            (health * 0.18)
            + (agility * 0.20)
            + (charisma * 0.21)
            + (knowledge * 0.08)
            + (energy * 0.17)
            + (resourcefulness * 0.16)
        )
    )


# Read the data
with open(
    "D:\\Users\\curtismechling\\Documents\\CTFs\\Hack The Box\\Business CTF 2024\\Coding\\coding_computational_recruiting\\data.txt",
    "r",
    encoding="utf-8",
) as file:
    lines = file.readlines()

people = []

# Parse each line and calculate scores
for line in lines[4:203]:  # Skip the header
    data = line.strip().split()
    first_name = data[0]
    last_name = data[1]
    health = int(data[2])
    agility = int(data[3])
    charisma = int(data[4])
    knowledge = int(data[5])
    energy = int(data[6])
    resourcefulness = int(data[7])

    # Calculate individual skill scores
    health_score = calculate_score(health, health_weight)
    agility_score = calculate_score(agility, agility_weight)
    charisma_score = calculate_score(charisma, charisma_weight)
    knowledge_score = calculate_score(knowledge, knowledge_weight)
    energy_score = calculate_score(energy, energy_weight)
    resourcefulness_score = calculate_score(resourcefulness, resourcefulness_weight)

    # Calculate overall value
    overall_value = calculate_overall_value(
        health_score,
        agility_score,
        charisma_score,
        knowledge_score,
        energy_score,
        resourcefulness_score,
    )

    people.append(
        {"first_name": first_name, "last_name": last_name, "score": overall_value}
    )

# Sort the people by score
sorted_people = sorted(people, key=lambda x: x["score"], reverse=True)

# Print the top 14 people
output = ", ".join(
    [
        f"{person['first_name']} {person['last_name']} - {person['score']}"
        for person in sorted_people[:14]
    ]
)
print(output)

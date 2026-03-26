# Mood vs Productivity Analyzer
# Simple AI + Graph + ML Project

import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Lists to store user data
moods = []
study_hours_list = []
sleep_hours_list = []
productivity_list = []

# Function to convert mood into number
def convert_mood(mood):
    if mood == "happy":
        return 3
    elif mood == "neutral":
        return 2
    elif mood == "sad":
        return 1
    else:
        return 2  # default value

# Taking user input
while True:
    print("\nEnter your daily details:")
    
    mood_input = input("Mood (happy/neutral/sad): ").lower()
    study = float(input("Study hours: "))
    sleep = float(input("Sleep hours: "))
    
    mood_value = convert_mood(mood_input)
    
    # Simple formula to calculate productivity
    productivity = (mood_value * 2 + study * 1.5 + sleep) / 3
    
    # Store values
    moods.append(mood_value)
    study_hours_list.append(study)
    sleep_hours_list.append(sleep)
    productivity_list.append(productivity)
    
    print("Your productivity score is:", round(productivity, 2))
    
    # Suggestions based on input
    print("\nSuggestions:")
    
    if mood_input == "sad":
        print("- Try taking a short break or do light revision.")
    elif mood_input == "neutral":
        print("- Stay consistent with your study.")
    else:
        print("- Great mood! This is the best time to study.")
    
    if study < 3:
        print("- Try to increase your study time.")
    
    if sleep < 5:
        print("- You should sleep more for better focus.")
    
    # Continue or stop
    choice = input("\nDo you want to add more data? (yes/no): ").lower()
    if choice != "yes":
        break

# =====================
# Graphs
# =====================

print("\nGenerating graphs...")

# Mood vs Productivity
plt.figure()
plt.scatter(moods, productivity_list)
plt.xlabel("Mood (1=Sad, 2=Neutral, 3=Happy)")
plt.ylabel("Productivity")
plt.title("Mood vs Productivity")
plt.show()

# Study vs Productivity
plt.figure()
plt.plot(study_hours_list, productivity_list, marker='o')
plt.xlabel("Study Hours")
plt.ylabel("Productivity")
plt.title("Study vs Productivity")
plt.show()

# =====================
# Machine Learning
# =====================

if len(moods) >= 3:
    X = []
    
    for i in range(len(moods)):
        X.append([moods[i], study_hours_list[i], sleep_hours_list[i]])
    
    y = productivity_list
    
    X = np.array(X)
    y = np.array(y)
    
    model = LinearRegression()
    model.fit(X, y)
    
    # Predict for last entry
    prediction = model.predict([[moods[-1], study_hours_list[-1], sleep_hours_list[-1]]])
    
    print("\nPredicted productivity (ML):", round(prediction[0], 2))
else:
    print("\nAdd at least 3 entries to use ML prediction.")

# =====================
# Average
# =====================

if len(productivity_list) > 0:
    avg = sum(productivity_list) / len(productivity_list)
    print("\nAverage productivity:", round(avg, 2))

print("\nThank you for using the program!")
import matplotlib.pyplot as plt

# Define the application categories and their counts
applications = {
    "Traffic Monitoring": 5,
    "Accident Prevention": 3,
    "Urban Planning": 4,
    "Environmental Assessment": 2,
    "Commercial Use": 3
}

# Define colors for each category
colors = ["#FF9999", "#66B3FF", "#99FF99", "#FFCC99", "#FFD700"]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Create a bar chart
bars = ax.bar(applications.keys(), applications.values(), color=colors, edgecolor='black')

# Set title and labels
ax.set_title("Applications of Vehicle Detection System by Category", fontsize=16)
ax.set_xlabel("Application Category", fontsize=12)
ax.set_ylabel("Count", fontsize=12)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Annotate each bar with its value
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 0.1, yval, ha='center', va='bottom', fontsize=10)

# Show the plot
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt

# Data for pie chart
labels = ['Office', 'Home', 'Other Locations']
sizes = [50, 21, 29]
colors = ['#36A2EB', '#FF6384', '#FFCE56']
explode = (0, 0, 0)

plt.figure(figsize=(6, 4))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.0f%%', startangle=140)
plt.title('Distribution of Work Locations in 2023')
plt.axis('equal')
plt.savefig('C:\\Users\\User\\Documents\\L2-Ongoing\\June Task\\N57214\\work_locations.png', bbox_inches='tight')
plt.close()

# Create second chart - productivity impact
fig, ax = plt.subplots(figsize=(8, 5))
categories = ['Open Plan Office', 'Well-Designed Office', 'Poor Lighting', 'Natural Lighting']
productivity_impact = [-37, +19, -15, +23]
colors_bar = ['#FF6384', '#36A2EB', '#FF6384', '#36A2EB']

bars = ax.bar(categories, productivity_impact, color=colors_bar)
ax.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
ax.set_ylabel('Productivity Impact (%)')
ax.set_title('Impact of Office Design Elements on Staff Productivity')
ax.set_ylim(-40, 30)

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
            f'{height}%', ha='center', va='bottom' if height > 0 else 'top')

plt.xticks(rotation=15, ha='right')
plt.tight_layout()
plt.savefig('C:\\Users\\User\\Documents\\L2-Ongoing\\June Task\\N57214\\productivity_impact.png', bbox_inches='tight')
plt.close()

print("Charts created successfully!")
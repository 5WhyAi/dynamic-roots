# Let's fix the error by using numpy arrays for the divorce_band so that we can perform comparisons.
divorce_band = np.array([0 if age < 28 else 0.2 if 28 <= age < 32 else
                         0.5 if 32 <= age < 37 else 0.8 if 37 <= age < 42 else 1 for age in age_range])

# Creating the gradient band with numpy for proper comparisons
fig, ax = plt.subplots(figsize=(14, 8))

# Plot responsibility levels
ax.plot(age_range, responsibility_over_age, color='blue', linewidth=2, label='Responsibility Over Age')

# Fill the area under the curve with gradient bands for divorce complexity
ax.fill_between(age_range, 0, responsibility_over_age, color='blue', alpha=0.2)

# Use a continuous color map for divorce complexity as gradient bands
norm = plt.Normalize(vmin=min(divorce_band), vmax=max(divorce_band))
sm = plt.cm.ScalarMappable(cmap='coolwarm', norm=norm)
sm.set_array([])
ax.fill_between(age_range, 0, responsibility_over_age, where=(divorce_band > 0), color=sm.to_rgba(divorce_band))

# Add annotations for key life milestones
for age, event in milestones.items():
    ax.annotate(event, xy=(age, responsibility_levels['Self + Partner']), xytext=(age, responsibility_levels['Self + Partner'] + 0.5),
                arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, color='darkred')

# Add some stress points and callouts for key intersections
stress_points = [32, 37]
for point in stress_points:
    ax.annotate('High Stress', xy=(point, responsibility_levels['Self + Partner + Children + Career']),
                xytext=(point, responsibility_levels['Self + Partner + Children + Career'] + 0.5),
                arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, color='darkblue')

# Set labels and title
ax.set_title('Enhanced View: Responsibility, Divorce Complexity, and Life Milestones', fontsize=14, fontweight='bold')
ax.set_xlabel('Age', fontsize=12)
ax.set_ylabel('Responsibility Level', fontsize=12)
ax.set_yticks([1, 2, 3, 4, 5])
ax.set_yticklabels(['Self', 'Self + Partner', 'Self + Partner + Children', 'Self + Career + Children', 'Self + Career + Divorce'])

# Adding the colorbar for divorce complexity
cbar = plt.colorbar(sm)
cbar.set_label('Divorce Complexity / Duration')

# Display the refined chart
plt.tight_layout()
plt.show()

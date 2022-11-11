"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""

text = input("Please enter your age : ")

age = int(text)

range = (220 - age)
max = range * 0.85
min = range * 0.65

print("When you exercise to strengthen your heart, you should")
print(f"Keep your heart rate between {min: .0f} and {max: .0f}")
print("beats per minute.")
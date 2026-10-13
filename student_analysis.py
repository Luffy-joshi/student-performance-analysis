
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ==========================================
# 1. PROJECT SETUP
# ==========================================

OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

sns.set_theme(style="whitegrid")


# ==========================================
# 2. CREATE THE STUDENT DATASET
# ==========================================

data = {
    "Name": [
        "Aarav", "Sita", "Hari", "Maya", "Rohan",
        "Anisha", "Bikash", "Priya", "Kiran", "Nisha"
    ],
    "Math": [85, 92, 67, 78, 56, 95, 72, 88, 61, 80],
    "Science": [78, 89, 72, 85, 60, 91, 75, 82, 65, 87],
    "English": [82, 95, 70, 80, 63, 88, 79, 91, 68, 84],
    "Study_Hours": [4, 6, 2, 4, 1, 7, 3, 5, 2, 5]
}

df = pd.DataFrame(data)


# ==========================================
# 3. HANDLE MISSING DATA
# ==========================================

# Demonstration only: make Hari's Math mark missing.
# This lets us demonstrate a common data-cleaning technique.
df.loc[2, "Math"] = np.nan

print("Missing values before cleaning:")
print(df.isnull().sum())

# Fill missing subject marks with that subject's mean.
subjects = ["Math", "Science", "English"]

for subject in subjects:
    df[subject] = df[subject].fillna(df[subject].mean())

print("\nMissing values after cleaning:")
print(df.isnull().sum())


# ==========================================
# 4. CALCULATE AVERAGES AND GRADES
# ==========================================

df["Average"] = df[subjects].mean(axis=1).round(2)


def assign_grade(average):
    if average >= 80:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 40:
        return "C"
    else:
        return "Fail"


df["Grade"] = df["Average"].apply(assign_grade)


# ==========================================
# 5. NUMERICAL ANALYSIS WITH NUMPY
# ==========================================

math_marks = df["Math"].to_numpy()

print("\nMath statistics:")
print("Mean:", round(np.mean(math_marks), 2))
print("Median:", round(np.median(math_marks), 2))
print("Standard deviation:", round(np.std(math_marks), 2))


# ==========================================
# 6. STUDENT PERFORMANCE REPORT
# ==========================================

print("\n===== STUDENT PERFORMANCE REPORT =====")
print("Total students:", len(df))
print("Class average:", round(df["Average"].mean(), 2))
print("Highest average:", df["Average"].max())
print("Lowest average:", df["Average"].min())

best_index = df["Average"].idxmax()
print("Best-performing student:", df.loc[best_index, "Name"])

print("\nGrade distribution:")
print(df["Grade"].value_counts().sort_index())

print("\nSubject averages:")
print(df[subjects].mean().round(2))

print("\nTop 3 students:")
print(
    df.sort_values("Average", ascending=False)
      [["Name", "Average", "Grade"]]
      .head(3)
      .to_string(index=False)
)


# ==========================================
# 7. VISUALIZATION 1: SUBJECT AVERAGES
# ==========================================

subject_averages = df[subjects].mean()

plt.figure(figsize=(8, 5))
subject_averages.plot(kind="bar")
plt.title("Average Marks by Subject")
plt.xlabel("Subject")
plt.ylabel("Average Marks")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "subject_averages.png", dpi=150)
plt.show()
plt.close()


# ==========================================
# 8. VISUALIZATION 2: STUDENT AVERAGES
# ==========================================

plt.figure(figsize=(10, 5))
sns.barplot(data=df, x="Name", y="Average")
plt.title("Average Marks of Students")
plt.xlabel("Student Name")
plt.ylabel("Average Marks")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "student_averages.png", dpi=150)
plt.show()
plt.close()


# ==========================================
# 9. VISUALIZATION 3: STUDY HOURS VS MATH
# ==========================================

plt.figure(figsize=(8, 5))
sns.regplot(data=df, x="Study_Hours", y="Math")
plt.title("Study Hours vs. Mathematics Marks")
plt.xlabel("Study Hours")
plt.ylabel("Math Marks")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "study_hours_vs_math.png", dpi=150)
plt.show()
plt.close()


# ==========================================
# 10. VISUALIZATION 4: CORRELATION HEATMAP
# ==========================================

correlation = df[
    ["Math", "Science", "English", "Study_Hours"]
].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Student Performance Correlation Heatmap")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "correlation_heatmap.png", dpi=150)
plt.show()
plt.close()


# ==========================================
# 11. SAVE THE CLEANED DATA
# ==========================================

df.to_csv(OUTPUT_DIR / "cleaned_student_data.csv", index=False)

print("\nProject complete!")
print("Charts and cleaned data saved in the outputs folder.")

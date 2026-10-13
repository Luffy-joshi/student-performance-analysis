# Student Performance Data Analysis

A beginner-friendly Python data analysis project exploring student marks, study hours, and academic performance using NumPy, Pandas, Matplotlib, and Seaborn.

## Project Overview

This project analyzes a sample dataset of 10 students. It calculates subject averages, assigns grades, handles a missing numerical value, and creates visualizations to explore student performance.

## Objectives

- Calculate mean, median, and standard deviation.
- Analyze average marks across subjects.
- Rank students by their average marks.
- Assign grades using Python functions and conditional statements.
- Demonstrate missing-value detection and imputation.
- Visualize student performance and correlations.
- Export cleaned data and charts.

## Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn

## Project Structure

```text
student-performance-analysis/
├── student_analysis.py
├── requirements.txt
├── README.md
├── .gitignore
└── outputs/
    ├── subject_averages.png
    ├── student_averages.png
    ├── study_hours_vs_math.png
    ├── correlation_heatmap.png
    └── cleaned_student_data.csv
```

## How to Run

1. Install Python 3.
2. Clone or download this repository.
3. Install the dependencies:

   ```bash
   python3 -m pip install -r requirements.txt
   ```

4. Run the analysis:

   ```bash
   python3 student_analysis.py
   ```

Charts and the cleaned dataset will be saved in the `outputs/` folder.

## Data Note

The dataset is sample data created for learning purposes, not real student records. One Math value is deliberately made missing to demonstrate missing-value handling. The missing value is replaced with the mean of the available Math marks.

## Learning Outcomes

This project provided hands-on experience with Python functions, Pandas DataFrames, NumPy statistics, missing-value handling, data visualization, and basic exploratory data analysis.

## Future Improvements

- Use a larger, real-world dataset with appropriate privacy safeguards.
- Explore more relationships between study habits and marks.
- Build a machine-learning model to predict academic outcomes.
- Add automated tests and more detailed analysis.

## Author

A beginner Python and data analysis project built as part of my learning journey toward AI and machine learning.
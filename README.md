# data_analysis_by-_using_pandas_DEP
---

## Employee Data Analysis

## Objectives

The objective of this code is to perform exploratory data analysis (EDA) on an employee dataset. The analysis includes various visualizations to understand the distribution of genders, salaries, and the relationship between salary and experience. The main goals are:

1. To provide a statistical summary of the dataset.
2. To visualize the distribution of gender and salary.
3. To identify any missing values and handle them appropriately.
4. To explore the correlation between different variables in the dataset.
5. To generate visualizations for better insights into the data.

## Requirements

To run this script, you need to have the following Python libraries installed:
- `pandas`
- `matplotlib`
- `seaborn`

You can install these libraries using pip if they are not already installed:
```bash
pip install pandas matplotlib seaborn
```

## Dataset

The script uses a dataset named `employees.csv`. Ensure this file is in the same directory as the script or provide the correct path to the file.

## Script Description

This script performs the following steps:

1. **Load the Dataset**: Reads the employee data from `employees.csv`.
2. **Basic Information**: Displays basic information about the dataset, including a statistical summary.
3. **Missing Values**: Checks for and drops any rows with missing values.
4. **Visualizations**:
   - **Gender Distribution**: A bar plot showing the distribution of employees by gender.
   - **Average Salary by Gender**: A bar plot showing the average salary for each gender.
   - **Salary Distribution**: A histogram showing the distribution of salaries among employees.
   - **Correlation Heatmap**: A heatmap displaying the correlation between different numerical features in the dataset.
   - **Salary vs. Experience**: A scatter plot showing the relationship between years of experience and salary, with points colored by gender.
   - **Box Plot of Salary by Gender**: A box plot showing the distribution of salaries for each gender.

5. **Output Files**: The visualizations are saved as PNG images in the same directory as the script:
   - `gender_distribution.png`
   - `average_salary_by_gender.png`
   - `salary_distribution.png`
   - `correlation_heatmap.png`
   - `salary_vs_experience.png`
   - `box_plot_salary_by_gender.png`

## Usage

1. Ensure you have the required libraries installed.
2. Place the `employees.csv` file in the same directory as this script.
3. Run the script using Python:
   ```bash
   python your_script_name.py
   ```
4. The script will generate and save several plots to the directory.

## How to Run This Code on Google Colab

1. **Upload the Dataset**:
   - Open Google Colab.
   - Go to the left sidebar and click on the `Files` tab.
   - Click `Upload` and select the `employees.csv` file from your local machine.

2. **Set Up the Environment**:
   - Ensure that the necessary libraries (`pandas`, `matplotlib`, and `seaborn`) are installed. You can install them using:
     ```python
     !pip install pandas matplotlib seaborn
     ```

3. **Run the Code**:
   - Copy and paste the provided code into a new Colab notebook cell.
   - Execute the cell by clicking the `Run` button or pressing `Shift + Enter`.

4. **Download Result Files**:
   - After running the code, the result files (images) will be saved in the working directory.
   - To download them, use the following commands:
     ```python
     from google.colab import files
     files.download('gender_distribution.png')
     files.download('average_salary_by_gender.png')
     files.download('salary_distribution.png')
     files.download('correlation_heatmap.png')
     files.download('salary_vs_experience.png')
     files.download('box_plot_salary_by_gender.png')
     ```

## Purpose

The purpose of this code is to provide an initial analysis of the employee dataset to understand key trends and patterns. The visualizations help to illustrate:

- The distribution of employees by gender.
- How salaries vary by gender and experience.
- The overall salary distribution.
- The correlation between different numerical variables.

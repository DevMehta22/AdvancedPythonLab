import pandas as pd

students_csv = pd.read_csv("student_grades.csv")

def avg_marks(df):
    return (df['Maths'] + df['Science'] + df['English']) / 3

students_csv['Average'] = avg_marks(students_csv)
result_df = students_csv[['Student_name', 'Average']]
result_df.to_csv("student_average_list.csv", index=False)
import matplotlib.pyplot as plt
import pandas as pd
# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
import plotly.express as px
import csv


def plot_survey2_data():
    with open('data01/survey2.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        # results = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]*10
        rows = ["On a scale of 1-10, how much do you feel appreciated for your work?",
                'How would you rate the relationships between colleagues from 1 to 10?',
                'How would you rate your work-life balance from 1 to 10?',
                'How would you rate your relationship with your superiors from 1 to 10?',
                'In your opinion, how stable to you experience the company’s financial stability from 1 to 10?',
                'How would you rate the learning and career development opportunities in your job from 1 to 10?',
                'How do you experience the Job security from 1 to 10?',
                'How satisfied are you with your salary from 1 to 10?',
                'How interested are you in the contents of your job from 1 to 10?',
                'How much do you agree with the company values from 1 to 10?']
        data = []
        results = [[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]]
        female = 0
        male = 0

        """for row in csv_reader:
            data.append(
                [row['Gender'], int(row['On a scale of 1-10, how much do you feel appreciated for your work?'])])

            if row['Gender'] == 'Male':
                male += 1
            else:
                female += 1"""

        for row in csv_reader:
            for i, question in enumerate(rows):
                if row['Gender'] == 'Female':
                    if i == 0:
                        female += 1
                    results[i][0][int(row[question]) - 1] += 1
                elif row['Gender'] == 'Male':
                    if i == 0:
                        male += 1
                    results[i][1][int(row[question]) - 1] += 1

    # in percentages
    for i in range(0, 10):
        temp_male = [i, 'male']
        temp_female = [i, 'female']
        for a in range(len(rows)):
            results[a][1][i] /= male
            results[a][0][i] /= female
            temp_male.append(results[a][1][i])
            temp_female.append(results[a][0][i])
        data.append(temp_male)
        data.append(temp_female)

    # fig = px.bar(x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], y=appreciation[0], title="Appreciation Female")
    # fig.show()
    # fig = px.bar(x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], y=appreciation[1], title="Appreciation Male")
    # fig.show()

    for a, question in enumerate(rows):
        fig = px.bar(data, x=0, y=a + 2, color=1, barmode='group', height=700, title=question)
        fig.show()


def plot_survey_data():
    data = pd.read_csv('data01/survey.csv')
    data_gender = data['gender'].values
    data_rating = data['rating'].values
    rating_women = []
    rating_men = []
    # iterate through data
    for i in range(len(data_gender)):
        if (data_gender[i] == 'Female'):
            rating_women.append(data_rating[i])
        else:
            rating_men.append(data_rating[i])
    average_women = sum(rating_women) / len(rating_women)
    average_men = sum(rating_men) / len(rating_men)
    print('amount of women working: ', len(rating_women))
    print('amount of men working: ', len(rating_men))
    # create bar diagramm with data
    plt.bar(['Male', 'Female'], [average_men, average_women])
    plt.xlabel('Gender')
    plt.ylabel('Average Rating')
    plt.show()
    # plot Gender on x Axis and Rating average on y axis


def plot_emp_data():
    with open('data01/emp.json') as json_file:
        json_list = json.load(json_file)
    employees = json_list["employees"]

    # plot altersverteilung wie viele mitarbeiter pro alter?
    ages = []
    workplaces = []
    for employee in employees:
        ages.append(employee['Age'])
        workplaces.append(employee['Workplace'])

    plot_age_distribution(ages, "general age distribution")

    # altersverteilung an jedem workplace -> unterschiedliche plots
    # ages_per_workplace = []
    for workplace in workplaces:
        workplace_ages = []
        for employee in employees:
            if employee['Workplace'] == workplace:
                workplace_ages.append(employee['Age'])
        # ages_per_workplace.append(workplace_ages)
        title = "Age distribution at " + workplace
        # plot_age_distribution(workplace_ages, title)

    # durchschnittsalter an jedem workplace


def plot_age_distribution(ages, title):
    amount_of_ages = []
    for age in ages:
        amount_of_ages.append(ages.count(age))

    plt.bar(ages, amount_of_ages)
    plt.xlabel('Ages')
    plt.ylabel('Amount of employees with this age')
    plt.title(title)
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # plot_survey_data()
    # plot_emp_data()
    plot_survey2_data()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

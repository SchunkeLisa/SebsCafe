import matplotlib.pyplot as plt
import pandas as pd
# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json

def plot_survey_data():
    data = pd.read_csv('data01/survey.csv')
    data_gender = data['gender'].values
    data_rating = data['rating'].values
    rating_women = []
    rating_men = []
    #iterate through data
    for i in range(len(data_gender)):
        if(data_gender[i] == 'Female'):
            rating_women.append(data_rating[i])
        else:
            rating_men.append(data_rating[i])
    average_women = sum(rating_women) / len(rating_women)
    average_men = sum(rating_men) / len(rating_men)
    print('amount of women working: ', len(rating_women))
    print('amount of men working: ', len(rating_men))
    #create bar diagramm with data
    plt.bar(['Male', 'Female'], [average_men, average_women])
    plt.xlabel('Gender')
    plt.ylabel('Average Rating')
    plt.show()
    #plot Gender on x Axis and Rating average on y axis


def plot_emp_data():
    with open('data01/emp.json') as json_file:
        json_list = json.load(json_file)
    employees = json_list["employees"]

    #plot altersverteilung wie viele mitarbeiter pro alter?
    ages = []
    workplaces = []
    for employee in employees:
        ages.append(employee['Age'])
        workplaces.append(employee['Workplace'])

    plot_age_distribution(ages,"general age distribution")

    #altersverteilung an jedem workplace -> unterschiedliche plots
    #ages_per_workplace = []
    for workplace in workplaces:
        workplace_ages = []
        for employee in employees:
            if employee['Workplace'] == workplace:
                workplace_ages.append(employee['Age'])
        #ages_per_workplace.append(workplace_ages)
        title = "Age distribution at " + workplace
        #plot_age_distribution(workplace_ages, title)

    #durchschnittsalter an jedem workplace

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
    #plot_survey_data()
    plot_emp_data()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

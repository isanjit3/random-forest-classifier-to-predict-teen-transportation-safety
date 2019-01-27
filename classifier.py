from sklearn.ensemble import RandomForestClassifier
import csv



clf = RandomForestClassifier(n_estimators=1)


'''with open('motorVehicleDataSet.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    x = 10
    while x > 0:
        for row in csv_reader:
            for line in row:

                print(line)
                x = x - 1

'''


age = int(input("Age:  "))
gender1 = str(input("Gender: "))
people = int(input("People in Car: "))
new1 = str(input("New Driver? "))
day1 = str(input("Day: "))
time = int(input("Time: "))


if (gender1 == 'male' or 'Male'):
    gender = 1
else:
    gender = 2

if new1 == 'true' or new1 =='True':
    new = 1
else:
    new = 2


if day1 == "monday" or "Monday":
    day = 1
elif day1 == "tuesday" or "Tuesday":
    day = 2
elif day1 == "wednesday" or "Wednesday":
    day = 3
elif day1 == "thursday" or "Thursday":
    day = 4
elif day1 == "friday" or "Friday":
    day = 5
elif day1 == "saturday" or "Saturday":
    day = 6
else:
    day = 7
# age, gender, people, new driver, day of week, time of day

# male, yes, monday = 1

age_val = 5
gender_val = 5
people_val = 6
new_driver_val = 8
day_of_week_val = 2
time_val = 7


X = [[16, 1, 5, 1, 6, 2350],[19, 2, 1, 2, 2, 930],[17, 1, 3, 1, 7, 1930],[18, 2, 1, 1, 3, 1125],[15, 1, 2, 1, 5, 2030],[19, 2, 2, 2, 1, 1115],[16, 1, 4, 1, 6, 2218]]

Y = ['high risk', 'low risk','high risk', 'low risk','high risk', 'low risk','high risk']

clf = clf.fit(X, Y)

#prediction = clf.predict([[22, 2, 5, 2, 2, 2350]])


prediction = clf.predict([[age,gender,people,new,day,time]])

print (prediction)

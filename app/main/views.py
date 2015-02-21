from flask import render_template
from time import localtime
from . import app

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/calendar")
def calendar():
    days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    all_activities = [
        {
            'title': 'Intramural Basketball',
            'category': 'Basketball'
        },
        {
            'title': 'Varsity Football',
            'category': 'Football'
        },
        {
            'title': 'Major League Soccer',
            'category': 'Soccer'
        }
    ]
    month_name = 'February'
    day_of_month = 1
    current_week = []
    aim = [current_week]
    week_counter = -1
    for d in range(1,29):
        week_counter += 1
        if week_counter >= 7:
            week_counter = 0
            current_week = []
            aim.append(current_week)
        
        activities = [
            all_activities[d % len(all_activities)]
        ]    
        
        current_week.append( {
            'day_of_week': days_of_week[week_counter],
            'day_of_month': d,
            'month': "February",
            'activities': activities
        } )


    return render_template('calendar.html', activities_in_month=aim)

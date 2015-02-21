from flask import Flask, render_template
import time
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/calendar")
def calendar():
    empty = {
        day_of_week: "monurday",
        day_of_month: "32",
        month:"marchuary",
        activities: []
    }

    fancyday = {
        day_of_week: "wednesday",
        day_of_month: "15",
        month: "February",
        activities: [
                        {
                            time:localtime(),
                            category: "basketball",
                            title: "intramural bball",
                        },
                        {
                            time:localtime(),
                            category: "football",
                            title: "varsity football"
                        }
                    ]
    }

    aim = [
        [empty, empty, fancyday, empty, empty],
        [empty, empty, empty, empty, empty],
        [empty, empty, empty, empty, fancyday],
        [empty, empty, empty, empty, empty],
    ]

    return render_template('calendar.html', activities_in_month=aim)


if __name__ == "__main__":
    app.run()

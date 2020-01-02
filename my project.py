import time
from datetime import date
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('project index.html')

@app.route('/democracy')
def democracy():
    today = date.today()
    democracy_day = date(today.year, 6, 12)
    if democracy_day < today:
        democracy_day = date(next.year, 6,12)
        time_to_democracy = abs(today - democracy_day)
        days_to = time_to_democracy.days

        return render_template('democracy.html', days_to = days_to)


    elif democracy_day > today:
        time_to_democracy = abs(democracy_day - today)
        days_to = time_to_democracy.days
        return render_template('democracy.html', days_to = days_to)

    elif democracy_day == today:
        days_to = "Hurray! It is Nigeria's Democracy Day!!!"

        return render_template('democracy.html')

@app.route('/independence')
def independence():
    today = date.today()
    independence = date(today.year, 10, 1)
    if independence < today:
        independence = date(2020, 10, 1)
        time_to_independence= abs(independence - today)
        days_to = time_to_independence.days
        return render_template('independence_day.html', days_to = days_to)


    elif independence > today:
        time_to_independence = abs(independence - today)
        days_to = time_to_independence.days
        return render_template('independence_day.html', days_to = days_to)

    elif independence == today:
        days_to = "Hurray! It is Nigeria's Independence Day!!!"

        return render_template('independence_day.html')

@app.route('/workers_day')
def workers_day():
    today = date.today()
    workers_day = date(today.year, 5, 1)
    if workers_day < today:
        workers_day = date(2020, 5, 1)
        time_to_workers = abs(workers_day - today)
        days_to = time_to_workers.days
        return render_template('workers_day.html', days_to = days_to)


    elif workers_day > today:
        time_to_workers = abs(workers_day - today)
        days_to = time_to_workers.days
        return render_template('workers_day.html', days_to = days_to)

    elif workers_day == today:
        days_to = "Hurray! It is Nigeria's Workers' Day!!!"

        return render_template('workers_day.html')

@app.route('/christmas_day')
def christmas_day():
    today = date.today()
    christmas_day = date(today.year, 12, 25)
    if christmas_day < today:
        christmas_day = date(2020, 12, 25)
        time_to_christmas = abs(christmas_day - today)
        days_to = time_to_christmas.days
        return render_template('christmas_day.html', days_to = days_to)


    elif christmas_day > today:
        time_to_christmas = abs(christmas_day - today)
        days_to = time_to_christmas.days
        return render_template('christmas_day.html', days_to = days_to)

    elif christmas_day == today:
        days_to = "Hurray! It's Christmas Day!!!"
        return render_template('christmas_day.html')

@app.route('/boxing_day')
def boxing_day():
    today = date.today()
    boxing_day = date(today.year, 12, 26)
    if boxing_day < today:
        boxing_day = date(2020, 12, 26)
        time_to_boxing = abs(boxing_day - today)
        days_to = time_to_boxing.days
        return render_template('boxing_day.html', days_to = days_to)


    elif boxing_day > today:
        time_to_boxing = abs(boxing_day - today)
        days_to = time_to_boxing.days
        return render_template('boxing_day.html', days_to = days_to)

    elif boxing_day == today:
        days_to = "Hurray! It's Boxing Day!!!"
        return render_template('boxing_day.html')

@app.route('/children_day')
def children_day():
    today = date.today()
    children_day = date(today.year, 5, 27)
    if children_day < today:
        children_day = date(2020, 5, 27)
        time_to_children = abs(children_day - today)
        days_to = time_to_children.days
        return render_template('children_day.html', days_to = days_to)


    elif children_day > today:
        time_to_children = abs(children_day - today)
        days_to = time_to_children.days
        return render_template('children_day.html', days_to = days_to)

    elif children_day == today:
        days_to = "Hurray! It's Childrens's Day!!!"
        return render_template('children_day.html')

@app.route('/eid_ul_adha')
def eid_ul_adha():
    today = date.today()
    eid_ul_adha_day = date(today.year, 7, 31)
    if eid_ul_adha_day < today:
        eid_ul_adha_day = date(2020, 7, 31)
        time_to_eid_ul_adha = abs(eid_ul_adha_day - today)
        days_to = time_to_eid_ul_adha.days
        return render_template('eid_ul_adha.html', days_to = days_to)


    elif eid_ul_adha_day > today:
        time_to_eid_ul_adha = abs(eid_ul_adha_day - today)
        days_to = time_to_eid_ul_adha.days
        return render_template('eid_ul_adha.html', days_to = days_to)

    elif childen_day == today:
        days_to = "Hurray! It's Eid_ul_Adha Celebration Day!!!"
        return render_template('eid_ul_adha.html')

@app.route('/eid_ul_fitr')
def eid_ul_fitr():
    today = date.today()
    eid_ul_fitr_day = date(today.year, 5, 24)
    if eid_ul_fitr_day < today:
        eid_ul_fitr_day = date(2020, 5, 24)
        time_to_eid_ul_fitr = abs(eid_ul_fitr_day - today)
        days_to = time_to_eid_ul_fitr.days
        return render_template('eid_ul_fitr.html', days_to = days_to)


    elif eid_ul_fitr_day > today:
        time_to_eid_ul_fitr = abs(eid_ul_fitr_day - today)
        days_to = time_to_eid_ul_fitr.days
        return render_template('eid_ul_fitr.html', days_to = days_to)

    elif childen_day == today:
        days_to = "Hurray! It's Eid-ul-Fitr Celebration Day!!!"
        return render_template('eid_ul_fitr.html')

@app.route('/inauguration')
def inauguration():
    today = date.today()
    inauguration = date(today.year, 5, 29)
    if inauguration < today:
        inauguration = date(2020, 5, 29)
        time_to_inauguration= abs(inauguration - today)
        days_to = time_to_inauguration.days
        return render_template('inauguration_day.html', days_to = days_to)


    elif inauguration > today:
        time_to_inauguration = abs(inauguration - today)
        days_to = time_to_inauguration.days
        return render_template('inauguration_day.html', days_to = days_to)

    elif inauguration == today:
        days_to = "Hurray! It is Nigeria's Inauguration Day!!!"
        return render_template('inauguration_day.html')

@app.route('/new_year_day')
def new_year_day():
    today = date.today()
    new_year = date(today.year, 1, 1)
    if new_year < today:
        new_year = date(2020, 1, 1)
        time_to_new_year= abs(new_year - today)
        days_to = time_to_new_year.days
        return render_template('new_year_day.html', days_to = days_to)


    elif new_year > today:
        time_to_new_year = abs(new_year - today)
        days_to = time_to_new_year.days
        return render_template('new_year_day.html', days_to = days_to)

    elif new_year == today:
        days_to = "Hurray! It is Nigeria's Inauguration Day!!!"
        return render_template('new_year_day.html')

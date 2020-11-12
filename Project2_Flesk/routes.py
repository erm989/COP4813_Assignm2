from Project2_Flesk import app, forms
from flask import request, render_template

@app.route('/')
def intro():
    intro = "This app uses the Search API to display the articles with a determined keyword " \
            "based on a specific topic and place selected by the user."
    return (intro)

@app.route('/search', methods=['GET', 'POST'])
def search():
    my_form = forms.NewsForm(request.form)
    if request.method == "POST":

        # format = request.form['format'] #this variable is assigned to the option selected by user

        search = request.form["search"]
        topic = request.form["topic"]
        sort = request.form["sort"]

        # Get teh values provided
        # Call API
        # Generate requested data
        result = forms.generateDataFromAPI(search, topic, sort)

        # response = [search, topic, sort]


        return render_template('results.html', response=result, form=my_form, topic = topic, sort=sort)

    return render_template('search.html', form=my_form)



from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, RadioField
import requests
from Project2_Flesk import main_functions
from wtforms.validators import InputRequired

class NewsForm(FlaskForm):
    search = StringField("Keyword", validators=[InputRequired()])
    topic = SelectField("Topic", choices=[('sports', 'Sports'),
                                          ('financial', 'Financial'),
                                          ('politics', 'Politics'),
                                          ('arts', 'Arts'),
                                          ('travel', 'Travel')])
    sort = RadioField("From", choices=[('newest', 'Newest'),
                                       ('oldest', 'Oldest')])

def generateDataFromAPI(search, topic, sort):
    url = "https://api.nytimes.com/svc/search/v2/articlesearch.json?q="
    my_key_dict = main_functions.read_from_file("Project2_Flesk/JSON_Files/api_key.json")
    my_key = my_key_dict["my_key"]

    final_url= url + search + "&fq=news_desk:" + topic + "&sort=" + sort + "&api-key=" + my_key
    print(final_url)

    """ May provide more info in api url"""

    response = requests.get(final_url).json()

    main_functions.save_to_file(response, "Project2_Flesk/JSON_Files/response.json")

    my_articles = main_functions.read_from_file("Project2_Flesk/JSON_Files/response.json")

    """" From the response dict, you need to filter the data requested by user"""

    return my_articles



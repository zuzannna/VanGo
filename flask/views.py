from flask import render_template
from flask import request
from flaskexample import app
import pandas as pd
import psycopg2
import utilities
from flask import request

#user = 'Jay' #add your username here (same as previous postgreSQL)
#host = 'localhost'
#dbname = 'birth_db'
#db = create_engine('postgres://%s%s/%s'%(user,host,dbname))
#con = None
#con = psycopg2.connect(database = dbname, user = user)


@app.route('/')
@app.route('/input')
def cesareans_input():
    return render_template("input.html")

# @app.route('/output')
# def cesareans_output():
#     return render_template("output.html")

@app.route('/contact')
def cesareans_contact():
    return render_template("contact.html")

@app.route('/about')
def cesareans_about():
    return render_template("about.html")

@app.route('/output')
def cesareans_output():

  #pull 'birth_month' from input field and store it
    
  #print(word_output)
  # if word_output == 'trees': 
  
  #return render_template("slider.html")

  if request.method == "GET":
    input_word = request.args.get('search_query')
    
    #print input_word
    #print type(input_word)
    #list_of_paintings = similarity(input_word)

    list_of_paintings = utilities.similarity(input_word)
    #answer = str(similarity("jack"))
    if str(list_of_paintings) == "error_message":
      print("this will do the calculation")
      return render_template("error.html")
    return render_template("output.html", list_of_paintings = list_of_paintings)

  #if request.method == "POST":



    #just select the Cesareans  from the birth dtabase for the month that the user inputs
#  query = "SELECT index, attendant, birth_month FROM birth_data_table WHERE delivery_method='Cesarean' AND birth_month='%s'" % patient
#  print query
#  query_results=pd.read_sql_query(query,con)
#  print query_results

#  for i in range(0,query_results.shape[0]):
#     irths.append(dict(index=query_results.iloc[i]['index'], attendant=query_results.iloc[i]['attendant'], birth_month=query_results.iloc[i]['birth_month']))
    #   the_result = ''
  #the_result = pd.read_csv("paintings.csv")
  #the_result = the_result.head()
  #return render_template("output.html", the_result = the_result)

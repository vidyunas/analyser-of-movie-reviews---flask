from flask import Flask,redirect,url_for,render_template,request,session
from pymongo import MongoClient 
client = MongoClient("mongodb://localhost:27017/") 
mydatabase = client["projdb"] 
mycollection = mydatabase["users"] 
import pandas
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
import statistics
import matplotlib.pyplot as plt
import collections 
import os



app=Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1
@app.route("/",methods=["POST","GET"])
def home():
	if request.method=="POST":
		
		user=request.form["uname"]
		pas=request.form["psw"]
		result=mycollection.find_one({"name":user,"pw":pas})
		if(result):
			session["user"]=user
			return render_template("chumma.html")
		else:
			return render_template("login.html")
			
		
		
	       	

	else:
		return render_template("login.html")


@app.route("/signup",methods=["POST","GET"])	
def sign():
	if request.method=="POST":
		user=request.form["name"]
		pas=request.form["psw"]
		rpas=request.form["rpas"]
		state=request.form["state"]
		sex=request.form["sex"]
		if(pas==rpas):
			rec={ "name":user, "pw":pas, "location":state, "sex":sex}
			x= mydatabase.users.insert_one(rec) 
			if(x):
				return render_template("login.html")
		else:
			return "password and confirm password not same"

	else:
		return render_template("signup.html")


@app.route("/main",methods=["POST","GET"])
def mainpage():
	if request.method=="POST":
		a=request.form["button"]
		lis=a.split()
		movie=lis[0]
		act=lis[1]
		session["moviename"]=movie
		if(act=="give"):
			
			return render_template("give_review.html",moviename=movie)

		else:
			return redirect(url_for("see"))


	
	else:
		return render_template("chumma.html")

@app.route("/give",methods=["POST","GET"])
def give():
	mycollection = mydatabase["review"]
	if request.method=="POST":
		review=request.form["review"]
		result=mycollection.find_one({"user":session["user"],"movie":session["moviename"]})
		if(result):
			return "<h1>you already gave the review</h1> "
				

		else:
			rec={"user":session["user"], "movie":session["moviename"], "rev":review}
			x= mydatabase.review.insert_one(rec) 
			if(x):
				return render_template("chumma.html")

	else:
		return render_template("give_review.html")
					
@app.route("/see")		
def see():
	
	
	mycollection = mydatabase["review"]
	mycollection2 = mydatabase["users"] 
	moviename=session["moviename"]
	obj = SentimentIntensityAnalyzer()

	reviews=[]
	username=[]
	value=[]
	sex=[]
	loc=[]
	cursor = mycollection.find({"movie":moviename}) 
	for record in cursor:
		reviews.append(record["rev"])
		username.append(record["user"])
	for i in reviews:
		sentiment_dict = obj.polarity_scores(i)
		value.append(50*(sentiment_dict['compound']+1))
	for i in username:
		cursor=mycollection2.find({'name':i})
		for temp in cursor:
			sex.append(temp["sex"])
			loc.append(temp["location"])

		
	freq_loc = collections.Counter(loc)
	freq_sex = collections.Counter(sex)
	
	unique_loc = list(set(loc))
	
	unique_sex = list(set(sex))	
	unique_count_loc=[]
	unique_count_sex=[]
	for i in unique_loc:
	   	unique_count_loc.append(freq_loc[i])
	for i in unique_sex:
	   	unique_count_sex.append(freq_sex[i])
	
	fig1, ax1 = plt.subplots()
	ax1.pie(unique_count_sex,  labels=unique_sex, autopct='%1.1f%%',
        shadow=True, startangle=90)
	ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

	
	plt.savefig('C:/Users/vidyu/Desktop/flask_project_final/static/images/a.png')


	fig2, ax2 = plt.subplots()
	ax2.pie(unique_count_loc,  labels=unique_loc, autopct='%1.1f%%',
        shadow=True, startangle=90)
	ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

	
	plt.savefig('C:/Users/vidyu/Desktop/flask_project_final/static/images/b.png')


	#plt.pie(unique_count_sex, labels = unique_sex,frame=True)
	#plt.title('reach of the movie among gender')
	#plt.axes().set_ylabel('')
	#plt.axes().set_xlabel('')
	#plt.savefig('C:/Users/vidyu/Desktop/flask_project_final/static/images/a.png')



	#plt.pie(unique_count_loc, labels = unique_loc,frame=True)
	#plt.title('reach of the movie among states')
	#plt.axes().set_ylabel('')
	#plt.axes().set_xlabel('')
	#plt.savefig('C:/Users/vidyu/Desktop/flask_project_final/static/images/b.png')

        	
    	
    		
		
	return render_template("see_review.html",average=str(statistics.mean(value)))
    

@app.after_request
def add_header(response):
    
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response
			
@app.after_request
def add_header(response):
    # response.cache_control.no_store = True
    if 'Cache-Control' not in response.headers:
        response.headers['Cache-Control'] = 'no-store'
    return response


			





	            	

if __name__=="__main__":
	app.secret_key="it is radom"
	app.run()
	


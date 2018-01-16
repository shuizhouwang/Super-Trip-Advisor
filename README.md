# Super-Trip-Advisor
python/jupyter

project contributors:
Shuizhou wang(sw3192)
Ruimin Zhao(rz2390)
Yixuan Ma(ym2617)

This project is our Big Data Analysis course project named Super Trip Advisor. 
The objectives of this project include Big data analysis for both practical use and theoretical results: We used NYC transportation datasets to develop a web application for the recommendation of the waiting spot for taxi or uber in NYC, and for providing some other practically useful transportation information such as public transportation stops nearby and weather condition;

Also, we applied some algorithms including three types of Clustering algorithm and linear regression into the datasets for data visualization as well as obtaining some interesting features out of them. We primarily utilize open source datasets including the NYC green taxi dataset, the NYC yellow taxi dataset and the NYC Uber dataset. The technologies involved in this project mainly include the data visualization package such as Pandas and Folium, data frame generator spark, data processing tool named MySQL workbench, and web application development framework named Flask for practical usage of processed data.

Particularly, this file including all our code for the final web application in the webapplication folder. We also include our data analysis results in the data anlysis folder.

How to run our web application:

1.download the file 

2.cd to the webapplication folder

3.change your root in the recommendation.py file.
In this python file, in order to acqure data, you should change all "your root" in root like:  "/your root/webapplication/bd/" as your own root where you put this webapplication folder.


4.In the terminal, cd to your webapplication folder and run following command.

(1).export FLASK_APP=application.py

(2).flask run

(3).access to http://127.0.0.1:5000/

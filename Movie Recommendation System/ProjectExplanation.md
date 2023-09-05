<h1><u>In this Project I build Movie Reccomendation system using ML in Python.</u></h1>
<h6>End Goal of this Project is to create a Movie Reccomenddation system which takes input from the user and reccomends a Movie similar to it</h6>
<h3>Importing Dataset</h3>
Step1 : Importing Important Libraries and modules that are to be used in the project <br>
Step2 : Importing Data Set and converting it into a Pandas Dataframe <br>
Step3 :  Getting the shape and the top 5 Rows of our given Data Set <br>
<h3>Feature Engineering and ML Model Implementation </h3> 
Step4 : Selecting Feature, which serves as the basis, on which we want the Movie to be recommended by the ML Model<br>
Step5 : Filling non-available data values with .fillna(), i.e. blank<br>
Step6 : Creating our main data frame, main_data, with the features selected from the initial dataset that we imported<br>
Step7 : Creating a variable, vectorizer, to store functionality of TfidfVectorizer() model from Scikit-Learn<br>
Step8 : Fitting values of main_data in vectorizer, which converts string data in the main_data into numerical values<br>
Step9 : Using Cosine Similarity Algorithm on the numerical values of the features<br>
Step10 : Printing the Output and Shape after using Similarity Algorithm, it gives a (4803, 4803) numpy array, as it gives a comparision of each movie with all the other movies
<h3>Taking Input from the User</h3>
Step11: Take input similar to what films he/she wants<br>
Step12: Create a dataframe containing all the title from the initial dataframe<br>
Step13: Using difflib library in python we find the Closest Match of the Movie Title entered by the user, it reduces any type error that the user may have done<br>
<h3>Finding and Printing similar Movies</h3>
Step14: Finding the Closest Match from our Dataset<br>
Step15: Finding and Printing the index of the Input Movie from the Dataset<br>
Step16: Finding Similarity of all The Movies with the Input Movie and storing it as a list. We use enumerate, as it keeps track of index<br>
Step17: We sort similarity of the movie in the list above using a lambda function<br>
Step18: Using For Loop to print the list of 10 Most Similar Movies

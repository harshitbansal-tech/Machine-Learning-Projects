<h1><u>In this Project I build Movie Reccomendation system using ML in Python.</u></h1>
<h6>End Goal of this Project is to create a Movie Reccomenddation system which takes input from the user and reccomends a Movie similar to it</h6>
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
Step11: Take input similar to what films he/she wants
Step12: Create a dataframe containing all the title from the initial dataframe

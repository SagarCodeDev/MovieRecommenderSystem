# MovieRecommenderSystem
Used Django framework to build a movie recommender system. Different users can Login or Register(if they dont't have the account).
The profile page will display the details of all the movies which the user have seen.
The recommendation page will recommend the movie based on the given movie mentioned in the database.
After selecting a movie it will display a list of 10 movies and the user can select one of the movie to add in the database.
Used 2 models namely profile and moviedb.
moviedb will contain the details of the movie like title,three of the top relevant casts,director and description.
Profile model will be in one-to-one relationship with django-user model and in many-to-many relationship with the moviedb.
The core for the recommendation system is imported from the .pkl file which will be located in movies/models directory.
The .pkl are the pickel files, one is the database for the moviedb and the other is the similarity matrix.

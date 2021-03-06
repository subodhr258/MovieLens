# Movie Recommendation System  

## Winter Project Team #40:
- Kushagra Nageshwar (2019IMT-053)
- Latikesh Ahire (2019IMT-055)
- Subodh Rajpopat (2019IMT-103)

## Project Description: 
A Movie Recommendation System on the MovieLens dataset with Flask API as backend.  
The recommendation system uses collaborative and content based approaches to filter top N movie recommendations.  
- Content based - uses the information of the movie. For example, movies which have similar ratings or genre or cast.
- Collaborative filtering - uses the information of the connection between the user and movies. For example, users which give similar ratings to a movie.
- Hybrid - uses a combination of collaborative and content based recommendations.    

Link to demo video: https://youtu.be/uQGfodeABoo  
FrontEnd Github Repository Link: https://github.com/Chaithanya45/RecoMovie  
MovieLens Dataset: https://grouplens.org/datasets/movielens/20m/  
### Recommendation Diagram:
<!-- ![Recommendation Diagram](https://drive.google.com/uc?export=view&id=1SYQUz1gWs0fBJOsh6yXesjBivjz0cQS_)   -->
<a href="https://drive.google.com/uc?export=view&id=1SYQUz1gWs0fBJOsh6yXesjBivjz0cQS_"><img src="https://drive.google.com/uc?export=view&id=1SYQUz1gWs0fBJOsh6yXesjBivjz0cQS_" style="width: 650px; max-width: 100%; height: auto" title="Click to enlarge picture" />  
### Directory Layout

    .
    ├── Files                           #pickle files of the data
        ├── latent_collaborative.pkl    #vectorized collaborative data
        ├── latent_content.pkl          #vectorized content data
        ├── map.pkl                     #map of movie titles to movie ids
        └── rating.pkl
    ├── ml-20m                          #dataset for the model
        ├── movies.csv                  #contains movieid, title and genre of the movies
        ├── ratings.csv                 #contains userid, movieid, rating and timestamp
        └── tags.csv                    #contains userid, movieid, tag and timestamp
    ├── .gitignore
    ├── Build_model.py                  #builds the model and saves it in a pickle format
    ├── Procfile                        
    ├── README.md 
    ├── app.py                          #main app that runs the server using the models from pkl files
    ├── model.py                        #returns the output from the models using cosine similarity
    ├── requirements.txt
    └── runtime.txt

## Hosted URL:
### Backend URL:
```
 https://movielens-ap.herokuapp.com/movies/[basis]/?movie=[movie]&limit=n
```
- [basis] can be replaced by 'content', 'collaborative' or 'hybrid'.
- [movie] can be replaced by the movie name.
- [n] can be replaced by the number of reccomendations to be displayed.

Example - Hybrid Filtering: 
```
 https://movielens-ap.herokuapp.com/movies/hybrid/?movie=Toy Story (1995)&limit=10
```
Output:
```
{
    "hybrid" : [
        "Lion King, The (1994)",
        "Pocahontas (1995)",
        "Forrest Gump (1994)",
        "Swan Princess, The (1994)",
        "Apollo 13 (1995)",
        "Gumby: The Movie (1995)",
        "Secret Adventures of Tom Thumb, The (1993)",
        "Flintstones, The (1994)",
        "Star Wars: Episode IV - A New Hope (1977)",
        "Goofy Movie, A (1995)"
    ]
}
```

## Backend Features Implemented:
- The algorithm returns recommendations with options among Content, Collaborative and Hybrid filtering:
    - Content - if the user wants recommendations on the basis of the type, genre, tags of the movie.
    - Collaborative - if the user wants recommendations on the basis of movies that other users have liked.
    - Hybrid - if the user wants recommendations on the basis of both content and collaborative based filtering.
- The user can set the number of recommendations (n) that he/she wants the API to return.

## Tech Stack:

### Backend:
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Numpy](https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)
![Sklearn](https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

## Local Setup:

1. Run git clone in the project folder
2. Run ```pip install -r requirements.txt``` in the project folder to install all the required packages.
3. Run ```python app.py``` or ```flask run``` to start the server
4. Visit ```http://127.0.0.1:33507/movies/content/?movie=Toy%20Story%20(1995)&limit=10``` to see a sample result of backend API

# Movie Recommendation System 
(Winter Project Team #40) 

## Team Members:
- Kushagra Nageshwar (2019IMT-53)
- Latikesh Ahire (2019IMT-55)
- Subodh Rajpopat (2019IMT-103)

## Project Description: 
A Movie Recommendation System on the MovieLens dataset with Flask API as backend.  
The recommendation system uses collaborative and content based approaches to filter top N movie recommendations.  
Content based - uses the information of the movie. For example, movies which have similar ratings or genre or cast.
Collaborative filtering - uses the information of the connection between the user and movies. For example, users which give similar ratings to a movie.
Hybrid - uses a combination of collaborative and content based recommendations.

MovieLens Dataset: https://grouplens.org/datasets/movielens/20m/

## Screenshots:

## Hosted URL:
### Frontend URL:
```
```
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


## Features Implemented:
### Frontend Features:

### Backend Features:

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
4. Visit ```http://127.0.0.1:5000/movies/content/?movie=Toy%20Story%20(1995)&limit=10``` to see a sample result of backend API

# Movie Recommendation System 
(Winter Project Team #40) 

## Team Members:
- Kushagra Nageshwar (2019IMT-53)
- Latikesh Ahire (2019IMT-55)
- Subodh Rajpopat (2019IMT-103)

## Project Description: 
A movie recommendation system...
MovieLens Dataset: https://grouplens.org/datasets/movielens/20m/

## Screenshots:

## Hostel URL:
### Frontend URL:
```
```
### Backend URL:
```
 https://movielens-ap.herokuapp.com/movies/[basis]/?movie=[movie]&limit=n
```

Example 1: 
```
 https://movielens-ap.herokuapp.com/movies/content/?movie=Toy%20Story%20(1995)&limit=10
```
Output:
```
{
    "content": [
        "Secret Adventures of Tom Thumb, The (1993)",
        "Gumby: The Movie (1995)",
        "Swan Princess, The (1994)",
        "Lion King, The (1994)",
        "Pocahontas (1995)",
        "Forrest Gump (1994)",
        "Flintstones, The (1994)",
        "Goofy Movie, A (1995)",
        "Balto (1995)",
        "Apollo 13 (1995)"
    ]
}

```

Example 2: 
```
 https://movielens-ap.herokuapp.com/movies/collaborative/?movie=Toy%20Story%20(1995)&limit=10
```
Output:
```
{
    "collaborative" : [
        "Star Wars: Episode IV - A New Hope (1977)",
        "Lion King, The (1994)","Pulp Fiction (1994)",
        "Apollo 13 (1995)",
        "True Lies (1994)",
        "Jurassic Park (1993)",
        "Forrest Gump (1994)",
        "Fugitive, The (1993)",
        "Mask, The (1994)",
        "Twelve Monkeys (a.k.a. 12 Monkeys) (1995)"
    ]
}
```

Example 3: 
```
 https://movielens-ap.herokuapp.com/movies/hybrid/?movie=Toy%20Story%20(1995)&limit=10
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

## Local Setup:

1. Run git clone in the project folder
2. Run ```pip install -r requirements.txt``` in the project folder to install all the required packages.
3. Run ```python app.py``` or ```flask run``` to start the server
4. Visit ```http://127.0.0.1:5000/movies/content/?movie=Toy%20Story%20(1995)&limit=10``` to see a sample result of backend API



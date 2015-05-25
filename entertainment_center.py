import fresh_tomatoes
import media

blind_side = media.Movie("The Blind Side", "The remarkable true story of all-American football star Michael Oher",
                         "http://upload.wikimedia.org/wikipedia/en/thumb/6/60/Blind_side_poster.jpg/220px-Blind_side_poster.jpg",
                         "https://www.youtube.com/watch?v=I24d30buecw")

school_of_rock = media.Movie("School of Rock", "Using rock music to learn",
                             "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

accepted = media.Movie("Accepted", "Boy decides to make up a college after every college turns him down",
                       "http://upload.wikimedia.org/wikipedia/en/thumb/b/b6/Acceptedposter.jpg/220px-Acceptedposter.jpg",
                       "https://www.youtube.com/watch?v=41C-VouZ7NY")

i_married_who = media.Movie("I Married Who?", "Straight-laced girl wakes up married to a movie star intead of her fiance",
                            "http://upload.wikimedia.org/wikipedia/en/c/cf/I_Married_Who_poster.jpg",
                            "https://www.youtube.com/watch?v=GSQwMMg7HcU")

                            
why_get_married = media.Movie("Why Did I Get Married?", "Eight married college friends begin to question their own marriage",
                              "http://upload.wikimedia.org/wikipedia/en/thumb/2/23/Why_did_i_get_married_ver2.jpg/215px-Why_did_i_get_married_ver2.jpg",
                              "https://www.youtube.com/watch?v=COjDsU0K0fw")

why_get_married_too = media.Movie("Why Did I Get Married Too?", "Four close couples eagerly reconnect, sharing news about their lives and relationships",
                                  "http://upload.wikimedia.org/wikipedia/en/thumb/b/bb/WhyDidIGotMarried2Poster2.jpg/220px-WhyDidIGotMarried2Poster2.jpg",
                                  "https://www.youtube.com/watch?v=xW1zSg6FLko")

movies = (blind_side, school_of_rock, accepted, i_married_who, why_get_married, why_get_married_too)
fresh_tomatoes.open_movies_page(movies)
#print (media.Movie.VALID_RATINGS)
print (media.Movie.__module__)





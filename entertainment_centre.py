import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "Story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.storyline)
#avatar.show_trailer()

the_mummy = media.Movie("The Mummy",
                        "Nick Morton is a soldier of fortune who plunders ancient sites for timeless artifacts and sells them to the highest bidder.When Nick and his partner come under attack in the Middle East, the ensuing battle accidentally unearths Ahmanet, a betrayed Egyptian princess who was entombed under the desert for thousands of years.With her powers constantly evolving, Morton must now stop the resurrected monster as she embarks on a furious rampage through the streets of London.",
                        "https://pbs.twimg.com/media/DCntM-0UIAA-ErP.jpg",
                        "https://www.youtube.com/watch?v=sCdV3esMr9M")

dawn_of_planet = media.Movie("Dawn of the planet of Apes",
                             "Ten years after a rife disease, apes who have endured the disease are drawn into a ferocious battle with a bunch of human survivors.",
                             "https://upload.wikimedia.org/wikipedia/en/7/77/Dawn_of_the_Planet_of_the_Apes.jpg",
                             "https://www.youtube.com/watch?v=DpSaTrW4leg")

pursuit_of_happiness = media.Movie("Pursuit of Happiness",
                                   "Chris Gardner takes up an unpaid internship in a brokerage firm after he loses his life's earnings selling a product he invested in. His wife leaves him and he is left with the custody of his son.",                                   
                                   "https://upload.wikimedia.org/wikipedia/en/8/81/Poster-pursuithappyness.jpg",
                                   "https://www.youtube.com/watch?v=89Kq8SDyvfg")
walk_to_remember = media.Movie("A Walk to Remember",
                               "Landon is assigned community service after getting in trouble. His punishment also involves participating in the spring play, during which he falls in love with Jamie, the reverend's daughter.",
                               "https://upload.wikimedia.org/wikipedia/en/d/dc/A_Walk_to_Remember_Poster.jpg",
                               "https://www.youtube.com/watch?v=i72wRvPw_ik")

movies = [toy_story, avatar, the_mummy, dawn_of_planet, pursuit_of_happiness, walk_to_remember]
fresh_tomatoes.open_movies_page(movies)



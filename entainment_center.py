import fresh_tomatoes
import media

one_day = media.Movie(
    "One Day",
    ("After spending the night together on the night of their college " +
     "graduation Dexter and Em are shown each year on the same date to" +
     " see where they are in their lives. They are sometimes together," +
     "sometimes not, on that day."),
    "https://upload.wikimedia.org/wikipedia/en/a/ad/One_Day_Poster.jpg",
    "https://www.youtube.com/watch?v=nk8W8DyZBiU")

titanic = media.Movie(
    "Titanic",
    ("A seventeen-year-old aristocrat falls in love with a kind but " +
     "poor artist aboard the luxurious, ill-fated R.M.S. Titanic."),
    "https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg",
    "https://www.youtube.com/watch?v=2e-eXJ6HgkQ")

love_actually = media.Movie(
    "Love Actually",
    ("Follows the lives of eight very different couples in dealing with " +
     "their love lives in various loosely interrelated tales all set " +
     "during a frantic month before Christmas in London, England."),
    "https://upload.wikimedia.org/wikipedia/en/e/eb/Love_Actually_movie.jpg",
    "https://www.youtube.com/watch?v=ZmUaH-n_wbA")

forest_gump = media.Movie(
    "Forest Gump",
    ("While not intelligent, Forrest Gump has accidentally been present at" +
     " many historic moments, but his true love, Jenny Curran, eludes him."),
    "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",
    "https://www.youtube.com/watch?v=bLvqoHBptjg")

the_great_gatsby = media.Movie(
    "The Great Gatsby",
    ("A writer and wall street trader, Nick, finds himself drawn to the " +
     "past and lifestyle of his millionaire neighbor, Jay Gatsby."),
    "https://upload.wikimedia.org/wikipedia/en/c/c2/TheGreatGatsby2013Poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=rARN6agiW7o")

the_devel_wears_prada = media.Movie(
    "The Devil Wears Prada",
    ("A smart but sensible new graduate lands a job as an assistant to " +
     "Miranda Priestly, the demanding editor-in-chief of a high " +
     "fashion magazine."),
    "https://upload.wikimedia.org/wikipedia/en/e/e7/The_Devil_Wears_Prada_main_onesheet.jpg",  # noqa
    "https://www.youtube.com/watch?v=XTDSwAxlNhc")

movies = [one_day, titanic, love_actually, forest_gump,
          the_great_gatsby, the_devel_wears_prada]
# fresh_tomatoes.open_movies_page(movies)
print(media.Movie.__doc__)

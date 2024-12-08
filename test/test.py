import gmap_popular_times_scrapper as gpts

place_url = "https://www.google.com/maps/place/example"

# Fetch popular times data
popular_times = gpts.gmap_popular_times(place_url)
print(popular_times)
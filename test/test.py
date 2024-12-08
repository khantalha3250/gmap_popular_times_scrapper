import gmap_popular_times_scrapper as gpts

place_url = "https://www.google.co.in/maps/place/Phoenix+Marketcity/@19.0863846,72.8864025,17z/data=!3m2!4b1!5s0x3be7c8878a6ce00d:0x5d860d2b775b3318!4m6!3m5!1s0x3be7c887efb78b9f:0x9f9dc99c3119470a!8m2!3d19.0863795!4d72.8889774!16s%2Fg%2F11bwnxxjkz?entry=ttu&g_ep=EgoyMDI0MTIwNC4wIKXMDSoASAFQAw%3D%3D"

# Fetch popular times data
popular_times = gpts.gmap_popular_times(place_url)
print(popular_times)
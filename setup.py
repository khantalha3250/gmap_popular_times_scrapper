from setuptools import setup, find_packages

setup(
    name="gmap_popular_times_scrapper",
    version="0.1.0",
    description="A library to scrape Google Maps popular times data.",
    author="Mohd Talha",
    author_email="kt7863250@gmail.com",
    packages=find_packages(),
    install_requires=[
        "selenium"
    ],
    
)

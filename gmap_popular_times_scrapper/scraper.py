from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def gmap_popular_times(place_url):

    # Set up the Selenium WebDriver
    driver = webdriver.Chrome()  # Replace with your WebDriver path if needed
    driver.get(place_url)

    try:
        # Wait for the page to load and popular times data to be visible
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'g2BVhd')]"))
        )

        # Locate all day containers (each day is typically grouped)
        day_containers = driver.find_elements(By.XPATH, "//div[contains(@class, 'g2BVhd')]")

        popular_times = {}

        for index, container in enumerate(day_containers):
            day_name = ["Sunday","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"][index]

            # Check if the day is marked as closed
            closed_message = container.find_elements(By.XPATH, ".//div[contains(text(), 'Closed')]")
            if closed_message:
                popular_times[day_name] = "Closed"
                continue

            # Extract busy data for the day
            hourly_data = container.find_elements(By.XPATH, ".//div[@role='img']")
            day_popular_times = {}
            for hour_div in hourly_data:
                aria_label = hour_div.get_attribute("aria-label")
                if aria_label and "busy at" in aria_label:
                    # Parse the aria-label to extract percentage and time
                    parts = aria_label.split(" busy at ")
                    percentage = parts[0].strip()  # E.g., "81%"
                    time = parts[1].strip().replace("\u202f", " ")  # Replace narrow no-break space
                    day_popular_times[time] = percentage

            # If no data is found for the day, mark it as "No Data"
            popular_times[day_name] = day_popular_times if day_popular_times else "No Data"

        return popular_times

    except Exception as e:
        print(f"Error scraping popular times: {e}")
        return None
    finally:
        driver.quit()


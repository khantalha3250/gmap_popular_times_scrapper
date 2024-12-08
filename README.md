
# gmap_popular_times_scrapper

A Python library for scraping "Popular Times" data for places from Google Maps.

---

## Overview

`gmap_popular_times_scrapper` allows you to scrape the **Popular Times** data from Google Maps for all days of the week. This data is useful for understanding foot traffic patterns at various locations.

---

## Features

- Scrape **Popular Times** data for all days of the week.
- Identify closed days and hours.
- Easy-to-use interface for integration into other projects.

---

## Installation

Install the library using pip:

```bash
pip install gmap_popular_times_scrapper
```

---

## Usage

Here’s how to use the library in your project:

### Code Example

```python
import gmap_popular_times_scrapper as gpts

# Provide the Google Maps place URL
place_url = "https://www.google.com/maps/place/example"

# Fetch popular times data
popular_times = gpts.gmap_popular_times(place_url)

# Print the result
print(popular_times)
```

### Output Example

```python
{
    "Monday": {"8 AM": "20%", "9 AM": "50%", ...},
    "Tuesday": {"Closed"},
    ...
}
```

---

## Dependencies

- `selenium`: For browser automation.
- **Chrome WebDriver**: Required for Selenium to interact with Chrome.

---


## Contributing

Contributions are welcome! If you’d like to contribute:

1. Fork this repository.
2. Create a feature branch:

    ```bash
    git checkout -b feature-name
    ```

3. Commit your changes:

    ```bash
    git commit -m "Add feature-name"
    ```

4. Push to the branch:

    ```bash
    git push origin feature-name
    ```

5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Support

If you encounter any issues, feel free to open an issue on GitHub.

---

## Disclaimer

This tool uses browser automation to scrape data from Google Maps. It is intended solely for personal and educational purposes. Using this tool for commercial, enterprise, or any unauthorized purposes may violate Google's Terms of Service and policies.

The developers of this tool are not responsible for any misuse, legal consequences, or actions taken by Google as a result of violating these terms. Please ensure compliance with all applicable laws, regulations, and policies before using this tool.

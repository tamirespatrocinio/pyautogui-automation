<h1 align="center">Pyautogui Automation</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/tamirespatrocinio/pyautogui-automation?color=56BEB8">
  <img alt="Github language count" src="https://img.shields.io/github/languages/count/tamirespatrocinio/pyautogui-automation?color=56BEB8">
  <img alt="Repository size" src="https://img.shields.io/github/repo-size/tamirespatrocinio/pyautogui-automation?color=56BEB8">
  <img alt="CC0 License" src="https://img.shields.io/badge/license-CC0_1.0-56BEB8.svg">



</p>

<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0; 
  <a href="#sparkles-features">Features</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="https://github.com/tamirespatrocinio" target="_blank">Author</a>
</p>

<br>

## :dart: About

This project automates the process of logging into a website and filling out a product form using PyAutoGUI. The script interacts with the browser, enters user credentials, and automatically fills in product information from a CSV file.

Additionally, it includes a helper script (`take-position.py`) to capture the cursor's position on the screen, which can be used to fine-tune automation coordinates.

Two CSV files are included in the project:
- `products-test.csv`: Contains two products for testing.
- `products.csv`: A full dataset for production use.

## :sparkles: Features

:heavy_check_mark: Automates login to a website;\
:heavy_check_mark: Fills in product details based on CSV data;\
:heavy_check_mark: Scrolls through the page after each submission.

## :rocket: Technologies

The following tools were used in this project:

- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)
- [Pandas](https://pandas.pydata.org/)
- [Python](https://www.python.org/)

## :white_check_mark: Requirements

Before starting, you need to have [Python](https://www.python.org/) and [Pandas](https://pandas.pydata.org/) installed.

## :checkered_flag: Starting

```bash
# Clone this project
$ git clone https://github.com/tamirespatrocinio/pyautogui-automation

# Access the project directory
$ cd pyautogui-automation

# Install dependencies (optional, depending on your setup)
$ pip install pyautogui pandas

# Run the script
$ python product-register.py

# To capture screen coordinates, run the position helper script
$ python take-position.py
```
&#xa0;

<a href="#top">Back to top</a>

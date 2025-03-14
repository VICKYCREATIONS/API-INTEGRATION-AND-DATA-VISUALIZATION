# API-INTEGRATION-AND-DATA-VISUALIZATION
*Company*:CODETECH IT SOLUTIONS

*Name*:SAI VEEKSHANA THOTA

*Intern ID*:CT6WRAK

*Domain*:PYTHON PROGRAMMING

*Duration*:6 WEEKS

*Mentor*:NEELA SANTOSH

This Python program integrates with the CoinGecko API to fetch Bitcoin price data for the last seven days and visualizes the price trend using Matplotlib. It begins by importing essential libraries: `requests` for API communication, `pandas` for data handling, and `matplotlib.pyplot` for visualization. The API endpoint is defined along with query parameters specifying that prices should be retrieved in USD, covering the past seven days with daily intervals. The program then sends a request to the API and checks if the response is successful. If the request is valid, it extracts the JSON data and ensures the expected `"prices"` key is present before processing the data. The timestamps provided in milliseconds are converted into a human-readable datetime format, and the corresponding price values are stored in a Pandas DataFrame for easy manipulation. The data is then visualized using Matplotlib, where a line graph plots the price trend over time, enhancing readability with proper labels, a title, grid lines, and rotated x-axis labels. Additionally, the program includes error handling to manage cases where the API request fails or the response format is incorrect, ensuring robustness. This script provides a simple yet effective way to integrate an external API and visualize financial data efficiently.

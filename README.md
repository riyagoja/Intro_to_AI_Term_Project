# Project README

## Overview

This term project for my EECS 118 class at UCI (Introduction to Artificial Intelligence), involves the utilization of two datasets: **Flights** and **Cereal**. The Flights dataset encompasses information related to airline flights, covering aspects such as airports, flights, fares, airplane types, flight legs, and seat reservations. On the other hand, the Cereal dataset focuses on nutritional content and ratings of various cereal products.

The guidelines for my project were:
1. Your program should show a list of queries to the user and ask the user to choose one to start with.
2. After the user selects a query, collect more information from the user if needed.
3. Your Python program must communicate with the database for each query.
4. After reporting the result, your program should ask the user to choose another query or quit the program.
5. Your program should allow the user to load and reload the dataset.
6. Your program should support 5 relational queries and 5 non-relational queries based on the skills you learn from the course, e.g., machine learning, and reasoning.

## Datasets

### Flights Dataset

The flight dataset is used to finish the five relational queries portion of this project. This dataset contains information related to airline flights, including details about airports, flights, fares, airplane types, airplane instances, flight legs, leg instances, seat reservations, and more. The dataset is organized into several tables, each representing different aspects of the airline industry.

- **Airport:** contains information about airports, including their code, name, city, and state.
- **Flight:** stores details about flights, such as flight number, airline, and information about whether the flight operates on weekdays.
- **Fare:** holds fare information for flights, including fare code, amount, and restrictions.
- **Airplane_type & Airplane:** Provide details about airplane types, their maximum seats, and specific instances of airplanes.
- **Can_land:** Specifies which airplanes can land at which airports.
- **Flight_leg:** Represents legs of a flight, detailing departure and arrival airports, and scheduled departure and arrival times.
- **Leg_instance:** Records specific instances of flight legs, including the number of available seats, departure, and arrival times.
- **Seat_reservation:** Contains information about seat reservations, including flight number, leg number, reservation date, seat number, customer name, and customer phone.

### Cereal Dataset

The Cereal data is used to finish the five nonrelational queries portion of this project. This dataset has information about various cereal products, focusing on their nutritional content and ratings. Cereal has the following attributes:

- **Name:** The name of the cereal product.
- **Manufacturer:** The company or brand manufacturing the cereal.
- **Type:** The type or category of the cereal.
- **Calories:** The caloric content per serving of the cereal.
- **Protein:** The protein content per serving.
- **Fat:** The fat content per serving.
- **Sodium:** The sodium content per serving.
- **Fiber:** The dietary fiber content per serving.
- **Carbohydrates:** The carbohydrate content per serving.
- **Sugars:** The sugar content per serving.
- **Potassium:** The potassium content per serving.
- **Vitamins:** The vitamin content per serving.
- **Rating:** The overall rating of the cereal.

## Functionality

### Query 1

Find the cheapest non-stop flight given airports and a date. This query prompts the user to input the departure airport code, destination airport code, and the date of the flight. It then queries the database to find the cheapest non-stop flight based on the provided information and displays the result, including the flight number and cost.

### Query 2

Find the flight and seat information for a customer. The user is asked to input the customer's name. The program queries the database to retrieve the flight and seat information for that customer and displays the results.

### Query 3

Find all non-stop flights for an airline. The user is prompted to input the name of the airline. The program queries the database to find all non-stop flights for that airline and displays the results.

### Query 4

Find flights with available seats greater than a given number. The user is asked to input the minimum number of available seats. The program queries the database to find flights with available seats greater than the specified number and displays the results.

### Query 5

Find flights departing from a specific airport. The user provides the airport code for departure, and the program queries the database to find all flights departing from that specific airport, displaying the results.

### Query 6

Visualize the distribution of calories in cereals. Utilizes data visualization to present the distribution of calories in cereal products.

### Query 7

Explore the relationship between sugars and rating. Utilizes a scatter plot to visualize the relationship between sugar content and cereal ratings.

### Query 8

Predict ratings using linear regression based on multiple features. Applies linear regression on cereal data to predict ratings based on multiple nutritional features.

### Query 9

Predict ratings using a decision tree based on multiple features. Utilizes a decision tree model to predict cereal ratings based on various nutritional features.

### Query 10

Show the decision tree structure. Generates and displays the structure of the decision tree used for predicting cereal ratings. (Note: If there are no corresponding results found for these queries, the program will print “No result found.”)

## Implementation

I wrote this Python program to interact with the 'flights' and 'cereal' datasets. It establishes connections using the pymysql library, with separate cursors for each database. The cereal data is loaded into a Pandas DataFrame, 'cereal_data,' for analysis and visualization. The program has a menu for the user, and allows for various flight-related queries, visualizations of cereal data, and machine-learning tasks for predicting cereal ratings. Utilizing libraries like pandas, matplotlib, seaborn, and scikit-learn, the code is organized into various functions. I also implemented error handling for SQL queries.

## How to Run

1. **Install Dependencies:**
   Ensure you have Python and the required libraries installed. You can install them using the following command:

   `pip install pandas matplotlib seaborn scikit-learn pymysql`

2. **Database Setup:**
   On the MySQLWorkbench create your respective database and tables using MySQL, and import the provided datasets into tables.

3. **Running the Program:**

   Open a terminal and navigate to the project directory.
   Run the main Python script:
  
   `python3 main.py`

4. **Interact with the Program:**

   Follow the on-screen instructions to choose queries, visualizations, or machine-learning tasks.
 


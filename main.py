import pymysql
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor, plot_tree
from sklearn.metrics import mean_squared_error
import seaborn as sns

# Function to execute a SQL query and fetch the result
def execute_query(sql, cur):
    try:
        cur.execute(sql)
        return cur.fetchall()
    except pymysql.Error as e:
        print(f"Error executing SQL query: {e}")
        return None

# Establish a connection to the MySQL database
db_flights = pymysql.connect(host='localhost', user='mp', passwd='eecs118', db='flights')
cur_flights = db_flights.cursor()

# Establish a connection to the MySQL database for cereal
db_cereal = pymysql.connect(host='localhost', user='mp', passwd='eecs118', db='cereal')
cur_cereal = db_cereal.cursor()

# Load the cereal data from MySQL into a DataFrame
sql_cereal = "SELECT * FROM cereal"
cereal_data = pd.read_sql(sql_cereal, db_cereal)

# Flight-related queries

def query_cheapest_flight():
    departure_airport = input("Please enter the airport code for the departure airport: ")
    destination_airport = input("Please enter the airport code for the destination airport: ")
    flight_date = input("What is the date of the flight in yyyy-mm-dd? ")

    # SQL query to find the cheapest non-stop flight
    sql = f"SELECT Flight_number, MIN(Amount) as MinAmount FROM flights.Fare " \
          f"WHERE Flight_number IN (SELECT Flight_number FROM flights.Flight_leg " \
          f"WHERE Departure_airport_code = '{departure_airport}' " \
          f"AND Arrival_airport_code = '{destination_airport}' " \
          f"AND Leg_date = '{flight_date}') GROUP BY Flight_number ORDER BY MinAmount LIMIT 1;"

    # Execute the query and fetch the result
    result = execute_query(sql, cur_flights)

    if result:
        flight_number, fare_amount = result[0]
        print(f"The cheapest flight is {flight_number}, and the cost is ${fare_amount}.")
    else:
        print("No result found.")

def query_customer_flight():
    customer_name = input("Please enter the customer’s name: ")

    # SQL query to find the flight and seat information for a customer
    sql = f"SELECT Flight_number, Seat_number FROM flights.Seat_reservation " \
          f"WHERE Customer_name = '{customer_name}';"

    # Execute the query and fetch the result
    result = execute_query(sql, cur_flights)

    if result:
        flight_number, seat_number = result[0]
        print(f"The flight number is {flight_number}, and the seat number is {seat_number}.")
    else:
        print("No result found.")

def query_airline_flights():
    airline_name = input("What is the name of the airline? ")

    # SQL query to find all non-stop flights for an airline
    sql = f"SELECT Flight_number FROM flights.Flight " \
          f"WHERE Airline = '{airline_name}' AND Flight_number IN " \
          f"(SELECT DISTINCT Flight_number FROM flights.Flight_leg " \
          f"WHERE Leg_number = 1);"

    # Execute the query and fetch the result
    result = execute_query(sql, cur_flights)

    if result:
        flights = ", ".join(str(flight[0]) for flight in result)
        print(f"The non-stop flights are: {flights}.")
    else:
        print("No result found.")

def query_available_seats():
    min_seats = int(input("Enter the minimum number of available seats: "))

    # SQL query to find flights with available seats greater than a given number
    sql = f"SELECT Flight_number, Leg_number, Leg_date, Number_of_available_seats " \
          f"FROM flights.Leg_instance " \
          f"WHERE Number_of_available_seats > {min_seats};"

    # Execute the query and fetch the result
    result = execute_query(sql, cur_flights)

    if result:
        for row in result:
            flight_number, leg_number, leg_date, available_seats = row
            print(f"Flight {flight_number}, Leg {leg_number} on {leg_date}: {available_seats} available seats.")
    else:
        print("No result found.")

def query_departing_flights():
    departure_airport = input("Please enter the airport code for departure: ")

    # SQL query to find flights departing from a specific airport
    sql = f"SELECT DISTINCT Flight_number FROM flights.Flight_leg " \
          f"WHERE Departure_airport_code = '{departure_airport}';"

    # Execute the query and fetch the result
    result = execute_query(sql, cur_flights)

    if result:
        flights = ", ".join(str(flight[0]) for flight in result)
        print(f"The flights departing from {departure_airport} are: {flights}.")
    else:
        print("No result found.")

# Cereal-related queries

def visualize_calories_distribution(data):
    plt.figure(figsize=(10, 6))
    sns.histplot(data['calories'], kde=True)
    plt.title('Distribution of Calories in Cereals')
    plt.xlabel('Calories')
    plt.ylabel('Frequency')
    plt.show()

def explore_sugars_rating_relationship(data):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='sugars', y='rating', data=data)
    plt.title('Relationship between Sugars and Rating')
    plt.xlabel('Sugars')
    plt.ylabel('Rating')
    plt.show()

def predict_ratings_linear_regression(data):
    features = ['calories', 'protein', 'fat', 'sodium', 'fiber', 'carbo', 'sugars', 'potass', 'vitamins']
    X = data[features]
    y = data['rating']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    linear_model = LinearRegression()
    linear_model.fit(X_train, y_train)

    linear_predictions = linear_model.predict(X_test)

    linear_rmse = mean_squared_error(y_test, linear_predictions, squared=False)
    print(f'Linear Regression RMSE: {linear_rmse:.2f}')
    print("RMSE measures the average magnitude of the errors between predicted and actual ratings. "
          "A lower RMSE indicates better accuracy.")

def predict_ratings_decision_tree(data):
    features = ['calories', 'protein', 'fat', 'sodium', 'fiber', 'carbo', 'sugars', 'potass', 'vitamins']
    X = data[features]
    y = data['rating']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    tree_model = DecisionTreeRegressor()
    tree_model.fit(X_train, y_train)

    tree_predictions = tree_model.predict(X_test)

    tree_rmse = mean_squared_error(y_test, tree_predictions, squared=False)
    print(f'Decision Tree RMSE: {tree_rmse:.2f}')
    print("RMSE measures the average magnitude of the errors between predicted and actual ratings. "
          "A lower RMSE indicates better accuracy.")

def show_decision_tree_structure(data):
    features = ['calories', 'protein', 'fat', 'sodium', 'fiber', 'carbo', 'sugars', 'potass', 'vitamins']
    X = data[features]
    y = data['rating']

    X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)

    tree_model = DecisionTreeRegressor()
    tree_model.fit(X_train, y_train)

    # Plot decision tree structure
    plt.figure(figsize=(20, 10))
    plot_tree(tree_model, feature_names=features, filled=True, rounded=True, fontsize=10)
    plt.title('Decision Tree Structure')
    plt.show()

# User menu
while True:
    print("\nSelect a query:")
    print("1. Find the cheapest non-stop flight given airports and a date")
    print("2. Find the flight and seat information for a customer")
    print("3. Find all non-stop flights for an airline")
    print("4. Find flights with available seats greater than a given number")
    print("5. Find flights departing from a specific airport")
    print("6. Visualize the distribution of calories in cereals")
    print("7. Explore the relationship between sugars and rating")
    print("8. Predict ratings using linear regression based on multiple features")
    print("9. Predict ratings using a decision tree based on multiple features")
    print("10. Show the decision tree structure")
    print("11. Quit")

    choice = input("Enter the query number (1-11): ")

    if choice == '1':
        query_cheapest_flight()
    elif choice == '2':
        query_customer_flight()
    elif choice == '3':
        query_airline_flights()
    elif choice == '4':
        query_available_seats()
    elif choice == '5':
        query_departing_flights()
    elif choice == '6':
        visualize_calories_distribution(cereal_data)
    elif choice == '7':
        explore_sugars_rating_relationship(cereal_data)
    elif choice == '8':
        predict_ratings_linear_regression(cereal_data)
    elif choice == '9':
        predict_ratings_decision_tree(cereal_data)
    elif choice == '10':
        show_decision_tree_structure(cereal_data)
    elif choice == '11':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 11.")

# Close the database connections
db_flights.close()
db_cereal.close()

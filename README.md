# Students-Rank-Prediction

This project is designed to analyze students' quiz performance and predict their probable NEET rank based on historical quiz data. Additionally, the project estimates the most likely medical college a student could get admission to based on the predicted rank.
The solution is built in Python and fetches quiz data from API endpoints, processes the performance metrics, and applies a ranking algorithm to generate insights.

# This Code does the following:
- Fetches current and historical quiz data from APIs.
- Extracts relevant details into Pandas DataFrames.
- Calculates accuracy for both current and historical performances.
- Predicts the student's NEET rank based on accuracy.
- Assigns a college based on predicted rank.
- Generates a final report summarizing the student's performance and recommendations.

# I have used to libraries for this project:
1. requests: This library is used to send HTTP requests (like fetching data from a website).
2. json: This library is used to work with JSON data (which is a common format for storing and exchanging data).

# Function to fetch quiz data.
This fetch_quiz_data function fetches quiz data from a given url.
It handles errors using a try-except block to prevent the program from crashing if something goes wrong.
The function extracts quiz questions from the JSON response and returns them.

# Function to calculate accuracy.
The calculate_accuracy function calculates the percentage of correct answers.
It checks how many questions are marked as correct (is_correct is True).
If there are no questions, it avoids division by zero and returns 0.

# Function to predict rank and college.
The predict_rank_and_college function predicts a student's NEET rank based on their quiz accuracy.
It calculates rank using a formula where higher accuracy gives a lower (better) rank.
Based on rank, it suggests a medical college:
Top Tier if rank < 10,000
Mid Tier if rank < 50,000
Lower Tier otherwise

# Function to generate report.
This function generates a detailed report on student performance.
It fetches current and historical quiz data from two URLs.
It calculates the current and past accuracy.
It predicts the rank and college based on accuracy.
It returns a formatted report.

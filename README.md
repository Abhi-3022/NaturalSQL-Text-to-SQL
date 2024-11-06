# NaturalSQL-Text-to-SQL

This project is a Streamlit application designed to convert natural language questions into SQL queries and execute them on a student database. The app utilizes Google’s Gemini model (via the google.generativeai API) to interpret questions, generate SQL queries, and then retrieve relevant data from a local SQLite database. The database named STUDENT contains columns like NAME, CLASS, SECTION, and MARKS. The user inputs questions in plain English, and the application formulates the appropriate SQL query to fetch data matching the question, displaying the results on the Streamlit interface.

# Project Purpose
The primary goal of this application is to simplify database interactions for users with limited SQL knowledge by enabling them to query a database using natural language questions. It serves as an intuitive interface for data retrieval, which can be especially useful for educators, administrators, and analysts who need quick access to student records without writing SQL code.

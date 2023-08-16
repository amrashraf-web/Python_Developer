# 13 Given two tables, `orders` and `customers`, with relevant fields, write an SQL query to retrieve all orders along with the corresponding customer names.
# Retrieving Orders with Corresponding Customer Names:

# SELECT orders.*, customers.customer_name
# FROM orders
# JOIN customers ON orders.customer_id = customers.customer_id


##############################################################################

# 14  Using a subquery, find the second-highest salary from a table named `employees`.

# Finding Second-Highest Salary using Subquery:

# SELECT DISTINCT salary
# FROM employees
# ORDER BY salary DESC
# LIMIT 1 OFFSET 1;

##############################################################################


# 15  Explain what indexes are in the context of a database. How can you create an index on a specific column to improve query performance?

# Indexes in a database are data structures that improve the speed of data retrieval operations on tables. They provide a faster way to look up rows based on the values in one or more columns. You can create an index on a specific column using the CREATE INDEX statement

# CREATE INDEX idx_column_name ON table_name (column_name);

##############################################################################

# 16  Describe the concept of database normalization. Provide an example of transforming an unnormalized table into third normal form (3NF).?

# Database normalization is the process of organizing the data in a database to minimize redundancy and dependency. It involves dividing a database into multiple related tables and defining relationships between them

# Suppose we have an unnormalized table named "Customers" with the following columns:

# - CustomerID(primary key)
# - FirstName
# - LastName
# - Address
# - City
# - State
# - ZipCode
# - PhoneNumber
# - Email
# - DateOfBirth
# - Gender
# - CreditCardNumber
# - CreditCardExpiryDate
# - CreditCardType

# To transform this table into 3NF, we can break it down into the following tables:

# - Customers(primary key: CustomerID)
# - Addresses(foreign key: CustomerID)
# - CreditCards(foreign key: CustomerID)

# The "Customers" table will contain the basic information about each customer, such as their name, address, and phone number. The "Addresses" table will contain the address information for each customer, including their city, state, and zip code. The "CreditCards" table will contain the credit card information for each customer, including their credit card number, expiry date, and type.

# By breaking down the "Customers" table into these three tables, we have normalized the data and reduced the redundancy of the data. This will make it easier to maintain and update the data in the future.


##############################################################################


# 17  Write an SQL query to calculate the average, maximum, and minimum order amounts from an `order_details` table.

# SELECT AVG(order_amount) AS avg_order_amount,
#        MAX(order_amount) AS max_order_amount,
#        MIN(order_amount) AS min_order_amount
# FROM order_details;


##############################################################################

# 18 Define window functions in SQL and provide an example of using the `ROW_NUMBER()` function to paginate results from a table.

# Window functions perform calculations across a set of table rows related to the current row. The ROW_NUMBER() function assigns a unique number to each row within a result set.

# SELECT *,
#        ROW_NUMBER() OVER (ORDER BY salary DESC) AS row_num
# FROM employees;

##############################################################################

# 19 Explain the purpose of Common Table Expressions (CTEs) in SQL. Create a CTE that calculates the total revenue for each month over a year from an `invoices` table.

# CTEs are temporary result sets that can be referenced within a SELECT, INSERT, UPDATE, or DELETE statement. They improve code readability and allow complex queries to be broken down into simpler parts.

# WITH MonthlyRevenue AS(
#     SELECT EXTRACT(MONTH FROM invoice_date) AS month, SUM(amount) AS total_revenue
#     FROM invoices
#     GROUP BY month
# )
# SELECT * FROM MonthlyRevenue


##############################################################################


# 20 Discuss what recursive queries are and when they might be used. Write a recursive SQL query to find all the ancestors of a given employee in an organizational hierarchy table.

# Recursive queries are used to query hierarchical or recursive data structures. They involve a common table expression (CTE) that references itself.

# WITH RECURSIVE EmployeeHierarchy AS (
#     SELECT employee_id, manager_id
#     FROM employees
#     WHERE employee_id = 123
#     UNION ALL
#     SELECT e.employee_id, e.manager_id
#     FROM employees e
#     JOIN EmployeeHierarchy eh ON e.employee_id = eh.manager_id
# )
# SELECT * FROM EmployeeHierarchy;


##############################################################################

# 21 Describe the JSONB data type in PostgreSQL. Write a query that retrieves specific values from a JSONB column named `data` within a table.

# JSONB is a binary format for storing JSON data in PostgreSQL. It allows for efficient storage, indexing, and querying of JSON data.

# SELECT data->'key1' AS value1,
#        data->>'key2' AS value2
# FROM table_name;


##############################################################################

# 22 How can stored procedures improve code organization and reusability in SQL? Provide an example of creating a stored procedure that inserts a new customer into a table

# Stored procedures are precompiled SQL statements that can be stored and executed on the database server. They improve code organization and reusability

# CREATE PROCEDURE InsertCustomer(IN name VARCHAR(255), IN email VARCHAR(255))
# BEGIN
#     INSERT INTO customers (customer_name, customer_email) VALUES (name, email);
# END;

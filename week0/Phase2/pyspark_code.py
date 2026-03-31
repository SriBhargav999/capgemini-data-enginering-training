from pyspark.sql import SparkSession
from pyspark.functions import sum,col,,count
spark = SparkSession.builder.appName("practice").getOrCreate()

customers_data = [
    (1, "Ravi", "Hyderabad", 25),
    (2, "Sita", "Chennai", 32),
    (3, "Arun", "Hyderabad", 28),
    (4, "Meena", "Bengaluru", 35),
    (5, "Kiran", "Chennai", 22)
]

orders_data = [
    (101, 1, 2500, "2026-03-01"),
    (102, 2, 1800, "2026-03-02"),
    (103, 1, 3200, "2026-03-03"),
    (104, 3, 1500, "2026-03-04"),
    (105, 5, 2800, "2026-03-05")
]

customers = spark.createDataFrame(customers_data, ["customer_id","customer_name","city","age"])
orders = spark.createDataFrame(orders_data, ["order_id","customer_id","amount","order_date"])

Codes:

1. Total order amount for each customer
  cus_amount= customers.join(orders, on="customer_id").groupBy(customers["customer_name"]).agg(sum(orders["amount"]).alias("total_amount"))
  cus_amount.show()

2. Top 3 customers by total spend
  cus_amount=customers.join(orders, on="customer_id").groupBy(customers["customer_name"]) .agg(sum(orders["amount"]).alias("total_amount")).orderBy(col("total_amount").desc()).limit(3)
  cus_amount.show()

3. Customers with no orders
  cus_amount=customers.join(orders, on="customer_id",how="left_anti")
  cus_amount.show()

4. City-wise total revenue
  cus_amount=customers.join(orders, on="customer_id").groupBy(customers["city"]).agg(sum(orders["amount"]).alias("total_amount"))
  cus_amount.show()

5. Average order amount per customer
  cus_amount= customers.join(orders, on="customer_id").groupBy(customers["customer_name"]).agg(avg(orders["amount"]).alias("total_amount"))
  cus_amount.show()

6. Customers with more than one order
  cus_amount= customers.join(orders, on="customer_id").groupBy(customers["customer_name"]).agg(count(orders["order_id"]).alias("total_orders")).filter(col("total_orders")>1)
  cus_amount.show()

7. Sort customers by total spend descending
  cus_amount=customers.join(orders, on="customer_id").groupBy(customers["customer_name"]) .agg(sum(orders["amount"]).alias("total_amount")).orderBy(col("total_amount").desc())
  cus_amount.show()

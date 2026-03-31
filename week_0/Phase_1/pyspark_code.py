from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Practice").getOrCreate()

customers = spark.createDataFrame([
 (1, "Ravi", "Hyderabad", 25),
 (2, "Sita", "Chennai", 32),
 (3, "Arun", "Hyderabad", 28)
], ["customer_id", "customer_name", "city", "age"])

#Implementing the codes

1. Show all customers
  customers.show()

2. Show customers from Chennai
  chennai_cus=customers.filter(customers["city"]=="Chennai")
  chennai_cus.show()

3. Show customers with age > 25
   cus_age=customers.filter(customers['age']>25)
   cus_age.show()

4. Show only customer_name and city
   cus_city=customers.select("customer_name", "city")
   cus_city.show()
                    (OR)
   from pyspark.sql.functions import col
   cus_city=customers.select(col("customer_name"), col("city"))
   cus_city.show()

5. Count customers city-wise
   cus_city=customers.groupBy("city").count.show()

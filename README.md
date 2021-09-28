# Pyspark

Spark was built is scala language. It provides API in Scala, Python, Java. It is a part of Hadoop Ecosystem (HDFS). It is capable of distributted computing. Spark doesn't run on one node or one machine, it runs on multiple node cluster. It was built to overcome some of the limitations of  Hadoop's MapReduce engine. 

MapReduce is awesome for parallel processing but its limitatioj is that everything has to be expressed as chain of map and reduce tasks. It doesn't have interactive environment. 

PySpark is an interface for Apache Spark. Pyspark uses python API to interact with Resilient Distributed Data (RDD).

#### Why do we need Pyspark
Python / R - It provides "Read-Evaluate-Print-Loop" (REPL) environment. It represents data in any form, explore and identify hidden pattern. They do all this with a fast feedback at every step. They cannot meet the performance and service level agreement (SLA) requirement of a production system. They can't be scaled, they can't be robust and they can't have all the auditing and logged in required in order to run the system for business needs.

In order to go from analysis of data to building a production system based on data, we need REPL environment as well as SLA.

Apache Spark is a general purpose engine for data processing and analysis. It is one engine which does the job of SQL, REPL (Python/R) and SAL (Java / C++)

PySpark is a great language to learn because it enables scalable analysis and ML pipelines


PySpark features quite a few libraries for writing efficient programs. Furthermore, there are various external libraries that are also compatible. Here are some of them:
1. PySparkSQL 
2. MLlib
3. GraphFrames

#### Advantages of using PySpark: 
1. Python is very easy to learn and implement. 
2. It provides simple and comprehensive API. 
3. With Python, the readability of code, maintenance, and familiarity is far better. 
4. It features various options for data visualization, which is difficult using Scala or Java.






######  This repository contains some of the custom functionality of Pyspark.






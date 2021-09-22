map_partition = {}
for pos, code in enumerate(list_of_codes):
	map_partition[code] = pos

        
def custom_partitioner(cat_cd): 
	"""This function return the partition number for a given category code"""
        return map_partition[code]
        
        
## Suppose there are 10 different codes and each code has 10 rows (total of 10*10 rows). This custom partitioner will create 10 partitions and each partition will have rows with same codes. (all code 1 rows in one partition, code 2 rows in another...)

df_rdd     = df.rdd.map(lambda x : (x[0], x)) 
df_rdd     = df_rdd.partitionBy(num_partitions, custom_partitioner) # creating rdd partitions
rdd_num_partitions  = df_rdd.getNumPartitions()  # get partition numbers


## creating df from rdd
final_df       = spark.createDataFrame(df_rdd.map(lambda x: x[1]))  

## to get the partition id to column mapping 
final_df_partitions  = final_df.withColumn("partitionId", spark_partition_id()).groupBy("partitionId").agg(countDistinct('{}'.format(any_column_name))).orderBy('partitionId').count()





            

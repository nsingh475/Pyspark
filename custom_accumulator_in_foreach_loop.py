## Below is the illustration of how one can collect values across partitions using accumulators.

import custom_accumulators as ca

## initialising the custom accumulator
acc         = spark.sparkContext.accumulator(list(), ca.ListAccumulator())
acc_manager = acc


## Function which will be called for each loop
def test(partition, acc_manager_inst):
	test_list = []
	for row in partition :
		i = row['any_column_name']
		test_list.append(i)

	accumulator = acc_manager_inst
        accumulator += test_list



## Calling a function for each loop
df.rdd.foreachPartition(lambda x: calculate_distance(x, acc_manager)

## getting value from accumulator
result = acc.value
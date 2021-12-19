import random
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
dice_result=[]
for i in range(0,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dice_result.append(dice1+dice2)
mean=sum(dice_result)/len(dice_result)
std_deviation=statistics.stdev(dice_result)
print("mean of the data is {}".format(mean))
print("standard deviation of the data is  {}".format(std_deviation))
median=statistics.median(dice_result)
mode=statistics.mode(dice_result)
print("mode of the data is {}".format(mode))
print("medain of the data is {}".format(median))
first_stdev_start,first_stdev_end=mean-std_deviation,mean+std_deviation
second_stdev_start,second_stdev_end=mean-(2*std_deviation),mean+(2*std_deviation)
third_stdev_start,third_stdev_end=mean-(3*std_deviation),mean+(3*std_deviation)

list_of_data_within_one_standard_deviation=[result for result in dice_result if result > first_stdev_start and  result < first_stdev_end]
list_of_data_within_two_standard_deviation=[result for result in dice_result if result > second_stdev_start and  result < second_stdev_end]
list_of_data_within_three_standard_deviation=[result for result in dice_result if result > third_stdev_start and  result < third_stdev_end]

print("{}% of data lies within 1 standard deviation ".format(len(list_of_data_within_one_standard_deviation)*100.0/len(dice_result)))
print("{}% of data lies within 2 standard deviation ".format(len(list_of_data_within_two_standard_deviation)*100.0/len(dice_result)))
print("{}% of data lies within 3 standard deviation ".format(len(list_of_data_within_three_standard_deviation)*100.0/len(dice_result)))

fig=ff.create_distplot([dice_result],["result"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[first_stdev_start,first_stdev_start],y=[0,0.17],mode="lines",name="stdev1"))
fig.add_trace(go.Scatter(x=[first_stdev_end,first_stdev_end],y=[0,0.17],mode="lines",name="stdev1"))
fig.add_trace(go.Scatter(x=[second_stdev_start,second_stdev_start],y=[0,0.17],mode="lines",name="stdev2"))
fig.add_trace(go.Scatter(x=[second_stdev_end,second_stdev_end],y=[0,0.17],mode="lines",name="stdev2"))
fig.add_trace(go.Scatter(x=[third_stdev_start,third_stdev_start],y=[0,0.17],mode="lines",name="stdev3"))
fig.add_trace(go.Scatter(x=[third_stdev_end,third_stdev_end],y=[0,0.17],mode="lines",name="stdev3"))
fig.show()
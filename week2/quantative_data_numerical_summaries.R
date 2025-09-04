# example data
Height <- c(61.7, 66.5, 68.3, 70.1, 75.1)

# summary data set
sumaary(Height)
#   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
#  61.70   66.50   68.30   68.30   70.10   75.10 

# 5-number summary를 자동으로 보여줌
# 5-number sumaary (min, 1st Quartile(=25%under 1사분위수), Median(=50%), 3rd Quartile(=75% 3사분위수), Max)

# here, we can get IQR which means InterQuartile Range. This means 3rd Quartile - 1st Quatile
# SD is standard deviation(표준편차) - measure of spread, the average distance that our data points fall from the mean value.
# n is sample size 
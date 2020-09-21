# geo1001_hw01 Linjun Wang 5214513
# geo1001_hw01.py
It's the  main function. It calls all of the functions for every part.
My 5 xls files are gathered as 5 sheets in one xls file named "HEAT.xls", you can find the file in my repository.

readHeat() is a function to read the xls file and return all the variables for one senor.

# hw01A1.py
This .py file is for questions in part A1. 
calMSV() calculate mean, standard diviation and vaiance and put them into a csv file for each of the sensor variables of one sensor.

plotHistogram() plot histogram for given data with the given bins.

plotPoligons() plot frequency poligons for given data, poligons will overlap in different color with a legend.

plotBox() plot boxplots for given data, the last argument should be 'T' for temperature or 'WS' for wind speed or 'WD' for wind direction.

# hw01A2.py
This .py file is for questions in part A2. 
plotPmf() will plot PMFs for given data, the data should be temperature data.

plotPdf() plot PDFs for given temperature data, PDFs will be Kernel density estimation when its plotted.

plotCdf() plot CDFs for given temperature data, they will be smooth CDFs in the plot.

plotWS() plot PDFs in discontinuous form and Kernel density estimation overlap on the PDFs for wind speed data.

pmf() is a function to calculate the probablity of the given data.

# hw01A3.py
This .py file is for questions in part A3.
calCorrelation() will calculate correlations between two arguments, return Pearson's and Spearman's correlation coefficients as well as their p values.

showCorrelation() will calculate correlations for temperature or wet bulb globe or crosswind speed between five sensors, it will plot the correlations on a scatter plot and show them on the terminal as well.

plotScatter() will plot a scatterplot to show the relation of two different sensors. For five sensors, it will show 10 scatter plots in total.

pScatter() is a function will be used in plotScatter() to remove nan numbers and interpolate to get the same size sample.

# hw01A4.py
This .py file is for questions in part A4.
calCI() will calculate 95% confidence intervals for 5 sensors' one variable. It will plot the CDFs for different sensors and overlap two lines as confidence interval on it. At the same time, it will put the confidence intervals into a csv file.

hypothesisTest() is to do hypothesis test. It will test if temperature and wind speed time series are the same for 4 sensor combinations. It will print the result of t value and p-value for every cases.

find_close() is a function used in calCI() to find a probability near 0.05 and 0.95.

# bonus.py
This .py file is for the bonus question.
readDate() will read the date data of HEAT.xls for one sensor and return a list of timestamp.

calHC() will make a dataframe which contains date and temperature and group the dataframe by date to calculate means of temperature. Finally it will find the highest value of temperature and the lowest, to find the hottest and the coldest day.

# geo1001_hw01WANGlatex_v2.zip
My latex code and pdf are in this zip with pictures used in latex code. 


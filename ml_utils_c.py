import pandas as pd
import numpy as np
import math
import sklearn.datasets
import ipywidgets as widgets

##Seaborn for fancy plots. 
#%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams["figure.figsize"] = (8,8)

class edaDF:
    """
    A class used to perform common EDA tasks

    ...

    Attributes
    ----------
    data : dataframe
        a dataframe on which the EDA will be performed
    target : str
        the name of the target column
    cat : list
        a list of the names of the categorical columns
    num : list
        a list of the names of the numerical columns

    Methods
    -------
    setCat(catList)
        sets the cat variable listing the categorical column names to the list provided in the argument catList
        
        Parameters
        ----------
        catlist : list
            The list of column names that are categorical

    setNum(numList)
        sets the cat variable listing the categorical column names to the list provided in the argument catList
        
        Parameters
        ----------
        numlist : list
            The list of column names that are numerical

    countPlots(self, splitTarg=False, show=True)
        generates countplots for the categorical variables in the dataset 

        Parameters
        ----------
        splitTarg : bool
            If true, use the hue function in the countplot to split the data by the target value
        show : bool
            If true, display the graphs when the function is called. Otherwise the figure is returned.
    
    histPlots(self, splitTarg=False, show=True)
        generates countplots for the categorical variables in the dataset 

        Parameters
        ----------
        splitTarg : bool
            If true, use the hue function in the countplot to split the data by the target value
        show : bool
            If true, display the graphs when the function is called. Otherwise the figure is returned. 

    outlier(self, col: str, k: int = 3)
        print outliers in the data

        Parameters
        ----------
        elf.df[(self.df[col] < lower) 
        if true, prints True 
        else print false

        (self.df[col] > upper)]
        if true prints true
        else print flase
    
    correlation(df)
         print the correlation between variables

        

    fullEDA()
        Displays the full EDA process. 
    """
    def __init__(self, data, target):
        self.data = data
        self.target = target
        self.cat = []
        self.num = []

    def info(self):
        return self.data.info()

    def giveTarget(self):
        return self.target
        
    def setCat(self, catList):
        self.cat = catList
    
    def setNum(self, numList):
        self.num = numList

    def countPlots(self, splitTarg=False, show=True):
        n = len(self.cat)
        cols = 2
        figure, ax = plt.subplots(math.ceil(n/cols), cols)
        r = 0
        c = 0
        for col in self.cat:
            if splitTarg == False:
                sns.countplot(data=self.data, x=col, ax=ax[r][c])
            if splitTarg == True:
                sns.countplot(data=self.data, x=col, hue=self.target, ax=ax[r][c])
            c += 1
            if c == cols:
                r += 1
                c = 0
        if show == True:
            figure.show()
        return figure

    def histPlots(self, kde=True, splitTarg=False, show=True):
        n = len(self.num)
        cols = 2
        figure, ax = plt.subplots(math.ceil(n/cols), cols)
        r = 0
        c = 0
        for col in self.num:
            #print("r:",r,"c:",c)
            if splitTarg == False:
                sns.histplot(data=self.data, x=col, kde=kde, ax=ax[r][c])
            if splitTarg == True:
                sns.histplot(data=self.data, x=col, hue=self.target, kde=kde, ax=ax[r][c])
            c += 1
            if c == cols:
                r += 1
                c = 0
        if show == True:
            figure.show()
        return figure

    def stats(self):
        return self.data.describe()

    def isnull(self):

        return self.data.isnull().sum()  

    def outliers(self, col: str, k: int = 3):
        mean = self.df[col].mean()
        std = self.df[col].std()
        lower = mean - k*std
        upper = mean + k*std
        return self.df[(self.df[col] < lower) | (self.df[col] > upper)]
    
    def correlation(self):
        return self.df.corr()

    def fullEDA(self):
        out1 = widgets.Output()
        out2 = widgets.Output()
        out3 = widgets.Output()
        out4 = widgets.Output()
        out5 = widgets.Output()
        out6 = widgets.Output()
        out7 = widgets.Output()

        tab = widgets.Tab(children = [out1, out2, out3,out4,out5,out6,out7])
        tab.set_title(0, 'Info')
        tab.set_title(1, 'Categorical')
        tab.set_title(2, 'Numerical')
        tab.set_title(3, 'Statistics')
        tab.set_title(4, 'NullValues')
        tab.set_title(5, 'Outliers')
        tab.set_title(6, 'Correlation Matrix')

        display(tab)

        with out1:
            self.info()

        with out2:
            fig2 = self.countPlots(splitTarg=True, show=False)
            plt.show(fig2)
        
        with out3:
            fig3 = self.histPlots(kde=True, show=False)
            plt.show(fig3)

        with out4:
            self.stats()
            
        with out5:
            self.data.isnull().sum()  

        with out6:
            self.outliers()

        with out7:
            self.correlation()


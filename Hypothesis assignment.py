#Question 1:
import pandas as pd
import scipy
import numpy as np
from scipy import stats
data=pd.read_csv("E:\\Assignments\\Assignment week 8\\Hypothesis\\Assignments\\cutlets.csv")
data1=data.iloc[0:35,]
data1.mean()
data1.columns = "cutlet1", "cutlet2"
#Normality test , we assume that H0: the data is normal ; H1: our data is not normal
stats.shapiro(data1.cutlet1)
stats.shapiro(data1.cutlet2)
# As both the Normality test are saying that p>0.05 so we cannot reject H0 
#hence we proceed with variance test
scipy.stats.levene(data1.cutlet1, data1.cutlet2)
# p-value = 0.417616 > 0.05 so p high null fly => Equal variances
# 2 Sample T test
scipy.stats.ttest_ind(data1.cutlet1, data1.cutlet2)
#Hence the T-test values is 0.4722394724599501>0.05. According to the conditon p high null fly
#We can conclude that both the cutlets are of same size.



#************************************************************************************************************************************
#Question 2:
import pandas as pd
import scipy
import numpy as np
from scipy import stats
q2=pd.read_csv("E:\\Assignments\\Assignment week 8\\Hypothesis\\Assignments\\lab_tat_updated.csv")
q2.columns
#Normality test , we assume that H0: the data is normal ; H1: our data is not normal
stats.shapiro(q2.Laboratory_1)
stats.shapiro(q2.Laboratory_2)
stats.shapiro(q2.Laboratory_3)
stats.shapiro(q2.Laboratory_4)
# As both the Normality test are saying that p>0.05 so we cannot reject H0 
#hence we proceed with variance test
scipy.stats.levene(q2.Laboratory_1, q2.Laboratory_2,q2.Laboratory_3,q2.Laboratory_4)
# p-value = 0.417616 > 0.05 so p high null fly => Equal variances
# One way anova test
q2.columns
F, p = stats.f_oneway(q2.Laboratory_1, q2.Laboratory_2 , q2.Laboratory_3,q2.Laboratory_4)
p
# As the p value is 2.1453e-58 <0.05 , So p low H0 go, So we are rejecting H0 and we can conclude that yes there is difference in the
#average Turn Around Time (TAT) of reports of the laboratories on their preferred list


#******************************************************************************************************************************************
#question3
import pandas as pd
import scipy
import numpy as np
from scipy import stats

BuyerRatio = pd.read_csv("E:\\Assignments\\Assignment week 8\\Hypothesis\\Assignments\\BuyerRatio.csv")
#count=pd.crosstab(BuyerRatio[""],BuyerRatio[""])
BuyerRatios = pd.melt(BuyerRatio.reset_index(),id_vars=['index'], value_vars=['East','West','North','South'],var_name=['regions'])
#BuyerRatios.columns=['MaleFemale','regions','values']
count=pd.crosstab(BuyerRatios.index,BuyerRatios.value)
#countrename=pd.crosstab(BuyerRatios.MaleFemale,BuyerRatios.values)
Chisquares_results=scipy.stats.chi2_contingency(count)
Chi_square=[['','Test Statistic','p-value'],['Sample Data',Chisquares_results[0],Chisquares_results[1]]]
Chi_square
# As the chi_square value is greater than 0.05 According to our H0 we can say that male-female buyer rations are similar across regions



#***********************************************************************************************************************************
#Question4
import pandas as pd
import scipy
import numpy as np
from scipy import stats
q4=pd.read_csv("E:/Assignments/Assignment week 8/Hypothesis/Assignments/CustomerOrderform.csv")
q4=q4.iloc[0:300,]
from statsmodels.stats.proportion import proportions_ztest

tab1 = q4.India.value_counts()
tab1
tab2 = q4.Malta.value_counts()
tab2
tab3 = q4.Indonesia.value_counts()
tab3
tab4 = q4.Phillippines.value_counts()
tab4

q4_1=pd.DataFrame([tab1,tab2,tab3,tab4])
q4data=pd.crosstab(q4_1["Error Free"],q4_1["Defective"])
q4data
chi_results=scipy.stats.chi2_contingency(q4data)

chi_final=[['Test statistic','p-value'] ,[chi_results[0],chi_results[1]]]
chi_final

# Hence our value is >0.05 occording our H0 hypothesis i.e The defects varies by centre is true..




#**************************************************************************************************************************

#Question 5

import pandas as pd
import scipy
import numpy as np
from scipy import stats
from statsmodels.stats.proportion import proportions_ztest
q5=pd.read_csv("E:/Assignments/Assignment week 8/Hypothesis/Assignments/Fantaloons.csv")
q5.columns
table=pd.crosstab(q5['Weekdays'],q5['Weekend'])
table
c=np.array([233,167])
d=np.array([520,280])

stats, pval = proportions_ztest(c,d, alternative = 'two-sided') 
print(pval) 

stats, pval = proportions_ztest(c,d, alternative = 'larger') 
print(pval) 
# yes there is evidence at 5 % significance level to support this hypothesis
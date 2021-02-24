##Question 1
library(readr)
library(readxl)
q1=read.csv(file.choose())
q1=q1[1:35,]
attach(q1)
colnames(q1)=c("cutlet1","cutlet2")
shapiro.test(cutlet1)
shapiro.test(cutlet2)
## AS THE P VALUE IS GREATER THAN 0.05 WE CAN GO WITH H0 AS WE FAIL TO REJECT H0.
### NOW WE CHECK THE VARIANCE TEST

var.test(cutlet1,cutlet2)
### As the vaariances are greater than 0.05 . We say that variances are equal.
t.test(cutlet1,cutlet2, alternative = "two.sided", conf.level = 0.95, var.equal = T)

#*********************************************************************************************
#*Question 2
#*

q2=read.csv(file.choose())  
attach(q2)
colnames(q2)
shapiro.test(Laboratory_1)
shapiro.test(Laboratory_2)
shapiro.test(Laboratory_3)
shapiro.test(Laboratory_4)
##variance test
var.test(Laboratory_1,Laboratory_2)
var.test(Laboratory_3,Laboratory_4)
var.test(Laboratory_2,Laboratory_4)
var.test(Laboratory_1,Laboratory_3)
var.test(Laboratory_1,Laboratory_4)
######One way anova test##############
stackdata=stack(q2)
attach(stackdata)
colnames(stackdata)
Anova_results <- aov(values ~ ind, data = stackdata)
summary(Anova_results)


#*********************************************************************************************************
#*Question 3
#*library(readr)
library(readxl)
library(readr)
library(tidyr)
buyerratio=read.csv(file.choose())
attach(buyerratio)
buyer.long <- pivot_longer(buyerratio, cols=2:5, names_to = "Region")
View(buyer.long)
buyer <- uncount(buyer.long, value)
colnames(buyer)=c("value","region")
attach(buyer)
table(value,region)
chisq.test(table(value,region))

#*********************************************************************************************************
#*Question 4
library(readxl)
q4=read.csv(file.choose())     
attach(q4)
q4$India <- as.vector(q4$India, mode = "any")
stacked_COF<-stack(q4)
q4$Malta <- as.vector(q4$Malta, mode = "any")
stacked_COF<-stack(q4)
q4$Phillippines <- as.vector(q4$Phillippines, mode = "any")
stacked_COF<-stack(q4)
q4$Indonesia <- as.vector(q4$Indonesia, mode = "any")
stacked_COF<-stack(q4)
colnames(stacked_COF)=c("status","country")
attach(stacked_COF)
table(status,country)
chisq.test(table(status,country))


#*************************************************************************************************************
#*Question 5

q5=read.csv(file.choose())
attach(q5)
colnames(q5)
Fantaloons=q5
Fantaloons$Weekdays <- as.vector(Fantaloons$Weekdays, mode = "any")
Fantaloons$Weekend <- as.vector(Fantaloons$Weekend, mode = "any")
stacked_Fantaloons<-stack(Fantaloons)
attach(stacked_Fantaloons)
colnames(stacked_Fantaloons)=c("gender","day")
table1 <- table(gender,day)
table1
table2=table(gender)
table2
table3=table(day)
table3
prop.test(x = c(233,167), n = c(520,280), conf.level = 0.95, alternative = "two.sided")

prop.test(x = c(287,113),n = c(520,280), conf.level = 0.95, alternative = "greater")


#*****************************************************************************************************************



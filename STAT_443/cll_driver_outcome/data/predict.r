## Function for predicting least-squares mean of EXPRESSION_CLUSTER
## Code produced by GUIDE 46.2 on 2/21/26 at 15:54
guide_predict <- function(){
 catvalues <- c("MUTATED")
 if(IGHV_MUTATION_STATUS %in% catvalues){
   catvalues <- c("POST_T")
   if(TREATMENT_STATUS %in% catvalues){
     nodeid <- 4
     predict <- 0.00000000000
   } else {
     nodeid <- 5
     predict <- 3.46800000000
   }
 } else {
   catvalues <- c("POST_T")
   if(TREATMENT_STATUS %in% catvalues){
     nodeid <- 6
     predict <- 0.00000000000
   } else {
     nodeid <- 7
     predict <- 1.85952380952
   }
 }
 return(c(nodeid,predict))
}
## end of function
##
##
## If desired, replace "data_clinical_patient_feb21.txt" with name of file containing new data
## New file must have at least the same variables with same names
## (but not necessarily the same order) as in the training data file
## Missing value code is converted to NA if not already NA
newdata <- read.table("data_clinical_patient_feb21.txt",header=TRUE,colClasses="character")
## node contains terminal node ID of each case
## pred contains predicted value of each case
node <- NULL
pred <- NULL
for(i in 1:nrow(newdata)){
    IGHV_MUTATION_STATUS <- as.character(newdata$IGHV_MUTATION_STATUS[i])
    TREATMENT_STATUS <- as.character(newdata$TREATMENT_STATUS[i])
    tmp <- guide_predict()
    node <- c(node,as.numeric(tmp[1]))
    pred <- c(pred,tmp[2])
}

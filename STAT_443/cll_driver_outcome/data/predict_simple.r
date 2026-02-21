## Function for predicting class posterior probabilities of EXPRESSION_CLUSTER
## Code produced by GUIDE 46.2 on 2/21/26 at 16:49
guide_predict <- function(){
 catvalues <- c("MUTATED")
 if(IGHV_MUTATION_STATUS %in% catvalues){
   nodeid <- 2
   predclass <- "0"
   posterior <- c( 0.41315E+00, 0.98127E-06, 0.77188E-01, 0.71416E-01, 0.86835E-01, 0.92624E-01, 0.18911E+00, 0.30877E-01, 0.23311E-01, 0.15488E-01)
 } else {
   catvalues <- c("POST_T")
   if(TREATMENT_STATUS %in% catvalues){
     nodeid <- 6
     predclass <- "0"
     posterior <- c( 0.99944E+00, 0.98127E-06, 0.44157E-04, 0.57895E-04, 0.48082E-04, 0.52007E-04, 0.10696E-03, 0.19625E-04, 0.16780E-03, 0.58876E-04)
   } else {
     if(!is.na(IGHV_IDENTITY_PERCENTAGE) & IGHV_IDENTITY_PERCENTAGE <= 99.6100000000 ){
       nodeid <- 14
       predclass <- "0"
       posterior <- c( 0.46294E+00, 0.98127E-06, 0.18544E-01, 0.31456E+00, 0.18548E-01, 0.18552E-01, 0.37107E-01, 0.55520E-01, 0.55668E-01, 0.18559E-01)
     } else {
       if(!is.na(FFS_MONTHS) & FFS_MONTHS <= 75.2200000000 ){
         nodeid <- 30
         predclass <- "EC_U1"
         posterior <- c( 0.33856E+00, 0.31348E-02, 0.62696E-02, 0.15674E-01, 0.94044E-02, 0.12539E-01, 0.18809E-01, 0.31348E-02, 0.45455E+00, 0.13793E+00)
       } else {
         nodeid <- 31
         predclass <- "0"
         posterior <- c( 0.51057E+00, 0.98127E-06, 0.42555E-01, 0.57895E-04, 0.48082E-04, 0.52007E-04, 0.63874E-01, 0.19625E-04, 0.23398E+00, 0.14885E+00)
       }
     }
   }
 }
 return(c(nodeid,predclass,posterior))
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
## pred.class contains predicted class
## prob contains predicted posterior probabilities
node <- NULL
pred.class <- NULL
prob <- NULL
for(i in 1:nrow(newdata)){
    IGHV_MUTATION_STATUS <- as.character(newdata$IGHV_MUTATION_STATUS[i])
    IGHV_IDENTITY_PERCENTAGE <- as.numeric(newdata$IGHV_IDENTITY_PERCENTAGE[i])
    TREATMENT_STATUS <- as.character(newdata$TREATMENT_STATUS[i])
    FFS_MONTHS <- as.numeric(newdata$FFS_MONTHS[i])
    tmp <- guide_predict()
    node <- c(node,as.numeric(tmp[1]))
    pred.class <- rbind(pred.class,tmp[2])
    prob <- rbind(prob,as.numeric(tmp[-c(1,2)]))
}

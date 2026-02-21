## Function for predicting class posterior probabilities of vital_status
## Code produced by GUIDE 46.2 on 2/15/26 at 17:21
guide_predict <- function(){
 catvalues <- c("N1b","N3b","N3c","NA","NX")
 catvalues <- c(catvalues,NA)
 if(is.na(ajcc_pathologic_n) | ajcc_pathologic_n %in% catvalues){
   catvalues <- c("NA","TCGA-3C-AAAU_diagnosis","TCGA-A2-A0YC_diagnosis","TCGA-A2-A0YJ_diagnosis","TCGA-A2-A25B_diagnosis","TCGA-A2-A25E_diagnosis","TCGA-A7-A26H_diagnosis","TCGA-A7-A3RF_diagnosis","TCGA-A7-A425_diagnosis","TCGA-AO-A03N_diagnosis","TCGA-AO-A0J9_diagnosis","TCGA-AO-A0JA_diagnosis","TCGA-AO-A126_diagnosis","TCGA-B6-A0RI_diagnosis","TCGA-B6-A402_diagnosis","TCGA-BH-A0BQ_diagnosis","TCGA-BH-A0C3_diagnosis","TCGA-C8-A137_diagnosis","TCGA-D8-A1JA_diagnosis","TCGA-E2-A10A_diagnosis","TCGA-E2-A152_diagnosis","TCGA-E2-A15O_diagnosis","TCGA-E2-A1IE_diagnosis","TCGA-E2-A1LL_diagnosis","TCGA-E9-A243_diagnosis","TCGA-EW-A1P0_diagnosis","TCGA-EW-A1P1_diagnosis","TCGA-EW-A1P7_diagnosis","TCGA-LL-A5YM_diagnosis","TCGA-LQ-A4E4_diagnosis","TCGA-OL-A97C_diagnosis","TCGA-Z7-A8R5_diagnosis")
   catvalues <- c(catvalues,NA)
   if(is.na(tumor_of_origin) | tumor_of_origin %in% catvalues){
     catvalues <- c("Core_Biopsy","NA","Surgical_Resection")
     catvalues <- c(catvalues,NA)
     if(is.na(method_of_diagnosis) | method_of_diagnosis %in% catvalues){
       catvalues <- c("not_reported","primary")
       if(classification_of_tumor %in% catvalues){
         catvalues <- c("4th","5th")
         if(ajcc_staging_system_edition %in% catvalues){
           nodeid <- 32
           predclass <- "Dead"
           posterior <- c( 0.15274E-03, 0.99985E+00)
         } else {
           catvalues <- c("Bone___NOS|Liver|Breast___NOS|Breast___Right_Upper_Inner|Breast___Right_Upper_Outer|Breast___Right_Lower_Inner|Breast___Right_Lower_Outer","Breast___Right_Upper_Inner|Breast___Right_Lower_Inner","NA")
           catvalues <- c(catvalues,NA)
           if(is.na(sites_of_involvement) | sites_of_involvement %in% catvalues){
             catvalues <- c("black_or_african_american","white")
             if(race %in% catvalues){
               nodeid <- 132
               predclass <- "Dead"
               posterior <- c( 0.30233E+00, 0.69767E+00)
             } else {
               nodeid <- 133
               predclass <- "Alive"
               posterior <- c( 0.88889E+00, 0.11111E+00)
             }
           } else {
             nodeid <- 67
             predclass <- "Alive"
             posterior <- c( 0.98214E+00, 0.17857E-01)
           }
         }
       } else {
         catvalues <- c("Combined_small_cell_carcinoma","Malignant_lymphoma___non-Hodgkin___NOS","Malignant_melanoma___NOS","Myelodysplastic_syndrome___NOS")
         if(primary_diagnosis %in% catvalues){
           nodeid <- 34
           predclass <- "Dead"
           posterior <- c( 0.15274E-03, 0.99985E+00)
         } else {
           nodeid <- 35
           predclass <- "Alive"
           posterior <- c( 0.93863E+00, 0.61372E-01)
         }
       }
     } else {
       catvalues <- c("stage_II","stage_IIA","stage_IIIB")
       if(ajcc_pathologic_stage %in% catvalues){
         if(!is.na(age_at_index) & age_at_index <= 65.0000000000 ){
           nodeid <- 36
           predclass <- "Alive"
           posterior <- c( 0.99997E+00, 0.27575E-04)
         } else {
           nodeid <- 37
           predclass <- "Dead"
           posterior <- c( 0.15274E-03, 0.99985E+00)
         }
       } else {
         nodeid <- 19
         predclass <- "Dead"
         posterior <- c( 0.53097E-01, 0.94690E+00)
       }
     }
   } else {
     nodeid <- 5
     predclass <- "Dead"
     posterior <- c( 0.15274E-03, 0.99985E+00)
   }
 } else {
   catvalues <- c("Metastasis___NOS")
   if(metastasis_at_diagnosis %in% catvalues){
     catvalues <- c("yes")
     if(prior_malignancy %in% catvalues){
       nodeid <- 12
       predclass <- "Alive"
       posterior <- c( 0.99997E+00, 0.27575E-04)
     } else {
       nodeid <- 13
       predclass <- "Dead"
       posterior <- c( 0.34483E-01, 0.96552E+00)
     }
   } else {
     catvalues <- c("2nd","3rd","4th")
     if(ajcc_staging_system_edition %in% catvalues){
       if(!is.na(age_at_index) & age_at_index <= 45.5000000000 ){
         nodeid <- 28
         predclass <- "Alive"
         posterior <- c( 0.83333E+00, 0.16667E+00)
       } else {
         nodeid <- 29
         predclass <- "Dead"
         posterior <- c( 0.19355E+00, 0.80645E+00)
       }
     } else {
       catvalues <- c("Breast___Left_Lower_Inner","Breast___Left_Upper_Inner|Breast___Left_Upper_Outer|Breast___Left_Lower_Inner|Breast___Left_Lower_Outer|Breast___NOS","Breast___Left_Upper_Outer|Breast___Left_Lower_Outer","Breast___NOS|Breast___Left_Upper_Outer|Breast___Left_Lower_Outer","Breast___NOS|Breast___Right_Lower_Outer","Breast___Right_Lower_Outer|Breast___NOS","Breast___Right_Upper_Inner|Breast___Right_Lower_Inner","Breast___Right_Upper_Outer|Breast___Right_Lower_Outer")
       if(sites_of_involvement %in% catvalues){
         catvalues <- c("N0___i+__","N0___i-__","N2","N3a")
         if(ajcc_pathologic_n %in% catvalues){
           catvalues <- c("NA")
           catvalues <- c(catvalues,NA)
           if(is.na(ajcc_staging_system_edition) | ajcc_staging_system_edition %in% catvalues){
             nodeid <- 120
             predclass <- "Alive"
             posterior <- c( 0.99997E+00, 0.27575E-04)
           } else {
             nodeid <- 121
             predclass <- "Dead"
             posterior <- c( 0.22951E+00, 0.77049E+00)
           }
         } else {
           catvalues <- c("Complex_Epithelial_Neoplasms")
           if(disease_type %in% catvalues){
             nodeid <- 122
             predclass <- "Dead"
             posterior <- c( 0.15274E-03, 0.99985E+00)
           } else {
             catvalues <- c("not_reported")
             if(race %in% catvalues){
               catvalues <- c("Lobular_carcinoma___NOS")
               if(primary_diagnosis %in% catvalues){
                 nodeid <- 492
                 predclass <- "Dead"
                 posterior <- c( 0.15274E-03, 0.99985E+00)
               } else {
                 nodeid <- 493
                 predclass <- "Alive"
                 posterior <- c( 0.99997E+00, 0.27575E-04)
               }
             } else {
               nodeid <- 247
               predclass <- "Alive"
               posterior <- c( 0.98113E+00, 0.18868E-01)
             }
           }
         }
       } else {
         catvalues <- c("Clear_cell_carcinoma","Large_cell_neuroendocrine_carcinoma","Paget_disease_and_infiltrating_duct_carcinoma_of_breast")
         if(primary_diagnosis %in% catvalues){
           nodeid <- 62
           predclass <- "Dead"
           posterior <- c( 0.15274E-03, 0.99985E+00)
         } else {
           catvalues <- c("Not_Reported")
           if(margin_status %in% catvalues){
             catvalues <- c("5th")
             if(ajcc_staging_system_edition %in% catvalues){
               nodeid <- 252
               predclass <- "Dead"
               posterior <- c( 0.62500E-01, 0.93750E+00)
             } else {
               catvalues <- c("NA","stage_IIIA","stage_IIIC")
               catvalues <- c(catvalues,NA)
               if(is.na(ajcc_pathologic_stage) | ajcc_pathologic_stage %in% catvalues){
                 nodeid <- 506
                 predclass <- "Dead"
                 posterior <- c( 0.44444E+00, 0.55556E+00)
               } else {
                 nodeid <- 507
                 predclass <- "Alive"
                 posterior <- c( 0.99997E+00, 0.27575E-04)
               }
             }
           } else {
             catvalues <- c("Distant_Site")
             if(treatment_anatomic_sites %in% catvalues){
               nodeid <- 254
               predclass <- "Dead"
               posterior <- c( 0.25000E+00, 0.75000E+00)
             } else {
               catvalues <- c("Capecitabine","Denosumab","Etoposide","Fulvestrant","Ifosfamide","Mesna","Mitomycin","Pamidronic_Acid","Pegylated_Liposomal_Doxorubicin_Hydrochloride","Prednisone","Rituximab","Vincristine")
               if(therapeutic_agents %in% catvalues){
                 if(!is.na(age_at_index) & !is.na(age_at_diagnosis) &  -0.277189507896E-02  * age_at_diagnosis + age_at_index <= -1.23254824168 ){
                   nodeid <- 1020
                   predclass <- "Alive"
                   posterior <- c( 0.87500E+00, 0.12500E+00)
                 } else {
                   nodeid <- 1021
                   predclass <- "Dead"
                   posterior <- c( 0.11111E+00, 0.88889E+00)
                 }
               } else {
                 catvalues <- c("Biopsy","Cytology","Excisional_Biopsy","Fine_Needle_Aspiration","Incisional_Biopsy")
                 if(method_of_diagnosis %in% catvalues){
                   catvalues <- c("N1","N1mi","N3a")
                   if(ajcc_pathologic_n %in% catvalues){
                     catvalues <- c("Biopsy","Cytology")
                     if(method_of_diagnosis %in% catvalues){
                       nodeid <- 4088
                       predclass <- "Dead"
                       posterior <- c( 0.15274E-03, 0.99985E+00)
                     } else {
                       catvalues <- c("6th","NA")
                       catvalues <- c(catvalues,NA)
                       if(is.na(ajcc_staging_system_edition) | ajcc_staging_system_edition %in% catvalues){
                         if(!is.na(age_at_index) & age_at_index <= 43.0000000000 ){
                           if(!is.na(age_at_index) & age_at_index <= 35.5000000000 ){
                             nodeid <- 32712
                             predclass <- "Dead"
                             posterior <- c( 0.15274E-03, 0.99985E+00)
                           } else {
                             nodeid <- 32713
                             predclass <- "Alive"
                             posterior <- c( 0.99997E+00, 0.27575E-04)
                           }
                         } else {
                           nodeid <- 16357
                           predclass <- "Dead"
                           posterior <- c( 0.15274E-03, 0.99985E+00)
                         }
                       } else {
                         nodeid <- 8179
                         predclass <- "Alive"
                         posterior <- c( 0.99997E+00, 0.27575E-04)
                       }
                     }
                   } else {
                     if(!is.na(age_at_diagnosis) & age_at_diagnosis <= 16645.5000000 ){
                       if(!is.na(age_at_index) & age_at_index <= 39.5000000000 ){
                         nodeid <- 8180
                         predclass <- "Alive"
                         posterior <- c( 0.99997E+00, 0.27575E-04)
                       } else {
                         catvalues <- c("Infiltrating_duct_carcinoma___NOS")
                         if(primary_diagnosis %in% catvalues){
                           if(!is.na(age_at_index) & age_at_index <= 43.5000000000 ){
                             catvalues <- c("Left")
                             if(laterality %in% catvalues){
                               nodeid <- 65448
                               predclass <- "Dead"
                               posterior <- c( 0.15274E-03, 0.99985E+00)
                             } else {
                               nodeid <- 65449
                               predclass <- "Alive"
                               posterior <- c( 0.99997E+00, 0.27575E-04)
                             }
                           } else {
                             nodeid <- 32725
                             predclass <- "Dead"
                             posterior <- c( 0.15274E-03, 0.99985E+00)
                           }
                         } else {
                           nodeid <- 16363
                           predclass <- "Alive"
                           posterior <- c( 0.99997E+00, 0.27575E-04)
                         }
                       }
                     } else {
                       nodeid <- 4091
                       predclass <- "Alive"
                       posterior <- c( 0.95957E+00, 0.40431E-01)
                     }
                   }
                 } else {
                   catvalues <- c("T1b","T4b")
                   if(ajcc_pathologic_t %in% catvalues){
                     catvalues <- c("Lobular_carcinoma___NOS","Mucinous_adenocarcinoma")
                     if(primary_diagnosis %in% catvalues){
                       catvalues <- c("stage_IIIB","stage_IIIC")
                       if(ajcc_pathologic_stage %in% catvalues){
                         nodeid <- 8184
                         predclass <- "Dead"
                         posterior <- c( 0.15274E-03, 0.99985E+00)
                       } else {
                         nodeid <- 8185
                         predclass <- "Alive"
                         posterior <- c( 0.99997E+00, 0.27575E-04)
                       }
                     } else {
                       nodeid <- 4093
                       predclass <- "Alive"
                       posterior <- c( 0.96250E+00, 0.37500E-01)
                     }
                   } else {
                     catvalues <- c("C50.8")
                     if(icd_10_code %in% catvalues){
                       nodeid <- 4094
                       predclass <- "Alive"
                       posterior <- c( 0.99997E+00, 0.27575E-04)
                     } else {
                       catvalues <- c("C50.2","C50.5")
                       if(icd_10_code %in% catvalues){
                         nodeid <- 8190
                         predclass <- "Alive"
                         posterior <- c( 0.99997E+00, 0.27575E-04)
                       } else {
                         catvalues <- c("C50.9")
                         if(icd_10_code %in% catvalues){
                           if(!is.na(age_at_index) & age_at_index <= 26.5000000000 ){
                             nodeid <- 32764
                             predclass <- "Dead"
                             posterior <- c( 0.15274E-03, 0.99985E+00)
                           } else {
                             nodeid <- 32765
                             predclass <- "Alive"
                             posterior <- c( 0.96296E+00, 0.37037E-01)
                           }
                         } else {
                           nodeid <- 16383
                           predclass <- "Alive"
                           posterior <- c( 0.87500E+00, 0.12500E+00)
                         }
                       }
                     }
                   }
                 }
               }
             }
           }
         }
       }
     }
   }
 }
 return(c(nodeid,predclass,posterior))
}
## end of function
##
##
## If desired, replace "my_dataset_feb_14.txt" with name of file containing new data
## New file must have at least the same variables with same names
## (but not necessarily the same order) as in the training data file
## Missing value code is converted to NA if not already NA
newdata <- read.table("my_dataset_feb_14.txt",header=TRUE,colClasses="character")
## node contains terminal node ID of each case
## pred.class contains predicted class
## prob contains predicted posterior probabilities
node <- NULL
pred.class <- NULL
prob <- NULL
for(i in 1:nrow(newdata)){
    disease_type <- as.character(newdata$disease_type[i])
    age_at_index <- as.numeric(newdata$age_at_index[i])
    race <- as.character(newdata$race[i])
    age_at_diagnosis <- as.numeric(newdata$age_at_diagnosis[i])
    ajcc_pathologic_n <- as.character(newdata$ajcc_pathologic_n[i])
    ajcc_pathologic_stage <- as.character(newdata$ajcc_pathologic_stage[i])
    ajcc_pathologic_t <- as.character(newdata$ajcc_pathologic_t[i])
    ajcc_staging_system_edition <- as.character(newdata$ajcc_staging_system_edition[i])
    classification_of_tumor <- as.character(newdata$classification_of_tumor[i])
    icd_10_code <- as.character(newdata$icd_10_code[i])
    laterality <- as.character(newdata$laterality[i])
    metastasis_at_diagnosis <- as.character(newdata$metastasis_at_diagnosis[i])
    method_of_diagnosis <- as.character(newdata$method_of_diagnosis[i])
    primary_diagnosis <- as.character(newdata$primary_diagnosis[i])
    prior_malignancy <- as.character(newdata$prior_malignancy[i])
    sites_of_involvement <- as.character(newdata$sites_of_involvement[i])
    tumor_of_origin <- as.character(newdata$tumor_of_origin[i])
    margin_status <- as.character(newdata$margin_status[i])
    therapeutic_agents <- as.character(newdata$therapeutic_agents[i])
    treatment_anatomic_sites <- as.character(newdata$treatment_anatomic_sites[i])
    tmp <- guide_predict()
    node <- c(node,as.numeric(tmp[1]))
    pred.class <- rbind(pred.class,tmp[2])
    prob <- rbind(prob,as.numeric(tmp[-c(1,2)]))
}

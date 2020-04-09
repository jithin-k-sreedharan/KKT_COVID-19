
# COVID-19 dataset of the Indian state - Kerala

## Introduction
In India, COVID-19 was first reported in the state of Kerala on Jan 31, 2020. Since then, the Government of Kerala has taken stringent measures and issued multiple regulations for the containment, management and control of COVID-19. To this end, the Directorate of Health Services (DHS), Kerala, has been publishing a daily bulletin starting Jan 31, 2020 in both English and Malayalam.

## Data source
The daily bulletin published by DHS in English is the primary source for this dataset. Though the bulletin is relatively rich in information, it is not in a form that's ready for data analysis. We collected and curated state, district and patient-level data from these bulletins to create this dataset. We have created an interactive dashboard to visually summarize this dataset. The dashboard can be accessed at https://covid19kerala.github.io/.

**For details on the inconsistencies in the data reported in the daily bulletin refer to the appendix file in this folder. We will soon post a detailed report.**

## Data files
* `kerala_state_summary.csv`: State level COVID-19 data from the daily bulletin starting from Jan 31, 2020.
* `kerala_district_summary.csv`: District level COVID-19 data from the daily bulletin starting from Jan 31, 2020.
* `kerala_positive_case_summary.csv`: Patient level COVID-19 data from the daily bulletin starting from Jan 31, 2020.

## Supplementary files
* `district_code.csv`: Numeric code for the 14 districts in Kerala.
* `appendix.pdf`: Details of inconsistencies in the daily bulletin published by the DHS.

## Attributes

The following fields are available in the state summary file:

* `Date`: date in dd-mm-yyyy
* `State_Name`: Kerala
* `State_Code`: Numeric State code (32 for Kerala). **Source**: The 2011 Census data collected by the [Office of the Registrar Geneal & Census Commissioner](https://censusindia.gov.in/2011census/Listofvillagesandtowns.aspx), India
* `Confirmed`: Total confirmed cases of COVID-19 as of that date
* `Active`: Total active cases of COVID-19 on that date
* `Recovered`: Total recovered cases of COVID-19 as of that date
* `Deceased`: Total COVID-19 deaths as of that date
* `Under_Observation`: Total under observation as of that date
* `Home_Isolation`: Toal under home isolation as of that date
* `Symptomatic_Hospitalized`: Total symptomatic hospitalized as of that date
* `Samples_Sent_For_Testing`: Total samples sent for testing as of that date
* `Samples_Tested_Negative`: Total samples tested negative as of that date

The attributes `Under_Observation`, `Home_Isolation`, and `Symptomatic_Hospitalized` have specific meaning in this dataset. DHS released two detailed reports on these classifications, and they are made localy available in this repo, see [report-1](DHS_test_treating_flowchart.pdf) and [report-2](DHS_guidelines_testing_quarantine_hospitalization.pdf) (accessed on April 9, 2020, from DHS [website](http://dhs.kerala.gov.in/%e0%b4%9c%e0%b4%be%e0%b4%97%e0%b5%8d%e0%b4%b0%e0%b4%a4-%e0%b4%a8%e0%b4%bf%e0%b4%b0%e0%b5%8d%e2%80%8d%e0%b4%a6%e0%b5%87%e0%b4%b6%e0%b4%99%e0%b5%8d%e0%b4%99%e0%b4%b3%e0%b5%8d%e2%80%8d/)). In particular, `Under_Observation = Home_Isolation + Symptomatic_Hospitalized`. **We will be including detailed information on this in the upcoming report.**

The attributes `Samples_Sent_For_Testing` and `Samples_Tested_Negative` are unavailable at the district level. The district level summary file has the following additional fields:

* `District`: Name of the district in Kerala
* `District_Code`: Numeric district code from the 2011 Census data collected by the [Office of the Registrar Geneal & Census Commissioner](https://censusindia.gov.in/2011census/Listofvillagesandtowns.aspx), India

The positive case summary file has the following fields:
* `Patient_ID`: a unique ID that **we assigned** to each COVID-19 case
* `District`: District to which the patient belongs
* `District_Code`: District code for the corresponding district
* `Positive_Date`: Date on which a person was declared COVID-19 positive
* `Negative_Date`: Date on which a COVID-19 infected person was declared negative
* `Death_Date`: Date on which a COVID-19 infected person died

If both `Negative_Date` and `Death_Date` are missing for a patient then that means the person is still under treatment. If either of them is present then that means the other is not applicable (NA).

## Citation
If you find this dataset useful please considering citing our report (will be posted soon).

Varun Vasudevan, Jithin K. Sreedharan, Varsha Sankar, and Siddarth A. Vasudevan, "KKT COVID-19 Dataset", 2020.

```latex
@report{KKT_COVID-19,
author = {Vasudevan, Varun and Sreedharan, Jithin K. and Sankar, Varsha and Vasudevan, Siddarth A.},
title = {{KKT COVID-19} {D}ataset},
year = {2020}}
```

## Contact
For further information on the dataset, contact **Varun Vasudevan** (devan at stanford dot edu) and **Jithin K. Sreedharan** (jithinks at purdue dot edu).

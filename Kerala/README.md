# COVID-19 dataset of the Indian state - Kerala

In India, COVID-19 was first identified in Kerala at the end of January 2020. Since then, Kerala has introduced extensive measures to contain the disease. We hope that the information of people under observation, home isolation (before testing positive), and symptomatic hospitalized cases will captutre the effect of contact tracing and containiment to reduce the spreading.

For further information on the datasets, contact Varun Vasudevan (devan at stanford dot edu) and Jithin K. Sreedharan (jithinks at purdue dot edu).

## Data files
* `kerala_state_summary.csv`: State level summary of the COVID-19 cases for dates starting from `2020-01-31`.
* `kerala_district_summary.csv`: District level summary of the COVID-19 cases for dates starting from `2020-01-31`.
* `district_code.csv`: Numeric code of the districts.

## Data source
We formed the datasets solely from the official information published by the Directorate of Health Services (D.H.S.), Kerala, and from the discussion with the government officials.

We faced mainly the following hurdles to form the district level information:
* For some dates, the bulletins released by the D.H.S. contain only the information of the district where the patient is finally hospitalized. This is not same as the residing district of the patient in many cases. To track community transmission, we have decided to find the residing district of the patient that is inferred from the text in the bulletins and use it in our district level summary.
* Everyday, we manually check the consistency of the data released by D.H.S. and if there are any discrepancies, we correct it in our data and notify the officials.
* More details on how we cleaned the data are summarized in a [report]().

## Attributes

The following are available in the state summary file:

* `Date`: date in Indian format
* `NSC`: Numeric state code (32 for Kerala) collected from the [Office of the Registrar Geneal & Census Commissioner](https://censusindia.gov.in/Census_Data_2001/PLCN/plcn.html), India
* `Confirmed`: Total confirmed as of that date
* `Active`: Total active as of that date
* `Recovered`: Total recovered as of that date
* `Deaths`: Total number of deaths as of that date
* `UO`: Total Under observation as of that date
* `HI`: Toal under Home isolation as of that date
* `SH`: Total Symptomatic hospitalized as of that date
* `SSFT`: Total Samples sent for testing as of that date
* `STN`: Total Samples tested negative as of that date

The attributes `SSFT` and `STN` are not available in the district summary file. It has the following additional fields:

* `NDC`: Numeric district code collected from the [Office of the Registrar Geneal & Census Commissioner](https://censusindia.gov.in/Census_Data_2001/PLCN/plcn.html), India
* `District`: District name



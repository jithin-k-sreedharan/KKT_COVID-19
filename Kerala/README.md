# COVID-19 dataset of the Indian state - Kerala

In India, COVID-19 was first identified in Kerala at the end of January 2020. Since then, Kerala has introduced extensive measures to contain the disease. These datasets capture that.

## Data files
* `kerala_state_summary.csv`: State level summary of the COVID-19 cases for dates starting from `2020-01-31`.
* `kerala_district_summary.csv`: District level summary of the COVID-19 cases for dates starting from `2020-01-31`.
* `district_code.csv`: Numeric code for the districts.

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

The district summary file does not have the attributes `SSFT` and `STN` in the state level summary. It has the following additional fields:

* `NDC`: Numeric district code collected from the [Office of the Registrar Geneal & Census Commissioner](https://censusindia.gov.in/Census_Data_2001/PLCN/plcn.html), India
* `District`: District name



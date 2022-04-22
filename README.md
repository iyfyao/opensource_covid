[![SWH](https://archive.softwareheritage.org/badge/swh:1:snp:f891106aad2f12f134bff7d230dc1a06cf62290b/)](https://archive.softwareheritage.org/swh:1:snp:f891106aad2f12f134bff7d230dc1a06cf62290b;origin=https://github.com/iyfyao/opensource_covid)

# opensource_covid

Build a COVID-19 dashboard.
This dashboard provides statistics and relevant informations about the covid cases across the world 

# Data Source 
Please find here the link to the repository : https://github.com/owid/covid-19-data <br/>
Please find here the source of the data : <br/> 
https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv <br/>
Data on COVID-19 (coronavirus) cases, deaths, • All countries • Updated daily by the World in Data <br/>


## SETUP INSTRUCTIONS

1. Clone the repository <br/> 
$ git clone https://github.com/iyfyao/opensource_covid.git <br/>

2. Create your virtual environmennt, please run the following commands <br/>
``` python -m venv your-virtual-env-name ```
then activate your virtual env ``` source your-virtual-env-name/bin/activate ```

3. Install requests package which automatically updates your virtual environment whenever a new packages is added <br/>
If you dont do it, every time you add a new package you have to update it yourself <br/>
``` pip install requests ``` <br/>

4. In order to use our application, please run this command <br/>
``` python -m pip install -r requirements.txt ``` <br/>

# Streamlit Cloud 
Please find below the link to the streamlit cloud <br/>
https://share.streamlit.io/iyfyao/opensource_covid/main/streamlit_app.py <br/>

# Run the dashboard Locally
Please find below the instructions to run the dashboard locally : <br/>
1. Please move to the directory of your project and type the following command, 
Note : The project is always at the root of your C:\
Example : cd C:\Users\[username]\git\opensource_covid>streamlit run streamlit_app.py


**STAY TUNE**

# Analysis of Taxi GPS Data in Porto  

This project explores travel patterns of taxis in Porto, Portugal, by analyzing their GPS data. The findings can help understand urban mobility and taxi route behaviors, providing insights for urban planning and transportation efficiency.

## Description  

The project uses a dataset containing one year of taxi GPS trajectories in Porto. The goal is to identify frequent routes of taxis and explore the change in taxis travel patterns across different scenarios (for instance, on weekdays and weekends). It involves exploratory data analysis, data preprocessing, map-matching, Natural Language Processing techniques, and route visualization using Python, geospatial and NLP libraries.

### Dataset
This dataset describes a complete year (from 01/07/2013 to 30/06/2014) of the trajectories for all the 442 taxis running in the city of Porto, in Portugal 
(i.e. one CSV file named "train.csv"). The data is available on [Kaggle datasets](https://www.kaggle.com/datasets/crailtap/taxi-trajectory/data). 

## Getting Started  

### Dependencies  

- Python 3.8+  
- Jupyter Notebook  
- Libraries
  - pandas
  - numpy
  - folium
  - matplotlib  

### Installing  

1. Clone this repository to your local machine:  
   ```bash  
   git clone https://github.com/chengzwk/Porto-taxi.git  
   ```  
2. Download the dataset [here](https://www.kaggle.com/datasets/crailtap/taxi-trajectory/data) and place `train.csv` in the project directory.  

### Executing Program  

1. Open the Jupyter Notebook:  
   ```bash  
   jupyter-notebook  
   ```  
2. Load the `exploratory_analysis.ipynb` file in Jupyter.  
3. To view interactive maps, open the notebook using [nbviewer](https://nbviewer.org):  
   - Copy the GitHub link to the notebook and paste it into the nbviewer tool.  

## Help  

For common issues, ensure that:  
- Jupyter Notebook is installed and running.  
- Required Python libraries are installed.  

For installation:  
```bash  
pip install pandas numpy folium matplotlib  
```  

## Authors  

**chengzwk**  
GitHub: [chengzwk](https://github.com/chengzwk)  

## Version History  

* 0.1  
    * Initial release  

## License  

This project is licensed under the MIT License - see the LICENSE.md file for details.  

## Acknowledgments  

- Dataset: [Kaggle](https://www.kaggle.com/datasets/crailtap/taxi-trajectory/data)  

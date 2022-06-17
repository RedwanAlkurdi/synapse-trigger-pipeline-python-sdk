# synapse-trigger-pipeline-python-sdk



# Creating the troubleshooting pipeline in azure synapse analytics

1- open up the synapse analytics workspace & switch to the integrate tab & press on the plus sign to add a new pipeline

![1](/screenshots/1.png)

2- change the name of the pipeline to "Google Troubleshooting Pipeline" on the right hand side and press on the code symbol

![2](/screenshots/2.png)
![3](/screenshots/3.png)


3- copy the json file (i.e., Google_Troubleshooting_Pipeline.json) into the code segment of the pipeline and press okay and then publish the code change
![4](/screenshots/4.png)


we now have a small pipeline that has negligible costs to test out the Synapse permissions.




# Testing out the Synapse permissions

1- clone the repo and create a new virtual env and activate the virtual env
```
git clone <REPO_URL.git>
virtualenv synapse_test --python=python3
source synapse_test/bin/activate
```

2- install the following packages using pip in the following order (P.S.: using the requirements.txt for installing the packages will lead to errors, just install them one-by-one in the following order)
```
pip install azure-synapse
pip install azure-identity
pip install azure-synapse-artifacts
```

3- edit the script and add the required information

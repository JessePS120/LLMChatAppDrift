## Overview 

This repo contains the code/scripts used for measuring LLMChat drift each week. The three models that are currently measured are: ChatGPT, Gemini, and Claude. 

## Tools 

This repo makes use of the eval plus library. All of the python libraries used can be found in requirements.txt file included in this repo. It is recommended to create a virtual environment but this is not required. 

## Results 

- The pilot results can be review under the Pilot_Results folder. 
- The prompt used from the pilot is as follows: Complete the following Python function. Do not ask any questions or generate any extra text. Return the complete function in a single Python code block. Do not write any comments.
- The results for each week are stored in their own folder i.e. Week1_Results/. 


## Running 
- After installing the necessary tools, the following scripts may be run. 
- generate_prompts.py which will generate the prompts used for each model under the prompts/ folder. 
- run_evalplus.sh(see file for details). Will use eval plus to run the test cases for a single week and will write the results to a .csv in that week's folder. 
- analysis.py which will scan each results folder and produce some graphs of the results under the analysis_results/ folder. 


![10 Academy](https://static.wixstatic.com/media/081e5b_5553803fdeec4cbb817ed4e85e1899b2~mv2.png/v1/fill/w_246,h_106,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/10%20Academy%20FA-02%20-%20transparent%20background%20-%20cropped.png)

# Prompt Engineering: In-context learning with GPT-3 and other Large Language Models

## Project Overview
A client has a system that collects news artifacts from web pages, tweets, facebook posts, etc. The client is interested in scoring a given new artifact against a topic. The client has hired experts to score a few of these news items in the range from 0 to 10; a score of 0 means the news item is totally NOT relevant while a score of 10 means the news item is very relevant. The range of results between 0 and 10 signifies the  degree of relevance of the news item to the topic. <br><br>
The client wants to explore how useful existing LLMs such as GPT-3 are for this task. You are hired as a consultant to explore the efficiency of GPT3-like LLMs to this task. If your recommendation is positive, you must demonstrate that your strategies to design prompts are reproducible and produce a consistent result. <br><br>
You should also set up an MLOps pipeline that helps automate the task of using different LLMs and different topics. Your pipeline should also allow future improvements in the prompt design to be integrated without breaking the system. A centralized log system should be incorporated into your pipeline to help monitor outputs, cost, performance, and other relevant artifacts.

***
## Data
Our data is versioned using DVC
> news - For now we have only one virsion of news data
> - **news-v0** : original version of the data
> - **news-v1** : first stage cleaned news data
> - **test-news-v1** : enhanced test data
> - **test-news-v2** : 2nd enhanced test data
> - **test_news-v0** : track test news data
> - **train-news-v1** :  enhanced train data
> - **train-news-v2** :  2nd enhanced train data
> - **train_news-v0** :  track train news data


## Project Structure
The directories for this project is self-explanatory. You can find the **api** (for making predictions) setup in `api` folder. The versioned data in `data` folder. `notebook` directory contains the notebooks for this project. You can find helper classes in `scripts` directory.

This project uses `co:here` api for making predictions. Thus you need to have your own **`api_key`**.

> create 
<!-- include how to setup apikey -->

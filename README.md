# About BadgerVisualization

This project is a submission for [Create Visualization Of Badger Boost Data](https://gitcoin.co/issue/Badger-Finance/gitcoin/27/100026488)

# Summary 

We built a visualisation/animation of the badger boost data that allows us to see the changes in the multipliers of users in Heroku web app over time and code to display aggregates of native/non native balances over time as well as individual addresses.

Apart from that the data processing script of offline and online data is included. Besides, we put the data and code on Kaggle which makes running the code as easy as pressing the button.

## The parts 

The address multiplier data is hosted on Heroku at https://dashbadger.herokuapp.com/

![Web App](Gif.gif)

The aggregate analysis of addresses is at https://www.kaggle.com/pavfedotov/badger-address-summary/

The analysis of individual addresses is at https://www.kaggle.com/pavfedotov/visualization-badgers/
## Installation
`pip install -r requirements.txt`

To run the project:

`py main.py`

## Additional Files and Work

Apart from the code in this github repository here is the code for data scrappig and preprocessing:

[The processing of boosts.zip](https://www.kaggle.com/pavfedotov/badger-data/)

[Scrapping of Latest Online date](https://www.kaggle.com/pavfedotov/badger-data?scriptVersionId=75918446)

[Full processed dataset](https://www.kaggle.com/pavfedotov/badgerdataset)

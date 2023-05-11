# README

### Setup hints:

`export OPENAI_API_KEY=<OPEN_AI_API_KEY>`

`pip install -r requirements.txt`

`chatgpt install`


## Overview

This Python script allows you to interact with a wrapper for OpenAI's ChatGPT model. The unique feature of this script is that it uses ChatGPT to "copyedit" its own responses before showing them to the user. This is done by ask ng ChatGPT to generate a response, then sending that response back to ChatGPT with a prompt asking it to copyedit the text.

Unless verbose mode is enabled for diagnostics, the user never sees the intermediate bounce. Just their own prompt, and the final (copyedited) response from chatGPT.

## Usage

Run `correction.py` and interact via CLI


## Example (normal mode)
```
==================================================
[User]: Please tell me about statistical moments, and give physical examples for the first through fourth
--> (sent)

==================================================
[ChatGPT]: Statistical moments are a useful tool for describing the properties of probability distributions. They offer valuable information regarding the shape, central tendency, spread, and other characteristics of a dataset. These moments are computed using mathematical formulas, and each moment provides insights into different aspects of the distribution.

The first moment is known as the mean or expected value. It represents the center of the distribution and provides the average value of the dataset. For instance, if we consider a dataset of individual heights in a population, the first moment would indicate the average height of the population.

The second moment is referred to as variance. It quantifies the spread or dispersion of the distribution. Variance measures how much the values in the dataset deviate from the mean. To illustrate, let's consider a dataset of object weights produced by a manufacturing process. The second moment, in this case, would capture the variability in the weights of the objects, indicating how much they differ from the average weight.

The square root of the variance is called the standard deviation. It is also a measure of the distribution's spread, but it is expressed in the same units as the original data. In our weight example, the standard deviation would provide a measure of the typical deviation from the average weight in the manufacturing process.

The third moment is termed skewness. It describes the asymmetry of the distribution. Positive skewness implies that the distribution's tail extends more towards the right, while negative skewness indicates a longer tail towards the left. A physical example of skewness could be the distribution of income in a population. If there is positive skewness, it implies that there are more people with low income and a few individuals with extremely high income.

The fourth moment is known as kurtosis. It measures the shape of the distribution's tails. A high kurtosis value suggests heavier tails and potentially more extreme outliers, while a low kurtosis value indicates lighter tails and a less peaked distribution. As an example, kurtosis can be employed to describe the distribution of stock market returns. A high kurtosis would indicate a higher likelihood of extreme market movements.

These four statistical moments, namely the mean, variance, skewness, and kurtosis, are commonly utilized to characterize distributions. They offer valuable insights into the properties of datasets, enabling us to comprehend the shape, spread, skewness, and tail behavior of probability distributions across various physical examples.

==================================================
[User]: 
```

## Example (diagnostic mode on showing intermediate response)
```
Welcome! Type 'exit' as your [User] prompt to quit
Diagnostics mode (shows intermediate replies)? [default off] (y/n): y

==================================================
[User]: Please tell me about statistical moments, and give physical examples for the first through fourth
--> (sent)

EXTRA DIAGNOSTICS DATA - chatGPT original response:
Statistical moments are a way to describe the properties of a probability distribution. They provide information about the shape, central tendency, spread, and other characteristics of a dataset. The moments are calculated using mathematical formulas, and different moments capture different aspects of the distribution.

The first moment is the mean or the expected value. It represents the center of the distribution and indicates the average value of the dataset. For example, if you have a dataset of the heights of individuals in a population, the first moment would be the average height of the population.

The second moment is the variance. It measures the spread or dispersion of the distribution. Variance determines how much the values in the dataset deviate from the mean. In a physical example, consider a dataset of the weights of objects produced by a manufacturing process. The second moment would quantify the variability in the weights of the objects, indicating how much they differ from the average weight.

The square root of the variance is called the standard deviation. It is also a measure of the spread of the distribution, but it is expressed in the same units as the original data. In our weight example, the standard deviation would provide a measure of the typical deviation from the average weight in the manufacturing process.

The third moment is called the skewness. It describes the asymmetry of the distribution. Positive skewness indicates that the tail of the distribution extends more to the right, while negative skewness indicates a longer tail to the left. A physical example can be the distribution of income in a population. If there is a positive skewness, it means that there are more people with low income and a few individuals with extremely high income.

The fourth moment is called the kurtosis. It measures the shape of the distribution's tails. A high kurtosis value indicates heavier tails and potentially more extreme outliers, while a low kurtosis value indicates lighter tails and a less peaked distribution. For instance, the kurtosis could be used to describe the distribution of stock market returns. A high kurtosis would suggest that there is a higher likelihood of extreme market movements.

These are the first four statistical moments commonly used to characterize distributions. They provide valuable insights into the properties of datasets and help us understand the shape, spread, skewness, and tail behavior of probability distributions in various physical examples.

==================================================
[ChatGPT]: Statistical moments are a useful tool for describing the properties of probability distributions. They offer valuable information regarding the shape, central tendency, spread, and other characteristics of a dataset. These moments are computed using mathematical formulas, and each moment provides insights into different aspects of the distribution.

The first moment is known as the mean or expected value. It represents the center of the distribution and provides the average value of the dataset. For instance, if we consider a dataset of individual heights in a population, the first moment would indicate the average height of the population.

The second moment is referred to as variance. It quantifies the spread or dispersion of the distribution. Variance measures how much the values in the dataset deviate from the mean. To illustrate, let's consider a dataset of object weights produced by a manufacturing process. The second moment, in this case, would capture the variability in the weights of the objects, indicating how much they differ from the average weight.

The square root of the variance is called the standard deviation. It is also a measure of the distribution's spread, but it is expressed in the same units as the original data. In our weight example, the standard deviation would provide a measure of the typical deviation from the average weight in the manufacturing process.

The third moment is termed skewness. It describes the asymmetry of the distribution. Positive skewness implies that the distribution's tail extends more towards the right, while negative skewness indicates a longer tail towards the left. A physical example of skewness could be the distribution of income in a population. If there is positive skewness, it implies that there are more people with low income and a few individuals with extremely high income.

The fourth moment is known as kurtosis. It measures the shape of the distribution's tails. A high kurtosis value suggests heavier tails and potentially more extreme outliers, while a low kurtosis value indicates lighter tails and a less peaked distribution. As an example, kurtosis can be employed to describe the distribution of stock market returns. A high kurtosis would indicate a higher likelihood of extreme market movements.

These four statistical moments, namely the mean, variance, skewness, and kurtosis, are commonly utilized to characterize distributions. They offer valuable insights into the properties of datasets, enabling us to comprehend the shape, spread, skewness, and tail behavior of probability distributions across various physical examples.

==================================================
[User]: 
```
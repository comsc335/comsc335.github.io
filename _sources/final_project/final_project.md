(final_proj)=

# Final Project

# Learning objectives

- Apply the machine learning principles you have learned in an area of your choice
- Follow the machine learning process from start to finish
- Gain experience communicating scientific results:
    - Visually and in writing through a [Myst article](https://myst-parser.readthedocs.io/en/latest/)
    - Verbally through a brief teaching presentation to the class

# Logistics and assessment breakdown

- Final project groups can be one to three students.
- Students are expected to contribute equally to the project, and the amount of work will scale with the size of the groups.

| Component | Points | Due Date |
| --- | --- | --- |
| [Dataset Proposal](final_proposal) | 3 | 3/30 |
| [Checkpoint](checkpoint) | 5 | 4/27 |
| Presentation and peer feedback | 5 | 4/30, 5/5 |
| [Final report](final_template) | 12 | 5/11 **noon** |


# Final report rubric

| Component | Points |
| --- | --- |
| Source code and Myst article file | 1 |
| Machine learning question | 1 |
| Data: datasheet | 2 | 
| Features: cleaning/engineering | 1 |
| Models: baseline, exploratory, and model of choice | 3.5 |
| Evaluation | 1 |
| Model card(s)  | 2 |
| Reflection | 0.5 | 
| Total | 12 |


:::{admonition} Evaluation Guidelines
:class: note

Your final report will be evaluated on both completion and quality. Specifically, I'll be looking for:

- A completed project that addresses each section of the final report template
- Clear visual and written presentation of your data, modeling choices, and results
- Thoughtful engagement with the datasheet and model card frameworks

This is your opportunity to showcase your understanding of the machine learning process and communicate your findings. I'm looking for thoughtful consideration of your approach rather than the highest possible model performance. If you have any questions, please do reach out!

:::

# Final project approach

All projects will develop a narrative of the machine learning process from start to finish: Data $\to$ Features $\to$ Model $\to$ Train $\to$ Evaluate. Specific deliverables for certain steps are described below.

## Data

Your proposal and report will include a variation of a **datasheet** for your dataset as proposed by [Gebru et al. (2021)](https://cacm.acm.org/research/datasheets-for-datasets/) like we saw in HW 2, which you will initially draft in the [dataset proposal](final_proposal).

## Features

You will need to split your data into training and test sets, and also modify features into a format that can be used by the model. That means applying one-hot encoding to categorical features and standard scaling numerical features, as well as any other necessary preprocessing and cleaning.

## Model and training

You will build and evaluate multiple models as part of your project. Specifically, you will fit and evaluate the following:
- **Baseline model**: logistic regression (for classification) or linear regression (for regression) with L2 regularization
- **Exploratory model(s)**: one new model **per group member** in [sckit-learn](https://scikit-learn.org/stable/index.html) that we did not cover in class. You will not need to understand every single detail of the model, but you will need to be able to use the API as well as describe the model's relevant hyperparameters.
- **Model of your choice**: one model of your choice that you think may perform well on your dataset. This could include random forests, gradient boosting, neural networks, etc.

## Evaluate

As part of your evaluation, you will write a variation of a **model card** by [Mitchell et al. (2018)](https://arxiv.org/pdf/1810.03993) that documents your model's characteristics, performance, and intended use. One model card will be created **per group member.** You may select any of the models you built for your project to write the model cards for -- not necessarily the best performing models! We will cover the model card reading after Spring Break.

## Report format

The final report will be submitted in the form of a [Myst website](https://myst-parser.readthedocs.io/en/latest/), which is the same engine that formats the course website. Modern scientific communication is moving beyond static papers towards the "executable book" format, which combines text, math, visualizations, and executable code in a single document. Your report can even be hosted online and showcased as part of your project portfolio. HW 3 will give you initial experience with the Myst website format, which you can then build on for your final project.

# Example resources

## Dataset repositories

The following repositories are suggestions for finding datasets, feel free to use other repositories as well!

- [folktables](https://github.com/socialfoundations/folktables): provides access to datasets derived from the US Census. We have used two of the datasets in class assignments but feel free to explore other datasets in the library.

- [TidyTuesday](https://github.com/rfordatascience/tidytuesday/blob/main/README.md): collection of real-world datasets intended for learning data science and visualization

- [ICPSR](https://www.icpsr.umich.edu/web/about/cms/5016): Inter-university Consortium for Political and Social Research, a repository of social science data covering:
    - health
    - population health
    - education
    - aging
    - criminal justice
    - substance abuse
    - arts and culture

- [Opportunity Insights](https://opportunityinsights.org/data/): a research organization that studies the impact of social programs on economic mobility, and also maintains a public data repository

- [Our World in Data](https://ourworldindata.org/): cleaned datasets and visualizations on global development, health, energy, environment, and inequality

- [Harvard Dataverse](https://dataverse.harvard.edu/): a repository of research datasets connected to academic studies -- good for replication studies

- [Google Dataset Search](https://datasetsearch.research.google.com/): a search engine for datasets if you have a general topic in mind
    - **a word of caution about Kaggle**: [Kaggle](https://www.kaggle.com/datasets) is popular and maintains a large collection of datasets so will show up in many search results. However the quality, context, and documentation around the datasets can vary a lot, which may make filling out the datasheet a bit challenging.

## Jupyter Book and Myst articles

These are few examples of how Jupyter Book + Myst Markdown can be used to produce nicely typeset articles with interactive elements:

- [Zipf's law from the Good Research Code Handbook](https://goodresearch.dev/zipf)
- [Programming Differential Privacy](https://programming-dp.com/ch1.html)
- [Computational Tools for Geographic Data Science](https://geographicdata.science/book/notebooks/02_geospatial_computational_environment.html)
- [More examples in Executable Book Gallery](https://executablebooks.org/en/latest/gallery/)
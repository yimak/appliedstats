## README: Statistical Analysis Assignment
## Name: Issam Chaaraddine

## Overview
This project consists of four tasks and a project designed to test your understanding of probability, statistics, and Python programming. The tasks involve solving problems related to permutations and combinations, normal distributions, t-tests, and ANOVA. The project focuses on analyzing the PlantGrowth dataset using statistical methods. Below are detailed instructions and requirements for each task and the project.

---

## Task 1: Permutations and Combinations

### Scenario
In an experiment involving 12 cups of tea, six cups have milk poured first, and the other six have tea poured first. A person claims to have the ability to identify the sequence by tasting the tea.

### Instructions
1. **Calculate Probability of Selecting Correct Cups:**
   - Assume the person is guessing randomly.
   - Use Python to calculate the probability of selecting all six cups correctly.
   - Justify your calculations with Markdown explanations and code comments.

2. **Calculate Probability with One Error Allowed:**
   - Calculate the probability of selecting at least five correct cups, assuming no special ability.
   - Explain your results and show your work in both code and Markdown.

3. **Consider Two Errors:**
   - Discuss whether two errors should be acceptable, providing reasoning and explanations.

---

## Task 2: numpy's Normal Distribution

### Scenario
Assess whether `numpy.random.normal()` generates values consistent with a normal distribution.

### Instructions
1. **Generate Data:**
   - Create a sample of 100,000 values using `numpy.random.normal()` with a mean of 10.0 and standard deviation of 3.0.

2. **Test for Normality:**
   - Use `scipy.stats.shapiro()` to test whether the sample follows a normal distribution.
   - Explain the results of the Shapiro-Wilk test in Markdown.

3. **Visualize Data:**
   - Plot a histogram of the sample values.
   - Overlay the normal distribution's probability density function (PDF) on the histogram.

---

## Task 3: t-Test Calculation

### Scenario
Analyze the following dataset of resting heart rates before and after a two-week exercise program:

| Patient ID | 0  | 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  | 9  |
|------------|----|----|----|----|----|----|----|----|----|----|
| Before     | 63 | 68 | 70 | 64 | 74 | 67 | 70 | 57 | 66 | 65 |
| After      | 64 | 64 | 68 | 64 | 73 | 70 | 72 | 54 | 61 | 63 |

### Instructions
1. **Calculate the t-statistic:**
   - Compare your result to the value obtained using `scipy.stats`.

2. **Explain Your Work:**
   - Provide Markdown explanations for your calculations and results.
   - Include sources for any external information or formulas used.

---

## Task 4: ANOVA

### Scenario
Estimate the probability of committing a type II error under specific conditions.

### Instructions
1. **Simulate Data:**
   - Use `numpy.random.normal()` to generate three samples of 100 values each.
   - Assign means of 4.9, 5.0, and 5.1, with a standard deviation of 0.1.
   - create a variable called no_type_ii and set it to 0.


2. **Perform ANOVA:**
   - Use one-way ANOVA to test for differences among the three groups.
   - Record how often a type II error occurs in 10,000 iterations.

3. **Summarize Results:**
   - Provide an explanation of your findings in Markdown.

---

## Project: PlantGrowth Dataset Analysis

### Scenario
Analyze the PlantGrowth dataset, which contains data on plant weights under three treatment groups (`ctrl`, `trt1`, `trt2`).

### Instructions
1. **Dataset Setup:**
   - Download the dataset from [Rdatasets](https://vincentarelbundock.github.io/Rdatasets/).
   - Save it to your repository.

2. **Describe the Dataset:**
   - Provide an overview of the dataset, including its structure and variables.

3. **t-Test Analysis:**
   - Explain what a t-test is and its assumptions.
   - Perform a t-test to determine if there is a significant difference between the `trt1` and `trt2` groups.

4. **ANOVA Analysis:**
   - Explain why ANOVA is appropriate for comparing multiple groups.
   - Perform ANOVA to compare the `ctrl`, `trt1`, and `trt2` groups.

5. **Documentation and Visualization:**
   - Use Markdown to explain your steps and findings.
   - Include plots to visualize differences among groups.



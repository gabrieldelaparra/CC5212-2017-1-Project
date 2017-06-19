# MDP Project
**Universidad de Chile**

**Departamento de Ciencias de la Computación**

**CC5212 - Procesamiento Masivo de Datos**

Ignacio Perez

Omar Sanhaji

Gabriel De La Parra

## Context

Our project is based on the [Kaggle Quora Question-Pair comptetition.](https://www.kaggle.com/c/quora-question-pairs) 

The goal of this project is to establish, using natural language processing tools, whether a pair of questions have the same intent, in the sense that the answer to any one of them would also answer the other. Specifically, we're measuring to what extent can term similarity help establish this fact, since we're counting on a dataset with ground-truth.

## DataSet

The dataset consists of a table with 404290 rows, with each row containing two different questions (each one not necessarily unique in the dataset) and a ground-truth column which indicates if the questions are duplicates or not. The file is a CSV with a size of 63.4 mb. It also has two columns with the IDs for each question in the row.

We chose this dataset because it is an interesting problem, which still hasn't got a solution, and since it came with a ground-truth, we could easily observe the results of our method.

## Data exploration

As it can be seen in the following examples, some questions are indeed different, while others seem to be the same, even when they are classified as different. 

Some questions, like 1 and 2 have clear words differences, which would be an easy result for word by word comparison. 

Questions like 3, 4 and 5 present a slight difference in which a personal pronoun is introduced. In 3, the questions are classified as similar, while in 4 they are classified as different. 5 indicates that a focused question is different, which we believe is contradictory with 3 and 4.

As it can be seen on examples 6 and 7, while on 6 the difference is on the type of question, in 7 the context indicates that the question is different. Still they are classified as same and different, which we agreed on.

```
1,"Why is creativity important?","Why creativity is important?",true
2,"What is the 2S class in Indian Railways?","What is TQWL in IRCTC wait list?",false
3,"How do I make friends.","How to make friends ?",true
4,"What is like to have sex with cousin?","What is it like to have sex with your cousin?",false
5,"What is one coin?","What's this coin?",false
6,"Which fruit contains fat?","What fruits contain fat?",true
7,"What is the step by step guide to invest in share market in india?","What is the step by step guide to invest in share market?",false
```

## Approach

Python was used at first to explore the data and see the first results using stemming, lemmatization and synonymization. Also, a TF-IDF was created using Lucene, but no further use was given to it (Since the data exploration observations). This was done for a few examples. 

Then we moved to the cluster. We used Pig because of its relative simplicity of use and because it's more suited for doing quick modifications. User defined functions were implemented in Java, including column transformations for stemming and stop word removal.

Abstractly speaking, we took each question pair as a bag of words, removed stop words and applied stemming over it, then counted the words that appeared on both questions **sharedWords**, counted the words that appeared only in one question **distinctWords**, normalized both counts over the sum of both word counts and calculated a similarity index:

```
S = normalizedSharedWords * 0.8 + normalizedDistinctWords*0.2.
```

We then arbitrarily established a threshold **T = 0.5** for the similarity index so that if **S >= T** then the questions are duplicates.

## Results

Applying our methods we found a 0.65 success rate was obtained in determining whether two questions were duplicates. This means that, although we achieve a better-than-random probability of being correct, there is not that much useful information for performing this task in term similarity. Probably, a higher success rate could be achieved if n-gram similarity were implemented. 

## Observations on Data

Reading the discussions and solutions at the competition's page, we realized that the most important part for achieving good results was feature mining, i.e., finding features of the dataset which don't have to do with the general problem but with the particular ensemble of data at hand. In this case, for example, it was leaked that more frequent questions in the dataset had a higher probability of being in duplicate pairs. This was disappointing for some participants in the competition, who expressed their dislike for this state of affairs, that put natural language processing on the background while the winners would be decided by the number and importance of dataset features they could extract.

## Conclussions

We ran into several issues with Java dependencies and Pig. Not knowing if it was something related to Pig, we tried to move to Apache Spark, but it didn't do any better so we finally stayed with Pig.
Pig offers several benefits, since it does not requires compilation and dependencies can be moved once to the cluster without having to upload the whole dependencies for every test.

There was a lot of time spent implementing and debugging the solution. Debugging on the cluster wasn't comfortable at first (is it even possible for UDFs?). Managing Java dependencies was a heavy waste of time. So, there wasn't enough resources left to think about what we were doing, and there were some losses like the finally unused TF-IDF.

## Report and Presentation

[Overleaf report](https://www.overleaf.com/10029701whtgnrgcsvrd)

[Google slides presentation](https://docs.google.com/presentation/d/1Q_mVNZ5vcDTOUoHMra-FgQYWhE3MMxWBPYAuq78imTg/edit?usp=sharing)

## Required Packages:
The following packages were used. These .jar are included in the repo.

Hadoop: [org.apache.hadoop;hadoop-common:2.3.0](http://search.maven.org/remotecontent?filepath=org/apache/hadoop/hadoop-common/2.3.0/hadoop-common-2.3.0.jar)

Pig: [org.apache.pig;pig;0.14](http://search.maven.org/remotecontent?filepath=org/apache/pig/pig/0.14.0/pig-0.14.0.jar)

Stemmer: [de.julielab;uea-stemmer:0.1](http://search.maven.org/remotecontent?filepath=de/julielab/uea-stemmer/0.1/uea-stemmer-0.1.jar)

## Useful commands
Some of the used commands for quick copy-paste reference :)

#### Upload Pig Script
```
scp -P 220 mdpProject01.pig uhadoop@cm.dcc.uchile.cl:/data/2017/uhadoop/gdlp
```

#### Upload Pig UDFs
Copy .jar to cluster
```
scp -P 220 udf.simplifyQuestion/dist/simplify.jar uhadoop@cm.dcc.uchile.cl:/data/2017/uhadoop/gdlp
```

```
scp -P 220 udf.similarQuestions/dist/similar.jar uhadoop@cm.dcc.uchile.cl:/data/2017/uhadoop/gdlp
```

```
scp -P 220 udf.differentQuestions/dist/different.jar uhadoop@cm.dcc.uchile.cl:/data/2017/uhadoop/gdlp
```

#### On Cluster:
(!) Remember to remove the output after every pig run:

##### If ExecType == Local:
```
rm results/ -rf
```

Run the results
```PigLatin
pig -x local mdpProject01.pig
```

#### Compress/Extract the dataset
Compress
```
tar -czvf train.tar.gz train.csv
```
Send to cluster
```
scp -P 220 train.tar.gz uhadoop@cm.dcc.uchile.cl:/data/2017/uhadoop/gdlp
```
Extract
```
tar -xvzf traing.tar.gz
```

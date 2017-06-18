# MDP Project



## Required Packages:
The following packages were used. These .jar are included in the repo.

Hadoop: [org.apache.hadoop:hadoop-common:2.3.0](http://search.maven.org/remotecontent?filepath=org/apache/hadoop/hadoop-common/2.3.0/hadoop-common-2.3.0.jar)
Pig: [org.apache.pig:pig:0.14](http://search.maven.org/remotecontent?filepath=org/apache/pig/pig/0.14.0/pig-0.14.0.jar)
Stemmer: [de.julielab:uea-stemmer:0.1](http://search.maven.org/remotecontent?filepath=de/julielab/uea-stemmer/0.1/uea-stemmer-0.1.jar)

## Useful commands
Some of the used commands for quick copy-paste reference :)

#### Upload Pig Script
```
scp -P 220 mdpProject01.pig uhadoop@cm.dcc.uchile.cl:/data/2017/uhadoop/gdlp
```

#### Upload Pig UDFs
Copy Simplify.jar
```
scp -P 220 udf.simplifyQuestion/dist/simplify.jar uhadoop@cm.dcc.uchile.cl:/data/2017/uhadoop/gdlp
```
Copy Similar.jar
```
scp -P 220 udf.similarQuestions/dist/similar.jar uhadoop@cm.dcc.uchile.cl:/data/2017/uhadoop/gdlp
```
Copy Different.jar
```
scp -P 220 udf.differentQuestions/dist/different.jar uhadoop@cm.dcc.uchile.cl:/data/2017/uhadoop/gdlp
```

#### On Cluster:
Remember to remove the outputs
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
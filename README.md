# MDP Project

### Upload Pig Script
```
scp -P 220 mdpProject01.pig uhadoop@cm.dcc.uchile.cl:/data/2017/uhadoop/gdlp
```

### Upload Pig UDFs
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

### On Cluster:
Remember to remove the outputs
```
rm results/ -rf
```
Run the results
```
pig -x local mdpProject01.pig
```

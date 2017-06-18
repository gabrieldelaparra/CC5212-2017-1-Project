REGISTER 'simplify.jar';
DEFINE Simplify org.mdp.project.pig.Simplify();

REGISTER 'similar.jar';
DEFINE Similar org.mdp.project.pig.SimilarQuestions();

REGISTER 'different.jar';
DEFINE Different org.mdp.project.pig.DifferentQuestions();

dirty_data = LOAD 'train.csv' USING PigStorage('"');

raw_data = FOREACH dirty_data 
		   GENERATE REPLACE($1, '\\"', '') as (pairId:int),
			   	    REPLACE($3, '\\"', '') as (q1Id:int),
					REPLACE($5, '\\"', '') as (q2Id:int),
					REPLACE($7, '\\"', '') as (q1:chararray),
					REPLACE($9, '\\"', '') as (q2:chararray),
					($11 == 0 ? false : true) as (isDuplicate:boolean);

-- test_data = LIMIT raw_data 30;
-- STORE raw_data INTO 'results';

parsed = FOREACH raw_data GENERATE $0, $5, Simplify($3), Simplify($4);
parsed = FOREACH parsed GENERATE $0, $1, $2, $3, Similar($2, $3), Different($2, $3);
parsed = FOREACH parsed GENERATE $0, $1, $2, $3, $4, $5, (0.8*$4 + 0.2*$5);
parsed = FOREACH parsed GENERATE $0, $1, $2, $3, $4, $5, $6, ($6 > 0.5 ? true : false);

matchItems = FILTER parsed by ($1 == $7);
realTrue = GROUP matchItems ALL;
realTrueCount = FOREACH realTrue GENERATE COUNT(matchItems);

items = GROUP parsed ALL;
itemCount = FOREACH items GENERATE COUNT(*);

DUMP realTrueCount;
DUMP itemCount;

STORE parsed INTO 'results';
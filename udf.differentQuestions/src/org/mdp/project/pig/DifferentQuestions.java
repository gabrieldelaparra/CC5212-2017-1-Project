package org.mdp.project.pig;

import java.io.IOException;
import org.apache.pig.EvalFunc;
import org.apache.pig.data.Tuple;

public class DifferentQuestions extends EvalFunc<Float> {
	
	public Float exec(Tuple input) throws IOException {
		if (input == null || input.size() == 0 )
			return 5.0f;
		try {
			String str1 = (String) input.get(0);
			String str2 = (String) input.get(1);
			
			if(str1 == null || str1 == "")
				return 5.1f;
			if(str2 == null || str2 == "")
				return 5.2f;
			
			return differentWords(str1, str2);
		} catch (Exception e) {
			throw new IOException("Caught exception processing input row ", e);
		}
	}
	
	public static float differentWords(String q1, String q2){
		String[] q1Words = q1.split(" ");
		String[] q2Words = q2.split(" ");
		
		int differentWords = 0;	
			
		for (int i = 0; i < q1Words.length; i++) {
			if(!q2.contains(q1Words[i])){
				differentWords++;	
			}
		}
		
		return (float)differentWords/(float)Math.max(q1Words.length, q2Words.length);
	}

}

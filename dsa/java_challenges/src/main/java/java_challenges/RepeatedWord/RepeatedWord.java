package java_challenges.RepeatedWord;

import java.util.HashMap;

public class RepeatedWord {
    public static String repeatedWord(String thisString){
        HashMap<String, Integer> wordCount = new HashMap<>();
        String[] justWords = thisString.split(" ");
        // iterate over the array
        for (int i=0; i< justWords.length; i++){
//            String[] words = justWords[i].split("(\\w*[^,\\s.!?;])");
            String[] words = justWords[i].split("[,?!]");
            String thisWord = words[0];
            if (wordCount.containsKey(thisWord.toLowerCase())){
                return thisWord;
            } else{
                wordCount.put(thisWord.toLowerCase(),1);
            }
        }
        return "no match found";
    }
}

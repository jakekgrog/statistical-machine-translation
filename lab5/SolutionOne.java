import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class SolutionOne {
    /** 
     * Given a file containing a number of sentences, please calculate the frequency (p(w)) of each word (w) in
     * these sentences 
    */
    
    public static void main(String args[]) {
        Map<String, Integer> hm = wordCounts(args[0]);

        Integer totalCount = 0;
        for (Map.Entry<String, Integer> entry : hm.entrySet()){
            totalCount += entry.getValue();
        }

        Map<String, Double> freqs = wordFrequency(hm, totalCount);

        System.out.println(Arrays.asList(freqs));
    }

    public static Map<String, Integer> wordCounts(String fileName) {
        Map<String, Integer> hm = new HashMap<>();

        try {
            File file = new File(fileName);
            Scanner scanner = new Scanner(file);

            Integer wordCount = 0;

            while (scanner.hasNext()) {
                String line = scanner.nextLine();
                String[] words = line.split(" ");
                for (int i = 0; i < words.length; i++) {
                    Integer count = hm.containsKey(words[i]) ? hm.get(words[i]) : 0;
                    hm.put(words[i], count + 1);
                    wordCount++;
                }
            }
            scanner.close();

            return hm;

        } catch (FileNotFoundException e) {
            System.out.println(e);
            return hm;
        }
    }

    public static Map<String, Double> wordFrequency(Map<String, Integer> wordCounts, Integer totalWords) {
        Map<String, Double> freq = new HashMap<>();

        for (Map.Entry<String, Integer> entry : wordCounts.entrySet()){
            Double wf = (double) entry.getValue() / totalWords;
            System.out.println(wf);
            freq.put(entry.getKey(), wf);
        }

        return freq;
    }
}
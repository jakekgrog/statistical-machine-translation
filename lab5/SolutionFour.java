import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;

public class SolutionFour {
    /**
     * Firstly, try another sentence using your program of Question 3.
     * Please calculate the probability of the sentence “<s> a cat sat on the car </s>”.
     * What result/error do you get? Please think about what the reason is and why we 
     * need smoothing techniques in language modeling.
     * 
     * Secondly, modify your function of bigram relative frequency according
     * to add-one smoothing formula.
     * 
     * Please use your smoothed function to calculate bigram probability
     * of a sentence of the two sentences
     * 
     * @CLIArg - corpus.txt
     * @Input - "<s> a cat sat on the mat </s>"
     * @ExpectedOutput - 0.000140949604457
     */

    public static void main(String args[]) {
        BufferedReader br = null;

        try {
            br = new BufferedReader(new FileReader(args[0]));

            // Build array, each entry being a sentence in the corpus
            List<String> references = new ArrayList<>();
            String line;
            while((line = br.readLine()) != null) {
                references.add(line);
            }
            
            // Build a list of all bigrams from the corpus
            List<String> referenceBigrams = new ArrayList<>();
            for (String sentence : references) {
                List<String> bigrams = ngrams(2, sentence);
                referenceBigrams.addAll(bigrams);
            }

            // Count the number of times each bigram occurs in the corpus.
            Map<String, Integer> bigramCounts = bigramCount(referenceBigrams);

            // Count the number of times each word appears alongside
            // every other word in the corpus
            Map<String, Integer> wordCount = wordCounts(referenceBigrams);
            
            // Calculate sentence probability
            Scanner inputScanner = new Scanner(System.in);
            String inputSentence = inputScanner.nextLine();
            List<String> bigramInput = ngrams(2, inputSentence);

            double probability = 1.0;
            int uniqueWordsCount = countUniqueWords(references);

            for (String bigram : bigramInput) {
                String firstGram = bigram.split(" ")[0];

                int countw1w2 = bigramCounts.containsKey(bigram) 
                    ? bigramCounts.get(bigram) + 1
                    : 1;

                int countw1w = wordCount.containsKey(firstGram) 
                    ? wordCount.get(firstGram) + uniqueWordsCount 
                    : uniqueWordsCount;

                // Bigram relative frequency with add-one smoothing
                double bigramRelFreq = (double) countw1w2 / countw1w;    
                
                probability = probability * bigramRelFreq;
            }
            
            System.out.println(probability);

        } catch (Exception e) {
            System.out.println(e);
        } finally {
            try {
                br.close();
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }

    public static int countUniqueWords(List<String> references) {
        Set<String> uniqueWords = new HashSet<>();
        for (String sentence : references) {
            String[] words = sentence.split(" ");
            Set<String> tmpSet = new HashSet<>(Arrays.asList(words));
            uniqueWords.addAll(tmpSet);
        }
        System.out.println(uniqueWords.toString());
        return uniqueWords.size();
    }

    public static Map<String, Integer> wordCounts(List<String> bigrams) {
        Map<String, Integer> wordCounts = new HashMap<>();
        for (String bigram : bigrams) {
            String word = bigram.split(" ")[0];
            Integer count = wordCounts.containsKey(word)
                ? wordCounts.get(word) + 1
                : 1;
            wordCounts.put(word, count);
        }
        return wordCounts;
    }

    public static Map<String, Integer> bigramCount(List<String> bigrams) {
        Map<String, Integer> bigramCount = new HashMap<>();
        for (String gram : bigrams) {
            Integer count = bigramCount.containsKey(gram)
                ? bigramCount.get(gram) + 1 
                : 1;
            bigramCount.put(gram, count);
        }
        return bigramCount;
    }

    public static List<String> ngrams(int n, String s) {
        List<String> grams = new ArrayList<String>();
        String[] words = s.split(" ");

        int i = 0;
        int j = n;
        while (j < words.length + 1) {
            grams.add(concat(words, i, j));
            i++;
            j++;
        }
        return grams;
    }

    public static String concat(String[] words, int start, int end) {
        StringBuilder sb = new StringBuilder();
        for (int i = start; i < end; i++) {
            sb.append((i > start ? " " : "") + words[i]);
        }
        return sb.toString();
    }
}
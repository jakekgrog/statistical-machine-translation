import java.util.Map;
import java.util.Scanner;


public class SolutionTwo {
    /**
     * Given a sentence (s) and a corpus, please calculate the unigram probability (language model) of the
     * sentence according to the formula: P(S = W1,...,W2) = P(W1) x ... x p(Wn)
     */
    public static void main(String args[]) {
        Map<String, Integer> hm = SolutionOne.wordCounts(args[0]);

        Integer totalCount = 0;
        for (Map.Entry<String, Integer> entry : hm.entrySet()){
            totalCount += entry.getValue();
        }

        Map<String, Double> freqs = SolutionOne.wordFrequency(hm, totalCount);
        
        Scanner inputScanner = new Scanner(System.in);
        String inputSentence = inputScanner.nextLine();

        Double prob = unigramProb(inputSentence, freqs);
        System.out.println(prob);
    }

    public static Double unigramProb(String s, Map<String, Double> freqs) {
        String[] words = s.split(" ");
        Double probability = 1.0;
        for (int i = 0; i < words.length; i++) {
            if (freqs.containsKey(words[i])) {
                probability = probability * freqs.get(words[i]);
            }
        }
        return probability;
    }
}
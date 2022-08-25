import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Question5 {

    public static void question5(int m, int p) throws Exception {
        DoubleHashTable doubleHashTable = new DoubleHashTable(m, p);
        int n = Math.floorDiv(m, 2);
        // Do this 6 times
        for (int i = 0; i < 6; i++) {
            System.out.print("Iteration #" + (i + 1) + ": ");
            // Generate new random sequence
            List<HashTableElement> sequence = generateSequence(n);
            long start = System.currentTimeMillis();
            // Insert sequence into the table
            for (HashTableElement hte : sequence) doubleHashTable.Insert(hte);
            // Clear table
            for (HashTableElement hte : sequence) doubleHashTable.Delete(hte.GetKey());
            long finish = System.currentTimeMillis();
            double elapsed = ((double) (finish - start) / 1000);
            System.out.println(elapsed + " seconds\n");
        }
    }

    public static List<HashTableElement> generateSequence(int n) {
        List<HashTableElement> sequence = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int b = getRandomInteger(0, 100);
            long a = (100L * i) + b;
            sequence.add(new HashTableElement(a, i));
        }
        return sequence;
    }

    public static int getRandomInteger(int origin, int bound) {
        Random random = new Random();
        return random.nextInt(origin, bound);
    }

    public static void main(String[] args) {
        int m = 10000019;
        int p = 1000000007;
        try {
            question5(m, p);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}

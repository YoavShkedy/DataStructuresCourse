import java.util.*;

public class Question4 {

    public static List<HashTableElement> generateSequence(int n) {
        List<HashTableElement> sequence = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int b = getRandomInteger(0, 100);
            long a = (100L * i) + b;
            sequence.add(new HashTableElement(a, i));
        }
        return sequence;
    }

    public static void runLPHashTable(int m, int p, List<HashTableElement> sequence) {
        LPHashTable lpHashTable = new LPHashTable(m, p);
        System.out.println("Experimenting with LPHashTable:");
        long start = System.currentTimeMillis();
        for (HashTableElement hte : sequence) {
            try {
                lpHashTable.Insert(hte);
            } catch (Exception e) { e.printStackTrace(); }
        }
        long finish = System.currentTimeMillis();
        double elapsed = ((double) (finish - start) / 1000);
        System.out.println("It took " + elapsed + " seconds\n");
    }

    public static void runQPHashTable(int m, int p, List<HashTableElement> sequence) {
        QPHashTable qpHashTable = new QPHashTable(m, p);
        System.out.println("Experimenting with QPHashTable:");
        long start = System.currentTimeMillis();
        for (HashTableElement hte : sequence) {
            try {
                qpHashTable.Insert(hte);
            } catch (Exception e) { e.printStackTrace(); }
        }
        long finish = System.currentTimeMillis();
        double elapsed = ((double) (finish - start) / 1000);
        System.out.println("It took " + elapsed + " seconds\n");
    }

    public static void runAQPHashTable(int m, int p, List<HashTableElement> sequence) {
        AQPHashTable aqpHashTable = new AQPHashTable(m, p);
        System.out.println("Experimenting with AQPHashTable:");
        long start = System.currentTimeMillis();
        for (HashTableElement hte : sequence) {
            try {
                aqpHashTable.Insert(hte);
            } catch (Exception e) { e.printStackTrace(); }
        }
        long finish = System.currentTimeMillis();
        double elapsed = ((double) (finish - start) / 1000);
        System.out.println("It took " + elapsed + " seconds\n");
    }

    public static void runDoubleHashTable(int m, int p, List<HashTableElement> sequence) {
        DoubleHashTable doubleHashTable = new DoubleHashTable(m, p);
        System.out.println("Experimenting with DoubleHashTable:");
        long start = System.currentTimeMillis();
        for (HashTableElement hte : sequence) {
            try {
                doubleHashTable.Insert(hte);
            } catch (Exception e) { e.printStackTrace(); }
        }
        long finish = System.currentTimeMillis();
        double elapsed = ((double) (finish - start) / 1000);
        System.out.println("It took " + elapsed + " seconds\n");
    }

    public static void firstQuestion() {
        int m = 10000019;
        int p = 1000000007;
        int n = Math.floorDiv(m, 2);
        List<HashTableElement> sequence = generateSequence(n);
        runLPHashTable(m, p, sequence);
        runQPHashTable(m, p, sequence);
        runAQPHashTable(m, p, sequence);
        runDoubleHashTable(m, p, sequence);
    }

    public static void secondQuestion() {
        int m = 10000019;
        int p = 1000000007;
        int n = Math.floorDiv(19 * m, 20);
        List<HashTableElement> sequence = generateSequence(n);
        runLPHashTable(m, p, sequence);
        runAQPHashTable(m, p, sequence);
        runDoubleHashTable(m, p, sequence);
    }

    public static int getRandomInteger(int origin, int bound) {
        Random random = new Random();
        return random.nextInt(origin, bound);
    }

    public static void main(String[] args) {
//        firstQuestion();
//        secondQuestion();
    }

}

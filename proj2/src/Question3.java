import java.util.HashSet;
import java.util.Random;
import java.util.Set;

public class Question3 {

    public static void main(String[] args) {
        int q = 6571;
        int p = 1000000007;
        System.out.println("Experimenting with quadratic probing:");
        generateQPHashTable(q, p);
        System.out.println("Experimenting with alternating quadratic probing:");
        generateAQPHashTable(q, p);
    }

    public static int calculateQ1(int q) {
        Set<Integer> set = new HashSet<>();
        for (int i = 0; i < q; i++) {
            set.add((int) (Math.pow(i, 2) % q));
        }
        return set.size();
    }

    public static int calculateQ2(int q) {
        Set<Integer> set = new HashSet<>();
        for (int i = 0; i < q; i++) {
            int res;
            int val = (int) (Math.pow(-1, i) * Math.pow(i, 2)) % q;
            if (val >= 0) res = val;
            else res = (val + q);
            set.add(res);
        }
        return set.size();
    }

    public static void generateQPHashTable(int m, int p) {
        for (int i = 0; i < 100; i++) {
            QPHashTable qpHashTable = new QPHashTable(m, p);
            for (int j = 0; j < m; j++) {
                int a = (100 * j) + getRandomInteger(0, 100);
                try {
                    qpHashTable.Insert(new HashTableElement(j, a));
                } catch (Exception e) { e.printStackTrace(); }
            }
        }
    }

    public static void generateAQPHashTable(int m, int p) {
        for (int i = 0; i < 100; i++) {
            AQPHashTable aqpHashTable = new AQPHashTable(m, p);
            for (int j = 0; j < m; j++) {
                int a = (100 * j) + getRandomInteger(0, 100);
                try {
                    aqpHashTable.Insert(new HashTableElement(j, a));
                } catch (Exception e) { e.printStackTrace(); }
            }
        }
    }

    public static int getRandomInteger(int origin, int bound) {
        Random random = new Random();
        return random.nextInt(origin, bound);
    }

}

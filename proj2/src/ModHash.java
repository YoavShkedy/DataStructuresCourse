import java.util.Random;

public class ModHash {
	private final int m;
	private final long p, a, b;

	private ModHash(int m, long p, long a, long b) {
		this.m = m;
		this.p = p;
		this.a = a;
		this.b = b;
	}
	
	public static ModHash GetFunc(int m, long p) {
		// Pick random 1 <= a < p and random 0 <= b < p
		long a = getRandomLong(1, p);
		long b = getRandomLong(0, p);
		return new ModHash(m, p, a, b);
	}
	
	public int Hash(long key) {
		// h(x) = ((ax + b) mod p) mod m
		long res = ((a * key) + b) % p;
		return (int) res % m;
	}

	public static long getRandomLong(long origin, long bound) {
		Random random = new Random();
		return random.nextLong(origin, bound);
	}

}

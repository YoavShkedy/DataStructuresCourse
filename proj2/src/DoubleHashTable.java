public class DoubleHashTable extends OAHashTable {
	private final ModHash h1;
	private final ModHash h2;

	public DoubleHashTable(int m, long p) {
		super(m);
		h1 = ModHash.GetFunc(m, p);
		h2 = ModHash.GetFunc(m - 1, p);
	}
	
	@Override
	public int Hash(long x, int i) {
		// h(k, i) = (h1(k) + i*h2(k)) mod m
		long res1 = h1.Hash(x);
		long res2 = ((long) i * (h2.Hash(x) + 1));
		return (int) ((res1 + res2) % length());
	}

}

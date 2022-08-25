public class QPHashTable extends OAHashTable {
	private final ModHash hashFunction;

	public QPHashTable(int m, long p) {
		super(m);
		hashFunction = ModHash.GetFunc(m, p);
	}
	
	@Override
	public int Hash(long x, int i) {
		// h(k, i) = (h'(k) + i^2) mod m
		int iSquared = (int) Math.pow(i, 2);
		return (hashFunction.Hash(x) + iSquared) % length();
	}

}

public class LPHashTable extends OAHashTable {
	private final ModHash hashFunction;
	
	public LPHashTable(int m, long p) {
		super(m);
		hashFunction = ModHash.GetFunc(m, p);
	}
	
	@Override
	public int Hash(long x, int i) {
		// h(k, i) = (h'(k) + i) mod m
		return (hashFunction.Hash(x) + i) % length();
	}

}

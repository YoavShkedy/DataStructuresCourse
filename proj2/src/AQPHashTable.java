public class AQPHashTable extends OAHashTable {
	private final ModHash hashFunction;

	public AQPHashTable(int m, long p) {
		super(m);
		hashFunction = ModHash.GetFunc(m, p);
	}
	
	@Override
	public int Hash(long x, int i) {
		// h(k, i) = (h'(k) + (-1)^i * i^2) mod m
		int sign;
		if (i % 2 == 0) sign = 1;
		else sign = -1;
		int iSquared = (int) Math.pow(i, 2);
		int res = (hashFunction.Hash(x) + (sign * iSquared)) % length();
		if (res >= 0) return res;
		else return res + length();
	}

}

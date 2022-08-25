// ID: 314939398
// Name: Yoav Shkedy
// Username: yoavshkedy

public abstract class OAHashTable implements IHashTable {
	
	private HashTableElement[] table;	// The table
	private int n;						// Number of elements in the table
	private int m;						// Size of the table

	private static final HashTableElement DELETED = new HashTableElement(-1, 0);

	public OAHashTable(int m) {
		this.table = new HashTableElement[m];
		this.m = m;
		this.n = 0;
	}
	
	@Override
	public HashTableElement Find(long key) {
		// If table is empty return null
		if (isEmpty()) return null;
		// Search key according to probing sequence
		for (int i = 0 ; i < m; i++) {
			int j = Hash(key, i);
			// If key does not exist in the table return null
			if (table[j] == null) return null;
			// Else, keep searching for key
			else if (table[j].GetKey() == key) {
				// Key was found, return hte associated with the key
				return table[j];
			}
		}
		return null;
	}
	
	@Override
	public void Insert(HashTableElement hte) throws TableIsFullException,
			KeyAlreadyExistsException {
		// If table is full throw exception
		if (isFull()) throw new TableIsFullException(hte);
		long key = hte.GetKey();
		// Ensure the key does not already exist in the table
		if (Find(key) != null) throw new KeyAlreadyExistsException(hte);
		// Search for an empty cell according to probing sequence
		for (int i = 0 ; i < m; i++) {
			int j = Hash(key, i);
			// If cell is empty or is marked deleted, insert hte to it
			if (table[j] == null || table[j] == DELETED) {
				table[j] = hte;
				n++;
				return;
			}
		}
		// No empty cell was found, throw exception
		throw new TableIsFullException(hte);
	}
	
	@Override
	public void Delete(long key) throws KeyDoesntExistException {
		// If table is empty throw exception
		if (isEmpty()) throw new KeyDoesntExistException(key);
		// Search key according to probing sequence
		for (int i = 0 ; i < m; i++) {
			int j = Hash(key, i);
			// If key does not exist in the table throw exception
			if (table[j] == null) throw new KeyDoesntExistException(key);
			// Else, keep searching for key
			else if (table[j].GetKey() == key) {
				// Key was found, mark cell as deleted
				table[j] = DELETED;
				n--;
				return;
			}
		}
		// Did not find key, throw exception
		throw new KeyDoesntExistException(key);
	}

	public int length() {
		return m;
	}

	/**
	 * Checks if the table is empty.
	 * @return {@code true} if the table is empty
	 */
	public boolean isEmpty() {
		return n == 0;
	}

	/**
	 * Checks if the table is full.
	 * @return {@code true} if the table is full
	 */
	public boolean isFull() {
		return n == m;
	}
	
	/**
	 * @param x The key to hash
	 * @param i The index in the probing sequence
	 * @return the index in the hash table to place the key x
	 */
	public abstract int Hash(long x, int i);

}

public interface IHashTable {
	
	/**
	 * @param hte The table entry to add
	 * @throws KeyAlreadyExistsException - Throws this if
	 * an entry of the same key already exists in the table.
	 * @throws TableIsFullException - Throws this if the probing sequence did not find a place for hte.
	 */
	public void Insert(HashTableElement hte) throws TableIsFullException, KeyAlreadyExistsException;
	
	/**
	 * 
	 * @param key The key to delete from the table
	 * @throws KeyDoesntExistException - Throws this if
	 * an entry of the searched key doesn't exist in the table.
	 */
	public void Delete(long key) throws KeyDoesntExistException;
	
	/**
	 * 
	 * @param key The key to find in the table
	 * @return The table entry with the required key if exists, or null otherwise.
	 */
	public HashTableElement Find(long key);
	
	public class TableIsFullException extends Exception {
		public HashTableElement hte;
		
		public TableIsFullException(HashTableElement hte) {	
			this.hte=hte;
		}
	}
	
	public class KeyAlreadyExistsException extends Exception{
		public HashTableElement hte;
		
		public KeyAlreadyExistsException(HashTableElement hte) {
			this.hte=hte;
		}
	}
	
	public class KeyDoesntExistException extends Exception{
		public long key;
		
		public KeyDoesntExistException(long key) {
			this.key=key;
		}
	}
}

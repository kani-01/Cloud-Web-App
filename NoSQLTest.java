
import java.net.UnknownHostException;
import java.util.List;
import java.util.Set;

import com.mongodb.DB;
import com.mongodb.MongoClient;

public class NoSQLTest {

	public static void main(String[] args) throws UnknownHostException {
		// TODO Auto-generated method stub

		MongoClient mongoClient = new MongoClient("localhost", 27017);

		List<String> databases = mongoClient.getDatabaseNames();

		for (String dbName : databases) {
			System.out.println("- Database: " + dbName);

			DB db = mongoClient.getDB(dbName);

			Set<String> collections = db.getCollectionNames();
			for (String colName : collections) {
				System.out.println("\t + Collection: " + colName);
			}
		}

		mongoClient.close();
	}

}

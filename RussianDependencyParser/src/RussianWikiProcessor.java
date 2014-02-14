
import de.tudarmstadt.ukp.wikipedia.api.*;
import de.tudarmstadt.ukp.wikipedia.api.WikiConstants.Language;
import de.tudarmstadt.ukp.wikipedia.api.exception.WikiApiException;
import de.tudarmstadt.ukp.wikipedia.api.exception.WikiInitializationException;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.io.Writer;
import java.sql.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Iterator;
import java.util.List;


public class RussianWikiProcessor {
	

	public static void main(String[] args) throws WikiApiException, SQLException, IOException{

		      
        DatabaseConfiguration dbConfig = new DatabaseConfiguration();
        dbConfig.setHost("localhost:3306");
        dbConfig.setDatabase("wikipedia");
        dbConfig.setUser("root");
        dbConfig.setPassword("rekap123");
        dbConfig.setLanguage(Language.russian);
        Wikipedia wiki = new Wikipedia(dbConfig);
        Iterator<Page> it = wiki.getArticles().iterator();
        //FileWriter f = new FileWriter(new File("WikipediaTestA"));
        String allDataDir = "/home/mtydykov/"
	    		+ "workspace/RussianDependencyParser/allData/";
        ArrayList<Integer> randomArticleNums = new ArrayList();
        int numArticles = 0;
        //get the total number of articles in the DB
        while(it.hasNext()){
        	it.next();
        	numArticles++;
        }
        // add 100 random numbers limited by the num of articles in the DB 
        for(int j = 0; j < numArticles; j++){
        	randomArticleNums.add(j);
        }
        Collections.shuffle(randomArticleNums);
        List randomArticleNumsSubset = randomArticleNums.subList(0, 100);
        // get new iterator to start from the beginning
        it = wiki.getArticles().iterator();
        // counter for article number
        int i = 0;
        // counter for number of articles selected 
        int m = 0;
        while(it.hasNext() && m < 100){
        	Page p = it.next();
        	if(randomArticleNumsSubset.contains(i)){
        		BufferedWriter out = new BufferedWriter(new OutputStreamWriter(
            	    new FileOutputStream(allDataDir+"article_"+m), "UTF-8"));
        		out.write("Title:" + p.getTitle()+"\n");
        		out.write("Id:" + p.getPageId()+"\n");
        		out.write(p.getPlainText());
        		out.close();
        		m++;
        	}
        	i++;
        }
	}
}

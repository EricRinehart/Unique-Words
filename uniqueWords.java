/*
   This program is the Java version of a Python program I wrote
   This program reads a .txt file and stores the unique words in a set
   An exception is thrown if no file is found
 */


import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashSet;
import java.util.Set;
import java.util.Scanner;


public class uniqueWords {
    
    public static void main(String[] args) throws FileNotFoundException {
        
        // Obtain file and extension from user to read
        System.out.print("Enter a file name with an extension: ");
        
        // Create Scanner object to perform operations on
        Scanner lookUp = new Scanner(System.in);
        File file = new File(lookUp.nextLine());
        Scanner read = new Scanner(file);

        // Create a set to contain unique words
        Set<String> unique = new HashSet<>();
        
        // Read file and...
        while (read.hasNext()) {
            // convert the word to lower case,
            // replace punctuation with whitespace, 
            // then trim whitespaces, 
            // and finally insert words into the set
            unique.add(read.next().toLowerCase().replaceAll("\\p{Punct}", "").trim());
        }
        // Iterate over the set to display each unique word
        for (String s : unique) {
            System.out.println(s);
        }
        // Close the read file
        read.close();
    }
}

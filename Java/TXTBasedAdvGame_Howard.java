// import java.util.*;
import java.util.Random;
import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;
// import java.io.ArrayList;

public class TXTBasedAdvGame_Howard {
    public static void main(String[] args) {
        //Restock Items then Gotta Dungeon aka. R.I.G.D just like Standard American Diet aka. S.A.D
        Scanner ui = new Scanner(System.in);
        Random rand = new Random();
    
        int account = 55;
        /*Python: itemList = []
          Java: List LISTNAME = new ArrayList();*/
        //https://www.geeksforgeeks.org/list-interface-java-examples/
        List <String> itemList = new ArrayList<>();
    
        while (account > 0){
            System.out.printf("Welcome to the R.I.G.D Item Shop You have $%d, What do you want to buy: ",account);
            System.out.print("armour: $35-$55, swords: $10-$25, shields: $40-15, firearms: $50-30, spells: $65-40: ");
            //https://stackoverflow.com/questions/34681199/change-user-input-to-lowercase
            String item = ui.nextLine().toLowerCase();  //the item will be set to all lowercase
    
            if (item.equals("armour")){     //if user asks for armour
                itemList.add(item);     //adds whatever item the user put in at the end of the list
                System.out.print("Would you like higher or lower quality? (high: $55 or low: $35): ");
                String qualityA = ui.nextLine().toLowerCase();  //quality for armour will be set to all lowercase
                if (qualityA.equals("high")){      //if the user asks for high quality
                    account -= 55;                 //charge them $55
                }
                else if (qualityA.equals("low")){  //if the user asks for low quality
                    account -= 35;                 //charge them 35$
                }
                System.out.printf("\nYou have $%s in your account\n",account);       //show user their new account total
            }
    
            if (item.equals("swords") || item.equals("sword")){  //if user asks for swords
                itemList.add(item);     //adds whatever item the user put in at the end of the list
                System.out.print("Would you like higher or lower quality? (high: $25 or low: $10-$15): ");
                String qualitySw = ui.nextLine().toLowerCase();  //quality for armour will be set to all lowercase
                if (qualitySw.equals("high")){      //if the user asks for high quality
                    account -= 25;                 //charge them $55
                }
                else if (qualitySw.equals("low")){  //if the user asks for low quality
                    for (int i=0; i<2;i++){        //loop once
                    int value = rand.nextInt(5)+10;    //randomly make them spend $10 or $15
                    account -= value;                 //charge them either $10 or $15$
                    }
                }
                System.out.printf("\nYou have $%s in your account\n",account);       //show user their new account total
            }

            if (item.equals("shield") || item.equals("shields")){     //if user asks for armour
                itemList.add(item);     //adds whatever item the user put in at the end of the list
                System.out.print("Would you like higher or lower quality? (high: $40 or low: $15): ");
                String qualitySh = ui.nextLine().toLowerCase();  //quality for armour will be set to all lowercase
                if (qualitySh.equals("high")){      //if the user asks for high quality
                    account -= 40;                 //charge them $40
                }
                else if (qualitySh.equals("low")){  //if the user asks for low quality
                    account -= 15;                 //charge them 15$
                }
                System.out.printf("You have $%s in your account\n",account);       //show user their new account total
            }
    
            if (item.equals("firearms") || item.equals("firearm")){  //if user asks for swords
                itemList.add(item);     //adds whatever item the user put in at the end of the list
                System.out.print("Would you like higher or lower quality? (high: $50 or low: $30): ");
                String qualityF = ui.nextLine().toLowerCase();  //quality for armour will be set to all lowercase
                if (qualityF.equals("high")){      //if the user asks for high quality
                    account -= 50;                 //charge them $50
                }
                else if (qualityF.equals("low")){  //if the user asks for low quality
                    account -= 30;                 //charge them 30$
                }
                System.out.printf("You have $%s in your account\n",account);       //show user their new account total
            }
            if (item.equals("spell") || item.equals("spells")){  //if user asks for swords
                itemList.add(item);     //adds whatever item the user put in at the end of the list
                System.out.print("Would you like higher or lower quality? (high: $65 or low: $40): ");
                String qualitySp = ui.nextLine().toLowerCase();  //quality for armour will be set to all lowercase
                if (qualitySp.equals("low")){  //if the user asks for low quality
                    System.out.printf("\nConsidering you selected a %s quality, it reminded me that we have a special deal that will upgrade the quality. So how about it? (y or n): ",qualitySp);
                    String newDeal = ui.nextLine().toLowerCase();  //quality for armour will be set to all lowercase
                    if (newDeal.equals("yes") || newDeal.equals("y")){
                        account -= 55;
                    }
                    else if (newDeal.equals("no") || newDeal.equals("n")){
                        account -= 40;
                    }
                }
                else if (qualitySp.equals("high")){      //if the user asks for high quality
                    account -= 65;                 //charge them $50
                }
                System.out.printf("You have $%s in your account\n",account);       //show user their new account total
            }

            System.out.println("Do you want to leave (y or n): ");
            String leave = ui.nextLine().toLowerCase();

            if (leave.equals("y") || leave.equals("yes")){
                System.out.printf("You said yes, are you sure?: (yes or no): ");
                String areYouSure = ui.nextLine().toLowerCase();

                if (areYouSure.equals("y") || areYouSure.equals("yes")){
                    System.out.printf("\nAlright since you said yes twice I guess you're free to go....\n\n\n");
                }
            }
        }
        System.out.println("    Thanks for the money, here are your items ");
        int i = 0;                                                      //initiating a variable so the wild loop can iterate through the list
        while (i < itemList.size()){                                    //loops through each item in the list
            System.out.println(toTitle(itemList.get(i)));               //prints out each item that has now gone through the Title proccess
            i++;                                                        //goes to the next item in the list
        }

        //https://www.geeksforgeeks.org/iterate-through-list-in-java/
        // for (int i = 0; i < itemList.size(); i++) {         // Loops through the list of Items

        //     // Print all elements of List
        //     System.out.println(itemList.get(i));            //Prints them Vertically and Formatted
        // }
        System.out.println("\n\nGo away now.\n");
        ui.close();
    }
    
    //https://www.baeldung.com/java-string-title-case
    public static String toTitle(String text) {
        if (text == null || text.isEmpty()) {       //if there is nothing in the parenthesis ()
            return text;                            //return nothing 
        }
    
        StringBuilder converted = new StringBuilder();  //like a list but it creates a string without all the brackets and commas
    
        boolean convertNext = true;
        for (char ch : text.toCharArray()) {
            if (Character.isSpaceChar(ch)) {        //if there is a space before the first actuall character
                convertNext = true;
            } else if (convertNext) {               //once it gets to the first letter character
                ch = Character.toTitleCase(ch);     //convert it to a Capital letter
                convertNext = false;
            } else {                                //the rest of the text
                ch = Character.toLowerCase(ch);     //make everything after the first letter Lowercase even if it is Uppercase
            }
            converted.append(ch);                   //creates the modified string
        }
    
        return converted.toString();                //function returns converted string
    }
}

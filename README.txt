README
To run either one of the files we just enter in terminal python <name_of_file_to_be_run> <testfile>


Functionality

letterLangId.py
The first question asked us to create a bigram model solely based on letters or to be more accurate character because we also accept whitespace into this bigram. The bigram models created for each language is then used to test what language a sentence is. The program made only 5 mistakes therefore getting an accuracy of 295/300 * 100 ~ 98.33%.
Yes it can be implemented without any smoothing because the number of letters available in a language is extremely limited and of a small finite amount unlike that of the number of words in a language. 


Algorithm:
-The algorithm is nearly the same for both except one we store the count of letters after a letter and the other we store the count of words after another word. 
-We create a dictionary of dictionaries. the key in the primary dictionary has a word/letter and in it's dictionary the key is the word/letter that comes after it and its value is the count. 
-We create a dictionary for each language. 
-Then on the test case we use the dictionary to calculate the probability of the next word occurring. 
-We multiply the probabilities and the dictionary with the highest one is the indicator of what language 

wordLangId 
As from before, it follows the same principle but uses words in the bigram model. Another important criteria is the usage of smoothing. We use add-one smoothing to further increase the accuracy given the number of unexpected words that can occur. The accuracy is surprisingly a little smaller 294/300 * 100  or 98%.
s
Analysis

I notice in my program that the letter predicting model has a higher accuracy but I believe that is because of the size of the model and the fact that there is a larger number of letters on our training set then words thereby giving a much accurate prediction. 

- The advantage of the second model is it saves a lot in processing and resources as it goes only by words whereas the first program needs to keep a count of each letter, thereby ensuring a larger amount of time on larger training sets. 
- The disadvantage of the first model is also a letter bigram has very limited advantages compared to the word bigram. Given the task of creating a word predictor it would make sense to use a word bigram model whereas a letter bigram model would offer too many unnecessary choices to choose from. 
- However for our given task the letter bigram model makes much more sense as the training set is quite small and also the testing set. However for larger models it is necessary to use the word bigram model 
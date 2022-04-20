// Write a Java, Javascript or Python program to do the following:
// o Replace all the vowels in the string “National Center for Supercomputing Applications” by their corresponding order number in alphabetical sequence (a with 1, e with 5, etc).
// o Print the resulting string.
// o Print the total number of consonants in the given string.

function change(str){
    return str.replace(/a/g, '1')
    .replace(/A/g, '1')
    .replace(/e/g, '5')
    .replace(/i/g, '9')
    .replace(/o/g, '15')
    .replace(/u/g, '21');
}

function consonantCount(str){
    var count = 0;
    var consonantNum = "bcdfghjklmnpqrstvwxzNCS";

    for (var i = 0; i < str.length; i++){
        if (consonantNum.indexOf(str[i]) > -1){
            count++;
        }
    }

    return "This string has " + count + " consonants";
}


console.log(change('National Center for Supercomputing Applications'));
console.log(consonantCount('National Center for Supercomputing Applications'));

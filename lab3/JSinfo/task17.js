// The answer is 2, that’s the first truthy value.

alert( null || 2 || undefined );



// The answer: first 1, then 2.
alert( alert(1) || 2 || alert(3) );

// The call to alert does not return a value. Or, in other words, it returns undefined.

// The first OR || evaluates its left operand alert(1). That shows the first message with 1.
// The alert returns undefined, so OR goes on to the second operand searching for a truthy value.
// The second operand 2 is truthy, so the execution is halted, 2 is returned and then shown by the outer alert.
// There will be no 3, because the evaluation does not reach alert(3).

// The answer: null, because it’s the first falsy value from the list.
alert(1 && null && 2);

// The answer: 1, and then undefined.

alert( alert(1) && alert(2) );

//The answer: 3.
alert( null || 2 && 3 || 4 );



//Write an if condition to check that age is between 14 and 90 inclusively.

// “Inclusively” means that age can reach the edges 14 or 90.

if (age >= 14 && age <= 90)


// Write an if condition to check that age is NOT between 14 and 90 inclusively.

// Create two variants: the first one using NOT !, the second one – without it.



// Runs.
// The result of -1 || 0 = -1, truthy
    if (-1 || 0) alert( 'first' );

// Doesn't run
// -1 && 0 = 0, falsy
if (-1 && 0) alert( 'second' );

// Executes
// Operator && has a higher precedence than ||
// so -1 && 1 executes first, giving us the chain:
// null || -1 && 1  ->  null || 1  ->  1
if (null || -1 && 1) alert( 'third' );






let userName = prompt("Who's there?", '');

if (userName === 'Admin') {

    let pass = prompt('Password?', '');

    if (pass === 'TheMaster') {
        alert( 'Welcome!' );
    } else if (pass === '' || pass === null) {
        alert( 'Canceled' );
    } else {
        alert( 'Wrong password' );
    }

} else if (userName === '' || userName === null) {
    alert( 'Canceled' );
} else {
    alert( "I don't know you" );
}
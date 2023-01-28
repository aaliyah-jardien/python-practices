//five steps to make unit tests and tdd easy
//1. decide on end goal of function (inputs and outputs)
//2. choose func signature (parameters, return values)
//3. decide on one aspect of functionality (instead of thinking about everything,focus on one)
//4. implement test
//5. implement code 

//wrinting a test that will check if the password is strong or not
//calling the function
var_strong = 'strongPassword'("Password string goes here");

//What is the smallest amount of code we can add to bring the function closer to working?

//The very simplest rule for password strength might be the empty password. That's really easy, the output should always be false when the password is empty.
//How the function behaves is what we want to test.
//step 4, implementing test
//Once you start testing behavior under some conditions (such as certain parameters,time of day, whatever), testing becomes a lot easier, because we can look atbehavior from the outside. 

//We decided....
//- the function takes a password as its only parameter
//- it returns a boolean to indicate whether the password was strong or not.
//- for an empty password, the result should always be false, to indicate an empty password is weak.

describe('strong_password', function()){
    it("should give negative result for empty string", function()){
        password = '';
        result = strong_password(password);
        expect(result).to.be.false;
    });
});
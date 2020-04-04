function golf(par, strokes) {
	if (strokes == 1) {
		return name;
	}
}

function caseInSwitch(val) {
	var answer = ""
	switch(val) {
		case 1:
			answer = "alpha";
			break;
		case 2:
			answer = "beta";
			break;
	}
	return answer;
}

function caseInSwitch2(val) {
	var answer = ""
	switch(val) {
		case 1:
		case 2:
		case 3:
			answer = "Low";
			break;
		case 4:
		case 5:
		case 6:
			answer = "High";
			break;
	}
	return answer;
}

function abTest(a,b) {
	if (a < 0 || b < 0 ) {
		return undefined;
	}
	return Math.round(Math)
}


var OurDog = {
	"name" : "Potato"
	"friends": ["everything!"]
};

var myDog = {
	"name": "Turnip"
	"friends": []
};

myDog.bark = "woof";
myDog['bark'] = "arf";

delete myDog.bark;


var lookup = {
	"alpha" : "Adams",
	"bravo" : "Boston",
};

result = lookup[val]

var myObj = {
	gift: "pony"
}

function checkObj(checkProp) {
	if (myObj.hasOwnPropery(checkProp)) {
		return myObj[checkProp]
	}
}

funcion lookUpProfile(name, prop) {
	for (var i =0; i < contacts.length; i ++) {

	if ([contacts[i].firstName] === "name") {
		return contacts[i][prop] || "Not found"
	}
  }

	return "Not found";
}

Math.random();

var randomNumberBetween0and10 = Math.floor(Math.random() * 11);

function checkEqual(a,b) {
	return a === b ? true: false;
}

function checkSign(num) {
	return num < 0 ? "positive" : num < 0 ? "negative" : "zero"
}

const squaredInts = arr.filter(num => Number.IsInteger(num) && num > 0). map(x => x *x);

const increment = (function()) {
	return function increment(number, value = 1) {
		return number + value 
	}
}

return function sum(...args) {

}

const { x : a, b : y} = voxel; // quicker way to assign things from object to variables

const source = [1,2,3];
fuction removeTwo(list) {
	const [ , ,...arr = list;  //DO nothing for 1st and 2nd element

	return arr;
}

const greeting = `Hello, my name is ${person.name}`;

const createPerson = (name, age, gender) => {

	return {
		name: name,
		age: age,
		gender: gender
	};
}

const createPerson = (name, age, gender) => ({ name, age, gender});


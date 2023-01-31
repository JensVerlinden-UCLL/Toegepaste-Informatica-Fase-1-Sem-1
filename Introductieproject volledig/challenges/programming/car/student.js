function myFirstFunction(bike) {
    forward(bike);
}

function twiceForward(bike) {
    forward(bike);
    forward(bike);
}

function thriceForward(bike) {
    forward(bike);
    forward(bike);
    forward(bike);
}

function forward4(bike) {
    forward(bike);
    forward(bike);
    forward(bike);
    forward(bike);
}

function forward5(bike) {
    let i = 5

    while (i>0) {
        forward(bike);
        i = i - 1
    }
}

function forward10(bike) {
    let i = 10

    while (i>0) {
        forward(bike);
        i = i - 1
    }
}

function right(bike) {
    turnRight(bike);
    forward(bike);
}

function ellShape(bike) {
    forward5(bike);
    turnRight(bike);
    forward4(bike);
}

function uTurn(bike) {
    thriceForward(bike);
    turnRight(bike);
    forward10(bike);
    turnRight(bike);
    twiceForward(bike);
}

function forwardN(bike, steps) {
    let i = steps;

    while (i > 0) {
        forward(bike);
        i = i - 1;
    }
}

function crookedUTurn(bike){
    forwardN(bike, 7);
    turnRight(bike);
    forwardN(bike, 9);
    turnRight(bike);
    forwardN(bike, 3);
}

function forwardUntilWall(bike){
    while (!sensor(bike)) {
        forward(bike);
    }
}

function smartEllShape(bike){
    forwardUntilWall(bike);
    turnRight(bike);
    forwardUntilWall(bike);
}

function spiral(car) {
    while (!sensor(car)){
        forwardUntilWall(car);
        turnRight(car);
    }
}

function turnLeft(car) {
    let i = 3;

    while (i>0) {
        turnRight(car);
        i = i - 1;
    }
}

function left(car) {
    turnLeft(car);
    forwardUntilWall(car);
}

function slalom(car){
    forwardUntilWall(car);
    turnLeft(car);
    forwardUntilWall(car);
    turnRight(car);
    forwardUntilWall(car);
    turnRight(car);
    forwardUntilWall(car);
    turnLeft(car);
    forwardUntilWall(car);
    turnLeft(car);
    forwardUntilWall(car);
    turnRight(car);
    forwardUntilWall(car);
    turnRight(car);
    forwardUntilWall(car);
}

function rightOrLeft(car){
    turnRight(car);
    if (sensor(car)){
        turnRight(car);
        turnRight(car);
    }
}

function leftOrRight(car){
    rightOrLeft(car);
    forwardUntilWall(car);
    rightOrLeft(car);
    forwardUntilWall(car);
}

function incompleteU(car){
    forwardUntilWall(car);
    turnRight(car);
    forwardUntilWall(car);
    turnRight(car);
    forwardUntilWall(car);
    turnRight(car);
}

function whichDirection(car){
    while (sensor(car)){
        turnRight(car);
    }
    forwardUntilWall(car);
}

function sensorRight(car) {
    turnRight(car);
    let result = sensor(car);
    turnLeft(car);

    return result;
}
function forwardUntilFreeRight(car) {
    while (sensorRight(car)) {
        forward(car);
    }
}

function firstRight(car) {
    forwardUntilFreeRight(car);
    turnRight(car);
    forwardUntilWall(car);
}

function sensorLeft(car) {
    turnLeft(car);
    let result = sensor(car);
    turnRight(car);

    return result;
}

function forwardUntilFreeLeft(car) {
    while (sensorLeft(car)) {
        forward(car);
    }
}

function firstLeft(car) {
    forwardUntilFreeLeft(car);
    turnLeft(car);
    forwardUntilWall(car);
}

function zigZag(car){
    firstRight(car);
    turnLeft(car);
    forward(car);
    firstLeft(car);
}

function secondRight(car){
    forwardUntilFreeRight(car);
    forward(car);
    firstRight(car);
}

function thirdRight(car){
    forwardUntilFreeRight(car);
    forward(car);
    forwardUntilFreeRight(car);
    forward(car);
    firstRight(car);
}

function nthRight(car, nrights){
    let i = nrights -1;
    while (i>0){
        forwardUntilFreeRight(car);
        forward(car);
        i = i -1        
    }
    firstRight(car);
}

function fourthRight(car){
    nthRight(car, 4);
}

function nthLeft(car, nlefts){
    let i = nlefts -1;
    while (i>0){
        forwardUntilFreeLeft(car);
        forward(car);
        i = i -1        
    }
    firstLeft(car);
}

function fifthLeft(car){
    nthLeft(car, 5);
}

function forwardUntilNthLeft(car, nlefts) {
    let i = nlefts;

    while (i > 0) {
        forward(car);

        if (!sensorLeft(car)) {
            i = i - 1;
        }
    }
}

function forwardUntilNthRight(car, nrights) {
    let i = nrights;

    while (i > 0) {
        forward(car);

        if (!sensorRight(car)) {
            i = i - 1;
        }
    }
}

function leftCorner(car){
    turnLeft(car);
    forward(car);
}

function rightCorner(car){
    turnRight(car);
    forward(car);
}


function maze(car){
    forwardUntilNthRight(car, 2);
    rightCorner(car);
    forwardUntilFreeLeft(car);
    leftCorner(car);
    forwardUntilNthLeft(car, 2);
    leftCorner(car);
    forwardUntilNthLeft(car, 2);
    leftCorner(car);
    forwardUntilNthRight(car, 4);
    rightCorner(car);
    forwardUntilFreeRight(car);
    rightCorner(car);
    nthLeft(car, 3);
}

function isDeadEnd(car) {
    if (!sensor(car)) {
        return false;
    }

    if (!sensorRight(car)) {
        return false;
    }

    if (!sensorLeft(car)) {
        return false;
    }

    return true;
}

function backward(car) {
    turnRight(car);
    turnRight(car);
    forward(car);
    turnRight(car);
    turnRight(car);
}

function findDeadEnd(car) {
    while (!isDeadEnd(car)) {
        forward(car);
        if (isDeadEnd(car)) {
            break ;
        }
        backward(car);
        turnLeft(car);
    }
}

function follow(car){
    while (!isDeadEnd(car)) {
        if (!sensor(car)) {
            forward(car);
        } else if (!sensorRight(car)) {
            turnRight(car);
            forward(car);
        } else {
            turnLeft(car);
            forward(car);
        }
    }
}

function rightHand(car){
    while (!isDeadEnd(car)) {
        if (!sensorRight(car)) {
            turnRight(car);
            forward(car);
        } else if (!sensor(car)) {
            forward(car);
        } else {
            turnLeft(car);
            forward(car);
        }
    }
}

function forwardUntilDestination(car){
    while(!destinationReached(car)){
        forward(car)
    }
}

function stop(car) {
    if (sensor(car)) {
        return true;
    }

    else if (destinationReached(car)) {
        return true;
    }

    else return false;
}

function clearRow(car) {
    while (!stop(car)) {
        forward(car);
    }
}

function roomba(car) {
    while (!destinationReached(car)) {
        clearRow(car)
        if (destinationReached(car)){
            break
        }
        turnRight(car);
        forward(car);
        turnRight(car);
        clearRow(car)
        if (destinationReached(car)){
            break
        }
        turnLeft(car);
        forward(car);
        turnLeft(car);
    }

}

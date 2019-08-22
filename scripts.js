function mappy() {
    var noteMap = new Map([
    [21, "A"], [22 , "A#"], [23, "B"], [24, "C"], [25, "C#"], [26, "D"],
    [27, "D#"], [28 , "E"], [29, "F"], [30, "F#"], [31, "G"], [32, "G#"]]); 
    var note = noteMap.get(28);
    document.getElementById("h").innerHTML = note;
}

function testScale() {
    var keyScale = 4;
    var acceptables = [-9, -7, -6, -5, -2, 0, 3, 5, 6, 7, 10]
    var validNotes = [];
    for(var i = 0; i < acceptables.length; i++) {
        if(keyScale + acceptables[i] >= 0 && keyScale + acceptables[i] <= 11) {
        validNotes.push(keyScale + acceptables[i]);
        }
    }
    document.getElementById("h").innerHTML = validNotes;
}

function testMod() {
    var mod = 3.8 % 1;
    document.getElementById("h").innerHTML = mod;

}

function saveKey() { 
    var noteMap = new Map([
    ['C', 0], ['C#', 1], ['D', 2], ['D#', 3], ['E', 4], ['F', 5],
    ['F#', 6], ['G', 7], ['G#', 8], ['A', 9], ['A#', 10], ['B', 11]]); 
    var keyyy = document.getElementById("keyInput").value;
    var note = noteMap.get(keyyy);
    sessionStorage.setItem("noteKey", note);
    //test note:
    //document.getElementById("output").innerHTML = note;
}

function saveBPM() { 
    var bpm = parseInt(document.getElementById("bpmInput").value);
    sessionStorage.setItem("bpmKey", bpm);
    //test bpm:
    //document.getElementById("output").innerHTML = bpm;
}

function readFolder() {
    alert("Start Achieved");
    let midiParser = require('midi-parser-js');
    const fs = require('fs');
    var directory = './Midi/Classical';
    alert("Finished variables");
    fs.readdir(directory, (err, files) => {
        alert(6);
        if(err) {
            console.log("Couldn't read folder");
        }
        else {
            alert(5);
            fs.readFile('./Midi/Classical/'+files[0], (err, data) => {
                if(err) {
                    console.log("Couldn't read file");
                }
                midiParser.parse(source, function(obj){
                    sessionStorage.setItem("myJSON", JSON.stringify(obj, undefined, 2));
                    document.getElementById("output").innerHtml = sessionStorage.getItem("myJSON"); 
                });
                console.log(data);
            });
            console.log('file ' + files[0]);
        }
    });
}

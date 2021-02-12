"use strict";

let konto_1 = {
    iban: "DE34556234523",
    bic: "WESEPDKAX",
    inhaber: {
        vorname: "Hans",
        nachname: "Meier",
        geschlecht: "männlich",
        alter: 85 
    },
    kontostand: 3500,
    aktiv: true
};


let konto_2 = {
    iban: "DE34556234555",
    bic: "WESEPDKAX",
    inhaber: {
        vorname: "Gertrude",
        nachname: "Linkmeier",
        geschlecht: "weiblich",
        alter: 55 
    },
    kontostand: 5500,
    aktiv: true
};

let wert_1 = konto_1["iban"];
console.log(wert_1);

let wert_2 = konto_1["inhaber"]["geschlecht"];
console.log(wert_2);

konto_2["abhebelimit"] = 1000;
console.log(konto_2["abhebelimit"]);

konto_1["kontostand"] = 3000;
console.log(konto_1["kontostand"]);

let eigentschaft = "iban";
let wert_3 = konto_1[eigentschaft];
console.log(wert_3);


/*
let wert_1 = konto_1.iban;
console.log(wert_1);

let wert_2 = konto_1.bic;
console.log(wert_2);

let wert_3 = konto_1.inhaber.vorname;
console.log(wert_3);


console.log(`${konto_1.inhaber.vorname} ${konto_1.inhaber.nachname} hat ${konto_1.kontostand}€ auf seinem Konto.`)

konto_1.abhebelimit = 1000;
console.log(konto_1);
console.log(konto_1.abhebelimit);


konto_1.kontostand = 3000;
console.log(konto_1.kontostand);
*/
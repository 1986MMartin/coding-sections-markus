"use strict";
/*
let inhaber_1 = {
    vorname: "Hans",
    nachname: "Meier",
    geschlecht: "männlich",
    alter: 85 
};

let inhaber_2 = {
    vorname: "Gertrude",
    nachname: "Linkmeier",
    geschlecht: "weiblich",
    alter: 55 
};

let konto_1 = {
    iban: "DE34556234523",
    bic: "WESEPDKAX",
    inhaber: inhaber_1,
    kontostand: 3500,
    aktiv: true
};

console.log(konto_1);

let konto_2 = {
    iban: "DE34556234555",
    bic: "WESEPDKAX",
    inhaber: inhaber_2,
    kontostand: 5500,
    aktiv: true
};

console.log(konto_2);

console.log("-----------------------------------")
*/

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

console.log(konto_1);

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

console.log(konto_2);
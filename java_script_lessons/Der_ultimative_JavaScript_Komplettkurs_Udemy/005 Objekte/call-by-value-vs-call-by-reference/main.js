"use strict";

let meine_variable = "Markus";
let mein_objekt = {
    zahl: 5000
};

const meine_funktion = function(v, o) {
    v = "Martin"
    o.zahl = 2500;
};

meine_funktion(meine_variable, mein_objekt);

console.log(meine_variable);
console.log(mein_objekt.zahl);


let konto = {
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

const funktion_einzahlung = function(betrag, objekt) {
    objekt.kontostand = objekt.kontostand + betrag;
    // alternativ geht auch "objekt.kontostand += betrag"
};

funktion_einzahlung(1000, konto);
console.log(konto.kontostand)

const funktion_ausszahlung = function(betrag, objekt) {
    objekt.kontostand = objekt.kontostand - betrag;
};

funktion_ausszahlung(2000, konto);
console.log(konto.kontostand)
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

const kontostand_ausgeben = function(konto) {
    console.log(`${konto.inhaber.vorname} ${konto.inhaber.nachname} hat ${konto.kontostand}€ auf seinem Konto.`)
};
kontostand_ausgeben(konto_1);
kontostand_ausgeben(konto_2);
"use strict";

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
    aktiv: true,
    einzahlen(e) {
        this.kontostand += e
    },
    auszahlung(a) {
        this.kontostand -= a
    }
};

konto.einzahlen(500);
console.log(konto.kontostand);

// -----------------------------------------------------------

let person = {
    vorname: "Max",
    nachname: "Mustermann",
    alter: 18,
    verarbeiten() {
        return {
            n: `${this.vorname} ${this.nachname}`,
            z: `${this.vorname} ${this.nachname} (${this.alter} Jahre)`,
            b: `Hallo ${this.vorname} ${this.nachname}!`,
        };
    }
};

console.log(person.verarbeiten());


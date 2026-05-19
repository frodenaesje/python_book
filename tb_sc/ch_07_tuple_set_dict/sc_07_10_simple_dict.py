
def vis_alle_studenter(studenter: dict) -> None:
    print("\n=== Alle studenter ===")
    if not studenter:
        print("(ingen studenter registrert)")
    else:
        for navn in sorted(studenter):
            print("-", navn)
    print("======================\n")


def vis_kurs_for_student(studenter: dict) -> None:
    navn = input("Skriv studentens navn: ").strip()
    kursmap = studenter.get(navn)
    if kursmap is None:
        print("Fant ikke studenten.")
        return

    print(f"\nKurs for {navn}:")
    if not kursmap:
        print("(ingen kurs registrert enda)")
    else:
        for kurskode, karakter in sorted(kursmap.items()):
            print(f"{kurskode} -> {karakter}")
    print()


def legg_til_kurs_for_student(studenter: dict) -> None:
    navn = input("Studentens fulle navn: ").strip()
    if not navn:
        print("Navn kan ikke være tomt.")
        return

    # Opprett studenten hvis han/hun ikke finnes
    if navn not in studenter:
        studenter[navn] = {}
        print(f"Opprettet ny student: {navn}")

    kurskode = input("Kurskode (f.eks INF100): ").strip().upper()
    if not kurskode:
        print("Kurskode kan ikke være tom.")
        return

    karakter = input("Karakter (A-F eller Bestått/Ikke bestått): ").strip().upper()
    if not karakter:
        print("Karakter kan ikke være tom.")
        return

    # Legg inn/oppdater karakter
    tidligere = studenter[navn].get(kurskode)
    studenter[navn][kurskode] = karakter

    if tidligere is None:
        print(f"La til {kurskode} -> {karakter} for {navn}.")
    else:
        print(f"Oppdaterte {kurskode}: {tidligere} -> {karakter} for {navn}.")


def vis_datastruktur(studenter: dict) -> None:
    print("\n=== Rå datastruktur (dict) ===")
    print(studenter)
    print("================================\n")


def meny() -> None:
    # Initielt dictionary med noen data
    studenter = {
        "Ola Nordmann": {
            "INF100": "B",
            "MAT110": "A",
        },
        "Kari Nordmann": {
            "DAT200": "C",
        },
        "Per Hansen": {
            "STAT101": "Bestått",
        },
    }

    while True:
        print("MENY:")
        print("1) List alle studenter")
        print("2) Vis kurs/karakterer for én student")
        print("3) Legg til/oppdater kurs og karakter for en student")
        print("4) Vis rå datastruktur (dict)")
        print("5) Avslutt")

        valg = input("Velg (1-5): ").strip()

        if valg == "1":
            vis_alle_studenter(studenter)
        elif valg == "2":
            vis_kurs_for_student(studenter)
        elif valg == "3":
            legg_til_kurs_for_student(studenter)
        elif valg == "4":
            vis_datastruktur(studenter)
        elif valg == "5":
            print("Avslutter …")
            break
        else:
            print("Ugyldig valg, prøv igjen.")
        input("Trykk Enter for å fortsette ...\n")


if __name__ == "__main__":
    meny()

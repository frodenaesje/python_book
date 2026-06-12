from datetime import datetime, timedelta
from pathlib import Path

# --- Konstanter og filstier ---
DISTANSE_KM = 5
FARTSGRENSE_KMT = 60
# Mer lesbart enn å regne timer: 5 km / 60 km/t = 5 minutter
MIN_TID = timedelta(minutes=5)

# Alle filer ligger i samme mappe som denne koden
# Pass på at du legger .txt filene der også
BASE_DIR = Path(__file__).resolve().parent
BOX_A_FILE = BASE_DIR / "box_a.txt"
BOX_B_FILE = BASE_DIR / "box_b.txt"
VEHICLE_FILE = BASE_DIR / "vehicles.dat"


# --- Klasser ---
class SpeedTicket:
	"""Representerer en registrert fartsoverskridelse."""

	def __init__(self, timestamp_A, timestamp_B, speed):
		self._timestamp_A = timestamp_A
		self._timestamp_B = timestamp_B
		self._speed = speed

	# vi definerer __eq__ for å kunne sjekke om en fartsbot allerede er registrert
	# Brukes av in operatoren i Vehicle.add_speed_ticket
	def __eq__(self, other):
		if not isinstance(other, SpeedTicket):
			return False
		return self._timestamp_A == other._timestamp_A and self._timestamp_B == other._timestamp_B

	def as_line(self):
		sA = self._timestamp_A.strftime("%Y-%m-%d %H:%M:%S")
		sB = self._timestamp_B.strftime("%Y-%m-%d %H:%M:%S")
		return f"A: {sA}  B: {sB}  fart: {self._speed:.1f} km/t"


class Vehicle:
	
	def __init__(self, regnr, merke, modell, modellaar, kilometerstand, pris):
		self._regnr = regnr.upper()
		self._merke = merke
		self._modell = modell
		self._modellaar = modellaar
		self._kilometerstand = kilometerstand
		self._pris = pris
		self._speed_tickets = []  # liste av SpeedTicket

	def add_speed_ticket(self, tA, tB, speed):
		ticket = SpeedTicket(tA, tB, speed)
		if ticket not in self._speed_tickets:
			self._speed_tickets.append(ticket)

	def report(self):
		if not self._speed_tickets:
			return "Ingen registrerte fartsoverskridelser."
		lines = [f"-- {self._regnr} ({len(self._speed_tickets)} treff) --"]
		for idx, ticket in enumerate(self._speed_tickets, 1):
			lines.append(f"{idx:2d}) {ticket.as_line()}")
		return "\n".join(lines)

	def __str__(self):
		base = (
			f"{self._regnr}: {self._merke} {self._modell} "
			f"({self._modellaar}), {self._kilometerstand} km, NOK {self._pris}"
		)
		if self._speed_tickets:
			return base + f"  ! {len(self._speed_tickets)}"
		return base


# --- Lagring ---
def load_vehicles():
	if not VEHICLE_FILE.exists():
		return {}
	try:
		import pickle

		with VEHICLE_FILE.open("rb") as fh:
			data = pickle.load(fh)
		if isinstance(data, dict):
			return data
	except Exception:
		pass
	return {}


def save_vehicles(vehicles):
	import pickle

	with VEHICLE_FILE.open("wb") as fh:
		pickle.dump(vehicles, fh)


# --- Hjelpere ---

def read_log(path):
	# TODO implementer denne funksjonen, se hint i oppgaveteksten

# hjelpefunksjoner for å finne fartsoverskridelser
# TODO: implementer nødvendige hjelpefunksjoner


def check_speeding_for_vehicle(vehicle, passA, passB):
	# TODO: implementer denne funksjonen, se hint i oppgaveteksten

def check_all_vehicles(vehicles, passA, passB):
	added = 0
	for v in vehicles.values():
		added += check_speeding_for_vehicle(v, passA, passB)
	return added

# --- Enkle menyvalg ---
def list_vehicles(vehicles):
	if not vehicles:
		print("Ingen kjøretøy registrert.")
		return
	print("\n-- Alle kjøretøy --")
	for reg in sorted(vehicles):
		print(vehicles[reg])


def add_vehicle(vehicles, passA, passB):
	
	# TODO: fullfør denne funksjonen (se slutten)
	regnr = input("Registreringsnummer: ").strip().upper()
	if not regnr:
		print("Regnr kan ikke være tomt.")
		return
	if regnr in vehicles:
		print("Dette regnr finnes allerede.")
		return
	merke = input("Merke: ").strip()
	modell = input("Modell: ").strip()
	try:
		modellaar = int(input("Modellår: "))
		kilometerstand = int(input("Kilometerstand: "))
		pris = int(input("Pris (NOK): "))
	except ValueError:
		print("Ugyldig tall.")
		return

	vehicle = Vehicle(regnr, merke, modell, modellaar, kilometerstand, pris)
	vehicles[regnr] = vehicle
	# TODO: Kall check_speeding_for_vehicle for å sjekke fartsoverskridelser ved opprettelse
	
	


def show_tickets_for_vehicle(vehicles):
	reg = input("Vis fartsoverskridelser for regnr: ").strip().upper()
	v = vehicles.get(reg)
	if not v:
		print("Fant ikke kjøretøyet.")
		return
	print(v.report())


def show_menu():
	print(
		"\n"
		"1) List alle\n"
		"2) Legg til\n"
		"3) Vis fartsoverskridelser for et kjøretøy\n"
		"4) Lagre\n"
		"5) Avslutt"
	)


def main():
	vehicles = load_vehicles()
	passA = read_log(BOX_A_FILE)
	passB = read_log(BOX_B_FILE)

	new_found = check_all_vehicles(vehicles, passA, passB)
	if new_found:
		print(f"! Ved oppstart ble det funnet {new_found} fartsoverskridelse(r) i loggene.")

	while True:
		show_menu()
		try:
			choice = int(input("Velg 1-5: ").strip())
		except ValueError:
			print("Ugyldig valg.")
			continue

		if choice == 1:
			list_vehicles(vehicles)
		elif choice == 2:
			add_vehicle(vehicles, passA, passB)
		elif choice == 3:
			show_tickets_for_vehicle(vehicles)
		elif choice == 4:
			save_vehicles(vehicles)
			print("Lagret.")
		elif choice == 5:
			save_vehicles(vehicles)
			print("Avslutter.")
			break
		else:
			print("Velg et tall 1-5.")
		input("\nEnter for å fortsette...")


if __name__ == "__main__":
	main()


from datetime import datetime, timedelta
from pathlib import Path
import pickle

# --- Konstanter og filstier ---
DISTANSE_KM = 5
FARTSGRENSE_KMT = 60
# Mer lesbart enn å regne timer: 5 km / 60 km/t = 5 minutter
MIN_TID = timedelta(minutes=5)

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
	"""Minimal representasjon av et kjøretøy og fartsoverskridelser."""

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
		with VEHICLE_FILE.open("rb") as fh:
			data = pickle.load(fh)
		if isinstance(data, dict):
			return data
	except Exception:
		pass
	return {} # returner tom dict ved feil eller manglende fil


def save_vehicles(vehicles):
	with VEHICLE_FILE.open("wb") as fh:
		pickle.dump(vehicles, fh)


# --- Hjelpere ---

def read_log(path):
	"""Les fil i formatet "REGNR, YYYY-MM-DD HH:MM:SS" 
	På bakgrunn av dette bygger vi en dictionary:
	{ regnr: [tidsstempel1, tidsstempel2, ...], ... }
	Hopper over linjer som ikke matcher formatet.
	"""
	result = {}
	if not path.exists():
		return result
	with path.open("r", encoding="utf-8") as f:
		for line in f:
			line = line.strip()
			if not line or "," not in line:
				continue
			reg, ts = line.split(",", 1)
			reg = reg.strip().upper()
			try:
				t = datetime.strptime(ts.strip(), "%Y-%m-%d %H:%M:%S")
			except ValueError:
				continue
			result.setdefault(reg, []).append(t)
	for reg in result:
		result[reg].sort()
	return result

def avg_speed_kmt(distance_km, travel):
	hours = travel.total_seconds() / 3600.0
	if hours <= 0:
		return float("inf")
	return distance_km / hours

def pair_first_after(a_times, b_times):
	#Aller enkleste kobling: for hvert A-tidspunkt, finn første B >= A.
	
	pairs = []
	for tA in a_times:
		for tB in b_times:
			if tB >= tA:
				pairs.append([tA, tB])
				break
	return pairs

def check_speeding_for_vehicle(vehicle, passA, passB):
	reg = vehicle._regnr
	if reg not in passA or reg not in passB:
		return 0
	before = len(vehicle._speed_tickets)
	for tA, tB in pair_first_after(passA[reg], passB[reg]):
		travel = tB - tA
		if travel < MIN_TID:
			speed = avg_speed_kmt(DISTANSE_KM, travel)
			vehicle.add_speed_ticket(tA, tB, speed)
	return len(vehicle._speed_tickets) - before

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
	added = check_speeding_for_vehicle(vehicle, passA, passB)
	if added:
		print(f"! Fant {added} fartsoverskridelse(r) i loggene.")
	print("Kjøretøy lagt til.")


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
	# toppstruktur: en dict av { regnr: Vehicle, ... }
	# vi forsøker å laste denne fra fil ved oppstart
	# load_vehicles returnerer en tom dict ved feil eller manglende fil
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


# Oppgave 21.02: Forelderreferanser i BST-noder


Bruk denne startfila:
- ex_21_02_parent_ref_start.py

## Oppgave
Vi skal introdusere en foreldrepeker i Node klassen til et binært søketre.  
Startkoden du har tilgjengelig er ganske lik koden til Liang fra kapittel 21,
men er noe mer pythonic.  
Gjør deg kjent med koden; - det er lagt inn hint som skal gjøre det greit å løse oppgaven

Det du skal gjøre:
1. Legg til en `parent`-attributt i `Node`.
2. Oppdater `insert()` slik at `parent` settes når et barn kobles inn.
3. Implementer `is_leaf(self, key) -> bool`.
   - Finn noden med `find(key)`.
   - Hvis noden ikke finnes: returner `False`.
   - En løvnode er en node uten barn, altsa `left is None` og `right is None`.
4. Implementer `get_path(self, key) -> list[int]`:
   - Returner verdier fra funnet node opp til rota.
   - Hvis key ikke finnes, returner en tom liste.
   - Bruk parent-pekerne til a gå oppover i treet.
5. Oppdater `delete()` slik at foreldrereferanser forblir korrekte etter omkobling av noder.

## Forventet oppforsel
- `is_leaf(20)` er True hvis node 20 ikke har barn.
- `get_path(40)` kan for eksempel returnere `[40, 30, 50]`, avhengig av treets struktur.
- Etter sletting skal parent-lenker fortsatt vere konsistente.

## Testkode
- Det ligger kode i main() som skal fungere etter att du har satt inn dine kodelinjer

## Notater
- I startkoden brukes `from __future__ import annotations` for a utsette evaluering av typeannotasjoner.
- Det gjør at vi kan skrive typer som `Node | None` direkte uten anførselstegn, selv når typen refererer til klassen vi er i ferd med å definere.
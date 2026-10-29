# Kurs Git & GitHub

Repozytorium szkoleniowe poświęcone praktycznej nauce systemu kontroli wersji Git oraz platformy GitHub, wspierane lokalnym asystentem AI (**Aider + Qwen 2.5 Coder 14B**).

---

## 🚀 Szybki start z Git

### 1. Podstawowy cykl pracy

```bash
# Sprawdzenie stanu repozytorium
git status

# Dodanie zmienionych plików do poczekalni (staging)
git add plik.txt
git add .

# Zatwierdzenie zmian z czytelnym opisem
git commit -m "feat: dodano plik powitalny"

# Wysłanie zmian do zdalnego repozytorium
git push origin main

```

### 2. Praca na gałęziach (Branches)

```bash
# Utworzenie i przejście na nową gałąź
git switch -c feature/nazwa-funkcji

# Podgląd dostępnych gałęzi
git branch -a

# Powrót do gałęzi głównej i scalenie zmian
git switch main
git merge feature/nazwa-funkcji

# Usunięcie niepotrzebnej gałęzi lokalnej
git branch -d feature/nazwa-funkcji

```

### 3. Diagnostyka i historia

```bash
# Czytelny, jednolinijkowy log z grafem
git log --oneline --graph --all

# Podgląd wprowadzonych modyfikacji
git diff

```

---

## 🤖 Praca z lokalnym agentem AI (Aider)

Projekt wykorzystuje lokalnego agenta programistycznego **Aider**, który współpracuje z modelem **Qwen 2.5 Coder 14B** uruchamianym na GPU (Ollama) w architekturze Windows + WSL2.

### 1. Wymagania przed startem

Upewnij się, że silnik Ollama na hoście Windows nasłuchuje na wszystkich interfejsach:

```powershell
# W terminalu PowerShell na Windowsie:
$env:OLLAMA_HOST="0.0.0.0"
ollama serve

```

W pliku `~/.aider.conf.yml` w WSL skonfiguruj stałe połączenie:

```yaml
model: ollama/qwen2.5-coder:14b
openai-api-base: [http://172.22.192.1:11434/v1](http://172.22.192.1:11434/v1)
check-update: false
show-model-warnings: false
chat-language: Polish
auto-commits: false
attribute-author: false
map-tokens: 2048

```

Uruchomienie asystenta z poziomu katalogu projektu w WSL:

```bash
cd ~/projekty/Kurs-Git-Github
aider

```

---

### 2. Kluczowe komendy Aidera

| Komenda             | Opis                                                                            |
| ------------------- | ------------------------------------------------------------------------------- |
| `/add <plik>`       | Dodaje plik do sesji edycyjnej (model może go bezpośrednio modyfikować).        |
| `/drop <plik>`      | Usuwa plik z kontekstu (zwalnia pamięć VRAM i przestrzeń tokenów).              |
| `/read-only <plik>` | Dodaje plik referencyjny (dokumentacja, API) – model go czyta, ale nie zmienia. |
| `/web <url>`        | Pobiera treść strony/dokumentacji z sieci i ładuje do pamięci modelu.           |
| `/run <polecenie>`  | Wykonuje polecenie shella w WSL i automatycznie przekazuje wynik/błąd do czatu. |
| `/ls`               | Wyświetla listę plików aktualnie dodanych do kontekstu.                         |
| `/undo`             | Cofa ostatnią modyfikację kodu wykonaną przez agenta.                           |
| `/clear`            | Czyści historię rozmowy, zachowując dodane pliki.                               |
| `/exit`             | Zakończenie pracy agenta.                                                       |

---

### 3. Scenariusze i szablony promptów

#### A. Tworzenie nowego kodu od zera

> `Stwórz plik scripts/git_check.py, który sprawdza stan repozytorium przez subprocess, filtruje nieśledzone pliki i wypisuje podsumowanie w kolorach ANSI.`

#### B. Praca z istniejącym kodem

```text
/add scripts/git_check.py
Dodaj do tego skryptu obsługę flagi CLI --verbose za pomocą biblioteki argparse oraz zabezpiecz obsługę błędów, gdy katalog nie jest repozytorium Git.

```

#### C. Integracja z zewnętrzną dokumentacją

```text
/web [https://docs.python.org/3/library/pathlib.html](https://docs.python.org/3/library/pathlib.html)
Przebuduj operacje na ścieżkach w pliku scripts/git_check.py, zastępując moduł os.path nowoczesnym podejściem opartym o pathlib zgodnie z wczytaną dokumentacją.

```

#### D. Pętla TDD (Testy i automatyczna naprawa błędów)

```text
/add tests/test_git_check.py
/run pytest tests/
Testy nie przeszły. Przeanalizuj powyższy błąd z terminala, popraw implementację w scripts/git_check.py i upewnij się, że wszystkie przypadki testowe zwracają status zielony.

```

---

## 📂 Struktura repozytorium

```text
Kurs-Git-Github/
├── README.md               # Dokumentacja projektu i przewodnik po narzędziach
├── pyproject.toml          # Metadane projektu i konfiguracja pytest
├── scripts/                # Narzędzia pomocnicze i skrypty automatyzujące
│   └── show_datetime.py    # Wypisuje aktualną datę i godzinę
└── tests/                  # Testy jednostkowe (pytest)
    └── test_show_datetime.py

```

Uruchomienie skryptu:

```bash
python scripts/show_datetime.py
```

## Uruchomienie testów

Aby uruchomić testy jednostkowe, użyj następującego polecenia:

```bash
pytest
```

To polecenie uruchomi wszystkie testy zdefiniowane w katalogu `tests/`.

## Zapis wyników testów

Aby zapisać wyniki testów w pliku zgodnie z najlepszymi praktykami, użyj następującego polecenia:

```bash
pytest --junitxml=results.xml
```

To polecenie uruchomi testy i zapisze wyniki w formacie JUnit XML w pliku `results.xml`.

## Uruchomienie testów i zapis wyników w pliku test_result_main.md

Aby uruchomić testy i zapisać wyniki w pliku `test_result_main.md`, użyj następującego skryptu:

```bash
pytest --durations=0 --junitxml=results.xml
junit2md results.xml > test_result_main.md
```

To polecenie uruchomi testy, zapisze wyniki w formacie JUnit XML w pliku `results.xml`, a następnie przekształci ten plik do formatu Markdown i zapisze w `test_result_main.md`.

## Instalacja pytest

Aby zainstalować `pytest`, użyj następującego polecenia:

```bash
pip install -e ".[dev]"
```

Upewnij się, że używasz odpowiedniego środowiska Python, jeśli korzystasz z wirtualnych środowisk.

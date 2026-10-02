# Zapytanie do fabryki (IFY AC) — co, po co, gotowy e-mail

Data: 2026-10-02 | Autor: Odyseusz (lead) dla 21Tech/IFY

---

## CZĘŚĆ 1: Co dokładnie potrzebujemy i PO CO (twoja ściąga)

| # | Czego żądamy | Po co nam to (funkcja w projekcie) |
|---|---|---|
| 1 | **PID** (Product ID) z Tuya IoT Platform + pełna nazwa produktu | Po PID odczytam w Tuya Cloud **pełną listę DP** (data points): które kody = temperatura/wentylator/swing/tryb/timer. Bez tego nie wiemy, co urządzenie umie i jak je sterować. To jest fundament. |
| 2 | **Tabela DP / standard instruction set** (eksport z Tuya IoT albo PDF fabryki) — najlepiej zrzut ekranu zakładki "Function Point" produktu | Weryfikacja, że funkcje fan level, swing, temperatura, tryby (heat/cool/dry), timer są **standarowymi kodami Tuya (kt)** — wtedy nasz kontrakt i panele działają od razu, bez customów |
| 3 | **Typ modułu Wi-Fi i firmware** (np. WR3E, CBU; wersja firmware; czy to standardowa platforma Tuya czy modyfikacja fabryczna) | Standardowy firmware = działamy po ścieżce Tuya SDK bez niespodzianek; modyfikowany = osobna rozmowa |
| 4 | **Panel**: czy urządzenie ma gotowy panel Tuya (standardowy AC panel), czy custom? Jeśli custom — czy udostępniają źródła / czy jest na Tuya "workbench"? | Panel to gotowy ekran sterowania w aplikacji. Standardowy = zero pracy dla nas. Custom bez źródeł = problem |
| 5 | **Własność PID / konto Tuya**: czy PID jest na koncie fabryki? Czy fabryka może **przenieść/zautoryzować PID na nasze konto** (Tuya "PID transfer" lub OEM authorization), albo udostępnić projekt jako "co-development"? | Żeby nasza aplikacja (własne AppKey) mogła sterować tym urządzeniem, PID musi być powiązany z naszym kontem deweloperskim. To formalność na Tuya, ale fabryka musi ją zrobić |
| 6 | **Tuya App Key / OEM**: czy fabryka ma już własną appkę OEM (i czy moglibyśmy jej użyć tymczasowo), czy my tworzymy własną od zera | Decyduje o trasie: OEM App (szybko) vs własna appka z SDK (pełna kontrola) |
| 7 | **Parowanie i protokoły**: WiFi 2.4 GHz tylko? Bluetooth pairing (BLE)? Matter? | Wpływa na UX onboarding w aplikacji i wymagania SDK |
| 8 | **Region danych Tuya** (datacenter): EU? | Dane klientów UE muszą być w regionie EU (RODO); nasz projekt na Tuya musi być w tym samym regionie co urządzenia |
| 9 | **OTA**: kto zarządza aktualizacjami firmware (fabryka przez Tuya OTA?) — czy my możemy publikować wersje? | Produkt komercyjny = musimy wiedzieć, kto i jak aktualizuje urządzenia w terenie |
| 10 | **Sterowanie lokalne (LAN)**: czy firmware wspiera Tuya local control (protocol 3.3/3.4)? | Jeśli tak — aplikacja może działać bez chmury w domu klienta (szybciej, odporniej). Jeśli nie — zawsze cloud |
| 11 | **Dokumentacja serwisowa**: schemat, lista części zamiennych (z numerami), instrukcja EN | Pod sklep z częściami i moduł serwisowy w aplikacji |
| 12 | **Certyfikaty**: CE, RoHS, EMC — skany | Sprzedaż komercyjna w UE — wymagane prawnie; też do modułu "produkt" w aplikacji |
| 13 | **Sample/dev unit**: czy mogą zapewnić 1–2 sztuki deweloperskie (z normalnym firmware) do testów SDK | Bez fizycznego urządzenia integrujemy "na ślepo"; sample przyspiesza wszystko |

**Minimalne must-have (bez tego nie ruszamy): 1, 2, 5, 7, 8.** Resztę można dociągnąć.

---

## CZĘŚĆ 2: Gotowy e-mail (EN) — kopiuj-wklej

Subject: **IFY-branded Tuya AC — PID, DP table, SDK authorization & dev samples (for our companion app)**

Hi [name],

We are finalizing the companion mobile app (Android + iOS) for the portable air
conditioner you produce under our brand, **innovation for you (IFY)**. The app
will connect **directly** to the device through the Tuya platform, so we need a
few items and clarifications from your side:

1. **Product ID (PID)** of the AC on Tuya IoT Platform (and product name), so we
   can read the full DP schema from the cloud.
2. **DP / standard instruction set table** for this PID — a screenshot of the
   "Function Point" page or an export. We specifically need the DPs for:
   power, target/current temperature, mode (heat/cool/dry), fan level, swing,
   and timer. Please confirm they use Tuya standard `kt` codes.
3. **Wi-Fi module type and firmware** (e.g. WR3E/CBU, firmware version) and
   confirmation that it is **standard Tuya firmware** (no factory modification).
4. **Panel**: is a standard Tuya AC panel assigned to this PID, or a custom one?
   If custom, can you share the panel source / grant access?
5. **PID ownership & authorization**: the PID is currently under your account.
   We will create our own Tuya IoT developer account for the IFY app
   (Android/iOS AppKey). Please confirm you can either (a) transfer the PID to
   our account, or (b) authorize our AppKey against this PID (OEM/authorization
   on Tuya), so our app can control the device.
6. **Data center region**: is the product provisioned on the **EU datacenter**?
   Our app and cloud project must match it (GDPR).
7. **Pairing**: Wi-Fi 2.4 GHz only, or BLE-assisted pairing? Any Matter?
8. **OTA**: who publishes firmware updates — your team via Tuya OTA, and can we
   request releases?
9. **Local control**: does the firmware support Tuya local LAN control
   (protocol 3.3/3.4) so the app can work without the cloud on the same LAN?
10. **Spare parts & service docs**: parts list with part numbers, exploded
    diagram, EN manual (for the in-app service & spare-parts shop).
11. **Certificates**: CE / RoHS / EMC scans for EU commercial sale.
12. **2 dev samples** with standard firmware for our SDK integration testing.

Items 1, 2, 5, 7 and 8 are blocking for us — the rest can follow.

Thanks,
[imię], innovation for you (IFY)
[kontakt]

---

## CZĘŚĆ 3: Co zrobisz po otrzymaniu odpowiedzi (2 minuty)

1. Załóż konto na developer.tuya.com (Cloud Project, region **EU/ Central Europe**).
2. Podaj mi Access ID + Access Secret (do `.env` na odyseuszu — nie na czat).
3. Gdy fabryka da PID: ja odczytam pełną mapę DP z API i zamknę kontrakt
   (`ac-v1.schema.json` → `dp_map`) — wtedy startuje pierwsza karta dla kodera.

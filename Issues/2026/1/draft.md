# Wydanie 1 - {data wydania}

## Wstęp

O AI piszą teraz niemal wszyscy. Jesteśmy zalewani newsami, opiniami oraz dyskusjami na temat sztucznej inteligencji. Niektóre artykuły są pisane przez ludzi bez wiedzy technicznej potrzebnej do krytycznej analizy możliwości technicznych obecnych systemów AI. Wiele publicznych opinii można podważać konfliktami interesów (obecna bańka spekulacyjna tylko ten proces mocniej nakręca). Co jakiś czas podczas rozmowy z ludźmi z branży dochodzę do wniosku, że przepaść informacyjna jest już teraz ogromna i powiększa się w zastraszającym tempie.

AI w takiej czy innej formie zmienił branżę na IT, myślę że na tym etapie nie jest już to dyskusją - stało się to faktem. Jednakże to jak ta zmiana wygląda obecnie i jak będzie wyglądać w przyszłości jest tematem który jest ciągle subiektywny i szeroko dyskutowany. Ten newsletter jest naszą próbą o zmniejszenia przepaści informacyjnej w naszej firmie. Przyświeca nam kilka podstawowych celów:

- Odfiltrować szum informacyjny i dostarczyć rzetelne informacje o AI, które są istotne dla naszej branży
- Analizować i interpretować obecne trendy w narzędziach AI, które mogą mieć wpływ na naszą pracę
- Dostarczać praktyczne wskazówki i strategie dotyczące wykorzystania AI w naszej codziennej pracy
- Przekazywać subiektywne opinie ludzi z branży oraz z naszej firmy, żeby rozszerzyć perspektywę i zainspirować do dyskusji

### Disclaimer

Zdecydowana większość tego newslettera będzie pisana przez ludzi. Każdy tekst generowany przez AI będzie wyraźnie oznaczony. Nie oznacza to że AI nie wspomaga nas w tworzeniu tego newslettera - wręcz przeciwnie, AI pomaga nam zarówno w przygotowaniu treści, jak i w jej redagowaniu. Cała praca jest prowadzona na publicznym repozytorium GitHub, dostępnym pod adresem: [https://github.com/jakoss/AiNewsletter](https://github.com/jakoss/AiNewsletter).

## Stan AI w IT

Pierwszy newsletter chciałbym poświęcić krótkiemu opisowi obecnego stanu AI w IT. Najpierw zacznę od mojej opinii w obecnej sekcji, następnie dołączę kilka linków do tekstów / wystąpień, które (w mojej opinii) dobrze oddają stan w którym się obecnej znajdujemy. Szukałem opinii jasno oddzielających hype od rzeczywistości, większość z ludzi których wypowiedzi będę linkować to ludzie z branży, jednak nie mający nic do wygrania ani przegrania w wyścigu o dominację AI. Nie będę tutaj cytować CEO firm takich jak Anthropic, które na każdym kroku podkreślają jak to nas wszystkich AI zastąpi oraz jak blisko (już tylko kilka miesięcy) jesteśmy do AGI.

## Krótka historia narzędzi AI dla developerów

AI zaczynaliśmy skromnie, gdy ChatGPT pojawił się niczym rycerz na białym koniu - potrafił wygenerować często nawet sensowny kod, ale kopiowanie i debugownie tego kodu to była pętla która nie przyspieszała naszej pracy w żaden mierzalny sposób. Pierwsze zintegrowane narzędzia do autocomplete (takie jak TabNine czy GitHub Copilot) były bardzo obiecująco i potrafiły przyspieszyć nieco pisanie kodu, ale nadal nie mówiliśmy o rewolucji w sposobie naszej pracy.

Te czasy mamy już za sobą. Rynek narzędzi AI zaczął przechodzić bardzo gwałtowną rewolucję od momentu wprowadzeniu autonomicznych agentów w narzędziach takich jak Claude Code. W ciągu ostatnich miesięcy obserwujemy bardzo efektywne połączenie dobrych modeli językowych (subiektywna opinia - pierwszy naprawdę dobry model do autonomicznego kodowania to Claude Sonnet 4) oraz coraz lepszych uprzęży (pozwolicie że to ostatni raz kiedy próbowałem przetłumaczyć z angielskiego "harness" - to nazwa na zestaw narzędzi które pozwalają agentowi AI na wykonywanie autonomicznych zadań jednocześnie oferując zabezpieczenia przed niepożądanymi operacjami na naszych maszynach. Takim harnessem jest np Claude Code, Copilot Cli czy Cursor). Mniej więcej od grudnia 2025 roku przestałem pisać kod ręcznie, jednocześnie budując systemy szybciej niż kiedykolwiek wcześniej. Oczywiście ciągle kontroluję jakość kodu, czasami robię ręczne edycje, ale zdecydowaną większość kodu generują mi narzędzia AI.

Można rozdzielić etapy rozwoju narzędzi AI dla developerów na kilka głównych faz:

- Chaty AI i kopiowanie kodu do edytora
- Autocomplete w ulubionych edytorach (GitHub Copilot, TabNine)
- Pół-automatyczne narzędzia do edycji kodu (GitHub Copilot z Edit mode w Visual Studio Code, Cursor)
- Automatyczne agenty do kodowania w IDE (Cursor, GitHub Copilot Agent Mode)
- Autonomiczne agenty do kodowania z rozszerzonym dostępem np. do linii komend (Claude Code, Copilot CLI, Opencode) - **Tutaj jesteśmy obecnie**
- W pełni zautomatyzowane systemy agentowe do tworzenia oprogramowania end-to-end (GasTown, Squad) - **głównie eksperymentalne, ale już działające systemy**

Ta lista pomija narzędzia typu Lovable - skupiam się wyłącznie na tworzeniu kodu przez developerów.

## Co robić, jak żyć, jak pracować?

Wszystko w branży zmienia się obecnie z dnia na dzień, dlatego w każdym wydaniu chciałbym dołączyć krótką rekomendację podejścia oraz narzędzi, które obecnie sprawdzają się najlepiej w mojej codziennej pracy.

Obecnie mój flow jest stosunkowo prosty - używam narzędzia Opencode (w wersji Desktop do większych zadań oraz w wersji cli do prostych funkcjonalności czy poprawek, które mogę realizować równolegle). W Opencode używam naszej firmowej licencji GitHub Copilot i wybieram model GPT 5.4 (złożone zadania), Claude Opus 4.6 (trudne problemy) lub Claude Sonnet 4.6 (jeżeli potrzebuję pomocy z mniejszymi zmianami).

W Opencode zawsze zaczynam od wykorzystania plan mode, który pozwala na zebranie odpowiedniego kontekstu dla AI oraz na iterację nad specyfikacją rozwiązania jeszcze przed jego implementacją. Takie podejście upraszcza code review (wiemy czego się spodziewać jeżeli znamy plan) oraz mocno redukuje ilość iteracji potrzebnych do osiągnięcia finalnego rozwiązania.

Jeżeli mam do zaadresowania proste rzeczy i "intuicyjnie" wiem że AI sobie z nimi poradzi - wtedy używam git worktree do zrównoleglenia pracy. Zachęcam do bezpośredniego kontaktu jeżeli chciałbyś zobaczyć jak to wygląda w praktyce lub potrzebujesz pomocy z wdrożeniem podobnego podejścia w swojej codziennej pracy.

## Cytat na dziś:

> Intelligence is the ability to avoid doing work, yet getting the work done.

Linus Torvalds (który jest zaskakująco optymistyczne w kwestii AI, polecam posłuchać jego opinii w [filmie nagranym z Linus Tech Tips](https://youtu.be/mfv0V1SxbNA?t=1993&si=R2qv_5kpeYFM2jbj)).

## Opinie z branży

Poniżej zamieszczam kilka linków do materiałów, które moim zdaniem warto obejrzeć. Nie wchodzą w detale (na to będziemy mieć czas w przyszłych wydaniach), ale stanowią dobry punkt wyjścia do zrozumienia w jakim kierunku wszyscy zmierzamy.

> [!IMPORTANT]
> Podsumowania do materiałów są wygenerowane przez AI i weryfikowane przez nas.

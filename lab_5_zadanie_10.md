Zadanie 1
```python
In [1]: from folder_aplikacji.models import Osoba

In [2]: osoby = Osoba.objects.all()

In [3]: print(osoby)
<QuerySet [<Osoba: GrzegorzBudka>, <Osoba: MariolaKieracka>, <Osoba: AndrzejWazon>, <Osoba: KaźmiżWędka>]>
```

Zadanie 2
```python
In [4]: osoba = Osoba.objects.get(id=3)

In [5]: print(osoba)
MariolaKieracka
```

Zadanie 3
```python
In [6]: osoba_a = Osoba.objects.filter(imie__startswith='A')

In [7]: print(osoba_a)
<QuerySet [<Osoba: AndrzejWazon>]>
```

Zadanie 4
```python
In [9]: stanowiska = Osoba.objects.values('stanowisko').distinct()

In [10]: print(stanowiska)
<QuerySet [{'stanowisko': 1}, {'stanowisko': 3}, {'stanowisko': 2}, {'stanowisko': 1}]>
```


Zadanie 5
```python
In [13]: from folder_aplikacji.models import Stanowisko

In [14]: Stanowisko.objects.values_list('nazwa', flat = True).order_by("-nazwa")
Out[14]: <QuerySet ['Tester', 'People Manager', 'Developer']>
```


Zadanie 6
```python
In [16]: In [15]: Osoba.objects.create(imie = 'Jan', nazwisko='Kowalski', plec='2', stanowisko= Stanowisko.objects.get(id=1))
Out[16]: <Osoba: JanKowalski>
```


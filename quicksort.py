import unittest


# Function quicksort:
# Parameter: unsortiertes Array mit Zahlen
# Result: sortiertes Array
def quicksort(unsortiert):
    laenge = len(unsortiert)
    if laenge <= 1:
        return unsortiert
    else:
        # 1. Gesamtarray in zwei Arrays aufteilen
        pivot = unsortiert[0]
        links = []
        rechts = []
        for i in range(1, laenge):
            if unsortiert[i] < pivot:
                links.append(unsortiert[i])
            else:
                rechts.append(unsortiert[i])

        # 2. Einzelteile sortieren
        links = quicksort(links)
        rechts = quicksort(rechts)

        # 3. zusammenbauen
        ergebnis = []
        for wert in links:
            ergebnis.append(wert)
        ergebnis.append(pivot)
        for wert in rechts:
            ergebnis.append(wert)

        return ergebnis


# Testcases
class TestQuicksort(unittest.TestCase):
    def test_quicksort_0(self):
        unsortiert = [5, 7, 12, 4, 8, 3, 9, 1, 2]
        sortiert = [1, 2, 3, 4, 5, 7, 8, 9, 12]
        self.assertEqual(quicksort(unsortiert), sortiert)

    def test_quicksort_1(self):
        unsortiert = [7, 12, 4, 8, 3, 9]
        sortiert = [3, 4, 7, 8, 9, 12]
        self.assertEqual(quicksort(unsortiert), sortiert)

    def test_quicksort_2(self):
        unsortiert = [1, 2, 4, 4, 2, 1]
        sortiert = [1, 1, 2, 2, 4, 4]
        self.assertEqual(quicksort(unsortiert), sortiert)

    def test_quicksort_3(self):
        unsortiert = []
        sortiert = []
        self.assertEqual(quicksort(unsortiert), sortiert)

    def test_quicksort_4(self):
        unsortiert = [2]
        sortiert = [2]
        self.assertEqual(quicksort(unsortiert), sortiert)


# Run Tests
if __name__ == "__main__":
    unittest.main()

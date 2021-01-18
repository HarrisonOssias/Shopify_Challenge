def mergeSort(arraym):
    length = len(arraym)
    if length > 1:
        midpoint = length // 2
        # split into left and right lists
        leftlist = arraym[midpoint:]
        rightlist = arraym[:midpoint]
        mergeSort(leftlist)
        mergeSort(rightlist)
        i = j = k = 0

        while i < len(leftlist) and j < len(rightlist):
            if leftlist[i] < rightlist[j]:
                arraym[k] = leftlist[i]
                i += 1
            else:
                arraym[k] = rightlist[j]
                j += 1
            k += 1

        while i < len(leftlist):
            arraym[k] = leftlist[i]
            i += 1
            k += 1

        while j < len(rightlist):
            arraym[k] = rightlist[j]
            j += 1
            k += 1

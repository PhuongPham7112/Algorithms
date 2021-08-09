# Binary search problem: Allocate library books with a minimum of a maximum number of pages. 
def isPossible(books, students, pages, currentMin):
    requiredStudent = 1
    currentSum = 0
    for i in range(books):
        # if the number of pages in a book is bigger than the current minimum => that book is not possible
        if pages[i] > currentMin:
            return False
        # if current sum + new pages exceeds the minimum, we add another student so we won't exceed the page number on the previous student
        if currentSum + pages[i] > currentMin:
            requiredStudent += 1
            currentSum = pages[i] # now the current sum focuses on the new student, the previous student is done and has reached his max page number
            if students < requiredStudent:
                return False
        else:
            currentSum += pages[i]
    return True

def AllocateBook (books, students, pages):
    pageSum = 0
    if students > books:
        return -1
    pageSum += sum(pages)
    start, end = 0, pageSum
    result = 10**9
    while start <= end:
        mid = (start + end)//2

        if isPossible(books, students, pages, mid):
            result = min(result, mid)
            end = mid - 1
        else:
            start = mid + 1
    return result

pages = [12, 34, 67, 90] 
books = len(pages)
students = 2
print(AllocateBook(books, students, pages))
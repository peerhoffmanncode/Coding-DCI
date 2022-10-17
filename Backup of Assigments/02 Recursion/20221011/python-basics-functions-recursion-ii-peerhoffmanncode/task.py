#### Task 1 ##################################################################
print()
print("#### Task 1 ####")

def sum_series(n: int) -> int:
    ''' recursive function that returns the sum of n '''
    if n <= 0:
        return 0
    return n + sum_series(n-2)

print(sum_series(7))
print(sum_series(8))
print(sum_series(15))
print(sum_series(20))




#### Task 2 ##################################################################
print()
print("#### Task 2 ####")

def drill_sum(data:list):
    ''' recursive function to sum up nested data in a give datatype of lists!
        data is the datatype
        '''
    #input(data) #<- to debug !
    # check if list is empty
    if not data:
        return 0
    # check if index is INT or LIST
    if not isinstance(data, list):
        # return number if int!
        return data
    # if list, add current value + following remaining list (upwhiling)
    return drill_sum(data[0]) + drill_sum(data[1:])


test_data1 = [
    1,
    [1, 2],
    [1, [2, 3]],
    [1, [2, [3, 4]]],
    [1, [2, [3, [4, 5]]]],
]
test_data2 = [
    [1, [[2, 6], [3, 4]]],
    [[5, 6, [7, 8]], [2, [3, [4, 5]]]],
    [1, [2, 3]],
    [1, 2],
    1,
]

# this was crazy!!! CRRAAAZZZY! :-)
print(drill_sum(test_data1))
print(drill_sum(test_data2))




#### Task 3 ##################################################################
print()
print("#### Task 3 ####")


def count_pages(page_list):
    ''' recursive function that returns the amount of pages a wp has '''

    # base case / check if list is empty
    if not page_list:
        return 0

    # main recursion happening here
    if isinstance(page_list, list):
        return count_pages(page_list[0]) + count_pages(page_list[1:])

    # if dict check if "pages" is there -> return 1 title + dict from "page"
    if isinstance(page_list, dict):
        if page_list.get("pages"):
            return 1 + count_pages(page_list["pages"])

    # retrun 1 per "title"
    return 1

test_data1 = [
    {
        "title": "Home",
        "pages": [
            {
                "title": "About",
                "pages": [
                    {
                        "title": "The company"
                    },
                    {
                        "title": "Our services"
                    },
                    {
                        "title": "Our products"
                    },
                    {
                        "title": "Our deliveries",
                        "pages": [
                            {
                                "title": "National"
                            },
                            {
                                "title": "International"
                            }
                        ]
                    }
                ]
            },
            {
                "title": "Shop",
                "pages": [
                    {
                        "title": "Browse all"
                    },
                    {
                        "title": "Categories"
                    }
                ]
            },
            {
                "title": "My account",
                "pages": [
                    {
                        "title": "Settings"
                    },
                    {
                        "title": "Edit profile"
                    },
                    {
                        "title": "My transactions"
                    }
                ]
            }
        ]
    }
]

print(count_pages(test_data1))
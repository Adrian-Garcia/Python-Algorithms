"""
Paginated API
Problem Description
A third-party API that we're using has a paginated API.  It returns results in
chunks of N.  This is implemented below on "fetch_page".
We don't think that API is very useful, and would prefer the following an implementation
where only one call to "fetch" will return a given number of results, abstracting away the
need to do pagination.
Your task will be to implement ResultFetcher.fetch()
"""

from typing import List
from typing import Optional
from typing import TypedDict


# These numbers are for testing only and may be changed by the interviewer.
MAX_RESULTS = 103
PAGE_SIZE = 10


class FetchPageResult(TypedDict):
    next_page: Optional[int]
    results: List[int]


# External API -- Should not be modified for solution
def fetch_page(page: int) -> FetchPageResult:
    """
    Return the page of results and the next page. Pages are 0 indexed.
    returns:
        {
            "results": [...],
            "next_page": 3
        }
    """
    if page * PAGE_SIZE > MAX_RESULTS:
        return {"next_page": None, "results": []}
    return {
        "next_page": page + 1,
        "results": list(
            range(page * PAGE_SIZE, min(MAX_RESULTS, (page + 1) * PAGE_SIZE))
        ),
    }


################## Implement Solution here ##################


class ResultFetcher:
    current_page: Optional[int]
    current_index: Optional[int]


    # 5
    # 10 / 5
    # 10 // 11 = 1
    # 10 // 20 = 2

    '''
    29 -> 29 primeros
        10
        10
        9
    '''

    '''
    10 -> 10 primeros
    15 -> 15 siguientes después de los 10 primeros
    30 -> 30 siguientes después de los 10 primeros
    '''

    def __init__(self):
        self.current_page = 0
        self.current_index = 0


    def flat_list(self, lists: List[List[int]]) -> List[int]:
        result = []
        for l in lists:
            for i in l:
                result.append(i)

        return result

    def fetch(self, num_results: int) -> List[int]:
        results = []

        num_of_requests = (PAGE_SIZE // num_results) + self.current_page
        for i in range(num_of_requests):
            num_results -= PAGE_SIZE                # 0
            res = fetch_page(self.current_page)     # Check this

            if num_results < PAGE_SIZE and num_results != 0:
                res["results"] = res["results"][:num_results]

            print(res["results"])

            results.append(res["results"])
            self.current_page = res["next_page"]

        results = self.flat_list(results)

        return results


#############################################################


def test_case(test_case: int, actual: List[int], expected: List[int]) -> None:
    if actual == expected:
        print(f"Test Case {test_case}: SUCCESS")
    else:
        print(f"Test Case {test_case}: FAILED")
        print(f"Expected {expected}. Got {actual}")


if __name__ == "__main__":
    fetcher = ResultFetcher()
    test_case(1, fetcher.fetch(5), list(range(5)))
    test_case(2, fetcher.fetch(2), list(range(5, 7)))
    test_case(3, fetcher.fetch(7), list(range(7, 14)))
    test_case(4, fetcher.fetch(103), list(range(14, 103)))
    test_case(5, fetcher.fetch(10), [])

    fetcher = ResultFetcher()
    test_case(6, fetcher.fetch(200), list(range(103)))

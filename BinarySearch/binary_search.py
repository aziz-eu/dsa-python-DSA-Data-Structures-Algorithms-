def main():
    input_data = {
        "cards": [],
        "query": 6
    }
    result = locate_card(**input_data)
    print(f"The Query Elements Found at {result} Position" if result != -1 else "Not Found!")
    
def locate_card(cards, query):
    lo, hi = 0, len(cards)-1
    while lo<=hi:
        mid= (lo+hi) //2
        ''' It Check is the query element is Exit or not. is it 1st elelemt or not doesn;t matter '''
        # if cards[mid] == query:
        #     return mid
        # elif cards[mid] < query: 
        #     lo = mid +1
        # else:
        #     hi = mid - 1

        ''' It will the find the 1st occerence of element in array in they are duplicate'''
        result = check_position(cards, query, mid)
        if result == 'found':
            return mid
        elif result == 'right':
            lo = mid + 1
        elif result == 'left':
            hi = mid -1
            
    return -1;
            
def check_position (cards, query, mid):
    if(cards[mid] == query):
        if(mid > 0 and cards[mid-1] == query):
            return "left"
        else:
            return "found"
    elif cards[mid] > query:
        return 'left'
    else:
        return 'right'
    

if __name__ == "__main__":
    main()
        
def main():
    input_data = {
        "cards": [11,2 ,1,2,3,4,55,66,77,88,99,111,222,333,444,555],
        "query": 11
    }
    result = locate_card(**input_data)
    print(f"The Query Elements found at {result} postion" if result != -1 else "Not Found!")
    
def locate_card(cards, query):
    for index, card in enumerate(cards):
        if(card == query):
            return index
    return - 1


if __name__ == "__main__":
    main()
        



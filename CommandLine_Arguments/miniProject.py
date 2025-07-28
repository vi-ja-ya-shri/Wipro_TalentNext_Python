import sys

def calculate_happiness(liked_str, disliked_str, given_str):
    liked = set(liked_str.split('-'))
    disliked = set(disliked_str.split('-'))
    given = given_str.split('-')

    happiness = 0

    for num in given:
        if num in liked:
            happiness += 1
        elif num in disliked:
            happiness -= 1
    return happiness

if __name__ == "__main__":
    # Example input: python script.py 3-1 5-7 1-5-3-8
    if len(sys.argv) != 4:
        print("Usage: python script.py <liked> <disliked> <given>")
    else:
        liked_str = sys.argv[1]
        disliked_str = sys.argv[2]
        given_str = sys.argv[3]

        result = calculate_happiness(liked_str, disliked_str, given_str)
        print(result)

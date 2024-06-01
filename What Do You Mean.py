def wdym():
    number = input()
    number = number.split("0")
    store = {"2":["a", "b", "c"], 
            "3":["d", "e", "f"],
            "4":["g", "h", "i"],
            "5":["j", "k", "l"],
            "6":["m", "n", "o"],
            "7":["p", "q", "r", "s"],
            "8":["t", "u", "v"],
            "9":["w", "x", "y", "z"]}
    word_list = []
    word_dict = {}
    text = ""
    while True:
        text = input()
        if text == "***":
            break
        text = text.split(" ")
        word_list += text
    for word in word_list:
        result = ""
        for char in word:
            for key, value in store.items():
                if char in value:
                    result += key
        word_dict[word] = result
    final = ""
    for num in number:
        count = 0
        for key in word_dict:
            if num == word_dict[key]:
                store = key
                count += 1
        if count > 1:
            final = "more than one answer"
            break
        elif count == 0:
            final = "cannot be found"
            break
        else:
            final += store + " "
    print(final)
